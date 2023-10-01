import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, WhiteKernel

# Initial conditions
maturities = np.array([0.25, 1, 2, 5, 10])[:, np.newaxis]
yields = np.array([2.96, 3.26, 3.51, 4.1, 4.71])
coefficients = np.polyfit(maturities.flatten(), yields, 2)
polynomial = np.poly1d(coefficients)
init_maturities = np.linspace(0, 10, 2)
maturities = init_maturities[:, np.newaxis]
true_yields = polynomial(init_maturities)
yields = true_yields + np.random.normal(0, 1, len(init_maturities))

# Initialize the figure and axis
fig, ax = plt.subplots()

# Initialize the plot
line, = ax.plot(maturities, yields, 'k-', label='estimated yield curve')
true_line, = ax.plot(maturities, true_yields, 'b-', label='true yield curve')
point, = ax.plot([], [], 'ro', label='new observation')
ax.set_xlim(0, 10.25)
ax.set_ylim(0, 7.7)
ax.set_xlabel('maturity (years)')
ax.set_ylabel('yield (%)')
ax.legend(loc='upper right')

# Initialize Gaussian Process
kernel = C() * RBF() + WhiteKernel()
gp = GaussianProcessRegressor(kernel=kernel)

# Initial fit
gp.fit(maturities, yields)

# main code
frame_text = ax.text(0.05, 0.95, '', transform=ax.transAxes,
                     verticalalignment='top')


def update(frame):
    global polynomial, maturities, yields

    # Simulate a new observation for a randomly selected maturity
    random_maturity = np.random.uniform(0, 10)
    new_obs_mean = polynomial([random_maturity])
    new_observation = max([new_obs_mean + np.random.normal(), 0])

    # Update data and re-train Gaussian Process
    maturities = np.vstack([maturities, [[random_maturity]]])
    yields = np.append(yields, new_observation)
    gp.fit(maturities, yields)

    # Predict yields for plotting
    x_pred = np.linspace(0, 10, 101)[:, np.newaxis]
    y_pred = np.clip(gp.predict(x_pred, return_std=False), 0, None)

    # Update plot
    line.set_data(x_pred, y_pred)
    point.set_data(random_maturity, new_observation)

    frame_text.set_text(f'iteration: {frame+1}')
    return line, point, true_line


# Do
ani = animation.FuncAnimation(fig, update, frames=range(100))
ani.save('about_fig.gif', writer='preference', fps=1)
