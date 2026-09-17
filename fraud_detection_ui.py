import streamlit as st
import pandas as pd
import joblib

model = joblib.load("/Users/SAI/Library/Mobile Documents/com~apple~CloudDocs/MS_DS/UCM/Machine Learning/Project Presentation/Fraud Detection/fraud_detection_pipeline.pkl")

# Simpler Title
st.title("🔍 Fraud Detection Prediction App")
st.caption("Enter transaction details to check if it's fraudulent.")

st.divider()

# Split layout
col1, col2 = st.columns(2)

with col1:
    transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
    amount = st.number_input("Amount", min_value=0.0, value=1000.0)
    oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)

with col2:
    newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
    oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
    newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

# Prediction Button
if st.button("🚀 Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result:")
    if prediction == 1:
        st.error("⚠️ This transaction may be fraudulent.")
    else:
        st.success("✅ This transaction appears to be legitimate.")
