import numpy as np
import pandas as pd

df = pd.read_excel("F:\\down\\TDS_Week_5_Dataset_2.xlsx")
M = np.array(df)

def kmeans(X, K, max_iters):
    # Initialize centroids randomly
    centroids = X[np.random.choice(range(len(X)), K), :]
    
    for i in range(max_iters):
        # Assign each data point to its closest centroid
        C = np.argmin(np.sqrt(np.sum((X - centroids[:, np.newaxis])**2, axis=2)), axis=0)
        
        # Update centroids to be the mean of the assigned data points
        for k in range(K):
            centroids[k] = np.mean(X[C == k], axis=0)
            
    return centroids

check = 30
x = kmeans(M,7,30)
print(x)
for i in range(7):
    for j in range(len(x[i])):
        if abs(x[i][j]-604)<=check and abs(x[i][j]-1173)<=check:
            print(True)