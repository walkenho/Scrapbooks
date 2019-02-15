# Importing necessary modules in Pyton
```python
from keras import layers
from keras.layers import Input, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D
from keras.layers import AveragePooling2D, MaxPooling2D, Dropout, GlobalMaxPooling2D, GlobalAveragePooling2D
from keras.models import Model
from keras.preprocessing import image
from keras.utils import layer_utils
from keras.utils.data_utils import get_file
from keras.applications.imagenet_utils import preprocess_input
import pydot
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
from kt_utils import *

import keras.backend as K
K.set_image_data_format('channels_last')
```

Here is an example of a model in Keras:

```python
def create_model(input_shape):
    # Define the input placeholder as a tensor with shape input_shape. Think of this as your input image!
    X_input = Input(input_shape)

    # Zero-Padding: pads the border of X_input with zeroes
    X = ZeroPadding2D((3, 3))(X_input)

    # CONV -> BN -> RELU Block applied to X
    X = Conv2D(32, (7, 7), strides = (1, 1), name = 'conv0')(X)
    X = BatchNormalization(axis = 3, name = 'bn0')(X)
    X = Activation('relu')(X)

    # MAXPOOL
    X = MaxPooling2D((2, 2), name='max_pool')(X)

    # FLATTEN X (means convert it to a vector) + FULLYCONNECTED
    X = Flatten()(X)
    X = Dense(1, activation='sigmoid', name='fc')(X)

    # Create model. This creates your Keras model instance, you'll use this instance to train/test the model.
    model = Model(inputs = X_input, outputs = X, name='HappyModel')

    return model
```

You can also use batch normalization as
`X = BatchNormalization(axis = 3, name = 'bn0')(X)`


Note that Keras uses a different convention with variable names than we've previously used with numpy and TensorFlow. 
In particular, rather than creating and assigning a new variable on each step of forward propagation such as X, Z1, A1, Z2, A2, etc. 
for the computations for the different layers, in Keras code each line above just reassigns X to a new value using X = .... 
In other words, during each step of forward propagation, we are just writing the latest value in the commputation into 
the same variable X. The only exception was X_input, which we kept separate and did not overwrite, since we needed it at the end 
to create the Keras model instance (model = Model(inputs = X_input, ...) above).

https://keras.io/models/model/

Four steps to train a model in Keras:
1. Create the model
2. Compile the model by calling model.compile(optimizer = "...", loss = "...", metrics = ["accuracy"])
3. Train the model on train data by calling model.fit(x = ..., y = ..., epochs = ..., batch_size = ...)
4. Test the model on test data by calling model.evaluate(x = ..., y = ...)

1. `mymodel = create_model(input_shape)`
2. `mymodel.compile(...)`  
    Find here the documentation of [optimizers](https://keras.io/optimizers/), [losses](https://keras.io/losses/) and [metrics]().  
    An optimizer is one of the two required inputs. There are two ways of defining the optimizer:
    * ```python
        from keras import optimizers

        model = Sequential()
        model.add(Dense(64, kernel_initializer='uniform', input_shape=(10,)))
        model.add(Activation('softmax'))

        sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='mean_squared_error', optimizer=sgd)
        ```
    * call the optimizer by its name. In this case, its default values will be used.
      ```python
      # pass optimizer by name: default parameters will be used
      model.compile(loss='mean_squared_error', optimizer='sgd')
 3. `mymodel.fit(x=X_train, y=Y_train)`  
      Note that if you run fit() again, 
      the model will continue to train with the parameters it has already learnt instead of reinitializing them.
 4. ```python  
    preds = myodel.evaluate(x=X_test, y=Y_test)
    print("Loss = " + str(preds[0]))
    print("Test Accuracy = " + str(preds[1]))
    ```

Two more useful features of Keras:

`model.summary()`: prints the details of your layers in a table with the sizes of its inputs/outputs
`plot_model()`: plots your graph in a nice layout. You can even save it as ".png" using SVG()

```python
mymodel.summary()
plot_model(happyModel, to_file='HappyModel.png')
SVG(model_to_dot(happyModel).create(prog='dot', format='svg'))
```
