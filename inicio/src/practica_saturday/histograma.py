import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


# Fixing random state for reproducibility
np.random.seed(19680801) 


N_points = 100000
n_bins = 20


# Generate a normal distribution, center at x=0 and y=5
x = np.random.randn(N_points)
y = .4 * x + np.random.randn(100000) + 5


fig, axs = plt.subplots(1, 2, tight_layout=True)


# N is the count in each bin, bins is the lower-limit of the bin
N, bins, patches = axs[0].hist(x, bins=n_bins, edgecolor='black')  # Added edgecolor


# We'll color code by height, but you could use any scalar
fracs = N / N.max()


# Normalize the data to 0..1 for the full range of the colormap
norm = colors.Normalize(fracs.min(), fracs.max())


# Loop through objects and set the color of each
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)


# Normalize inputs by the total number of counts
axs[1].hist(x, bins=n_bins, density=True, edgecolor='black')  # Added edgecolor


# Format the y-axis to display percentage
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))


plt.show()
