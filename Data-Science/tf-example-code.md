# Basic Example of Tensorflow Code

```python
import numpy as np
import tensorflow as tf

coefficients = np.array([1.], [-10.], [25.])

w = tf.Variable(0, dtype=tf.float32) # variable
x = tf.placeholder(tf.float32, [3,1]) # tells tensorflow that you will provide values later

cost = tf.add(tf.add(w**2, tf.multiply(-10, 2)), 25) # (w-5)**2
# tensorflow allows for overloading, therefor equivalently:
# cost = x[0][0]*w**2 + x[1][0]*w + x[2][0]

train = tf.train.GradientDescentOptimizer(0.01).minimum(cost) # 0.01 is learning rate
init = tf.global_variables_initializer()

session = tf.Session()
session.run(init) # Initialize variables
print(session.run(w)) # print w

# alternatively:
with tf.Session() as session:
  session.run(init)
  print(session.run(w))

# running gradient descent:
# (if using mini-batch: at each iteration use feed_dict to feed in different part of training data)
for i in range(1000):
  session.run(train, feed_dict={x:coefficients) # one step of gradient descent
```

# More in Detail
TensorFlow programms consist in the following steps:
1. Create Tensors (variables)
2. Define operations between these variables
3. Initialize Tensors
4. Create Session
5. Run Session

A simple example is:
```python
x1 = tf.constant(1, name='x1')            
x2 = tf.constant(2, name='x2')                    
mysum = tf.Variable(x1 + x2, name='mysum')

init = tf.global_variables_initializer()         # When init is run later (session.run(init)),
                                                 # the mysum variable will be initialized and ready to be computed
with tf.Session() as session:                    # Create a session and print the output
    session.run(init)                            # Initializes the variables
    print(session.run(loss))                     # Runs session and prints output
```

Alternatively, one can do sth like this:
```python
a = tf.constant(2)
b = tf.constant(10)
c = tf.multiply(a,b)
print(c)
>>> Tensor("Mul:0", shape=(), dtype=int32)

sess = tf.Session()
print(sess.run(c))
>>> 20
```


Remember to close the session:
```python
sess.close()
```

You can also create placeholders:
```python
sess = tf.Session()
x = tf.placeholder(tf.int64, name = 'x')
print(sess.run(2 * x, feed_dict = {x: 3}))
sess.close()
```

Defining a named constant of dimension (3,1):
```python
X = tf.constant(np.random.randn(3,1), name = "X")
```

## Math
```python
tf.matmul(..., ...) to do a matrix multiplication
tf.add(..., ...) to do an addition

tf.placeholder(tf.float32, name = "...")

sess.run(..., feed_dict = {x: z})
```

## Initialization
```
tf.ones(shape)
tf.zeros(shape)
tf.constant(np.random.randn(3,1), name = "X") to initialize randomly
W1 = tf.get_variable("W1", [25,12288], initializer = tf.contrib.layers.xavier_initializer(seed = 1))
b1 = tf.get_variable("b1", [25,1], initializer = tf.zeros_initializer())
```

## Relu, sigmoid, etc
```python
tf.nn.relu(...)
tf.sigmoid(...)
tf.softmax(...)
```

## One-hot-encoding
```python
tf.one_hot(
    indices,
    depth,
    on_value=None,
    off_value=None,
    axis=None,
    dtype=None,
    name=None
)
```
The locations represented by indices in indices take value on_value, while all other locations take value off_value.

## Cost Function
```python
tf.nn.sigmoid_cross_entropy_with_logits(logits = ...,  labels = ...)
tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = ..., labels = ...))
```
−1/m∑i=1/m(y(i)log σ(z[2](i))+(1−y(i))log(1−σ(z[2](i)))(2)
Note: What we've been calling "z" and "y" in this class are respectively called "logits" and "labels" 
in the TensorFlow documentation. So logits will feed into z, and labels into y. 

tf.reduce_mean basically summs over the examples. 
Note, that he "logits" and "labels" inputs of tf.nn.softmax_cross_entropy_with_logits are expected to be of shape (number of examples, num_classes). You might to transpose your z and y values:
```python
logits = tf.transpose(z3)
labels = tf.transpose(y)
```
    
## Optimization
```python
optimizer = tf.train.GradientDescentOptimizer(learning_rate = learning_rate).minimize(cost)
_ , c = sess.run([optimizer, cost], feed_dict={X: minibatch_X, Y: minibatch_Y})

optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)
```
