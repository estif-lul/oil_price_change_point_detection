from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS
import logging
logging.basicConfig(level=logging.INFO)


app = Flask(__name__)
CORS(app)


# Load datasets
brent_data = pd.read_csv("data/BrentOilPrices.csv", parse_dates=["Date"])
change_points = pd.read_csv("data/change_point_index_date_counts.csv")
events = pd.read_csv("data/oil_price_event_dataset.csv")

@app.route("/")
def index():
    return "Brent Oil Dashboard API is running!"

@app.route("/api/v1/prices")
def get_prices():
    data = brent_data.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1/change-points")
def get_change_points():
    data = change_points.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1/events")
def get_events():
    data = events.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1/stats")
def get_summary():
    stats = {
        "max_price": brent_data["Price"].max(),
        "min_price": brent_data["Price"].min(),
        "mean_price": brent_data["Price"].mean()
    }
    return jsonify(stats)

@app.route("/api/v1/prices/filter")
def filter_prices():
    start = request.args.get("start")
    end = request.args.get("end")
    filtered = brent_data[(brent_data["Date"] >= start) & (brent_data["Date"] <= end)]
    return jsonify(filtered.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
