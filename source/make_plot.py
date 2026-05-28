import plotly.express as plt
import plotly.graph_objects as go
from plotly.io import show
from plotly.subplots import make_subplots
from source.analyse import HF_Zonen


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
def plot_line_power(data):

    fig = fig = make_subplots()
    # Leistung
    fig.add_trace( go.Scatter( y=data['PowerOriginal'], mode='lines', name='Leistung'), secondary_y=False)

    
    fig.update_layout(title='Leistung über Zeit')


    fig.update_xaxes(title_text='Zeit (s)')
    fig.update_yaxes(title_text='Leistung (W)')
    return fig


def plot_line_hr(data, max_hr):
    HF_Zonen_df = HF_Zonen(data, max_hr)
    
    data = data.copy()
    data["Zone"] = HF_Zonen_df["Zone"]

    colors = {
        1: "lightblue",
        2: "green",
        3: "yellow",
        4: "orange",
        5: "red"
    }

    fig = go.Figure()

    # Herzfrequenz-Linie
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data["HeartRate"],
        mode="lines",
        name="Herzfrequenz",
        line=dict(color="black")
    ))
   
    # Horizontale Zonenflächen
    zone_ranges = {
        1: (0.5 * max_hr, 0.6 * max_hr),
        2: (0.6 * max_hr, 0.7 * max_hr),
        3: (0.7 * max_hr, 0.8 * max_hr),
        4: (0.8 * max_hr, 0.9 * max_hr),
        5: (0.9 * max_hr, max_hr)
    }

    for zone, (y0, y1) in zone_ranges.items():
        fig.add_hrect(
            y0=y0,
            y1=y1,
            fillcolor=colors.get(zone, "gray"),
            opacity=0.2,
            line_width=0,
            layer="below"
        )

        fig.add_trace(go.Scatter(
            x=[None],
            y=[None],
            mode="lines",
            line=dict(width=10, color=colors.get(zone, "gray")),
            name=f"Zone {zone}: {int(y0)}-{int(y1)} bpm"
        ))

    fig.update_layout(
        title="Herzfrequenz über Zeit mit HF-Zonen",
        xaxis_title="Zeit (s)",
        yaxis_title="Herzfrequenz (bpm)"
    )

    return fig

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