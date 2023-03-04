import plotly.express as px
import pandas as pd
import json
import plotly.io as io
import sklearn
from sklearn import datasets

def plotGraph():
    
    data = datasets.load_wine()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df=df[['ash','alcalinity_of_ash']]
    fig = px.scatter(df, x="ash", y="alcalinity_of_ash", title = "Scatter Plot")

    #fig.show()
    return io.to_json(fig)

dynamic_outputs = plotGraph()
