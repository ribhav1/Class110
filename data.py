import statistics
import csv
import pandas as pd
import plotly.figure_factory as ff

with open('data.csv') as f:
    file_data = pd.read_csv(f)

data = file_data['temp'].tolist()
data_mean = statistics.mean(data)

dist_graph = ff.create_distplot([data], ['temp'], show_hist=False)
dist_graph.show()