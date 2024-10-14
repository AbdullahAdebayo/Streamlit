import streamlit as st
import yfinance as yf
import pandas as pd

st.title('Simple Stock Price')

tickerSymbol = 'MSFT'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = '3mo' , start = '2017-08-02' , end = '2017-11-01')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


#Task2
import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Stock Price Viewer")

tickerSymbol = "MSFT"

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = "5y" , interval = '1mo' , start = '1990-02-01' , end = '1995-02-01')

st.line_chart(tickerDf.Close)