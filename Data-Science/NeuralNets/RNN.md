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


## Resources
* [The fall of RNN/LSTM](https://towardsdatascience.com/the-fall-of-rnn-lstm-2d1594c74ce0)
