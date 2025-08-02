import numpy as np
import pandas as pd
import pymc as pm
import arviz as az
import pickle

class BayesianChangePointModel:
    def __init__(self):
        self.model = None
        self.trace = None
        self.results = {}
        self.tau = None

    def create_model(self, data):
        self.data = np.array(data.dropna())
        self.N = len(self.data)

        with pm.Model() as model:
            tau = pm.DiscreteUniform("tau", lower=0, upper=self.N)

            mu1 = pm.Normal("mu1", mu=0, sigma=1)
            mu2 = pm.Normal("mu2", mu=0, sigma=1)
            sigma1 = pm.HalfNormal("sigma1", sigma=1)
            sigma2 = pm.HalfNormal("sigma2", sigma=1)

            idx = np.arange(self.N)
            mu = pm.math.switch(tau >= idx, mu1, mu2)
            sigma = pm.math.switch(tau >= idx, sigma1, sigma2)

            obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=self.data)

            self.model = model

    def fit(self, samples=2000, tune=1000):
        if self.model is None:
            raise RuntimeError("Model not initialized. Run create_model() first.")
        with self.model:
            self.trace = pm.sample(samples, tune=tune, target_accept=0.95, return_inferencedata=True)

            self.results["summary"] = az.summary(self.trace)
            self.tau = int(self.trace.posterior["tau"].mean().values)

    def predict(self):
        if self.trace is None:
            raise RuntimeError("Model not yet fit. Run fit() first.")
        return self.tau, self.trace.posterior

    def score(self):
        if self.trace is None:
            raise RuntimeError("Model not yet fit. Run fit() first.")
        rhat = self.results["summary"]["r_hat"]
        convergence = all(rhat < 1.1)
        return {"converged": convergence, "r_hat": rhat}

    def save(self, filepath="bcp_model.pkl"):
        with open(filepath, "wb") as f:
            pickle.dump({
                "trace": self.trace,
                "model": self.model,
                "tau": self.tau,
                "results": self.results
            }, f)

    def load(self, filepath="bcp_model.pkl"):
        with open(filepath, "rb") as f:
            saved = pickle.load(f)
            self.trace = saved["trace"]
            self.model = saved["model"]
            self.tau = saved["tau"]
            self.results = saved["results"]
