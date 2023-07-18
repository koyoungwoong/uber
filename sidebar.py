import streamlit as st
import numpy as np
import pandas as pd 
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


iris_dataset = load_iris()


st.sidebar.title('iris 정보')

df= pd.DataFrame(data=iris_dataset.data,columns= iris_dataset.feature_names)
# df

df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다
df['species']= iris_dataset.target 


species_dict = {0 :'setosa', 1 :'versicolor', 2 :'virginica'} 

def mapp_species(x):
  return species_dict[x]


df['species'] = df['species'].apply(mapp_species)
print(df)

select_species = st.sidebar.selectbox(
    '확인하고 싶은 종을 선택하세요',
    ['setosa','versicolor','virginica']
)

tmp_df = df[df['species']== select_species]

st.table(tmp_df.head())


select_multi_species = st.sidebar.multiselect(
    '확인하고자 하는 종을 선택해 주세요. 복수선택가능',
    ['setosa','versicolor','virginica']

)

tmp_df = df[df['species'].isin(select_multi_species)]
st.table(tmp_df)



radio_select =st.sidebar.radio(
    "what is key column?",
    ['sepal length', 'sepal width', 'petal length','petal width'],
    horizontal=True
    )

slider_range = st.sidebar.slider(
    "choose range of key column",
     0.0, #시작 값 
     10.0, #끝 값  
    (2.5, 7.5) # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정가능
)

start_button = st.sidebar.button(
    "filter apply 📊 "#"버튼에 표시될 내용"
)

if start_button:
    tmp_df = df[df['species'].isin(select_multi_species)]
    tmp_df= tmp_df[ (tmp_df[radio_select] >= slider_range[0]) & (tmp_df[radio_select] <= slider_range[1])]
    st.table(tmp_df)
    st.sidebar.success("Filter Applied!")


