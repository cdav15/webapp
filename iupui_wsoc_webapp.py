# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 16:44:14 2023

@author: cadgo
"""

import pandas as pd
import streamlit as st
from urllib.request import urlopen
import matplotlib.pyplot as plt
from PIL import Image
from highlight_text import fig_text
from mplsoccer import PyPizza, add_image, FontManager
import numpy as np
from scipy import stats
import math

@st.cache_data()

def get_data():
    df = pd.read_csv('https://raw.githubusercontent.com/cdav15/webapp/main/IUPUI_WSOC_FORWARDS.csv')
    return df.set_index("Player")

def get_data2():
    df2 = pd.read_csv('https://raw.githubusercontent.com/cdav15/webapp/main/Horizon_League_Goalkeepers.csv')
    return df2.set_index("Player")

try:
    df = get_data()
    st.write("# Chandler Davis Portfolio Project")
    st.write("#### Forwards, Midfielders, Defenders")
    df = df.drop(columns=['Position'])
    player_select = st.selectbox(
        "Choose one player", list(df.index)
    )
    if not player_select:
        st.error("Please Select a Player.")
    else:
        data = df.loc[[player_select]]
        
        st.write("### Player Stats", data)

        params = list(df.columns)
        
        player = df.loc[[player_select]].reset_index()
        player = list(player.loc[0])
        player = player[1:]
        
        values = []
        for x in range(len(params)):
            values.append(math.floor(stats.percentileofscore(df[params[x]],player[x])))
            
        font_normal = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/roboto/'
                                  'Roboto%5Bwdth,wght%5D.ttf')
        font_italic = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/roboto/'
                                  'Roboto-Italic%5Bwdth,wght%5D.ttf')
        font_bold = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
                                'RobotoSlab%5Bwght%5D.ttf')
            
        baker = PyPizza(
        params=params,                  # list of parameters
        straight_line_color="#000000",  # color for straight lines
        straight_line_lw=1,             # linewidth for straight lines
        last_circle_lw=1,               # linewidth of last circle
        other_circle_lw=1,              # linewidth for other circles
        other_circle_ls="-."            # linestyle for other circles
        )

        # plot pizza
        fig, ax = baker.make_pizza(
            values,              # list of values
            figsize=(12, 12),      # adjust figsize according to your need
            param_location=110,  # where the parameters will be added
            kwargs_slices=dict(
                facecolor="cornflowerblue", edgecolor="#000000",
                zorder=2, linewidth=1
            ),                   # values to be used when plotting slices
            kwargs_params=dict(
                color="#000000", fontsize=10, fontproperties=font_normal.prop,
                va="center"
            ),                   # values to be used when adding parameter
            kwargs_values=dict(
                color="#000000", fontsize=12,  fontproperties=font_normal.prop,
                zorder=3,
                bbox=dict(
                    edgecolor="#000000", facecolor="cornflowerblue",
                    boxstyle="round,pad=0.2", lw=1
                )
            )                    # values to be used when adding parameter-values
        )

        # add title
        fig.text(
            0.515, 0.97, player_select, size=18,
            ha="center",  fontproperties=font_bold.prop, color="#000000"
        )

        # add subtitle
        fig.text(
            0.515, 0.942,
            "per 90 min Percentile Rank compared to teammates",
            size=15,
            ha="center", fontproperties=font_normal.prop, color="#000000"
        )

        # add credits
        CREDIT_1 = "Data: Wyscout, compiled together by Chandler Davis"
        CREDIT_2 = ""

        fig.text(
            0.99, 0.005, f"{CREDIT_1}\n{CREDIT_2}", size=9,
            fontproperties=font_italic.prop, color="#000000",
            ha="right"
        )

        st.pyplot(fig)
###########################################################################
###########################################################################

        st.write("#### Comparison Chart")
        players = st.multiselect(
            "Choose two players", list(df.index), ['C. Kelley', 'E. Antoine']
        )
        datas = df.loc[players]
        
        st.write("### Player Stats", datas)
        
        p1 = datas.index[0]
        p2 = datas.index[1]        
        
        params3 = list(df.columns)
        
        player3 = df.loc[[p1]].reset_index()
        player3 = list(player3.loc[0])
        player3 = player3[1:]
        
        values3 = []
        for x in range(len(params3)):
            values3.append(math.floor(stats.percentileofscore(df[params3[x]],player3[x])))
       
        player4 = df.loc[[p2]].reset_index()
        player4 = list(player4.loc[0])
        player4 = player4[1:]
        
        values4 = []
        for x in range(len(params3)):
            values4.append(math.floor(stats.percentileofscore(df[params3[x]],player4[x]))) 
            
        baker3 = PyPizza(
            params=params3,                 
            background_color="#EBEBE9",     
            straight_line_color="#222222",
            straight_line_lw=1,             
            last_circle_lw=1,               
            last_circle_color="#222222",    
            other_circle_ls="-.",           
            other_circle_lw=1               
        )


        fig3, ax3 = baker3.make_pizza(
            values3,                     
            compare_values=values4,    
            figsize=(12, 12),             
            kwargs_slices=dict(
                facecolor="#1A78CF", edgecolor="#222222",
                zorder=2, linewidth=1
            ),                          
            kwargs_compare=dict(
                facecolor="#FF9300", edgecolor="#222222",
                zorder=2, linewidth=1,
            ),
            kwargs_params=dict(
                color="#000000", fontsize=10,
                fontproperties=font_normal.prop, va="center"
            ),                          
            kwargs_values=dict(
                color="#000000", fontsize=12,
                fontproperties=font_normal.prop, zorder=3,
                bbox=dict(
                    edgecolor="#000000", facecolor="cornflowerblue",
                    boxstyle="round,pad=0.2", lw=1
                )
            ),                          
            kwargs_compare_values=dict(
                color="#000000", fontsize=12, fontproperties=font_normal.prop, zorder=3,
                bbox=dict(edgecolor="#000000", facecolor="#FF9300", boxstyle="round,pad=0.2", lw=1)
            ),                          
        )

        fig_text(
            0.515, 0.99, f"<{p1}> vs <{p2}>", size=17, fig=fig3,
            highlight_textprops=[{"color": '#1A78CF'}, {"color": '#EE8900'}],
            ha="center", fontproperties=font_bold.prop, color="#000000"
        )

        fig3.text(
            0.515, 0.942,
            "IUPUI Women's Soccer Player Comparison",
            size=15,
            ha="center", fontproperties=font_bold.prop, color="#000000"
        )

        CREDIT_1 = "data: Wyscout, compiled together by Chandler Davis"
        CREDIT_2 = ""

        fig3.text(
            0.99, 0.005, f"{CREDIT_1}\n{CREDIT_2}", size=9,
            fontproperties=font_italic.prop, color="#000000",
            ha="right"
        )

        st.pyplot(fig3)
###########################################################################
###########################################################################

        st.write('## Goalkeepers')
        df2 = get_data2()
        df2 = df2.drop(columns=['Team'])
        player_select2 = st.selectbox(
            "Choose one goalkeeper", list(df2.index)
        )
        data2 = df2.loc[[player_select2]]
        
        st.write("### Goalkeeper Stats", data2)
        
        df2['Conceded Goals'] *= -1
        df2['xCG'] *= -1
        df2['Shots Against'] *= -1
        
        params2 = list(df2.columns)
        
        player2 = df2.loc[[player_select2]].reset_index()
        player2 = list(player2.loc[0])
        player2 = player2[1:]
        
        values2 = []
        for x in range(len(params2)):
            values2.append(math.floor(stats.percentileofscore(df2[params2[x]],player2[x])))
        
        baker2 = PyPizza(
            params=params2,                  # list of parameters
            straight_line_color="#000000",  # color for straight lines
            straight_line_lw=1,             # linewidth for straight lines
            last_circle_lw=1,               # linewidth of last circle
            other_circle_lw=1,              # linewidth for other circles
            other_circle_ls="-."            # linestyle for other circles
        )

        # plot pizza
        fig2, ax2 = baker2.make_pizza(
            values2,              # list of values
            figsize=(12, 12),      # adjust figsize according to your need
            param_location=110,  # where the parameters will be added
            kwargs_slices=dict(
                facecolor="cornflowerblue", edgecolor="#000000",
                zorder=2, linewidth=1
            ),                   # values to be used when plotting slices
            kwargs_params=dict(
                color="#000000", fontsize=10, fontproperties=font_normal.prop,
                va="center"
            ),                   # values to be used when adding parameter
            kwargs_values=dict(
                color="#000000", fontsize=12,  fontproperties=font_normal.prop,
                zorder=3,
                bbox=dict(
                    edgecolor="#000000", facecolor="cornflowerblue",
                    boxstyle="round,pad=0.2", lw=1
                )
            )                    # values to be used when adding parameter-values
        )

        # add title
        fig2.text(
            0.515, 0.97, player_select2, size=18,
            ha="center",  fontproperties=font_bold.prop, color="#000000"
        )

        # add subtitle
        fig2.text(
            0.515, 0.942,
            "per 90 min Percentile Rank compared to Horizon League Goalkeepers",
            size=15,
            ha="center", fontproperties=font_normal.prop, color="#000000"
        )

        # add credits
        CREDIT_1 = "Data: Wyscout, compiled together by Chandler Davis"
        CREDIT_2 = ""

        fig2.text(
            0.99, 0.005, f"{CREDIT_1}\n{CREDIT_2}", size=9,
            fontproperties=font_italic.prop, color="#000000",
            ha="right"
        )

        st.pyplot(fig2)
#################################################################################
#################################################################################
        df2['Conceded Goals'] *= -1
        df2['xCG'] *= -1
        df2['Shots Against'] *= -1
        
        st.write("#### Goalkeeper Comparison Chart")
        players2 = st.multiselect(
            "Choose two players", list(df2.index), ['A. Kudlo', 'C. Junk']
        )
        datas2 = df2.loc[players2]
        
        st.write("### Goalkeeper Stats", datas2)
        
        df2['Conceded Goals'] *= -1
        df2['xCG'] *= -1
        df2['Shots Against'] *= -1
        
        p11 = datas2.index[0]
        p22 = datas2.index[1]        
        
        params4 = list(df2.columns)
        
        player5 = df2.loc[[p11]].reset_index()
        player5 = list(player5.loc[0])
        player5 = player5[1:]
        
        values5 = []
        for x in range(len(params4)):
            values5.append(math.floor(stats.percentileofscore(df2[params4[x]],player5[x])))
       
        player6 = df2.loc[[p22]].reset_index()
        player6 = list(player6.loc[0])
        player6 = player6[1:]
        
        values6 = []
        for x in range(len(params4)):
            values6.append(math.floor(stats.percentileofscore(df2[params4[x]],player6[x]))) 
            
        baker4 = PyPizza(
            params=params4,                 
            background_color="#EBEBE9",     
            straight_line_color="#222222",
            straight_line_lw=1,             
            last_circle_lw=1,               
            last_circle_color="#222222",    
            other_circle_ls="-.",           
            other_circle_lw=1               
        )


        fig4, ax4 = baker4.make_pizza(
            values5,                     
            compare_values=values6,    
            figsize=(12, 12),             
            kwargs_slices=dict(
                facecolor="#1A78CF", edgecolor="#222222",
                zorder=2, linewidth=1
            ),                          
            kwargs_compare=dict(
                facecolor="#FF9300", edgecolor="#222222",
                zorder=2, linewidth=1,
            ),
            kwargs_params=dict(
                color="#000000", fontsize=10,
                fontproperties=font_normal.prop, va="center"
            ),                          
            kwargs_values=dict(
                color="#000000", fontsize=12,
                fontproperties=font_normal.prop, zorder=3,
                bbox=dict(
                    edgecolor="#000000", facecolor="cornflowerblue",
                    boxstyle="round,pad=0.2", lw=1
                )
            ),                          
            kwargs_compare_values=dict(
                color="#000000", fontsize=12, fontproperties=font_normal.prop, zorder=3,
                bbox=dict(edgecolor="#000000", facecolor="#FF9300", boxstyle="round,pad=0.2", lw=1)
            ),                          
        )

        fig_text(
            0.515, 0.99, f"<{p11}> vs <{p22}>", size=17, fig=fig4,
            highlight_textprops=[{"color": '#1A78CF'}, {"color": '#EE8900'}],
            ha="center", fontproperties=font_bold.prop, color="#000000"
        )

        fig4.text(
            0.515, 0.942,
            "Horizon League Goalkeeper Comparison",
            size=15,
            ha="center", fontproperties=font_bold.prop, color="#000000"
        )

        CREDIT_1 = "data: Wyscout, compiled together by Chandler Davis"
        CREDIT_2 = ""

        fig4.text(
            0.99, 0.005, f"{CREDIT_1}\n{CREDIT_2}", size=9,
            fontproperties=font_italic.prop, color="#000000",
            ha="right"
        )

        st.pyplot(fig4)
except:
    st.error( "Error Present")
