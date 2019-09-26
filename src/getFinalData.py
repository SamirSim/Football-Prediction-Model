dataTrain = pd.read_csv('../dataTrain.csv')
dataTest = pd.read_csv('../dataTest.csv')

y_train = dataTrain['final_score']
x_train = dataTrain.drop('final_score', axis=1)

y_test = dataTest['final_score']
x_test = dataTest.drop('final_score', axis=1)
