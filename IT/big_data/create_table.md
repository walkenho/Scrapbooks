CREATE EXTERNAL TABLE database_name.table_name
(
columnname1 string,
columnname2 string
) ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  'adl://path/databasename.db/foldername';

hadoop fs -mkdir adl://path/databasename.db/foldername

hdfs dfs -put i017.csv adl://path/databasename.db/foldername.
