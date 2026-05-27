import plotly.express as plt
import plotly.graph_objects as go
from plotly.io import show
from plotly.subplots import make_subplots
from analyse import HF_Zonen


#plot, mit 2 y-Achsen, Leistung und Herzfrequenz
def plot_line(data):

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Leistung
    fig.add_trace( go.Scatter( y=data['PowerOriginal'], mode='lines', name='Leistung'), secondary_y=False)

    # Herzfrequenz
    fig.add_trace( go.Scatter( y=data['HeartRate'], mode='lines', name='Herzfrequenz'), secondary_y=True)

    fig.update_layout(title='Leistung und Herzfrequenz über Zeit')


    fig.update_xaxes(title_text='Zeit (s)')
    fig.update_yaxes(title_text='Leistung (W)', secondary_y=False)
    fig.update_yaxes(title_text='Herzfrequenz (bpm)', secondary_y=True)
    return fig

#plot, mit 1 y-Achse, Leistung und Herzfrequenz in einem Plot
'''def plot_line(data):

    fig = go.Figure()

    # Leistung
    fig.add_trace(go.Scatter( y=data['PowerOriginal'], mode='lines', name='Leistung (W)'))

    # Herzfrequenz
    fig.add_trace(go.Scatter (y=data['HeartRate'], mode='lines', name='Herzfrequenz (bpm)'))

    fig.update_layout( title='Leistung und Herzfrequenz über Zeit', xaxis_title='Zeit (s)', yaxis_title='Wert')
    
    return fig'''

#Balkendiagramm
def bar(HF_Zone1, HF_Zone2, HF_Zone3, HF_Zone4, HF_Zone5):
    fig_bar = go.Figure()
    # Herzfrequenz
    fig_bar.add_trace(go.Bar (y=[(HF_Zone1)], name='HeartRate_Zone1'))
    fig_bar.add_trace(go.Bar (y=[(HF_Zone2)], name='HeartRate_Zone2'))
    fig_bar.add_trace(go.Bar (y=[(HF_Zone3)], name='HeartRate_Zone3'))
    fig_bar.add_trace(go.Bar (y=[(HF_Zone4)], name='HeartRate_Zone4'))
    fig_bar.add_trace(go.Bar (y=[(HF_Zone5)], name='HeartRate_Zone5'))

    fig_bar.update_layout( title='Zeit in den 5 verschiedenen Herzfrequenz-Zonen', xaxis_title='Zonen', yaxis_title='Zeit', barmode='group')
    return fig_bar