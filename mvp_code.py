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
    return df1.set_index('City Code')

try:
    df11 = get_data()
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
        st.altair_chart(chart, use_container_width=True)
except:
    st.error("Error Present")
    

        
    
    
