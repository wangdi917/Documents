<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 04:49:38 2018

@author: fang
"""

#随机森林2

from sklearn.tree import DecisionTreeRegressor  
from sklearn.ensemble import RandomForestRegressor  
import numpy as np  

from sklearn.datasets import load_iris  
iris=load_iris()  

from sklearn.model_selection import cross_val_score, ShuffleSplit  
X = iris["data"]  
Y = iris["target"]  
names = iris["feature_names"]  

rf = RandomForestRegressor()  
scores = []  
for i in range(X.shape[1]):  
     score = cross_val_score(rf, X[:, i:i+1], Y, scoring="r2",  
                              cv=ShuffleSplit(len(X), 3, .3))  
     scores.append((round(np.mean(score), 3), names[i]))  

=======
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 04:49:38 2018

@author: fang
"""

#随机森林2

from sklearn.tree import DecisionTreeRegressor  
from sklearn.ensemble import RandomForestRegressor  
import numpy as np  

from sklearn.datasets import load_iris  
iris=load_iris()  

from sklearn.model_selection import cross_val_score, ShuffleSplit  
X = iris["data"]  
Y = iris["target"]  
names = iris["feature_names"]  

rf = RandomForestRegressor()  
scores = []  
for i in range(X.shape[1]):  
     score = cross_val_score(rf, X[:, i:i+1], Y, scoring="r2",  
                              cv=ShuffleSplit(len(X), 3, .3))  
     scores.append((round(np.mean(score), 3), names[i]))  

>>>>>>> 5ebd46b6c812546b4aeb41d11bfffa10731f94a3
print(sorted(scores, reverse=True))