# Batch Normalization in Neural Networks
## Background 
In logistic regression, we normalize the inputs to speed up learning. Batch normalization does the equivalent thing
for the inputs of each layer in a NN (ie the outputs of the previous layer).  
It is discussed if we should normalize before or after calculating the activation function, ie. if we should normalize
a or z. In practice most people normalize z. 

## Maths
Let z(i), ... z(m) be the output of some hidden layer l. We calculate  
mu = 1/m * sum_i z(i)  
sigma\*\*2 = 1/m * sum_i (z(i) - mu)\*\*2  
z_norm = [z(i) - mu]/sqrt(sigma\*\*2 + epsilon)

However, we don't want z to be constraint to for example only the linear part of the sigmoid function, so we introduce the
learnable parameters gamma and beta and calculate  
z~ = gamma * z_norm + beta  
This allows us to set both mean and standard deviation of z. Note, that this formalism makes the use of the parameter beta useless.

In practice, batch normalization is often used together with mini-batch. In this case, when calculating mu and sigma\*\*2, we use an
exponentially weighted average of the mu's and sigma\*\*2's of the mini-batches (similar to theta). 

## Advantages of Batch Normalization
* In a *covariate shift*, the input distribution changes, whilst the output distribution stays the same.
   Batch normalization reduces the covariate shift in the deeper layers, since it effectively slightly decouples the layers.
   This leads to a larger robustness of the learning process under covariate shift and a faster learning.
* If used in mini-batch, each mini-batch is scaled by a slightly different mean/variance computed only for this mini-batch. This adds
  some noise to each layer's activation. Similar to drop-out regularization, this noise teaches the layers not to rely too much on a 
  single unit, effectively adding regularization.
  Note, that therefore a bigger mini-batch size leads to a smaller regularization effect.
  However, independently of the batch size, the regularization effect is small and should therefore not be seen as main 
  but rather as additional advantage of batch normalization.
