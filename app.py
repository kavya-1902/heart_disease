import streamlit as st
import sklearn
import pickle

st.set_page_config(page_title="Diabetes Prediction App", page_icon="icon.png")

pickle_in = open("classifier.pkl","rb")
regressor=pickle.load(pickle_in)
st.title("Diabetes prediction")

a = float(st.number_input("Number of Pregnencies"))
b = float(st.number_input("Glucose"))
c = float(st.number_input("BloodPressure"))
d = float(st.number_input("Skin Thickness"))
e = float(st.number_input("Insulin"))
f = float(st.number_input("Body Mass Index"))
g = float(st.number_input("Diabetes Pedigree Function"))
h = float(st.number_input("Age"))


btn = st.button("predict")

if btn:
    prediction=regressor.predict([[a,b,c,d,e,f,g,h]])
    st.subheader("Predicted diabetes:")
    if prediction[0]==1:
        st.text("Yes there is a chance of Diabetes")
    else:
        st.text("There is a no chance of Diabetes")


st.markdown(
    """
    ***
    this app is created by k.kavya 
    """
)
