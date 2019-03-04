# Norm Clipping in Tensorflow

Tensorflow includes four different ways of norm-clipping:
1. By L2 norm  
  `tf.clip_by_norm`
2. By average L2 norm (so that average L2 norm is less given value)
  `tf.clip_by_average_norm` (deprecated)
3. By global norm
  `tf.clip_by_global_norm`
4. By fixed value  
  `tf.clib_by_value`

Numpy version:
[`np.clip()`](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.clip.html) 
