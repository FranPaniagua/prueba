import streamlit as st 

import pandas as  pd

datos = pd.read_json('https://gpax.io/api/cursor.recommendations?token=MTEwODAwOTMxOm82L0ZPeGJURVdqY2ZRZ01iVmIwMVBmU2dzOD0')

st.bar_chart(datos)

