import pandas as pd

def make_trial(st):
   st.write("making a trial")




   # Create a sample dataframe
   data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

   df = pd.DataFrame(data)

   # Display the dataframe as a table
   st.write("Sample DataFrame")
   st.dataframe(df)