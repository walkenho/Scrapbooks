```python
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
X_train_counts = cv.fit_transform(train_x)
X_train_counts.shape

X_test_counts = cv.transform(test_x)

cv.vocabulary_.get(u'meter')

from sklearn.feature_extraction.text import TfidfTransformer

# only tf
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
X_train_tf.shape

# tf-idf
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape

X_test_tfidf = tfidf_transformer.transform(X_test_counts)

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB().fit(X_train_tfidf, train_y)
pred = clf.predict(X_test_tfidf)

from sklearn import metrics
print(metrics.classification_report(test_y, pred))

conf_mat = metrics.confusion_matrix(test_y, pred)
print(conf_mat)

labels = ['Class 0', 'Class 1']
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(conf_mat, cmap=plt.cm.Blues)
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('Expected')
plt.show()
```
