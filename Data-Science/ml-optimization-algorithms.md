# Optimization Algorithms

## Batch Gradient Descent
Uses the full training set at each iteration of gradient descent.

## Mini-batch Gradient Descent
Whilst in batch gradient descent, we train with the full training set in every iteration, in mini-batch gradient descent, we split the training
set into mini-batches and then perform **one step** of gradient descent for each mini-batch. One **epoch of training** denotes a full pass through
the training set. In contrast to batch gradient descent, the cost function does not necessarily decrease at each iteration. 

## Stochastic Gradient Descent
Stochastic Gradient Descent is a specific variant of mini-batch gradient descent. In stochastic gradient descent, the batch-size is one and
at each iteration we randomly choose a training example. 

## Guidelines for how to choose a descent method:
* Batch gradient descent takes very long time per iteration, very noisy
* Stochastic gradient descent: Since batches are processed one-at-a-time, using stochastic gradient descent, one looses almost all 
speed-up from vectorization.
* In practice, an intermediate batch-size usually performs best. 
* small training set (m <= 2000): batch gradient descent
* typical mini-batch size: 64, 128, 256, 51, (1024)
* X<sup>(t)</sup>, Y<sup>(t)</sup> need to fit into memory
* mini-batch size can be a hyperparameter that can be tuned

# Adaptive Learning Rate Algorithms
## Gradient Descent with Momentum
Because stochastic and mini-batch gradient descent make a parameter update after seeing just a subset of examples, the direction of the update has some variance, and so the path taken by mini-batch gradient descent will "oscillate" toward convergence. Using momentum can reduce these oscillations.
In gradient descent with momentum, we calculate the **exponentially averaged momentum** of the parameters and take this into account 
when updating. Gradient
descent with momentum is almost always faster then normal gradient descent. 

#### Interlude: Bias Correction in Exponentially Weighted Averages / Exponentially Weighted Moving Averages
#### Exponentially Weigthed Average
If we calculate v<sub>t</sub> as
<img src="https://latex.codecogs.com/svg.latex?\Large&space;v_t={\beta}v_{t-1}+(1-{\beta}){\Theta}_t"/>
then the influence of v<sub>t</sub> decays in about 
<img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{1}{1-\beta}"/> 
days (ie shrinks to approx 1/e of its value). 
#### Bias Correction
If we start with v0 = 0, then the first few v's are very small. (Example: v1 = beta * v0 + (1-beta) * theta1).
To counteract this, we can introduce a **bias correction** by dividing through (1-beta^t):  
v_t = v_t/(1-beta^t)  
This does not effect values for larger t's too much, but has a significant effect on small t's. 

### Application to Gradient Descent
At each iteration, when calculate the momenta and update the parameters using these momenta:  
v_dW = beta * v_dW + (1-beta) * dW  
v_db = beta * v_db + (1-beta) * db  

If we want, we can apply the bias correction:
v_dW = (beta * v_dW + (1-beta) * dW) / (1-beta\*\*t)  
v_db = (beta * v_db + (1-beta) * db) / (1-beta\*\*t)  

W = W - alpha * v_dW  
b = b - alpha * v_db  
Using the momenta smoothes out the oscillations in the descent, allowing us to choose a larger learner parameter alpha. 

### In Practice
* common choice: beta = 0.9
* people often don't bother with bias correction (since decay time is about 10 iterations for beta = 0.9)
* often, one sees the 1-beta factor omitted, resulting in: v_dW = beta * dW + dW  
  For this implementation, we need to adapt the alpha to alpha/(1-beta). However, this is a bit problematic, since it mixes alpha and beta and if you tune one, you need to re-tune the other, too.

### Nesterov Momentum
A variant of Gradient Descent with Momentum is to use the Nesterov Momentum, where the momentum is calculated at the approximate next point (instead of the current point).

## RMS Prop
RMS stands for *root mean square*. Here, we exponentially weight the squares of momentum. In formulas this looks like this:  
SdW = beta * SdW + (1-beta) * dW<sup>2</sup>  
Sdb = beta * Sdb + (1-beta) * db<sup>2</sup>  

W = W - alpha * dW / (sqrt(SdW)+ epsilon)
b = b - alpha * db / (sqrt(Sdb) + epsilon)

If we want, we can also use a bias correction analogue to gradient descent.

## Adam (Adaptive Moment) Optimization 
The Adam Optimization Algorithm is a combination of RMSProp and Gradient with Momentum. This is how it goes.
1. Initialize everything to zero  
   vdW = SdW = vdb = Sdb = 0
2. Calculate momemta (using bias correction) and momenta squared  
   vdW = (beta1 * vdW + (1-beta1) * dW) / (1-beta1\*\*t) 
   vdb = (beta1 * vdb + (1-beta1) * db) / (1-beta1\*\*t)  
   SdW = beta2 * SdW + (1-beta2) * dW\*\*2  
   Sdb = beta2 * Sdb + (1-beta2) * db\*\*2  
3. Update parameters  
   W := W - alpha * vdW / (sqrt(SdW) + epsilon)
   b := b - alpha * vdb / (sqrt(Sdb) + epsilon)
The hyperparameters suggested in the [Adam paper](https://arxiv.org/abs/1412.6980) are:
* alpha: requires tuning
* b1 = 0.9
* b2 = 0.999
* epsilon = 10*-8 (not that important)

## Adagrad

## Learning Rate Decay
Using mini-batch gradient descent introduces noise into the algorithm. This noise can lead to the algorithm not converging, if the learning rate alpha is too large. One way of dealing with this is by dynamically decreasing alpha during the optimization, a technique called learning rate decay.

A few possibly implementations are:
* alpha = alpha0 / (1 + k * epoch_number)
* alpha = k ^ epoch_number * alpha0 (exponential decay)
* alpha = k / sqrt(epoch_number)
* alpha = k / sqrt(mini_batch_number) * alpha0
* choosing alpha as a sequence of decreasing constant values
* manual decay (for models which are being baby-sitted)

Note: Learning rate decay can help, but is not necessarily the most important thing to tune.

# Further Resources:
* http://cs231n.github.io/neural-networks-3/#sgd
* https://wiseodd.github.io/techblog/2016/06/22/nn-optimization/
