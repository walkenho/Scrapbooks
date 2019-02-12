# Softmax Regression
When doing a multiclass classification, we can choose a softmax function as activation function of the output layer. The softmax activation
function return the probability of each class (in contrast to the hard-max classifier, which returns 0 or 1). It can be shown
that the softmax activation function is the generalization of logistic regression to multiple outputs and logistic regression results
out of the the softmax classifier for C = 2 output classes.

## Softmax Activation Function
For the output layer L:  
z[L] = omega[L]*a[L-1] + b[L]

Choose the activation as follows:  
t = exp(z[L]) (elementwise)  
a[L] = exp(z[L])/(sum_i t_i)

## Training a Softmax Classifier
The loss function of the softmax classifier is  
L(y, yhat)  = -sum_i y_i*log(y_i) = -log yhat_k  
where yhat_k is the ground-truth class
