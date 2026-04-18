from flask import Flask, render_template, request
import pandas as pd
import pickle
import os
from sklearn.metrics import r2_score, mean_absolute_error

app = Flask(__name__)

# ── Absolute paths ─────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR, 'model.pkl'), 'rb'))
df    = pd.read_excel(os.path.join(BASE_DIR, 'all_stocks_5yr.xlsx'))

# ── Model evaluation ───────────────────────────────────────────
X_eval      = df[['close']].iloc[:-1]
y_eval      = df['close'].shift(-1).dropna()
y_pred_eval = model.predict(X_eval)

metrics = {
    "r2":     round(r2_score(y_eval, y_pred_eval), 4),
    "mae":    round(mean_absolute_error(y_eval, y_pred_eval), 2),
    "method": "Ordinary Least Squares (OLS)",
    "note":   "Evaluated using time-based split to avoid data leakage"
}

prediction_note = "Prediction based on historical trend. Accuracy may vary during volatile market conditions."

# ── Routes ────────────────────────────────────────────────────
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            input_price = float(request.form['price'])

            if input_price <= 0:
                raise ValueError("Price must be a positive number.")
            if input_price > 100000:
                raise ValueError("Price seems unrealistically high. Please check your input.")

            prediction = model.predict([[input_price]])[0]

            return render_template(
                'new.html',
                prediction=round(float(prediction), 2),
                original=round(input_price, 2),
                metrics=metrics,
                note=prediction_note
            )

        except Exception as e:
            return render_template('new.html', error=str(e), metrics=metrics, note=prediction_note)

    return render_template('new.html', metrics=metrics, note=prediction_note)

@app.route('/contact')
def contact():
    return render_template('contact.html', metrics=metrics)

if __name__ == '__main__':
    app.run(debug=True)