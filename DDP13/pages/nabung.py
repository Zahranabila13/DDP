import streamlit as st

st.title("Ini Halaman Nabung!")

with st.form("nabung"):
    nama = st.text_input("Masukan nama")
    nominal = st.number_input("Masukan nominal nabung")
    submit_button = st.form_submit_button("Simpan")

    if submit_button:
        st.write(nama)
        st.session_state['Nabung'].append({
            'Nama': nama,
            'Nominal': nominal

        })
        st.success("Berhasil Menabung!")