import streamlit as st
from PIL import Image
from analyse import HF_Zonen
from pandas_df import df_csv
from make_plot import bar, plot_line

#person_dict = read_data.load_person_data()
#person_names = read_data.get_person_list(person_dict)
st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

'''
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
'''
# Wo startet sie Zeitreihe
# Wo endet sich
# Was ist die Maximale und Minimale Spannung
# Grafik
tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

HF_Zone1, HF_Zone2, HF_Zone3, HF_Zone4, HF_Zone5, HF_Zone1_time, HF_Zone2_time, HF_Zone3_time, HF_Zone4_time, HF_Zone5_time = HF_Zonen(df_csv())

with tab1:
    st.header("Herzfrequenzzonen")
    st.write("Zone 1: 50-60% der maximalen Herzfrequenz: ",HF_Zone1_time)
    st.write("Zone 2: 60-70% der maximalen Herzfrequenz: ",HF_Zone2_time)
    st.write("Zone 3: 70-80% der maximalen Herzfrequenz: ",HF_Zone3_time)
    st.write("Zone 4: 80-90% der maximalen Herzfrequenz: ",HF_Zone4_time)
    st.write("Zone 5: 90-100% der maximalen Herzfrequenz: ",HF_Zone5_time)

    st.plotly_chart(bar(HF_Zone1, HF_Zone2, HF_Zone3, HF_Zone4, HF_Zone5))

with tab2:
    st.header("Power-Data")
    st.write("Maximale Leistung: ", Maximum(df_csv())[0], "Watt, erreicht bei: ", Maximum(df_csv())[1], "min")
    st.write("Minimale Leistung: ", Minimum(df_csv())[0], "Watt, erreicht bei: ", Minimum(df_csv())[1], "min")