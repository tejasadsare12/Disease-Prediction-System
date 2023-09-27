#!/usr/bin/env python
# coding: utf-8

# ## *Import the libraries*

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ## *Get the data*
# source: https://www.kaggle.com/uciml/pima-indians-diabetes-database

# <img src="cover image.jpg" style="height:350px; width:600px">

# In[10]:


data = pd.read_csv("diabetes.csv")
data.head(10)


# In[11]:


X = data.iloc[:,0:-1].values
y = data.iloc[:,-1].values


# ## *Train-Test split*

# In[12]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 4)


# ## *Feature Scaling*

# In[13]:


from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


# ## *SVM classifier*

# In[14]:


from sklearn.svm import SVC
model_SVC = SVC(kernel = 'rbf', random_state = 4)
model_SVC.fit(X_train, y_train)

y_pred_svm = model_SVC.decision_function(X_test)


# ## *Logistic Classifier*

# In[15]:


from sklearn.linear_model import LogisticRegression
model_logistic = LogisticRegression()
model_logistic.fit(X_train, y_train)

y_pred_logistic = model_logistic.decision_function(X_test)


# ## *Plot ROC and compare AUC*
# For more info visit: https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html

# In[16]:


from sklearn.metrics import roc_curve, auc

logistic_fpr, logistic_tpr, threshold = roc_curve(y_test, y_pred_logistic)
auc_logistic = auc(logistic_fpr, logistic_tpr)

svm_fpr, svm_tpr, threshold = roc_curve(y_test, y_pred_svm)
auc_svm = auc(svm_fpr, svm_tpr)

plt.figure(figsize=(5, 5), dpi=100)
plt.plot(svm_fpr, svm_tpr, linestyle='-', label='SVM (auc = %0.3f)' % auc_svm)
plt.plot(logistic_fpr, logistic_tpr, marker='.', label='Logistic (auc = %0.3f)' % auc_logistic)

plt.xlabel('False Positive Rate -->')
plt.ylabel('True Positive Rate -->')

plt.legend()

plt.show()

