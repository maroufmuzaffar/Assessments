# -*- coding: utf-8 -*-
"""Final-4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F3muyQVPQ1H4lf7YKrHNW02K_diunV8T
"""

#as per question doing anomaly detection
#here Import necessary libraries required
import pandas as pd
from sklearn.ensemble import IsolationForest
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import seaborn as sns

#here loading dataset
df = pd.read_csv("/content/anomaly_train.csv")
df.head()

df.info()

df.describe()

#here handling null values
df.isnull().sum()

#here handling duplicate values
df.duplicated().sum()

df["Amount"].value_counts()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df["Amount"]=le.fit_transform(df["Amount"])
df.head()

sns.boxplot(df)
#there are NO outliers

df = df[~df['Type'].str.contains('Retail Purchase')]
df = df[~df['Type'].str.contains('Online Purchase')]

sns.heatmap(df.corr(),cmap="viridis",annot=True)

#here Selecting the features to be used for anomaly detection
features = ["Type", "Location", "User"]

#here Create a new dataframe with the selected features
X = df[features]

#here taking the model
model = IsolationForest()
model.fit(X)
y_pred = model.predict(X)

df["anomaly_score"] = model.decision_function(X)
anomalies = df.loc[df["anomaly_score"] < 0]

#here scatter plot of suspicious activity vs posting activity
plt.scatter(df["posting_activity"], df["anomaly_score"], label="Not Anomaly")
plt.scatter(anomalies["posting_activity"], anomalies["anomaly_score"], color="r", label="Anomaly")
plt.xlabel("Posting Activities")
plt.ylabel("anomaly_score")
plt.legend()
plt.show()

#here scatter plot of suspicious activity vs social connections
plt.scatter(df["social_connections"], df["anomaly_score"], label="Not Anomaly")
plt.scatter(anomalies["social_connections"], anomalies["anomaly_score"], color="r", label="Anomaly")
plt.xlabel("Posting Activities")
plt.ylabel("anomaly_score")
plt.legend()
plt.show()