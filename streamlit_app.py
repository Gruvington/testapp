import streamlit as st

# Create a selectbox for navigation
tabs = st.selectbox("Select a tab", ["Tab 1", "Tab 2", "Tab 3"])

# Show different content for each tab
if tabs == "Tab 1":
    st.write("This is content for Tab 1.")
    elif tabs == "Tab 2":
        st.write("This is content for Tab 2.")
        elif tabs == "Tab 3":
            st.write("This is content for Tab 3.")