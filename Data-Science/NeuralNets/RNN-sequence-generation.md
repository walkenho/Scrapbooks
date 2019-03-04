# Stuff
The RNN-Shakespeare model is very similar to the one you have built for dinosaur names. The only major differences are:

* LSTMs instead of the basic RNN to capture longer-range dependencies
* The model is a deeper, stacked LSTM model (2 layer)
* Using Keras instead of python to simplify the code
* If you want to learn more, you can also check out the Keras Team's text generation implementation on GitHub: https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py.

References:

This exercise took inspiration from Andrej Karpathy's implementation: https://gist.github.com/karpathy/d4dee566867f8291f086. To learn more about text generation, also check out Karpathy's blog post.
For the Shakespearian poem generator, our implementation was based on the implementation of an LSTM text generator by the Keras team: https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py
