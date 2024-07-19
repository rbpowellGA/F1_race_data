
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


@st.cache_data
def heatmap():
   
    tm145 = pd.read_csv('data/race_data/TelemetryData_14577742557187250604.csv', low_memory=False)

    lapfilter = tm145['currentLapNum'] < 36
    tm145 = tm145[lapfilter]
    tm145 = tm145.replace([0], np.NaN)

    tm145_1 = tm145[['worldVelocityX', 'worldVelocityY',
        'worldVelocityZ', 'gForceLateral', 'gForceLongitudinal',
        'gForceVertical', 'yaw', 'pitch', 'roll', 'speed', 'throttle', 'steer',
        'brake', 'clutch', 'gear', 'engineRPM', 'brakesTemperature',
        'tyresSurfaceTemperature', 'tyresInnerTemperature', 'engineTemperature',
        'tyresPressure', 'surfaceType', 'fuelInTank', 'fuelRemainingLaps', 'tyresWear',
        'carPosition', 'currentLapNum', 'totalDistance']]#corr(numeric_only=True)

    tm145_1.corr(numeric_only=True)

    fig, ax = plt.subplots(figsize=(12,8))
    sns.heatmap(tm145_1.corr(numeric_only=True),linewidth=.5,linecolor='black')
    st.pyplot(fig)


st.set_page_config(page_title="Correlation Heatmap", page_icon="📊")
st.markdown("# Correlation Heatmap")
st.sidebar.header("Correlation Heatmap")
st.write(
    """This is a heatmap correlation for all numeric columns in the F1 Dataset"""
)

heatmap()

