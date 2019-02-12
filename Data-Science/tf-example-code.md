# Basic Example of Tensorflow Code

```python
import numpy as np
import tensorflow as tf

coefficients = np.array([1.], [-10.], [25.])

w = tf.Variable(0, dtype=tf.float32)
x = tf.placeholder(tf.float32, [3,1])

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


