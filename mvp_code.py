# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:10:20 2023

@author: cadgo
"""


import pandas as pd
import streamlit as st
import altair as alt

@st.cache_data()


def get_data():
    path = ("https://raw.githubusercontent.com/cdav15/webapp/main/Clean_Zillow_Price_Index.csv")
    df = pd.read_csv(path)
    df['City_State'] = df[['City', 'State']].agg(', '.join, axis=1)
    df11 = df.drop(labels=['City','State','City Code', 'Metro', 'County', 'Population Rank','Average_PI'], axis = 1)
    return df11.set_index('City_State')

def raw_data():
    path1 = ("https://raw.githubusercontent.com/cdav15/webapp/main/Clean_Zillow_Price_Index.csv")
    df1 = pd.read_csv(path1)
    df1 = df1.drop(['Average_PI'], axis = 1)
    return df1.set_index('City Code')

try:
    df11 = get_data()
    df12 = get_data()
    dfraw = raw_data()
    st.write("## Zillow Price Index Webapp")
    st.write("### Developed by Chandler Davis")
    st.write('Below, you can take a look at the dataframe used for this project.')
    st.dataframe(dfraw)
    st.write("### Use the following search box to compare the Zillow Price Index between cities to follow housing trends")
    cities = st.multiselect(
        "Choose cities", list(df11.index), ["Indianapolis, IN", "Chicago, IL", "Cincinnati, OH"]
    )
    if not cities:
        st.error("Please select at least one city.")
    else:
        data = df11.loc[cities]
        st.write("### Zillow Price Index", data.sort_index())
        
        data = data.T.reset_index()

        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "Month", "value": "Zillow Price Index"}
        )
        chart = (
             alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="Month:T",
                y=alt.Y("Zillow Price Index:Q", stack=None),
                color="City_State:N",
            )
        )
        st.write("### Zillow Price Index Comparison Graph")
        st.altair_chart(chart, use_container_width=True)

        st.write("### Percentage Change Calculator")
        st.write("The following is a calculator to allow you to view the percentage change of a city's Zillow Price Index over your specified time period")
        st.write("#### City 1:")
        city = st.selectbox("Choose a City", list(df11.index))
        data2 = df11.loc[city]

        date1 = st.selectbox("Choose the start date", list(data2.index))
                             
        default_value = 15           
        date2 = st.selectbox("Choose the end date", list(data2.index), index = default_value)
        
        value1 = data2.loc[date1]
        
        value2 = data2.loc[date2]

        percent_change = ((value2 - value1) / value1) * 100

        st.write(f"Percentage Change for {city}: {percent_change: .2f}%")
        
        st.write("#### City 2:")
        city2 = st.selectbox("Choose a city for comparison", list(df12.index))
        data22 = df12.loc[city2]

        date11 = st.selectbox("Choose the start date", list(data22.index))
                             
        default_value2 = 15           
        date22 = st.selectbox("Choose the end date", list(data22.index), index=default_value2)
        
        value11 = data22.loc[date11]
        
        value22 = data22.loc[date22]

        percent_change2 = ((value22 - value11) / value11) * 100

        st.write(f"Percentage Change for {city2}: {percent_change2: .2f}%")
        
except:
    st.error("Error Present")
    

        
    
    
