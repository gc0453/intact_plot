import streamlit as st
from PIL import Image
from analyse import HF_Zonen, Minimum, Maximum, Umrechnen, HF_Zonen_zeit, durchschnittsleistung_pro_zone
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
tab1, tab2 = st.tabs(["Herzfrequenz-Zonen", "Power-Data"])

zone_times = HF_Zonen_zeit(HF_Zonen(df_csv()))

with tab1:
    #st.dataframe(Zonen_df[['Zone','HeartRate', 'PowerOriginal']], use_container_width=True)
    st.header("Herzfrequenz-Zonen")
    st.write("Zone 1: 50-60% der maximalen Herzfrequenz")
    st.write("Zeit in der Zone 1 verbracht: ",Umrechnen(zone_times[0]))
    st.write("durchschnittliche Leistung in Zone 1: ", durchschnittsleistung_pro_zone(df_csv())[1], "Watt")
    st.write("Zone 2: 60-70% der maximalen Herzfrequenz")
    st.write("Zeit in der Zone 2 verbracht: ",Umrechnen(zone_times[1]))
    st.write("durchschnittliche Leistung in Zone 2: ", durchschnittsleistung_pro_zone(df_csv())[2], "Watt")
    st.write("Zone 3: 70-80% der maximalen Herzfrequenz")
    st.write("Zeit in der Zone 3 verbracht: ",Umrechnen(zone_times[2]))
    st.write("durchschnittliche Leistung in Zone 3: ", durchschnittsleistung_pro_zone(df_csv())[3], "Watt")
    st.write("Zone 4: 80-90% der maximalen Herzfrequenz")
    st.write("Zeit in der Zone 4 verbracht: ",Umrechnen(zone_times[3]))
    st.write("durchschnittliche Leistung in Zone 4: ", durchschnittsleistung_pro_zone(df_csv())[4], "Watt")
    st.write("Zone 5: 90-100% der maximalen Herzfrequenz")
    st.write("Zeit in der Zone 5 verbracht: ",Umrechnen(zone_times[4]))
    st.write("durchschnittliche Leistung in Zone 5: ", durchschnittsleistung_pro_zone(df_csv())[5], "Watt")

    st.plotly_chart(bar(zone_times[0], zone_times[1], zone_times[2], zone_times[3], zone_times[4]))

with tab2:
    st.header("Power-Data")
    st.write("Maximale Leistung: ", Maximum(df_csv())[0], "Watt, erreicht bei: ", Maximum(df_csv())[1])
    st.write("Minimale Leistung: ", Minimum(df_csv())[0], "Watt, erreicht bei: ", Minimum(df_csv())[1])

    st.plotly_chart(plot_line(df_csv()))