from pathlib import Path  # Python Standard Library
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import streamlit as st
import altair as alt
import pyxlsb
import git
import time
import datetime as dt
from datetime import datetime, timezone,timedelta

# Page setting
st.set_page_config(layout="wide")

# dashboard title
st.subheader("Real-Time / Live Data Dashboard: ")

this_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
wb_file_path = this_dir / 'OLenMaster_v1.xlsb'

df = pd.read_excel(
                io=wb_file_path,
                engine='pyxlsb',
                sheet_name='eWon',
                skiprows=18,
                usecols='BL:BY',
                nrows=1441,
                )
        #print(df)

        #  ----- SideBar  ____
ySelect = st.sidebar.selectbox(label="Select Scale", options=["LFC8","LC2", "LC7","LC17","LC20","LC14"])

        #Add Refresh Date
Today_Date=str(dt.datetime.now())
                        
        # convert datetime column to just date
chart = alt.Chart(df).mark_line().encode(
                        x=alt.X('DateTime', axis=alt.Axis(labelOverlap="greedy",grid=False)),
                        y=alt.Y(ySelect))

st.altair_chart(chart, use_container_width= True)

thistime=datetime.now(timezone(timedelta(hours=-5), 'EST'))
#st.write(thistime)

timenow = thistime.strftime("%m-%d-%y %H:%M:%S")  
st.markdown(f"{ySelect} Scale :  last updated on -- {timenow}")





#Refresh Delay
time.sleep(30)
#st.experimental_rerun()