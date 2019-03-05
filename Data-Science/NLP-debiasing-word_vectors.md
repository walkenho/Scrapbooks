## Introduction
....

## Calculating the Bias
(Note that you can calculate this bias vector
in different ways. The simplest one is to calculate the distance vector between "woman" and "man". A more general approach 
could be to average over the distance vectors of word-pairs like "woman"-"man", "grandmother"-"grandfather", etc.

# Debiasing non-gender specific words
Let g be the direction of bias, i.e. the direction of the vector from "female" to "male". Let w be the word vector of a word which should 
not have a gender bias (eg "technology"). We can debias w by projecting at onto the plan orthogonal to g. Mathematically this can be done
by subtracting the bias compoment $e_{bias}=\frac{e\cdot{g}}{||g||_2^2}*g$
from e $e_{debiased}=e-e_{bias}$.
calculating 


References
* [Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings](https://arxiv.org/abs/1607.06520)
* https://www.theguardian.com/technology/2015/jul/08/women-less-likely-ads-high-paid-jobs-google-study
* https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
