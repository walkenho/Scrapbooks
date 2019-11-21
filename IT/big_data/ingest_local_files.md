`
https://stackoverflow.com/questions/34900023/read-files-sent-with-spark-submit-by-the-driver 
./bin/spark-submit \
--class com.MyClass \
--master yarn-cluster \
--files /path/to/some/file.ext \
--jars lib/datanucleus-api-jdo-3.2.6.jar,lib/datanucleus-rdbms-3.2.9.jar,lib/datanucleus-core-3.2.10.jar \
/path/to/app.jar file.ext 
`
