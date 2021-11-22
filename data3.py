import statistics
import csv
import pandas as pd
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

file_data = pd.read_csv('data.csv')

data = file_data['temp'].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    
    return mean

def show_figure(mean_list):
    file_data = mean_list
    mean = statistics.mean(mean_list)
    print('Mean of sampling distribution: ', mean)
    figure = ff.create_distplot([file_data], ['temp'], show_hist=False)
    figure.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = 'lines', name = 'mean'))
    figure.show()


def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    
    show_figure(mean_list)

setup()

population_mean = statistics.mean(data)
print('Population mean: ' + str(population_mean))

def get_stdev():
    mean_list = []
    for i in range(0, 1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    
    standard_deviation = statistics.stdev(mean_list)
    
    print('Standard deviation of sampling distribution: ', standard_deviation)

get_stdev()