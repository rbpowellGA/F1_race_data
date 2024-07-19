import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st   


@st.cache_data
def fuelvstemp():
    tm145 = pd.read_csv('data/race_data/TelemetryData_14577742557187250604.csv', low_memory=False)

    plotdf = tm145[['currentLapNum','engineTemperature','fuelInTank','speed','gear','engineRPM']]
    plotdf = plotdf.groupby(['currentLapNum']).mean()

    plt.rcParams.update({'font.size': 16})
    fig, ax = plt.subplots()
    ax.plot(plotdf.index, plotdf.engineTemperature, color = 'green', label = 'Temperature')
    ax.set_xlabel('Lap')
    ax.set_ylabel('Engine Temperature', color='green')
    ax1 = ax.twinx()
    ax1.plot(plotdf.index, plotdf.fuelInTank, color = 'red', label = "Remaining Fuel (liters)")
    ax1.set_ylabel('Remaining Fuel (liters)', color='red')

    st.pyplot(fig)

st.set_page_config(page_title="Fuel Level vs Engine Temperature", page_icon="📊")
st.markdown("# Fuel Level vs Engine Temperature")
st.sidebar.header("Fuel Level vs Engine Temperature")
st.write(
    """This is a two stacked line charts comparing fuel level and engine temp as laps progress."""
)

fuelvstemp()