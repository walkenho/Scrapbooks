This entry deals with how to use a udf. First, we take a look at how to use a udf in the simplest case: a function with one
input and one output variable. Afterwards we look at leveling up our udf abilities and using a function with multiple in- and 
output variables.

A general remark: When dealing with udfs, it is important to be aware of the type of output that your function returns. If you get this 
one wrong, your udf will return only nulls.

For both of the examples we need to import the following modules:
```
from pyspark.sql.functions import udf, struct, col
```

## Level 0: One-In-One-Out
### Step 1: Define your function
I was recently recoding binned ages into numeric format. This is an abbreviated version of a function that takes a string, compares it to several options and finally returns a float.
```
def extractAge(mystring):
    if mystring.strip() == 'age 18-25':
        return 21.5
    if mystring.strip() == 'age 26-35':
        return 30.5
    else:
        return None
```

### Step 2: Create the udf (user-defined function)
`extractAge()` takes a single input and returns a single output of type float. The udf-syntax therefore is:
```
extract_age_udf = udf(lambda row: extractAge(row), FloatType())
```
### Step 3: Usage
Create a test dataframe:
```
df = sc.parallelize([[1., 'age 18-25'], [2., 'age 100+']]).toDF(["f1","age"])
df.show()
>>>
+---+---------+
| f1|      age|
+---+---------+
|1.0|age 18-25|
|2.0| age 100+|
+---+---------+
```
Apply function:
```
df_new = df.withColumn('age_n', extract_age_udf(col('age')))
df_new.show()
>>>
+---+---------+-----+
| f1|      age|age_n|
+---+---------+-----+
|1.0|age 18-25| 21.5|
|2.0| age 100+| null|
+---+---------+-----+
```

## Levelling up: Many-In-Many-Out

### Step 1: Define your function
Let’s assume we want to create a function which takes as input two columns and returns the sum and the difference of the two columns.

```
def sum_diff(f1, f2):
	return [f1 + f2, f1-f2]
```

### Step 2: Create the udf
Since the function now returns a vector, we can’t just use the FloatType() data type anymore, we need to first assemble the schema of the output. Both the elements are of type float, so the schema looks like this:

```
schema = StructType([
    StructField("sum", FloatType(), False),
    StructField("diff", FloatType(), False)
])
```

Having defined the schema, we can define the udf as follows:
```
sum_diff_udf = udf(lambda row: sum_diff(row[0], row[1]), schema)
```

Alternatively, we can define function and udf as
```
def sum_diff(row):
	return [row[0] + row[1], row[0]-row[1]]
	
sum_diff_udf = udf(lambda row: sum_diff(row), schema)
```
and still get the same output.


### Step 3: Usage
Create a test dataframe:
```
df = spark.createDataFrame(pd.DataFrame([[1., 2.], [2., 4.]], columns=['f1', 'f2']))
df.show()
>>>
+---+---+
| f1| f2|
+---+---+
|1.0|2.0|
|2.0|4.0|
+---+---+
```

Apply function:
```
df_new = test_data.withColumn("sum_diff", sum_diff_udf(struct([col('f1'), col('f2')])))\
	.select('*', 'sum_diff.*')
df_new.show()

>>>
+---+---+----------+---+----+
| f1| f2|  sum_diff|sum|diff|
+---+---+----------+---+----+
|1.0|2.0|[3.0,-1.0]|3.0|-1.0|
|2.0|4.0|[6.0,-2.0]|6.0|-2.0|
+---+---+----------+---+----+

```



