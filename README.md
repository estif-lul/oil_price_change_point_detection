# 🛢️ Oil Price Change Point Detection

Welcome to the **Oil Price Change Point Detection** project! This repository provides a full-stack solution for detecting change points in oil price time series data using Bayesian modeling. The project leverages **PyMC** for statistical inference, **Flask** for the backend API, and **React** for an interactive frontend dashboard.

---

## 🚀 Features

- **Bayesian Change Point Detection**: Robust modeling of structural changes in oil price data using PyMC.
- **RESTful API**: Flask backend serving model predictions and data endpoints.
- **Interactive Dashboard**: React-based frontend for data visualization and user interaction.
- **Modular Architecture**: Easily extend or adapt for other time series datasets.

---

## 🏗️ Project Structure

```
oil_price_change_point_detection/
├── backend/           # Flask API code (Python)
│   ├── app.py
│   └── ...
├── frontend/          # React dashboard (JavaScript/TypeScript)
│   ├── src/
│   └── ...
├── models/            # PyMC models and scripts
│   └── change_point_model.py
├── data/              # Sample datasets
│   └── oil_prices.csv
├── README.md
└── requirements.txt
```

---

## 🧑‍💻 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/oil_price_change_point_detection.git
cd oil_price_change_point_detection
```

### 2. Backend Setup (Flask + PyMC)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### 3. Frontend Setup (React)

```bash
cd ../frontend
npm install
npm start
```

The React app will run on [http://localhost:3000](http://localhost:3000) and communicate with the Flask API.

---

## 📊 Usage

1. **Upload Data**: Use the dashboard to upload or select oil price time series data.
2. **Run Detection**: Trigger Bayesian change point detection via the dashboard.
3. **Visualize Results**: View detected change points and model diagnostics interactively.

---

## 🧠 Technologies Used

- [PyMC](https://www.pymc.io/) - Bayesian statistical modeling
- [Flask](https://flask.palletsprojects.com/) - Python web API
- [React](https://react.dev/) - Frontend UI
- [Plotly](https://plotly.com/) - Data visualization (optional)

---

## 📂 Documentation

- **Backend**: See `backend/README.md` for API endpoints and model details.
- **Frontend**: See `frontend/README.md` for dashboard features and customization.
- **Modeling**: See `models/change_point_model.py` for PyMC implementation.

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License.

---

## ✨ Acknowledgements

- PyMC community for Bayesian modeling tools
- Flask and React contributors

---

Happy modeling! 🚀