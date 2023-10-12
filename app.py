from flask import Flask, render_template, request, Response
import yfinance as yf
import pandas as pd 

ticker = "AAPL"
stock_data = yf.download(ticker, start='2023-10-10', end='2023-10-12')
finance_df = pd.DataFrame(stock_data)


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', data=finance_df, len=len(finance_df))

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
