#!/usr/bin/python

from pandas import read_csv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

##
## fix tkinter.TclError: https://stackoverflow.com/a/44597266
##
plt.switch_backend('agg')

## local variables
num_clusters = 3

## load dataset
df = read_csv('Donors_Data.csv')

##
## remove columns
##
## @axis, 0 for rows and 1 for columns
## @inplace, edit dataframe in place
##
df.drop(
    [
        'Row Id',
        'Row Id.',
        'zipconvert_2',
        'zipconvert_3',
        'zipconvert_4',
        'zipconvert_5'
    ],
    axis=1,
    inplace=True
)

##
## wealth vs avg gift
##
wealth = df.loc[:,['WEALTH']]
avg_gift = df.loc[:,['AVGGIFT']]
case_1 = df[['WEALTH', 'AVGGIFT']]

## normalize data
wealth_norm = (wealth - wealth.mean()) / (wealth.max() - wealth.min())
avg_gift_norm = (avg_gift - avg_gift.mean()) / (avg_gift.max() - avg_gift.min())

## apply pca
pca_1 = PCA(n_components=1).fit(avg_gift_norm)
pca_1a = pca_1.transform(avg_gift_norm)
pca_1w = pca_1.transform(wealth_norm)

## implement kmeans
kmeans = KMeans(n_clusters=num_clusters)
kmeans_output = kmeans.fit(avg_gift_norm)
plt.scatter(pca_1w[:, 0], pca_1a[:, 0], c=kmeans_output.labels_, s=50, alpha=.25)
plt.xlabel('wealth')
plt.ylabel('average gift')

## save visualization
plt.savefig('kmeans_wealth_gift')

##
## child vs avg gift: data was not normalized
##
num_child = df.loc[:,['NUMCHLD']]
avg_gift_norm = df.loc[:,['AVGGIFT']]
case_2 = df[['NUMCHLD', 'AVGGIFT']]

## apply pca
pca_1 = PCA(n_components=1).fit(avg_gift)
pca_1c = pca_1.transform(num_child)

## implement kmeans
kmeans = KMeans(n_clusters=num_clusters)
kmeans_output = kmeans.fit(avg_gift)
plt.scatter(pca_1c[:, 0], pca_1a[:, 0], c=kmeans_output.labels_, s=50, alpha=.25)
plt.xlabel('number of children')
plt.ylabel('average gift')

## save visualization
plt.savefig('kmeans_child_gift')