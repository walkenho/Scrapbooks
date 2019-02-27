# Recurrent Neural Network (RNN)
## General Overview
RNNs are the standard NN architecture to deal with temporal data. They can be used to analyze situations 
where the length of the input variable can vary 
and in situations where the length of input and output vectors are different. 
Similar to CNNs, RNNs allow the network to share features across the network. For CNNs this means, that in image recognition,
features learned in one part of the image can be re-used in other parts of the image. For RNNs this means, that features learned 
for one point in time can be used in the future (or past for BRNNs). 

RNNs can be categorized broadly according to their input/output as:
* many-to-many with T_x = T_y  
  * number of input features equals number of output features  
  * example: named entity-recognition
* many-to-many with T_x != T_y  
  * example: machine translation
* many-to-one  
  * only output at final t=T_x  
  * example: classification
* one-to-many  
  * example: music generation  
  * generates output with input only at t=0; afterwards only input is activation of previous layer or re-use input at t=0 as input at every timestep
* one-to-one  
  * basically just a standard NN
  
Being specialized in sequential data, RNNs come with a broad range of usecases as varied as:
* Speech recognition
* Music generation
* Sentiment classification
* DNA sequence analysis
* Machine translation
* Video activity recognition
* Named entity recognition
  
  
## Working Principle
* the initial activation is most often initialized to zero; it can also be initialized randomly though 
* at each time-step, the prediction then takes into account both the input as well as the activation of the previous time-step

Information about inputs filters from left to right, from earlier in time to later in time. This has the drawback, that the network only uses information from previous time-steps not future timesteps. Whilst this makes sense for some applications, for others it might be useful to take into account inputs at later states. This is solved in bi-directional RNNs (see below). 

A simplified structure looks like:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;a^{<t>}=g(\omega_a\[a^{<t-1>},x^{<t>}]+b_a)"/>

with the output

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\hat{y}^{<t>}=g(\omega_y\a^{<t>}+b_y)"/>

Here, <img src="https://latex.codecogs.com/svg.latex?\Large&space;a^{<t>}=[a^{<t-1>},x^{<t>}]"/> denotes a^{<t-1>} and x^{<t>} stacked on top of each other.
 
 The loss function is created as sum over the loss function at each time step t, where each loss function is the usual cross-entropy
 loss L = - y * log(\hat{y}) - (1-y) * log(1-hat{y})
 
 ## Sequence Generation 
 ...
 
## LSTMs and GRUs and LSTMs - Tackling the Vanishing Gradient Problem
Exploding gradients can be a problem for RNNs, but can be solved through so-called *gradient clipping*, which is done by rescaling the gradient vector in case if it surpassed a set threshold. The bigger problem are vanishing gradients.
Language tends to have long-time dependencies since the end of a sentence can strongly depend on the beginning. Vanilla RNNs have a problem of dealing with these long-term dependencies because of the vanishing gradient problem. Two possible solutions are LSTMs (long short term memory) and their simplyfied version GRUs (gated recurrent units). 

### LSTM
LSTM were introduced in the paper [Long short term memory](https://www.mitpressjournals.org/doi/10.1162/neco.1997.9.8.1735) by Hochreiter & Schmidthuber in 1997.

## Resources
* [The fall of RNN/LSTM](https://towardsdatascience.com/the-fall-of-rnn-lstm-2d1594c74ce0)
