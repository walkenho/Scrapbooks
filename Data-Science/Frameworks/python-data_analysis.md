# Data Analysis Commands in Python

This is just a collection of commands, that I have come across recently.

## Stratified Train Test Split
Stratified Split of housing dataset, stratified by income_cat:
```python
from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['income_cat']):
  strat_train_set = housing.loc[train_index]
  strat_test_set = housing.loc[test_index]
```

## Looking for Correlations
```python
corr_matrix = housing.corr()
``` 
Also:
```python
from pandas.plotting import scatter_matrix
attributes = ['median_house_value', 'median_income']
scatter_matrix(housing[attributes], figsize=(12, 8))
