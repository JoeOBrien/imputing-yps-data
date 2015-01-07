from pandas import read_csv, DataFrame
from sklearn import naive_bayes, cross_validation, metrics
from sklearn.feature_extraction.text import CountVectorizer

train = read_csv("spaces_all_train_bools.csv").dropna(axis=0)
test = read_csv("spaces_all_test.csv")
test = test.dropna()
#print train
#print train
vectorizer = CountVectorizer()
x_train = vectorizer.fit_transform(train.location)
x_test = vectorizer.transform(test.location)
#print train

types = ['cctv', 'electronic_payment', 'security_lighting', 'security_gates', 'security_guards', 'security_key', 'sheltered_parking', 'underground_parking', 'restrooms', 'twentyfour_hours_access', 'arranged_transfer', 'car_wash']
#types = train.cctv, train.electronic_payment, train.security_lighting, train.security_gates, train.security_guards, train.security_key, train.sheltered_parking, train.underground_parking, train.restrooms, train.twentyfour_hours_access, train.arranged_transfer, train.car_wash]
submissions = DataFrame({'id': test.id})
for yy in types:
    model = naive_bayes.MultinomialNB().fit(x_train, list(train[yy]))
    print yy
    print cross_validation.cross_val_score(naive_bayes.MultinomialNB(), x_train, train[yy])
    fpr, tpr, thresholds = metrics.roc_curve(train[yy], model.predict(x_train), pos_label=1)
    print metrics.auc(fpr, tpr)
    predictions = model.predict_proba(x_test)[:,1]
    submissions[yy] = predictions
submissions.to_csv('imputed.csv', index=False)