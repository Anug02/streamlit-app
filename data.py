import pandas as pd 
import streamlit as st

df =pd.read_csv("C:\\Users\Anurag\\Downloads\\abalone.csv")
st.subheader('1. Displaying the whole DataFrame.')
st.dataframe(df)

st.subheader('2. Displaying the head of DataFrame.')
st.dataframe(df.head())

st.subheader('3. Displaying the tail of DataFrame.')
st.dataframe(df.tail())

st.subheader('4. Displaying the table as DataFrame of first 10 rows')
st.table(df.head(10))

st.title('5 .Displaying the JSON')
js =[{'pid' :1,'name' :'5star'},
    {'pid' :2,'name' :'Milk-Bar'},
    {'pid' :3,'name' :'Multigrain Bread'},
    {'pid' :4,'name' :'Butter'},
    {'pid' :5,'name' :'Dairy Milk'}]

st.json(js)

st.subheader('6. Displaying the description of data')
st.table(df.describe())