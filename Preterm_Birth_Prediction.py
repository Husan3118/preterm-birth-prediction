#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = pd.read_csv(r"C:\Users\husan\Downloads\preterm birth dataset .csv")

#Check missing values
print("1. Missing Values:\n",data.isnull().sum())

#Feature scaling
columns = ['Count Contraction', 'lenght of contraction', 'STD']
scaler = MinMaxScaler()
data[columns] = scaler.fit_transform(data[columns])

#Select input and output features
Xcolumns = ['Entropy', 'Contraction times', 'Count Contraction',
       'lenght of contraction', 'STD']
Ycolumns = ['Pre-term']
X = data[Xcolumns]
Y = data[Ycolumns]


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=1) 
model = LogisticRegression(penalty="l1",C=3,solver="liblinear")
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)

cm = confusion_matrix(Y_test, Y_pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("confusion_matrix.png")
plt.show()

importance = model.coef_[0]
feature_importance = pd.DataFrame({
    'Feature':Xcolumns,
    'Importance':importance
})

plt.figure(figsize=(7,4))
plt.barh(
    feature_importance['Feature'],
    feature_importance['Importance']
)
plt.title("Feature Importance")
plt.savefig(
    "feature_importance.png"
)
plt.show()

accuracy = accuracy_score(Y_test, Y_pred)
print("\n2.Model Accuracy :", accuracy)

print("\n3.Confusion Matrix:\n")
print(confusion_matrix(Y_test, Y_pred))

print("\n4.Classification Report:\n")
print(classification_report(Y_test, Y_pred))


# In[ ]:




