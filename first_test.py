import streamlit as st
import yfinance as yf
import pandas as pd

st.title('Simple Stock Price')

tickerSymbol = 'MSFT'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = '3mo' , start = '2017-08-02' , end = '2017-11-01')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)