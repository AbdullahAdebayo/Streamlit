import yfinance as yf 
import streamlit as st 
import pandas as pd

st.write( """
         
          # Simple Stock Price App \n Here is the Opening,Closing Price nad Volume of Microsoft,Tesla and Apple in the past 6 months! 
         
         
         """)
    

tickerSymbols = ["MSFT" , "TSLA" , "AAPL"] 

interval = "1w"

tickerData = yf.download(tickerSymbols , period= "6mo")


print(tickerData.Open)
print(tickerData.Close)
print(tickerData.Volume)

st.line_chart(tickerData.Open)
st.line_chart(tickerData.Close)
st.line_chart(tickerData.Volume)