# Basic Definitions and the Confusion Matrix
to be done

# Accuracy
<img src="https://latex.codecogs.com/svg.latex?\Large&space;ACC=\frac{TP+TN}{TP+TN+FP+FN}"/>

# F1-Score
f = (1+\beta^2) * TP / [(1+\beta^2) TP + \beta^2 * FN + FP)]

f1 = 2 * recall*precision / (recall + precision)

# Matthew's Correlation Coefficient
MCC = (TP*TN - FP*FN)/[(TP+FP)(TP+FN)(TN+FP)(TN+FN)]

# ROC and PR Curves
There are two curves usually used to analyze model performance for models where the threshold can be chosen. The **ROC (receiver-operating characteristic) curve** and the **precision-recall curve**. In addition to providing the curve as visualization, they can also be summarized via the **AUC (area under curve)** metric. This is also called **AUROC** for the ROC curve. Finally the AUROC leads to the **Gini coefficient**, which is G = 2\*(AUROC-0.5), the difference of the AUC of the model and the AUC of a non-distinguishing model times two. 

Both ROC and PR curve are most commonly used for binary classification problems, even though generalizations to multi-class classifications have been proposed (to do: dig out sources).

This is roughly how they are different (taken from [Jason Brownlee's ML mastery here](https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/)):

* ROC Curves summarize the trade-off between the true positive rate and false positive rate for a predictive model using different probability thresholds.
* Precision-Recall curves summarize the trade-off between the true positive rate and the positive predictive value for a predictive model using different probability thresholds.
* ROC curves are appropriate when the observations are balanced between each class, whereas precision-recall curves are appropriate for imbalanced datasets.

Let's look at each of them in detail.

## ROC Curve
The ROC curve plots the **true positive rate (TPR)** (also called **recall** or **sensitivity** on the y-axis as a function of the **false positive rate (FPR)** (being 1-specifity) on the x-axis. In other words in plots the hit rate as a function of the false alarm rate. A nice explanation of the ROC curve with some good graphs can be found [here](https://towardsdatascience.com/understanding-auc-roc-curve-68b2303cc9c5). For an explanation we can distinguish the three cases of perfect class separation, overlapping class distributions, identical class distributions.

### Perfect class separation
Let's assume the distributions of our two classes are perfectly separated, the negative class with low probabilities, the positive class with higher probabilities. In order to ease notation, let's also assume that the threshold to seperate them is 0.5 (this is purely to ease notation, you can do the same calculation for any threshold). We can then identify two regimes: 

1. a threshold below 0.5
2. a threshold above 0.5

Let's see what happens in both cases. 
1. threshold below 0.5  
  For a threshold below 0.5, all the positive samples are classified as positive, there are no false negatives. In this case recall = 1. What happens with the FPR? For a threshold of 0, the all negative samples are classified as positive and we have no true negatives, therefore FPR = 1. For a threshold of 0.5, all negative samples are classified as negative, there are not false positives, FPR = 0. In between there is a continuum of values for FPR. In summary, this range is characterized by TRP=1 and FPR in [0,1]. 
2. threshold above 0.5  
  For a threshold of above 0.5, the case is symmetric to the case described for a threshold of below 0.5 but with the roles of FPR and TPR swapped. All negative samples are classified as negative and no false positives exist. Therefore FPR = 1. What about TPR? For a threshold of 0.5 all positive samples are classified as positive, no false negatives, therefore TPR=1. For a threshold of 1, all positive samples are classified as negative, all are false negatives, no true positives, therefore TPR=0. In summary, this range is characterized by FPR=1 and TPR in [0,1].
  
 Putting these two cases together we end up with a ROC curve shaped like a square, where the curve touches upper left corner 
 ```
 _______________________
 |
 |
 |
 |
 ```
 
 The area under the curve is 1, the Gini coefficient 2\*(1-0.5)=1.

 ### Identical Class Distributions / No Distinguishing Power
 In the case of identical class distributions, let's look at the extreme thresholds first. The thresholds 0 and 1 as for the previous case result in FPR=TPR=1 and FPR=TPR=0. But what happens in between? If we start at a threshold of 1 (TP=FP=0) and then decrease the threshold, for two identical distributions, for each TP we gain, we also gain a FP and for each FN we lose, we also lose a TP. Therefore TPR and FPR evolve in exactly the same way and plotting TPR against FPR results in a straight diagonal leading to an AUC of 0.5 and a Gini coefficient of 0. 
  
 ### Overlapping Class Distributions
 If the class distributions overlap, we find a mixture of the two cases describes above. This results in the the curve losing its box shape (from the perfectly separated classes) and the edges becoming round. The more overlap, the more the curves resemble a line. The AUC is between 1 and 0.5, the Gini coefficient between 1 and 0. (That is not exactly accurate, since the AUC can be below 0.5 indicating an inverted model).
 
 ### Python Code
 A full example of how to calculate and plot a ROC curve (taken from [here](https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/)
 ```python
 from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot
# generate 2 class dataset
X, y = make_classification(n_samples=1000, n_classes=2, weights=[1,1], random_state=1)
# split into train/test sets
trainX, testX, trainy, testy = train_test_split(X, y, test_size=0.5, random_state=2)
# fit a model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(trainX, trainy)
# predict probabilities
probs = model.predict_proba(testX)
# keep probabilities for the positive outcome only
probs = probs[:, 1]
# calculate AUC
auc = roc_auc_score(testy, probs)
print('AUC: %.3f' % auc)
# calculate roc curve
fpr, tpr, thresholds = roc_curve(testy, probs)
# plot no skill
pyplot.plot([0, 1], [0, 1], linestyle='--')
# plot the roc curve for the model
pyplot.plot(fpr, tpr, marker='.')
# show the plot
pyplot.show()
```
 
 ## Precision-Recall Curve
 The precision-recall curve also plots the precision (true predictive power) on the y-axis against the recall (sensitiviy; true positive rate) on the x-axis. 
 ```
Precision = True Positives / (True Positives + False Positives)
 ```
The precision tells us how many of the positive predicted values are real positives. 
The precision-recall curve is a better choice for imbalanced datasets than the ROC curve. Why is that? In an imbalanced dataset where we have many negative samples and only a few positives, we are typically more interested in predicting the positive samples correctly than in predicting the negative samples correctly. The ROC curve on its x-axis shows the false positive rate, which in its denominator has the true negatives. In contrast the precision is not interested in predicting the negatives, it only focuses on the positive class. 

The no-skill line of the precision-recall curve is defined by the number of true positives divided by the total number of cases, which is the precision of a model which predicts the positive class for all cases.

Some attempts of summarizing the precision-recall curve are:
* f1-score: Harmonic mean of precision and recall
* average precision: weighted increase in precision with each change in recall for the thresholds in the precision-recall curve
* AUC: area-under-curve as for AUROC
Notable, the f1-score is for a single threshold, average precision and AUC are a summary of the whole precision-recall curve. 

### Python Code
```python
# precision-recall curve and f1
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import f1_score
from sklearn.metrics import auc
from sklearn.metrics import average_precision_score
from matplotlib import pyplot
# generate 2 class dataset
X, y = make_classification(n_samples=1000, n_classes=2, weights=[1,1], random_state=1)
# split into train/test sets
trainX, testX, trainy, testy = train_test_split(X, y, test_size=0.5, random_state=2)
# fit a model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(trainX, trainy)
# predict probabilities
probs = model.predict_proba(testX)
# keep probabilities for the positive outcome only
probs = probs[:, 1]
# predict class values
yhat = model.predict(testX)
# calculate precision-recall curve
precision, recall, thresholds = precision_recall_curve(testy, probs)
# calculate F1 score
f1 = f1_score(testy, yhat)
# calculate precision-recall AUC
auc = auc(recall, precision)
# calculate average precision score
ap = average_precision_score(testy, probs)
print('f1=%.3f auc=%.3f ap=%.3f' % (f1, auc, ap))
# plot no skill
pyplot.plot([0, 1], [0.5, 0.5], linestyle='--')
# plot the precision-recall curve for the model
pyplot.plot(recall, precision, marker='.')
# show the plot
pyplot.show()
```

## ROC vs Precision-Recall Curve for Imbalanced Datasets
Generally the decision on ROC vs precision-recall curves should be based on the degree of imbalance in the dataset. Generally, the use of ROC curves and precision-recall curves are as follows:
* ROC curves should be used when there are roughly equal numbers of observations for each class.
* Precision-Recall curves should be used when there is a moderate to large class imbalance.
The reason for this is -as stated above- that the ROC curve makes use of the number of true negatives, which will always be large in an imbalanced dataset. Opinions on using the ROC curve for imbalanced datasets range from "overly optimistic" to "deceptive". 

>However, ROC curves can present an overly optimistic view of an algorithm’s performance if there is a large skew in the class distribution. […] Precision-Recall (PR) curves, often used in Information Retrieval , have been cited as an alternative to ROC curves for tasks with a large skew in the class distribution.

(from [The relationship between Precision-Recall and ROC curves, 2006](https://dl.acm.org/citation.cfm?id=1143874))

>[…] the visual interpretability of ROC plots in the context of imbalanced datasets can be deceptive with respect to conclusions about >the reliability of classification performance, owing to an intuitive but wrong interpretation of specificity. [Precision-recall curve] >plots, on the other hand, can provide the viewer with an accurate prediction of future classification performance due to the fact that >they evaluate the fraction of true positives among positive predictions

(from [The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4349800/), 2015)

The reason is the use of the true negatives in the false positve rate:
>If the proportion of positive to negative instances changes in a test set, the ROC curves will not change. Metrics such as accuracy, >precision, lift and F scores use values from both columns of the confusion matrix. As a class distribution changes these measures will >change as well, even if the fundamental classifier performance does not. ROC graphs are based upon TP rate and FP rate, in which each >dimension is a strict columnar ratio, so do not depend on class distributions.

(from [Tom Fawcett, ROC Graphs: Notes and Practical Considerations for Researchers](http://www.blogspot.udec.ugto.saedsayad.com/docs/ROC101.pdf), 2004)

Some more papers on the topic:
* [A critical investigation of recall and precision as measures of retrieval system performance](https://dl.acm.org/citation.cfm?id=65945), 1989
* [The Relationship Between Precision-Recall and ROC Curves](https://dl.acm.org/citation.cfm?id=1143874), 2006
* [The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4349800/), 2015
* Tom Fawcett, [ROC Graphs: Notes and Practical Considerations for Researchers](http://www.blogspot.udec.ugto.saedsayad.com/docs/ROC101.pdf), 2004)
