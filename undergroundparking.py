from pandas import read_csv, DataFrame
from sklearn import naive_bayes, cross_validation, metrics
from sklearn.feature_extraction.text import CountVectorizer

train = read_csv("spaces_train_bools.csv").dropna(axis=0)
test = read_csv("spaces_test.csv").drop('underground_parking', 1)
test = test.dropna()
#print train
#print test
vectorizer = CountVectorizer()
x_train = vectorizer.fit_transform(train.location)
x_test = vectorizer.transform(test.location)
model = naive_bayes.MultinomialNB().fit(x_train, list(train.underground_parking))
print cross_validation.cross_val_score(naive_bayes.MultinomialNB(), x_train, train.underground_parking)
fpr, tpr, thresholds = metrics.roc_curve(train.underground_parking, model.predict(x_train), pos_label=1)
print metrics.auc(fpr, tpr)
predictions = model.predict_proba(x_test)[:,1]
submissions = DataFrame({'id' : test.id, 'underground_park': predictions})
#submissions.to_csv('underground_parking_probabilites.csv')
submissions.to_csv('underground_proba.csv', index=False)
