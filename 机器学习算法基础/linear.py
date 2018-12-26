# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 05:24:05 2018

@author: fang
"""

from sklearn import linear_model #导入线性模型
clf = linear_model.LinearRegression() #使用线性回归
clf.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2]) #对输入和输出进行一次fit，训练出一个模型
print(clf.score([[0, 0], [1, 1], [2, 2]], [0, 1, 2]))
print(clf.coef_)  #系数矩阵
