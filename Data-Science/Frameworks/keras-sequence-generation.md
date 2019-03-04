The function djmodel() will call the LSTM layer  Tx  times using a for-loop, and it is important that all  Tx  copies have the same weights. I.e., it should not re-initiaiize the weights every time---the  TxTx  steps should have shared weights. 
The key steps for implementing layers with shareable weights in Keras are:

* Define the layer objects (we will use global variables for this).
* Call these objects when propagating the input.

Some layers:
* Reshapes an output to a certain shape.  
  https://keras.io/layers/core/#reshape
  ```python
  keras.layers.Reshape(target_shape)
  ```
*  
  https://keras.io/layers/recurrent/#lstm
  ```python
  keras.layers.LSTM(units, activation='tanh', recurrent_activation='hard_sigmoid', use_bias=True, kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal', bias_initializer='zeros', unit_forget_bias=True, kernel_regularizer=None, recurrent_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, recurrent_constraint=None, bias_constraint=None, dropout=0.0, recurrent_dropout=0.0, implementation=1, return_sequences=False, return_state=False, go_backwards=False, stateful=False, unroll=False)
  ```
* Just your regular densely-connected NN layer.  
  https://keras.io/layers/core/#dense
  ```
  keras.layers.Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
  ```
* Lambda layer  
  Wraps arbitrary expression as a Layer object.
  ```python
  keras.layers.Lambda(function, output_shape=None, mask=None, arguments=None)
  
  # example: add a x -> x^2 layer
  model.add(Lambda(lambda x: x ** 2))
  ```
  
## Defining layer objects
```python
reshapor = Reshape((1, 78))                       
LSTM_cell = LSTM(n_a, return_state = True)         
densor = Dense(n_values, activation='softmax')
```
Each of reshapor, LSTM_cell and densor are now layer objects. 
In order to propagate a Keras tensor object X through one of these layers, 
use layer_object(X) (or layer_object([X,Y]) if it requires multiple inputs.). 
For example, reshapor(X) will propagate X through the Reshape((1,78)) layer defined above.
