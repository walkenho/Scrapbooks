This entry deals with how to use a udf. First, we take a look at how to use a udf in the simplest case: a function with one
input and one output variable. Afterwards we look at leveling up our udf abilities and using a function with multiple in- and 
output variables.

A general remark: When dealing with udfs, it is important to be aware of the type of output that your function returns. If you get this 
one wrong, your udf will return only nulls.

## Level 0: 1-in-1-out:
### Step 1: Define your function
This is an example of a function that takes a string, compares it to several options and finally returns a float.  (it is important to realize which data type your return is):

```
def extract_age(mystring):
    if mystring.strip() == 'age 18-25':
        return 21.5
    if mystring.strip() == 'age 26-35':
        return 30.5
    else:
        return 0.0
```

### Step 2: Create the udf (user-defined function)
`extract_age()` takes a single input and returns a single output of type float. The udf-syntax therefore is:
```
extract_age_udf = udf(lambda row: extract_age(row), FloatType())
```
Step 3: Usage
```
df_new = df.withColumn('age_n', extract_age_udf(col('age')))
```

## Levelling up: Multiple In- and Outputs

### Step 1: Define your function
Let’s assume we want to create a function which takes a row object, and returns the sum and the difference  of the two numbers in the row. 

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



