## Pivot Data


```python
df2 = df1\
    .groupby('col1', 'col2')\
    .pivot('col3')\
    .sum('col4')
```

| col | function |
| ---- | ---------|
| col1, col2 | to keep |
| col3  | column to be pivoted |
| col4 | data to be kept |
