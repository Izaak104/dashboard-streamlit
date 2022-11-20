#import libraries
import pandas as pd
import streamlit as st
import numpy as np

#load dataset
df = pd.read_csv('vaccination_data.csv')
df = df.dropna()

#create title and header for the app
st.title('WHO Covid Vaccinations Data')
st.header('This dataset represents reports on covid vaccinations administered around the world')
st.write(df)

#create new dataframe with chosen columns
df1 = df.iloc[: , [2, 5, 12, 14]].copy()

#create Dataframe
df2 =pd.DataFrame(df1)
df2

##creating new dashboard for selected columns
df2.to_csv('relevant_data.csv')
df2
#df2 = pd.read_csv('relevant_data.csv')
st.header('WHO Regions and Total Vaccinations')
st.write(df2)

#create bar chart
st.header("Bar Chart")

data = {"a":['WHO_REGION'], "b":['TOTAL_VACCINATIONS'], 
"c":['FIRST_VACCINE_DATE']}

df3 = pd.DataFrame(data)
df3

st.bar_chart(data=df3)












