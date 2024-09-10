import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Stock Price Viewer")

tickerSymbol = "MSFT"

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = "5y" , interval = '1mo' , start = '1990-02-01' , end = '1995-02-01')

st.line_chart(tickerDf.Close)