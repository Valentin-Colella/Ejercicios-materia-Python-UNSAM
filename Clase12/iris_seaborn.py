# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 19:19:08 2021

@author: HP
"""

from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns

iris_dataset = load_iris()

# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
# y hacemos una matriz de gráficos de dispersión, asignando colores según la especie
#pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)

#Agrego al columna target:
iris_dataframe = iris_dataframe.assign(target = iris_dataset['target'])

#Matriz de gráficos de dispersión, asigno formas según la especie.
sns.pairplot(data=iris_dataframe,hue='target', height=1.5, 
             diag_kind='hist',diag_kws= dict(bins=20, hue=None, linewidth=0),
             plot_kws=dict(s=17))