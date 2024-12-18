import streamlit as st

st.title("Ini Halaman Dashboard!")
st.session_state['Nabung']

jumlah = 0
for sesssion in st.session_state['Nabung']:
    jumlah += sesssion['Nominal']

st.write("Total nominal menabung sebesar", jumlah)