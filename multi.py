import pickle
import streamlit as st
model = pickle.load(open("multi.pkl", "rb"))
def mydeploy():
    st.title("Area Price Prediction App")
    area = st.number_input("Area (in sq ft)")
    age = st.number_input("Age of the house (in years)")
    bedrooms = st.number_input("Number of bedrooms")
    if st.button("Predict"):
        features = [[area, bedrooms, age]]
        x= model.predict(features)[0]
        st.success(f"Price of area is: ₹ {round(x, 2)}")
mydeploy()
