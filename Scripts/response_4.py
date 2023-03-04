import pandas as pd
import numpy as np
from pathlib import Path
from azure.storage.blob import BlockBlobService
from io import StringIO
import datetime
import plotly.express as px
import json
from itertools import chain
from plotly.io import to_json
import plotly.graph_objects as go
import plotly.io as io

def getGraph():
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4, 5, 6, 7],y=[1.1, 1, 1.3, 0.7, 0.8, 0.9, 0.4, 0.1], name= 'Scatter Plot', mode='markers'))
    fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4, 5, 6, 7],y=[0.2, 1.2, 1.8, 0.8, 0.5, 1, 1.5, 1.2], name= 'Line Plot', mode='lines'))
    fig.add_trace(go.Bar(x=[0, 1, 2, 3, 4, 5, 6, 7], y=[1, 0.5, 0.7, 1.2, 0.3, 0.4, 1.5, 1.7], name = 'Bar Plot'))
    fig.add_trace(go.Pie(labels=['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen'],values=[1500,1200,1053,700], name = 'Pie Chart'))
    fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4, 5, 6, 7],y=[1.8, 2.2, 0.3, 1.7, 0.4, 0.7, 0.8, 1.1], name= 'Bubble Chart', mode='markers', marker_size=[10, 22, 12.5, 18.2, 5.3, 15.8, 29.8]))


    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(

                        label="Scatter",
                        args=[{"visible": [True, False, False, False, False]}, "chart_type", "Scatter"],
                        method="restyle"
                    ),
                    dict(

                        label="Line",
                        args=[{"visible": [False, True, False, False, False]}, "chart_type", "Line"],
                        method="restyle"
                    ),
                    dict(

                        label="Bar",
                        args=[{"visible": [False, False, True, False, False]}, "chart_type", "Bar"],
                        method="restyle"
                    ),
                    dict(

                        label="Pie",
                        args=[{"visible": [False, False, False, True, False]}, "chart_type", "Pie"],
                        method="restyle"
                    ),
                    dict(

                        label="Bubble",
                        args=[{"visible": [False, False, False, False, True]}, "chart_type", "Bubble"],
                        method="restyle"
                    )

                ]),
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0,
                xanchor="left",
                y=1.2,
                yanchor="top"
            )
        ]
    )
    # fig.show()
    return io.to_json(fig)
   
dynamic_outputs = getGraph()
