import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st   


@st.cache_data
def single_driver():

    tm145 = pd.read_csv('data/race_data/TelemetryData_14577742557187250604.csv', low_memory=False)

    lapfilter = tm145['currentLapNum'] < 36
    tm145 = tm145[lapfilter]
    tm145 = tm145.replace([0], np.NaN)

    pilot_filter = tm145.pilot_index == 10
    tm_145_pilot1 = tm145[pilot_filter]
    
    plt.rcParams.update({'font.size': 14})
    df = tm_145_pilot1[['gForceLateral', 'gForceLongitudinal',
        'yaw', 'pitch', 'roll', 'speed', 'throttle', 'steer',
        'brake', 'gear', 'engineRPM', 'brakesTemperature',
        'tyresSurfaceTemperature', 'tyresInnerTemperature', 'engineTemperature',
        'tyresPressure', 'surfaceType', 'fuelInTank', 'tyresWear',
        'carPosition', 'currentLapNum', 'totalDistance']].corr(numeric_only=True)
    fig, ax = plt.subplots()
    #fig.subplots_adjust(wspace=0.01)


    sns.heatmap(df, cmap="vlag", ax=ax, cbar=False, linewidths=.5)#.set_xticklabels(sns.heatmap(df, cmap="vlag", ax=ax, cbar=False, linewidths=.5).get_xticklabels(), rotation=45, ha='right')
    #sns.heatmap(tm145_1.corr(numeric_only=True), cmap="plasma", ax=ax2, cbar=False, linewidths=.5)
    plt.xticks(rotation=45, ha ='right')
    plt.yticks(rotation=45, va ='top')

    st.pyplot(fig)

st.set_page_config(page_title="Single Driver Heatmap", page_icon="📊")
st.markdown("# Single Driver Heatmap")
st.sidebar.header("Single Driver Heatmap")
st.write(
    """This is a heatmap correlation for a single driver in the F1 Dataset"""
)

single_driver()


