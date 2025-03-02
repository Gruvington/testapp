import pandas as pd

def make_trial(st):
   st.write("making a trial")




   # Create a sample dataframe
   data = {
    'Name': ['Vitacress 1', 'Vitacress 2', 'Flavourfresh 1', 'Flavourfresh 2'],
    'Start Date': ['2024-01-01', '2024-02-17', '2025-03-01', '2025-03-02'],
    'Location': ['Aldergrove', 'Aldergrove', 'Bristop', 'Bristol']
}

   df = pd.DataFrame(data)

   # Hide the row index
   df.index = [''] * len(df)

   # Display the dataframe as a table
   st.write("Sample DataFrame")
   st.dataframe(df)