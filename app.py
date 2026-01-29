import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Disease Prediction System")

st.title("🩺 Disease Prediction System")
st.write("ML-based disease prediction using symptoms")

# ---------- LOAD DATA ----------
@st.cache_data
def load_data():
    df = pd.read_csv("training.csv")
    return df

df = load_data()

# ---------- SPLIT DATA ----------
X = df.drop("prognosis", axis=1)
y = df["prognosis"]

# ---------- ENCODE OUTPUT ----------
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# ---------- TRAIN MODEL ----------
model = DecisionTreeClassifier()
model.fit(X, y_encoded)

# ---------- UI ----------
st.subheader("Select Symptoms")

selected_symptoms = st.multiselect(
    "Choose all symptoms you have:",
    X.columns.tolist()
)

if st.button("Predict Disease"):
    if len(selected_symptoms) == 0:
        st.warning("Please select at least one symptom")
    else:
        input_data = []
        for symptom in X.columns:
            input_data.append(1 if symptom in selected_symptoms else 0)

        prediction = model.predict([input_data])
        disease = le.inverse_transform(prediction)[0]

        st.success(f"🧠 Predicted Disease: **{disease}**")
