# import streamlit as st
# import matplotlib.pyplot as plt

# # Page configuration
# st.set_page_config(page_title="Working Capital Calculator", layout="centered")

# # Title and description
# st.title("Working Capital Calculator")
# st.write("Calculate MPBF (Maximum Permissible Bank Finance) and DP (Drawing Power)")

# # Input fields
# tca = st.number_input("Total Current Assets (TCA)", min_value=0.0, format="%f")
# ocl = st.number_input("Other Current Liabilities (OCL)", min_value=0.0, format="%f")

# # Calculate button
# if st.button("Calculate"):
#     # Calculations
#     wcg = tca - ocl
#     min_nwc = tca * 0.25
#     mpbf = (tca - min_nwc) * 0.75
#     dp = mpbf

#     # Display results
#     st.subheader("Results")
#     st.write(f"**Working Capital Gap (WCG):** ₹{wcg:.2f}")
#     st.write(f"**Minimum Stipulated NWC:** ₹{min_nwc:.2f}")
#     st.write(f"**Maximum Permissible Bank Finance (MPBF):** ₹{mpbf:.2f}")
#     st.write(f"**Drawing Power (DP):** ₹{dp:.2f}")

#     # Plotting the bar chart
#     st.subheader("Visualization")
#     fig, ax = plt.subplots()
#     labels = ["WCG", "Min NWC", "MPBF", "DP"]
#     values = [wcg, min_nwc, mpbf, dp]
#     colors = ["#4299e1", "#38b2ac", "#ed8936", "#ed64a6"]
#     ax.bar(labels, values, color=colors)
#     ax.set_ylabel("Amount in INR")
#     ax.set_title("Working Capital Components")
#     st.pyplot(fig)

# # Explanation of calculations
# with st.expander("See calculation logic"):
#     st.write("""
#     1. **Working Capital Gap (WCG):** WCG = TCA - OCL  
#     2. **Minimum Stipulated Net Working Capital (NWC):** NWC = 25% of TCA  
#     3. **Maximum Permissible Bank Finance (MPBF):** MPBF = (TCA - NWC) * 0.75  
#     4. **Drawing Power (DP):** DP = MPBF  
#     """)


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Title and description
st.title("Working Capital Calculator")
st.write("Calculate MPBF (Maximum Permissible Bank Finance) and DP (Drawing Power)")

# Inputs
tca = st.number_input("Total Current Assets (TCA)", min_value=0.0, format="%.2f")
ocl = st.number_input("Other Current Liabilities (OCL)", min_value=0.0, format="%.2f")

# Calculation function
def calculate_working_capital(tca, ocl):
    wcg = tca - ocl
    min_nwc = tca * 0.25
    mpbf = (tca - min_nwc) * 0.75
    dp = mpbf
    return wcg, min_nwc, mpbf, dp

# Button for calculation
if st.button("Calculate"):
    wcg, min_nwc, mpbf, dp = calculate_working_capital(tca, ocl)

    # Display results
    st.subheader("Calculation Results")
    st.write(f"**Working Capital Gap (WCG):** ₹{wcg:.2f}")
    st.write(f"**Minimum Stipulated NWC:** ₹{min_nwc:.2f}")
    st.write(f"**MPBF:** ₹{mpbf:.2f}")
    st.write(f"**DP:** ₹{dp:.2f}")

    # Data for bar chart
    results_data = pd.DataFrame({
        "Metric": ["WCG", "Min NWC", "MPBF", "DP"],
        "Amount": [wcg, min_nwc, mpbf, dp]
    })

    # Bar chart
    fig = px.bar(results_data, x="Metric", y="Amount", title="Working Capital Metrics", labels={"Amount": "INR"}, text_auto=True)
    st.plotly_chart(fig)

    # Explanation of calculations
with st.expander("See detailed calculation logic"):
    st.write("""
    ### Calculation Steps:
    1. **Working Capital Gap (WCG):** WCG = TCA - OCL  
       This represents the difference between your total current assets and other current liabilities, indicating the amount available for day-to-day operations.

    2. **Minimum Stipulated Net Working Capital (NWC):**  
       Net Working Capital is set at 25% of TCA to ensure a healthy liquidity buffer.

    3. **Maximum Permissible Bank Finance (MPBF):**  
       MPBF represents the maximum loan allowed by the bank, calculated as 75% of the balance left after covering the Minimum Stipulated NWC.

    4. **Drawing Power (DP):**  
       Drawing Power is the actual finance available, set equal to MPBF in this calculation.
    """)
