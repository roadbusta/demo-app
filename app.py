import streamlit as st
import pandas as pd
import numpy as np

st.markdown("""# This is a header
## This is a sub header
This is text""")


df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df

st.write("My key is:", st.secrets['API_KEY'])
