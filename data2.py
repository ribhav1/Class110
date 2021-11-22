import statistics
import csv
import pandas as pd
import plotly.figure_factory as ff
import random
import plotly.graph_objects as graph_objects

file_data = pd.read_csv('data.csv')

data = file_data['temp'].tolist()
population_mean = statistics.mean(data)
standard_deviation_population = statistics.stdev(data)

print('Population mean: ' + str(population_mean))
print('Standard deviation population: ' + str(standard_deviation_population))

def show_figure(mean_list):
    file_data = mean_list
    figure = ff.create_distplot([file_data], ['temp'], show_hist=False)
    figure.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = 'lines', name = 'mean'))
    figure.show()

dataset = []

for i in range(0, 100):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
standard_deviation = statistics.stdev(dataset)

print('Mean of sample: ' + str(mean))
print('Standard deviation of sample: ' + str(standard_deviation))