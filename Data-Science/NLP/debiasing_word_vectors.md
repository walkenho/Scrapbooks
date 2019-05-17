## Introduction
Introduction

Machine Learning Algorithms learn from data. If the data is biased, then the resulting model will be. This can lead to severe consequences (as for example when
models biased against minorities are used to inform court decisions (see propublica article)). On top of this, it can also lead to the further reinforcement of the already
existing biases, ultimately pushing us towards a more biased vision of society.

Word embeddings are used in a variety of applications from Web Search to parsing CVs. Pre-trained embeddings like Word2Vec or GloVe are readily available for download.
These embeddings are trained on large quantities of text written by humans and consequently learn our biases. 

How can we demonstrate this? Word embeddings can be used to generate analogies:
Male is to Female, what King is to ... Queen, exactly. 
Male is to Female, what Brother is to ... Sister...
Father is to Mother, what Doctor is to ... Nurse .. Wait, what? 


In 2016, Tolga Bolukbasi and co-workers published an article where they investigated biases in readily available embeddings and proposed techniques to compensate for 
these biases. 


Three Steps:

Identify the direction of bias
Neutralize (project neutral words onto neutral plane)
Equalize pairs (shift vectors, so they are equally far away from both words)


Identifying the Gender Subspace/ the Direction of Bias
(Note that you can calculate this bias vector in different ways. The simplest one is to calculate the distance vector between "woman" and "man". A more general approach could be to average over the distance vectors of word-pairs like "woman"-"man", "grandmother"-"grandfather", etc.

Debiasing non-gender specific words
Let g be the direction of bias, i.e. the direction of the vector from "female" to "male". Let w be the word vector of a word which should not have a gender bias (eg "technology"). We can debias w by projecting at onto the plan orthogonal to g. Mathematically this can be done by subtracting the bias compoment $e_{bias}=\frac{e\cdot{g}}{||g||2^2}*g$ from e $e{debiased}=e-e_{bias}$. calculating

References

Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings, same article, but with less material and in nice: https://papers.nips.cc/paper/6228-man-is-to-computer-programmer-as-woman-is-to-homemaker-debiasing-word-embeddings.pdf
https://www.theguardian.com/technology/2015/jul/08/women-less-likely-ads-high-paid-jobs-google-study
https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
Men Also Like Shopping: Reducing Gender Bias Amplification using Corpus-level Constraints
Quantifying and Reducing Stereotypes in Word Embeddings
https://www.nytimes.com/2016/06/26/opinion/sunday/artificial-intelligences-white-guy-problem.html
GloVe Word-Embeddings: https://nlp.stanford.edu/projects/glove/

Three Steps:
1. Identify the direction of bias
2. Neutralize (project neutral words onto neutral plane)
3. Equalize pairs (shift pair vectors, so they are equally far away from neutral words)

## Identifying the Direction of Bias
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
* [Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings](https://arxiv.org/abs/1607.06520), same article, but with less material and in nice: https://papers.nips.cc/paper/6228-man-is-to-computer-programmer-as-woman-is-to-homemaker-debiasing-word-embeddings.pdf
* https://www.theguardian.com/technology/2015/jul/08/women-less-likely-ads-high-paid-jobs-google-study
* https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
* [Men Also Like Shopping: Reducing Gender Bias Amplification using Corpus-level Constraints](https://arxiv.org/abs/1707.09457)
* [Quantifying and Reducing Stereotypes in Word Embeddings](https://arxiv.org/abs/1606.06121)
* https://www.nytimes.com/2016/06/26/opinion/sunday/artificial-intelligences-white-guy-problem.html
* https://towardsdatascience.com/is-artificial-intelligence-racist-and-other-concerns-817fa60d75e9
* https://developers.googleblog.com/2018/04/text-embedding-models-contain-bias.html
* https://developers.google.com/machine-learning/fairness-overview/


GloVe Word-Embeddings: https://nlp.stanford.edu/projects/glove/
