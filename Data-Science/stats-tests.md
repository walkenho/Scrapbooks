# Kolmogorov–Smirnov test
The [Kolmogorov-Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test) can be used to compare a sample distribution 
with a reference distribution (one-sided) or two sample distributions.
The test quantifies the distance between the empirical distribution function of the sample and the cumulative distribution function 
of the reference (one-sided) or between the two empirical distribution functions of the samples. 

The two-sample K–S test is one of the most general nonparametric methods for comparing two samples, 
as it is sensitive to differences in both location and shape of the empirical cumulative distribution functions of the two samples.
It does not require a normal distribution, but can be used to test
for normality. However, when testing for normality it is less powerful than the [Shapiro–Wilk test](https://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test)
or the [Anderson–Darling test](https://en.wikipedia.org/wiki/Anderson%E2%80%93Darling_test)<sup id="a1">[[1]](#f1)</sup>.
The K-S-test tests against the null-hypotheses that the two samples come from the same distribution. 
If the K-S statistic is small or the p-value is high, then we cannot reject the hypothesis that the distributions of the two samples are the same, ie:
* small p-value: likely not the same
* large p-value: likely the same

The python syntax for performing 2-sample Kolmogorov-Smirnov test is
```python
>>> from scipy.stats import ks_2samp
>>> import numpy as np
>>> 
>>> np.random.seed(42)
>>> x = np.random.normal(0, 1, 1000)
>>> y = np.random.normal(0, 1, 1000)
>>> z = np.random.normal(1.1, 0.9, 1000)
>>> 
>>> ks_2samp(x, y)
Ks_2sampResult(statistic=0.022999999999999909, pvalue=0.95189016804849647)
>>> ks_2samp(x, z)
Ks_2sampResult(statistic=0.41800000000000004, pvalue=3.7081494119242173e-77)
ks_2samp(y1, y2)
```


<b id="f1">[1]</b>  Stephens, M. A. (1974). "EDF Statistics for Goodness of Fit and Some Comparisons". 
Journal of the American Statistical Association. 69 (347): 730–737. doi:10.2307/2286009. JSTOR 2286009. [↩](#a1)
