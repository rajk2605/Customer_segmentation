#import lib
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

#load the data
data = pd.read_csv("customers_oct23.csv")
print(data)
print(data.head())
print(data.info())

#check for null data
print(data.isnull().sum())

# features
features = data[["Annual_Income", "Spending_Score"]]

#  features scaling
mms = MinMaxScaler()
nfeatures = mms.fit_transform(features)

#model
model = KMeans(n_clusters=5)
res = model.fit_predict(nfeatures)
data["clusters"] = res 
print(data)


#predict
income = float(input("Enter Income:"))
spending = float(input("Enter Spending:"))
d = [[income, spending]]
nd = mms.transform(d)
ans = model.predict(nd)

if ans == 0:
	print("High in. low spe.(Cluster 0)")
elif ans == 1:
	print("mid in. mid spe.(Cluster 1)")
elif ans == 2:
	print("High in. high spe.(Cluster 2)")
elif ans == 3:
	print("low in. high spe.(Cluster 3)")
elif ans == 4:
	print("low in. low spe.(Cluster 4)")


#visualize
d0 = data[data.clusters == 0]
d1 = data[data.clusters == 1]
d2 = data[data.clusters == 2]
d3 = data[data.clusters == 3]
d4 = data[data.clusters == 4]

plt.scatter(d0["Annual_Income"],d0["Spending_Score"], label="High in. low spe.")

plt.scatter(d1["Annual_Income"],d1["Spending_Score"], label="mid in. mid spe.")

plt.scatter(d2["Annual_Income"],d2["Spending_Score"], label="High in. high spe.")

plt.scatter(d3["Annual_Income"],d3["Spending_Score"], label="low in. high spe.")

plt.scatter(d4["Annual_Income"],d4["Spending_Score"], label="low in. low spe.")

plt.scatter(income,spending, s=200, marker="x", label="data")

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")

plt.legend()
plt.show()




















