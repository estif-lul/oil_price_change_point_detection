import numpy as np
import pandas as pd
import pymc as pm
import arviz as az
import pickle
import joblib
import os

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

    def save(self, file_prefix, custom_params=None):
        """
        Saves the trace and custom params to files with the given file_prefix.

        Parameters
        ----------
        file_prefix : str
            path and prefix used to identify where to save the trace for this model,
            e.g. given file_prefix = 'path/to/file/'
            This will attempt to save to 'path/to/file/trace.pickle'.

        custom_params : dict (defaults to None)
            Custom parameters to save
        """
        fileObject = open(os.path.join(file_prefix,'trace.pickle'), 'wb')
        joblib.dump(self.trace, fileObject)
        fileObject.close()

        if custom_params:
            fileObject = open(os.path.join(file_prefix,'params.pickle'), 'wb')
            joblib.dump(custom_params, fileObject)
            fileObject.close()

    def load(self, file_prefix, load_custom_params=False):
        """
        Loads a saved version of the trace, and custom param files with the given file_prefix.

        Parameters
        ----------
        file_prefix : str
            path and prefix used to identify where to load the saved trace for this model,
            e.g. given file_prefix = 'path/to/file/'
            This will attempt to load 'path/to/file/trace.pickle'.

        load_custom_params : bool (defaults to False)
            flag to indicate whether custom parameters should be loaded

        Returns
        ----------
        custom_params : Dictionary of custom parameters
        """
        self.trace = joblib.load(os.path.join(file_prefix,'trace.pickle'))

        custom_params = None
        if load_custom_params:
            self.trace = joblib.load(os.path.join(file_prefix,'params.pickle'))

        self.results["summary"] = az.summary(self.trace)
        self.tau = int(self.trace.posterior["tau"].mean().values)

        return self.trace