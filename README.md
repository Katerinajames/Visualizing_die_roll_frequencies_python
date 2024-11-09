rolls=[random.randrange(1,7) for i in range(600)] :We create a list of 600 random die values 
values, frequencies = np.unique(rolls, return_counts=True) :We use numpy's function unique to determine the unique roll values 
sns.set_style('whitegrid'):Seaborn plots graphs on a plain white background but we can choose several styles 
