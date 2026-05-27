import plotly.express as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pandas_df import df_csv #kann später gelöscht werden, wenn die Daten direkt übergeben werden können

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

#später löschen, nur zum Testen
'''
fig2 = plot_line(df_csv())
fig2.show()
'''
