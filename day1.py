import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Number of points
num_points = 100

# Generate random data
x = np.random.rand(num_points) * 10
y = np.random.rand(num_points) * 10
colors = np.random.rand(num_points)

# Create plot
fig, ax = plt.subplots()
scatter = ax.scatter(x, y, c=colors, s=50)

# Update function for animation
def animation_call(i):
    x = np.random.rand(num_points) * 10
    y = np.random.rand(num_points) * 10
    scatter.set_offsets(np.c_[x, y])
    return scatter,

# Create animation
anim = FuncAnimation(fig, animation_call, frames=200, interval=50)

plt.show()


# books = Book.objects.select_related('author').all()
# authors = Author.objects.prefetch_related('books').all()

