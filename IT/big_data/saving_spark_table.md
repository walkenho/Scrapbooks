`
target_table_suffix="SQOOP" #might be SQOOP in future
target_table_name="{0}_{1}".format(evt,target_table_suffix)
target_table_full="{0}.{1}".format(hive_database,target_table_name)
target_table_dir = "adl://path/{0}.db/{1}".format(hive_database,target_table_name)
                                    
df_union.write.mode("overwrite").option("path",target_table_dir ).saveAsTable(target_table_full); 
`
