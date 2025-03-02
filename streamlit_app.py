import streamlit as st
from make_trial import make_trial

# Create a selectbox for navigation
tabs = st.selectbox("Select a tab", ["Make Trial", "Make Analysis Datasets", "Review"])

# Show different content for each tab
if tabs == "Make Trial":
    make_trial(st)
elif tabs == "Make Analysis Datasets":
    st.write("This is content for Tab 2.")
elif tabs == "Review":
    st.write("This is content for Tab 3.")