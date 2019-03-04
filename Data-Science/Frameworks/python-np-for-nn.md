# Clipping gradients
[`np.clip()`](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.clip.html) 

# Using RNNs for text generation
## Sampling according to probability distribution using `random.choice()`
```python
np.random.seed(0)
p = np.array([0.1, 0.0, 0.7, 0.2])
index = np.random.choice([0, 1, 2, 3], p = p.ravel())
```

