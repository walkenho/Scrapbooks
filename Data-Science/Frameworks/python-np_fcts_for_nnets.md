# Some Useful Functions in numpy for NNets
## Gradient clipping
[`np.clip()`](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.clip.html) 

## Sampling according to a probability distribution
(is for example needed when using RNNs to generate text)

`random.choice()`

Example:
```python
np.random.seed(0)
p = np.array([0.1, 0.0, 0.7, 0.2])
index = np.random.choice([0, 1, 2, 3], p = p.ravel())
```

