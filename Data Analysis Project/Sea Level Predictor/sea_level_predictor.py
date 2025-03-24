import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

    # Read data from file
    df = pd.read_csv('/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv')
    df.set_index('Year', inplace=True)
    df.index = df.index.astype(int)

    # Create scatter plot

    plt.scatter(df.index, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit

    slope, intercept, _, _, _ = linregress(df.index, df['CSIRO Adjusted Sea Level'])
    x_fit = np.arange(min(df.index), 2051)
    y_fit = slope * x_fit + intercept
    plt.plot(x_fit, y_fit, color='red')

    # Create second line of best fit

    new_df = df[df.index >= 2000]
    slope, intercept, _, _, _ = linregress(new_df.index, new_df['CSIRO Adjusted Sea Level'])

    x_fit_2 = np.arange(min(new_df.index), 2051)
    y_fit_2 = slope * x_fit_2 + intercept
    plt.plot(x_fit_2, y_fit_2, color='green')

    # Add labels and title

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()