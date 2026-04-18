# 📈 Predictive Modeling for Stock Price Forecasting

**MSc Statistics with Data Science — Final Year Project**  
Sree Sankara College, Kalady (MG University) | Mufeed T H

---

## Overview

This project applies supervised machine learning to financial time-series data to forecast next-day S&P 500 closing prices. Built as a complete end-to-end system combining a trained predictive model, an interactive web terminal, and an analytical Power BI dashboard.

The goal was to bridge statistical modelling with real-world usability — not just building a model, but making it accessible and interpretable through a deployable interface.

---

## Project Structure

```
stock-price-forecasting/
│
├── app.py                  # Flask web application
├── model.pkl               # Trained OLS regression model
├── templates/              # HTML templates (Home, Terminal, Contact)
├── requirements.txt        # Python dependencies
└── README.md
```

> **Note:** The dataset (`all_stocks_5yr.xlsx`, ~29MB) exceeds GitHub's file size limit and is not included in this repository.  
> Dataset source: [S&P 500 Stock Data — Kaggle](https://www.kaggle.com/datasets/camnugent/sandp500)  
> 📊 Power BI Dashboard (.pbix): [Download from Google Drive](https://drive.google.com/file/d/1r6THn-0jC9PRR2GRQHNczZfdF8xOBf-T/view?usp=sharing)

---

## Tech Stack

| Layer | Tools |
|---|---|
| Modelling | Python, scikit-learn, Pandas |
| Web App | Flask |
| Visual Analytics | Power BI |
| Evaluation | R², MAE, time-based train/test split |

---

## Model Details

- **Algorithm:** Ordinary Least Squares (OLS) Regression
- **Dataset:** S&P 500 — 5 Year Historical Data
- **Input Feature:** Previous day's closing price
- **Target:** Next trading session closing price (T+1)
- **Train / Test Split:** 80 / 20 (time-based, no shuffle — to prevent data leakage)
- **Evaluation Metrics:** R² ≈ 0.98 | MAE ≈ $0.91

> The high R² is expected for a univariate lag-based model on financial time-series — it reflects the strong autocorrelation in stock prices. The model is designed as an interpretable statistical baseline rather than a production trading system.

---

## Flask Web App

Three-page application built with Flask:

- **Home** — Project overview, key features, and model profile
- **Terminal** — Live inference engine: enter a closing price, get a T+1 forecast
- **Contact** — Full project summary and system stack

---

## Power BI Dashboard

Four-page interactive dashboard:

- **Home** — Project title and navigation overview
- **Market Overview** — KPI cards, MA 50/200 trend, cyclical performance matrix, market momentum index
- **Price Analysis** — Actual vs predicted price chart, YoY growth, volatility corridor, volume-price correlation
- **Stock Intelligence** — Top stocks by close price, sector liquidity treemap, daily return distribution

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/mufeeedddd/stock-price-forecasting.git
cd stock-price-forecasting

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Flask app
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

## Requirements

Create a `requirements.txt` with:

```
flask
scikit-learn
pandas
numpy
```

---

## Author

**Mufeed T H**  
MSc Statistics with Data Science  
Sree Sankara College, Kalady — MG University

[LinkedIn](https://linkedin.com/in/mufeeedddd) • [GitHub](https://github.com/mufeeedddd)
