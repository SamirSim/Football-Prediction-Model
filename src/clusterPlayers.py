from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

A = df 
for k in range (1, 21):
     # Create a kmeans model on our data, using k clusters.  random_state helps ensure that the algorithm returns the same results each time.
    kmeans_model = KMeans(n_clusters=k, random_state=1).fit(A.iloc[:, :])

    # These are our fitted labels for clusters -- the first cluster has label 0, and the second has label 1.
    labels = kmeans_model.labels_
 
    # Sum of distances of samples to their closest cluster center
    inertia = kmeans_model.inertia_
    print("k:",k, " cost:", inertia)
    
    
 
import matplotlib.pyplot as plt


x = [178392.41013843272, 144626.3559712018, 128214.62529766273, 118604.52050755064, 111187.212037825, 107551.3349203424, \
     104359.70705658448, 101629.57976602908, 99400.99315725932, 97529.37884869617, 95684.37439026595, 94258.53027672542, \
     92933.73048258385, 91678.08760111309, 90752.05627655494, 89543.19995843308, 88447.44911528328, 87607.72994440656, \
     86846.43821287867, 86047.64883507]
plt.rcParams['figure.figsize'] = [10, 10]
plt.plot(x)
plt.xlabel('k values')
plt.ylabel('cost function value')
plt.savefig('image.jpg')


kmeans = KMeans(n_clusters=5)
kmeans.fit(A)

plt.rcParams['figure.figsize'] = [10, 10]
plt.scatter(A.iloc[:,11],A.iloc[:,40], c=kmeans.labels_, cmap='rainbow')
plt.savefig('k_means.jpg')
