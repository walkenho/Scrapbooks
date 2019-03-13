# ML Introduction
## Terminology
Machine learning is the art of programming computers so they are able to learn from data. 
The term machine-learning was coined by [Arthur Lee Samuel](https://en.wikipedia.org/wiki/Arthur_Samuel) in 1959 as
> Machine learning is the field of study that gives computers the ability to learn without being explicitly programmed.

Nowadays, the most widely used definition of machine learning is that of Carnegie Mellon University Professor 
Tom Mitchell: 
> A computer program is said to learn from experience ‘E’, with respect to some class of tasks ‘T’ and performance measure ‘P’ if 
> its performance at tasks in ‘T’ as measured by ‘P’ improves with experience ‘E’.

## Categorization
Machine learning can be categorized along different axis:
* supervised vs unsupervised vs semisupervised vs reinforcement learning
* online vs batch learning
* instance-based vs model-based learning

### Supervised, Unsupervised, Semisupervised, Reinforcement Learning
#### Supervised Learning
Some important supervised learning algorithms are:
* kNN
* linear regression
* logistic regression
* SVM
* tree-based algorithms (decision trees, random forests, ...)
* neural networks (neural nets can also be unsupervised (autoencoders, restricted Boltzmann machines) or semi-supervised (deep belief networks, unsupervised pre-training)

#### Unsupervised Learning
Some important unsupervised learning algorithms are:
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
  * Apriori
  * Eclat
  
#### Semisupervised Learning
Most semi-supervised algorithms are combinations of supervised and unsupervised algorithms. For example, deep belief networks (DBNs) stack
multiple restricted Boltzmann machines (RBMs) on top of another. They then train sequentially in an unsupervised manner and then fine-tune
the whole system using supervised techniques.

#### Reinforcement Learning
In reinforcement learning you train an agent to interact with its environement in order to maximize its reward. 
