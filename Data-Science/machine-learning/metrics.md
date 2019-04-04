# Basic Definitions and the Confusion Matrix
to be done

# Accuracy
<img src="https://latex.codecogs.com/svg.latex?\Large&space;ACC=\frac{TP+TN}{TP+TN+FP+FN}"/>

# F1-Score
f = (1+\beta^2) * TP / [(1+\beta^2) TP + \beta^2 * FN + FP)]

f1 = 2 * recall*precision / (recall + precision)

# Matthew's Correlation Coefficient
MCC = (TP*TN - FP*FN)/[(TP+FP)(TP+FN)(TN+FP)(TN+FN)]

# Curves
There are two curves usually used to analyze model performance. The **ROC (receiver-operating characteristic) curve** and the **precision-recall curve**. In addition to providing the curve as visualization, they can also be summarized via the **AUC (area under curve)** metric. This is also called **AUROC** for the ROC curve. Finally the AUROC leads to the **Gini coefficient**, which is G = 2\*AUROC-1.  Note that both curves are usually only used for binary classification problems, even though generalizations to multi-class classifications have been proposed (to do: dig out sources).

## ROC Curve
The ROC curve plots the **true positive rate (TPR)** (also called **recall** or **sensitivity** on the y-axis as a function of the **false positive rate (FPR)** (being 1-specifity) on the x-axis. A nice explanation of the ROC curve with some good graphs can be found [here](https://towardsdatascience.com/understanding-auc-roc-curve-68b2303cc9c5). For an explanation we can distinguish the three cases of perfect class separation, overlapping class distributions, identical class distributions.

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
 _______________________
 |
 |
 |
 |
 The area under the curve is 1, the Gini coefficient 2\*1-1=1.

 
 ### Identical Class Distributions / No Distinguishing Power
 In the case of identical class distributions, let's look at the extreme thresholds first. For a threshold of 0, false positives are 0
 
  
 ### Overlapping Class Distributions
 If the class distributions overlap, the curve loses its box shape and becomes more rounded. The AUC is between 1 and 0.5, the Gini coefficient between 1 and 0.
