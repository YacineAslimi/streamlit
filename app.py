import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Basic Statistical Analysis App')

# Option for user to choose data input method
data_option = st.selectbox("Choose your data input method", ["Enter Data", "Generate Fake Data"])

data_input = ""
if data_option == "Enter Data":
    data_input = st.text_area("Enter your data, separated by commas:")
elif data_option == "Generate Fake Data":
    if st.button("Generate Data"):
        data_input = ",".join([str(np.random.rand()) for _ in range(100)])

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

            # Create and display a simple plot
            fig, ax = plt.subplots()
            ax.hist(data, bins=20, color='blue', alpha=0.7)
            ax.set_title('Data Distribution')
            ax.set_xlabel('Values')
            ax.set_ylabel('Frequency')
            st.pyplot(fig)

        except ValueError:
            st.error("Please enter a valid list of numbers, separated by commas.")
    else:
        st.warning("Please enter some data or generate fake data.")
