import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st   


@st.cache_data
def speedvsbrake():

    tm145 = pd.read_csv('data/race_data/TelemetryData_14577742557187250604.csv', low_memory=False)

    lapfilter = tm145['currentLapNum'] < 36
    tm145 = tm145[lapfilter]
    tm145 = tm145.replace([0], np.NaN)

    

    tm145[['TempBrake1', 'TempBrake2',  'TempBrake3', 'TempBrake4']] = tm145['brakesTemperature'].str.split('/', expand=True)

    tm145[['TempBrake1', 'TempBrake2',  'TempBrake3', 'TempBrake4']] = tm145[['TempBrake1', 'TempBrake2',  'TempBrake3', 'TempBrake4']].astype(float)

    plotdf2 = tm145[['currentLapNum','speed','TempBrake1','TempBrake2','TempBrake3','TempBrake4']]
    plotdf2 = plotdf2.groupby(['currentLapNum']).mean()

    speed_filter = plotdf2['speed'] > 190

    plotdf2 = plotdf2[speed_filter]

    fig,ax = plt.subplots()
    ax.plot(plotdf2.index, plotdf2['speed'], color = 'blue', label = 'speed')
    ax.set_xlabel('Lap')
    ax.set_ylabel('Speed', color='Blue')
    ax.set_ylim([190, 210])
    ax1 = ax.twinx()
    ax1.plot(plotdf2.index, plotdf2['TempBrake1'], color = 'orange', label = "Brake Temperature")
    ax1.set_ylabel("Brake Temperature", color='orange')

    st.pyplot(fig)

st.set_page_config(page_title="Speed vs Brake Temperature", page_icon="📊")
st.markdown("# Speed vs Brake Temperature")
st.sidebar.header("Speed vs Brake Temperature")
st.write(
    """This is two stacked line charts comparing speed vs brake temperature"""
)

speedvsbrake()