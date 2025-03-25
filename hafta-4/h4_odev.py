import pandas as pd
import SimpSOM as sps
from sklearn.cluster import KMeans
import numpy as np

veri = pd.read_csv("D:\PYTHON\yapayzeka\hafta-4\CC GENERAL.csv")
X = veri.drop(["mall","avail...per_week"],axis=1)

#Ağın oluşturalım aşkoo

net= sps.somNet(20,20, X.valuecds, PBC=True)

#Ağı eğitelim aşko

net.train(0.01, 1000)

hrt = np.array((net.project(X.values)))
kmeans = KMeans(n_clusters= 3, max_iter = 300, random_state=0)

y_kmeans = kmeans.fit_predict(hrt)

# Kümelerin etiketlerinin belirlenmesi
veri["kümeler"] = kmeans.labels_

# 1 numaralı kümenin değerlerine bakılması
print(veri[veri["kümeler"]==0].head(5))

# 2 numaralı kümenin değerlerine bakılması
print(veri[veri["kümeler"]==1].head(5))

#3 numaralı
print(veri[veri["kümeler"]==2].head(5))
