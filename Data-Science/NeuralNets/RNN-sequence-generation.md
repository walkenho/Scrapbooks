
# Example Treated in the Course
In the course, we have seen three examples:
* generating dinosaur names
* generating shakespear verses
* generating jazz

The major differences between the dinosaurs and Shakespear are:
* Shakespear used LSTMs instead of the basic RNN to capture longer-range dependencies
* the Shakespear model is a deeper, stacked LSTM model (2 layer)
* we used Keras instead of python

## References:
### Text Generation
* Keras Team's text generation implementation on GitHub: https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py.
* Andrej Karpathy's implementation: https://gist.github.com/karpathy/d4dee566867f8291f086
* [Karpathy's blog post]() for more info on text generation
* Keras example of LSTM text generator on [their github](https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py)
### Music Generation:
* Theory: 
  * [Jon Gillick, Kevin Tang and Robert Keller, 2009. Learning Jazz Grammars](http://ai.stanford.edu/~kdtang/papers/smc09-jazzgrammar.pdf)
  * [Robert Keller and David Morrison, 2007, A Grammatical Approach to Automatic Improvisation](http://smc07.uoa.gr/SMC07%20Proceedings/SMC07%20Paper%2055.pdf) 
  * [François Pachet, 1999, Surprising Harmonies]( http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.5.7473&rep=rep1&type=pdf)
* Implementation: 
  * Ji-Sung Kim, 2016, [deepjazz](https://github.com/jisungk/deepjazz)
