import streamlit as st

st.set_page_config(page_title="Disease Prediction App")

st.title("🩺 Disease Prediction System")
st.write("This is a demo ML-based disease prediction website.")

symptoms = st.multiselect(
    "Select symptoms:",
    [
        "Fever",
        "Cough",
        "Headache",
        "Fatigue",
        "Sore throat",
        "Nausea"
    ]
)

if st.button("Predict Disease"):
    if "Fever" in symptoms and "Cough" in symptoms:
        st.success("Possible Disease: Flu")
    elif "Headache" in symptoms:
        st.success("Possible Disease: Migraine")
    else:
        st.success("Possible Disease: Common Cold")
