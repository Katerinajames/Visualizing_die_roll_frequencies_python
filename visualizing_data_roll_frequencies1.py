import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import math 
import seaborn as sns 
rolls=[random.randrange(1,7) for i in range(600)]
values, frequencies = np.unique(rolls, return_counts=True)
sns.set_style('whitegrid')
hue_order = ["low", "medium", "high"]
axes = sns.barplot(x=values, y=frequencies,hue=values, legend=False, palette='bright')
plt.title(f'Rolling a Six-Sided Die {len(rolls):,} Times')
plt.xlabel("Sides of a die ")
plt.ylabel("Roll frequencies")
plt.show()


