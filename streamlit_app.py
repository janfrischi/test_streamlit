import streamlit as st

st.set_page_config(page_title="My Streamlit App", page_icon="🚀")

st.title("🚀 Welcome to My Streamlit App")

st.write("This is a basic Streamlit application!")

# Add some interactive widgets
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! 👋")

# Add a slider
age = st.slider("Select your age", 0, 100, 25)
st.write(f"You are {age} years old")

# Add a selectbox
favorite_color = st.selectbox(
    "What's your favorite color?",
    ["Red", "Blue", "Green", "Yellow", "Purple"]
)
st.write(f"Your favorite color is {favorite_color}")

# Add a button
if st.button("Click me!"):
    st.balloons()
    st.success("Thanks for clicking! 🎉")