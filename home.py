import streamlit as st

btn1 = st.button('Say hello')
if btn1:
    st.write('Why hello there')

def btn1_click():
    st.write('btn clicked!')

def btn2_click():
    st.write('btn2 clicked!')    

btn2 = st.button('Say hello world', on_click=btn1_click)

state=st.checkbox('Show state', value=True, on_change=btn2_click)

sb=st.selectbox('Select box', options=['apple','banana','tomato'], 
                index=0, on_change=btn2_click)
st.write(sb)

sb2=st.multiselect('Select box', options=['apple','banana','tomato'], 
                   default=['apple','banana'])
st.write(sb2)

sb3=st.slider('Select box', min_value=0, 
              max_value=100, value=50, step=5)


image=st.file_uploader('File uploader', type=['png', 'jpg'])
if image is not None:
    st.image(image)

video=st.file_uploader('File uploader', type=['mp4'])
if video is not None:
    st.video(video)

data=st.file_uploader('File uploader', type=['txt'])
if data is not None:
    file=data.read()
    st.write(file)



val=st.text_input('Text input', value='default')
st.write(val)

val2=st.number_input('Number input', value=10)
st.write(val2)

val3=st.text_area('Text area', value='default')
st.write(val3)

val4=st.date_input('Date input', value=None)
st.write(val4)

val5=st.time_input('Time input', value=None)
st.write(val5)

val6=st.color_picker('Color picker', value='#000000')
st.write(val6)

val7=st.radio('Radio', options=['apple','banana','tomato'])
st.write(val7)

val8=st.checkbox('Checkbox', value=True)
st.write(val8)

import time


bar=st.progress(0)
# for i in range(100):
#     bar.progress(i+1)
#     time.sleep(0.1)


form=st.form(key='my_form')
name=form.text_input('Enter your name')
submit=form.form_submit_button('Submit')
if submit:
    st.write('Your name is', name)


form=st.form(key='my_form2')
fname=form.text_input('Enter your first name')
lname=form.text_input('Enter your last name')
submit2=form.form_submit_button('Submit')
if submit2:
    st.write('Your name is', fname, lname)


with st.form(key='my_form3'):
    col1, col2 = st.columns(2)
    fname=col1.text_input('Enter your first name')
    lname=col2.text_input('Enter your last name')
    submit3=st.form_submit_button('Submit')
    if submit3:
        st.write('Your name is', fname, lname)


expander=st.expander('FAQ')
expander.write('Here you could put in some really, really long explanations...')


with st.spinner('Wait for it...'):
    time.sleep(5)


st.success('Done!')

st.error('This is an error')

st.warning('This is a warning')

st.info('This is a purely informational message')

st.exception('This is an exception message')

st.help(st.button)


# sidebar
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


st.sidebar.title('This is a sidebar')

st.sidebar.subheader('This is a subheader')

st.sidebar.text('This is a text')

table=pd.DataFrame()










