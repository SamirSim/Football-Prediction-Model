## Initializing all models and parameters
#Initializing classifiers
RF_clf = RandomForestClassifier(n_estimators = 50, random_state = 1, class_weight = 'balanced')
AB_clf = AdaBoostClassifier(n_estimators = 500, random_state = 2)
GNB_clf = GaussianNB(priors=None, var_smoothing=1e-05)
KNN_clf =  KNeighborsClassifier()
clfs = [RF_clf, GNB_clf, KNN_clf]

#Print Scores
for clf in clfs:
    pca_X_train = normalized_std_train
    pca_X_test = normalized_std_test
    clf.fit(pca_X_train, y_train)
    print("Score of {} for training set: {:.4f}.".format(clf.__class__.__name__, accuracy_score(y_train, clf.predict(pca_X_train))))
    print("Score of {} for test set: {:.4f}.".format(clf.__class__.__name__, accuracy_score(y_test, clf.predict(pca_X_test))))
    print(classification_report(y_train, clf.predict(pca_X_train)))
