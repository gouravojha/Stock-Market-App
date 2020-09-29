import streamlit as st
from nsetools import Nse
from nsepy import get_rbi_ref_history
from nsepy import get_history
from nsepy import get_index_pe_history
from nsepy.history import get_price_list
from datetime import date
import pandas as pd
import numpy as np

PAGE_CONFIG = {"page_title": "SM APP","layout": "centered"}
st.beta_set_page_config(**PAGE_CONFIG)
nse = Nse()

st.title("The Stock Market App")
st.header("What  changed in the market while you were asleep ?")
if st.button("Check Market"):
      q = nse.get_index_quote("nifty 50")
      r = nse.get_index_quote("nifty 500")
      s = nse.get_index_quote("nifty bank")
      st.write(q)
      st.write(r)
      st.write(s)

st.header("Have a look at the Top gainers today!")
if st.button("Check Gainers"):
      top_gainers = nse.get_top_gainers(10)
      st.write(top_gainers)

st.header("Have a look at the Top losers today!")
if st.button("Check Losers"):
      top_losers = nse.get_top_losers(5)
      st.write(top_losers)

st.header("Analyze Market")
st.markdown("Enter year, month and date to analyze Forex rates , Market valuation and Market Volatility")
sy = int(st.number_input("Enter starting year"))
sm = int(st.number_input("Enter starting  month"))
sd = int(st.number_input("Enter starting  day"))
ey = int(st.number_input("Enter ending year"))
em = int(st.number_input("Enter ending month"))
ed = int(st.number_input("Enter ending date"))
st.header("RBI Currency rates")
st.markdown("USD, GBP, EURO, YEN to INR rbi reference rates")
if st.button("Check Rates"):
      rbi_ref = get_rbi_ref_history(date(sy,sm,sd), date(ey,em,ed))
      st.write(rbi_ref)

st.header("Market Volatility")
st.markdown("India VIX is a volatility index which gives a measurement of market volatility based on NIFTY options contract. This servers as important parameter in option pricing")
if st.button("Check Volatility"):
      vix = get_history(symbol = "INDIAVIX",start = date(sy,sm,sd), end = date(ey,em,ed),index = True)
      st.write(vix)
      st.area_chart(vix[["Close"]])

st.header("Market Valuation")
st.markdown("P/E ratio of a security helps to estimate if the security is over-priced or under-priced and further make investment decisions. P/B value helps determine the intrinsic value of a security with regards to its market price" )
if st.button("Check Valuation"):
      pe = get_index_pe_history(symbol = "NIFTY",start = date(sy,sm,sd), end = date(ey,em,ed))
      st.write(pe)
      st.area_chart(pe[["P/E"]])
      st.line_chart(pe[["P/B"]])

st.header("All stock quotes")
st.markdown("Enter year,date and time to get stock quotes of entire market")
y = int(st.number_input("Enter  year"))
m = int(st.number_input("Enter month"))
d = int(st.number_input("Enter date"))
if st.button("Check Quotes"):
      prices = get_price_list(dt=date(y,m,d))
      st.write(prices)
      
      

      

    
