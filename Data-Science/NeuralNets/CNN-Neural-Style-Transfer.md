# Neural Style Transfer

* Originally implemented using the VGG

Gram matrix
* the matrix of dot products
* Gij=v<sup>T</sup>i*vj=np.dot(vi,vj)
* One important part of the gram matrix is that the diagonal elements such as  GiiGii  
  also measures how active filter  ii  is. For example, suppose filter  ii  is detecting vertical textures in the image.  
  Then  GiiGii  measures how common vertical textures are in the image as a whole: If  GiiGii  is large, this means that the image has a lot of vertical texture.

By capturing the prevalence of different types of features ( GiiGii ), as well as how much different features occur together ( GijGij ), the Style matrix  GG  measures the style of an image.
* G_A=AA^T
* GA = tf.matmul(A, tf.transpose(A))

Resources:
* [Original paper](https://arxiv.org/abs/1508.06576)
* [Google colab demo](https://colab.research.google.com/github/tensorflow/models/blob/master/research/nst_blogpost/4_Neural_Style_Transfer_with_Eager_Execution.ipynb#scrollTo=dzJTObpsO3TZ)
* [Blog post comparing different optimizers for Neural Style Transfer](https://blog.slavv.com/picking-an-optimizer-for-style-transfer-86e7b8cba84b)
* [bash tool for neural style transfer](https://github.com/cysmith/neural-style-tf)
