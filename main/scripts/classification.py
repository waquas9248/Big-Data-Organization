from sklearn.cluster import MiniBatchKMeans, KMeans
from sklearn.decomposition import PCA
import pickle
import pandas as pd
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import random
import collections
from google.cloud import storage


os.environ['516778109899-compute@developer.gserviceaccount.com'] = r'/mnt/disks/se-413-375302-7cd244d5721a.json'


client = storage.Client()
bucket = client.get_bucket('schooldataset')

mbk = pickle.load(open('mainModel.pkl', 'rb'))

count = 0
nArray = []
frameInfo = []

for dirpath, dirnames, files in os.walk('/mnt/disks/Google/dataframes2'):
    for f in files:
            print(count)
            tempArr  = np.loadtxt(os.path.join(dirpath, f), delimiter=",", dtype=float)
            for i in range(1000):
                frameInfo.append([count, i + 1])
                nArray.append(tempArr[i])

            count = count + 1


labels = mbk.predict(nArray)
u_labels = np.unique(labels)
maximum = sortedLabels[0]
minimum = sortedLabels[-1]

print(f"Maximum Cluster: {maximum[0]}")
print(f"Maximum Count: {maximum[1]}")
print(f"Minimum Cluster: {minimum[0]}")
print(f"Minimum Count: {minimum[1]}")

pca = PCA(2)
df = pca.fit_transform(nArray)

pandaDF = pd.DataFrame({"0": df[:, 0], "1": df[:, 1], "labels": labels})
pandaDF.to_csv('finalFrame.csv', index=False)


