import streamlit as st

# Create a selectbox for navigation
tabs = st.selectbox("Select a tab", ["Make Trial", "Make Analysis Datasets", "Review"])

# Show different content for each tab
if tabs == "Make Trial":
    st.write("This is content for Tab 1.")
elif tabs == "Make Analysis Datasets":
    st.write("This is content for Tab 2.")
elif tabs == "Review":
    st.write("This is content for Tab 3.")