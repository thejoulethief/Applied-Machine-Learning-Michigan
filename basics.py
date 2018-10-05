import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

#%matplotlib notebook

fruits  = pd.read_table('fruit_data_with_colors.txt')

X = fruits[['mass', 'width' , 'height']]
y = fruits['fruit_label']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

from matplotlib import cm

cmap = cm.get_cmap('gnuplot')
scatter = pd.scatter_matrix(X_train, c= y_train, marker = 'o', s=40, hist_kwds={'bins':15}, figsize=(12,12), cmap=cmap)

plt.show(

