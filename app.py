import streamlit as st
import pandas as pd

st.write(" The is the first streamlit web python app")
st.write (pd.DataFrame(
    {
        'first column': [1, 2, 3, 4, 5],
        'second column': [10, 20, 30, 40, 50]
    }
))

option=st.selectbox("how do you want to be contacted",
                    ('Email', 'phone'))

st.write("You selected", option)
                    

st.write("Hello world")