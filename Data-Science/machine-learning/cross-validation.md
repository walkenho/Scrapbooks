# Useful links

1. [Cross-Validation done wrong](http://www.alfredo.motta.name/cross-validation-done-wrong/) points out 
    how feature selection outside of cross-validataion, i.e. on the complete training set (training and validation set) 
    can leak information into the validation set,
    therefore creating spuriously good performance in cross-validation. 
    
    Great comment section with additional useful info.
    
2. [DEALING WITH IMBALANCED DATA: UNDERSAMPLING, OVERSAMPLING AND PROPER CROSS-VALIDATION](https://www.marcoaltini.com/blog/dealing-with-imbalanced-data-undersampling-oversampling-and-proper-cross-validation)
    deals with the question about when to over/undersample when dealing with imbalanced datasets. The argument is as before: Over/Undersampling
    needs to happen after the fold for cross validation has been created. 
    The blog entry contains a nice demonstration of this using a data set predicting pre-term births.

3. [A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection](http://ai.stanford.edu/~ronnyk/accEst.pdf)

4. [No Unbiased Estimator of the Variance of K-Fold Cross-Validation](http://www.jmlr.org/papers/volume5/grandvalet04a/grandvalet04a.pdf)
