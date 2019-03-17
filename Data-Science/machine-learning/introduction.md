# ML Introduction
## Terminology
Machine learning is the art of programming computers so they are able to learn from data. 
The term machine-learning was coined by [Arthur Lee Samuel](https://en.wikipedia.org/wiki/Arthur_Samuel) in 1959 as
> Machine learning is the field of study that gives computers the ability to learn without being explicitly programmed.

Nowadays, the most widely used definition of machine learning is that of Carnegie Mellon University Professor 
Tom Mitchell: 
> A computer program is said to learn from experience ‘E’, with respect to some class of tasks ‘T’ and performance measure ‘P’ if 
> its performance at tasks in ‘T’ as measured by ‘P’ improves with experience ‘E’.

## Categorization of ML
Machine learning can be categorized along different axis:
* supervised vs unsupervised vs semisupervised vs reinforcement learning
* online vs batch learning
* instance-based vs model-based learning

### Supervised, Unsupervised, Semisupervised, Reinforcement Learning
#### Supervised Learning
Most common tasks:
* classification
* regression

Some important supervised learning algorithms are:
* kNN
* linear regression
* logistic regression
* SVM
* tree-based algorithms (decision trees, random forests, ...)
* neural networks (neural nets can also be unsupervised (autoencoders, restricted Boltzmann machines) or semi-supervised (deep belief networks, unsupervised pre-training)

#### Unsupervised Learning
Some important unsupervised learning tasks and algorithms are:
* Clustering
  * k-Means
  * Hierarchical Cluster Analysis (HCA)
  * Expectation Maximization
* Visualization and dimensionality reduction
  * PCA
  * Kernel PCA
  * Locally-Linear Embedding (LLE)
  * t-SNE (t-distributed Stochastic Neighbor Embedding)
* Assiociation rule learning
  * [Apriori](https://en.wikipedia.org/wiki/Apriori_algorithm)
  * Eclat (Equivalence Class Transformation)
* Anomalie Detection
  
#### Semisupervised Learning
Most semi-supervised algorithms are combinations of supervised and unsupervised algorithms. For example, deep belief networks (DBNs) stack
multiple restricted Boltzmann machines (RBMs) on top of another. They then train sequentially in an unsupervised manner and then fine-tune
the whole system using supervised techniques.

#### Reinforcement Learning
In reinforcement learning you train an agent to interact with its environement in order to maximize its reward. 

### Online vs Batch Learning
In batch learning the system learns using all data at-once, it cannot learn incrementally. The system is trained, then it is deployed and applies what is has learned. This is called **offline-learning**. This solution poses problems if you need to often retrain or if your dataset if large. For these systems, a better approach is **online learning**, where you train your system incrementally, either one example at a time or in mini-batches. This is great for continous data flows for example. Online learning is also useful where the datasets are so large that they do not fit onto a single machine. This is called **out-of-core learning**. Since online learning also learns from bad data, your performance will decrease if you feed in faulty data. The rate of decline is governed by the learning rate. In order to guard against this, it is necessary to put in place data quality monitoring and closely monitor the model performance. 

### Instance-based vs Model-based Learning
In instance-based learning, the model learns all training examples by heart and then compares a new example against the training data using a chosen similarity measure. Opposed to this is the model-based learning, where you learn a model, then apply this model to the new data.  

## The Unreasonable Effectiveness of Data
In their paper [Learning Curves for Confusion Set Disambiguation](https://dl.acm.org/citation.cfm?id=1073017) Microsoft researchers M. Banko and E. Brill showed that very different ML algorithms (including very simple ones) performed similarly on a data set of natural language disambiguation once they were given enough data. The idea that data matters more than than fancy algorithms for complex tasks was further supported in the paper [The Unreasonable Effectiveness of Data](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf) by P. Norvig et al. However, it needs to stay clear, that this holds true for large data sets, not necessarily for small to medium size data sets. 

## Overfitting vs Underfitting
Some solutions to overfitting:
* choose a simpler model or use regularization
* gather more training data
* reduce noise in the data set

Some solutions to underfitting: 
* select a more powerful model
* feed better features into the model (eg by feature engineering)
* reduce constraints on model (for example reduce regularization)

## Testing and Validating
Terminology:
* **generalization error**/**out-of-sample error**

## No Free Lunch Theorem
A model is a simplification of reality. In order to build a model, you always need to make assumptions. In his 1991 paper [The Lack of A Priori Distinctions Between Learning Algorithms](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.390.9412&rep=rep1&type=pdf), D. Wolpert demonstrated that if you make absolutely no assumptions about the underlying data, there is no model that is *a priori* guaranteed to work best. 

## Main Challenges of ML
* insufficient quantity of training data
* non-representative training data
* poor-quality data
* irrelevant features
