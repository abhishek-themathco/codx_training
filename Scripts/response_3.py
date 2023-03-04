import plotly.express as px
import pandas as pd
import numpy as np
import json
import plotly.io as io
import sklearn
from sklearn import datasets
import plotly.graph_objects as go

def plotGraph():
    
    x = np.linspace(1, 10, 11)
    y = x**2
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x,y=y, name= 'Line Plot', mode='lines'))
    # fig.show()
    return io.to_json(fig)

dynamic_outputs = plotGraph()
