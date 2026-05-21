"""
import streamlit as st
from PIL import Image

#person_dict = read_data.load_person_data()
#person_names = read_data.get_person_list(person_dict)
st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

# Dieses Mal speichern wir die Auswahl als Session State
st.session_state.current_user = st.selectbox(
    'EKG',
    options = person_names, key="sbVersuchsperson")

st.write("Der Name ist: ", st.session_state.current_user) 

if 'picture_path' not in st.session_state:
    st.session_state.picture_path = 'data/pictures/none.jpg'

if st.session_state.current_user in person_names:
    st.session_state.picture_path = read_data.find_person_data_by_name(st.session_state.current_user)['picture_path']

if 'birth_date' not in st.session_state:
    st.session_state.birth_date = '1.1.1990'

image = Image.open(st.session_state.picture_path)
st.image(image, caption=st.session_state.current_user)
"""