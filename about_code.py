import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, WhiteKernel

# Loading a yield data file using the pandas library
df = pd.read_csv('yield_panel_monthly_frequency_monthly_maturity.csv',
                 parse_dates=[0], index_col=0)
df['Year-Month'] = df.index.to_period('M')
df.index = df['Year-Month']
df.drop('Year-Month', axis=1, inplace=True)
maturities = np.append([1, 3, 6, 9], np.linspace(12, 60, 9))
maturities = np.append(maturities, np.linspace(72, 120, 5))
maturities_str = maturities.astype(int).astype(str)
df = 100*df[maturities_str]
maturities = maturities/12
dates = pd.date_range(start='2016-01', end='2023-09', freq='M').to_period('M')

# Initialize the figure and axis
fig, ax = plt.subplots()

# Initialize the plot
line, = ax.plot(maturities, np.array(
    df.loc[dates[0]]), 'k-', label='representative yield curve over the last year')
quantile_band = ax.fill_between(
    [], [], [], alpha=0.2, color='blue', label='95% posterior interval')
point, = ax.plot([], [], 'bo', label='current observations')
ax.set_xlim(0, 10.25)
ax.set_ylim(-0.1, 7.1)
ax.set_xlabel('maturity (years)')
ax.set_ylabel('yield (percent per annum)')
ax.legend()
frame_text = ax.text(0.025, 0.95, '', transform=ax.transAxes,
                     verticalalignment='top')

# Initialize Gaussian Process
kernel = C() * RBF() + WhiteKernel()
gp = GaussianProcessRegressor(kernel=kernel)

# Main loop


def update(frame):
    global maturities, dates, df

    gp.fit(np.tile(maturities, 12)[:, np.newaxis], np.array(
        df.loc[:dates[frame]].tail(12)).flatten())

    # Predict yields for plotting
    x_pred = np.linspace(0, 10, 101)[:, np.newaxis]
    y_pred, sigma = gp.predict(x_pred, return_std=True)

    # Update plot
    line.set_data(x_pred, y_pred)
    point.set_data(maturities, np.array(df.loc[dates[frame]]))

    for coll in ax.collections:
        coll.remove()  # Remove the previous band
    ax.fill_between(x_pred.ravel(), y_pred - 1.96 * sigma,
                    y_pred + 1.96 * sigma, alpha=0.2, color='blue')

    frame_text.set_text(
        f'today: {str(df.loc[dates[frame]].name)}')
    return line, point


# Do
ani = animation.FuncAnimation(fig, update, frames=range(dates.size))
ani.save('about_fig.gif', writer='pillow', fps=1)
