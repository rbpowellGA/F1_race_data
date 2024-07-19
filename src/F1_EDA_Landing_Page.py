import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="F1 Analysis",
        
    )

    st.write("# F1 Analysis Landing Page")

    st.sidebar.success("Select chart above.")

    st.markdown(
        """
        ## **Overview**
The following EDA aims to use python data analysis libraries to determine correlations between telemetry subsystems in simulated F1 race vehicles. I'll also explore race outcomes that can be derived purely from telemetered data. For this analysis I'll be using simulated telemetry from F1 2020.

## **Telemetry**
Telemetry can be described as the measurement and transmission of instrument readings.  Example: Engine temperature readings being wirelessly transmitted to the pit crew. These readings help to determine the status and health of various subsystems and assist in operation and maintenance of the overall system.

## **Dataset**
The dataset used for this EDA was pulled from kaggle : https://www.kaggle.com/datasets/coni57/f1-2020-race-data?select=TelemetryData_10230136787177318441.csv.
The data includes telemetry from 20 drivers across 22 simulated races.  The data frame for each race contains over 1,250,000 records for 56 telemetry categories. For this EDA, I'll primarily use the data frame from a single race.
    """
    )


if __name__ == "__main__":
    run()