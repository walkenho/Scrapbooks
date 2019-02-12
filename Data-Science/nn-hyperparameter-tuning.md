# Hyperparameter Tuning
## Tuning process
Possible hyperparameters to tune (and tuning priority):
* [ 1 ] learning rate alpha
* [ 2 ] momentum beta
* [ x ] Adam's parameters beta_1, beta_2, epsilon
* [ 3 ] \# layers
* [ 3 ] \# hidden units
* [ 3 ] learning rate decay
* [ 2 ] mini-batch size

General rule: Don't use grid search for hyperparameter tuning, better use random values.  
Reason: It is not always clear from the beginning which hyperparameters are most important to tune. By choosing random values,
we can get observations for more values of the important hyperparameters. 

Also: Use the *coarse-to-fine sampling scheme*

## Appropriate scales to pick hyperparamters
Random does not necessarily mean uniform. If your range spans multiple orders or magnitude you need to randomly sample on a log scale. 
Two examples are:
1. Sample the learning rate between 0.001 and 1:  
   ```
   r = -4*np.random.rand()
   alpha=10**r
   ```
2. Sample the exponent beta for the weighted average between 0.9 and 0.999  
   -> Sample 1-beta between 0.001 and 0.1  
   Here, it is important to sample more closely around beta=1, since the number of samples taken into account (1/(1-beta)) is more sensitive
   to beta around beta\approx 1.
   
 ## Tuning in pratice: Panda vs. Caviar
 Two possible methodologies: Panda vs Caviar
 * Panda: Baby-sitting one model; used when computational resources are scarce in comparison to training effort
 * Caviar: Train lots of models.
   

