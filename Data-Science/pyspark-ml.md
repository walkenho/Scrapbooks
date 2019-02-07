# Table of Contents
## General prep
- [Simple ways to deal with nulls](#simple-ways-to-deal-with-nulls)
- [Split into train and test](#split-into-train-and-test)


# General prep

## Simple ways to deal with nulls
(a) fill nulls 
```
df = df.na.fill({'numerical_feature1' : 0, 'numerical_feature2' : 0, 'string_feature' : 'feature_value'})
```

(b) drop all rows with nulls:
```
for column in df.columns:
    df = df.filter(col(column).isNotNull())
```

## Split into train and test
```
train, test = df.randomSplit([0.7, 0.3], seed=42)
```

## Converting string variables to index variables
Indexing has to be done only once. If you want to do model-comparison/cross-validation/etc, it makes sense to 
do the indexing once, save the transformed dataset and only include in the pipeline the steps which you want 
to play with. So we create a preprocessing pipeline and then another training pipeline. This is how a preprocessing
pipe made from labelIndexers could look like.
```
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer

labelIndexer_varname1 = StringIndexer(inputCol="columnname_string_column1", outputCol="columnname_integer_column1")
labelIndexer_varname2 = StringIndexer(inputCol="columnname_string_column2", outputCol="columnname_integer_column2")

pre_pipeline = Pipeline(stages=[labelIndexer_varname1, labelIndexer_varname2])
pre_pipeline_fit = pre_pipeline.fit(train)

train_indexed = pre_pipeline_fit.transform(train)
train_indexed.cache()
```
