import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.rand(10, 12)

# Create heatmap
sns.heatmap(data, cmap='viridis')
plt.show()
