import streamlit as st

st.title("Streamlit Demo")
st.subheader("Enter your details")
name = st.text_input("What is your name?")
age = st.number_input("How old are you?", min_value=0, max_value=100)

if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old")