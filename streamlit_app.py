import streamlit as st
import joblib

# Load trained model and vectorizer
model = joblib.load("src/model.pkl")
vectorizer = joblib.load("src/vectorizer.pkl")

st.title("📱 SMS Spam Classifier")

msg = st.text_area("Apna SMS yahan likhiye:")

if st.button("Predict"):
    if msg.strip() == "":
        st.warning("⚠️ Kripya ek message likhiye.")
    else:
        data = vectorizer.transform([msg])
        result = model.predict(data)[0]
        if result == 1:
            st.error("🚫 Ye message Spam hai!")
        else:
            st.success("✅ Ye message Safe hai!")
