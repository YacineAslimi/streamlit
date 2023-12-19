import streamlit as st
import pandas as pd
import numpy as np

st.title('Basic Statistical Analysis App')

data_input = st.text_area("Enter your data, separated by commas:")

if st.button('Analyze'):
    if data_input:
        try:
            # Convert the input data into a list of numbers
            data = np.array(data_input.split(','), dtype=float)

            # Perform basic statistical analysis
            mean = np.mean(data)
            median = np.median(data)
            std_dev = np.std(data)

            # Display the results
            st.write(f"Mean: {mean}")
            st.write(f"Median: {median}")
            st.write(f"Standard Deviation: {std_dev}")
        except ValueError:
            st.error("Please enter a valid list of numbers, separated by commas.")
    else:
        st.warning("Please enter some data.")
