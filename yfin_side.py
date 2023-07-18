import yfinance as yf
import streamlit as st

st.sidebar.title('stock selection')
pname = 'GOOGL'

form=st.sidebar.form(key='my_form')
name=form.text_input('Enter stock name')
submit=form.form_submit_button('Submit')
if submit:
    tickerSymbol=name
else:
    tickerSymbol=pname
        

st.title('Stock information')
st.title(name)

tickerData = yf.Ticker(tickerSymbol)

st.subheader('Stock information')
expander=st.expander('STOCK INFO')
expander.write(tickerData.info)

st.subheader('Stock Chart')

with st.spinner('Wait for it...'):
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2023-6-30')
st.success('Done!')


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

st.subheader('Stock information: 1 month')
data = yf.download(name, period="1mo")
data
