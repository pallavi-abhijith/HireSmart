# _*_ coding: utf-8 _*_

import json, os, sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import *


s3_data = "s3a://github-stackoverflow-analysis-project/data-file/testing/users.csv"

spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config('spark.default.parallelism', '100') \
        .getOrCreate()

df = spark.read.csv(s3_data)
#df.printSchema()
#df.show(5)
#df1 = df.show(5)
#df1.printSchema()
c = df.count() #to dinf number of rows
dc = df.distinct().count() #To remove duplicate values from datasets
print("Total number of rows",c)
print("Total number of distinct rows",dc)
df1 = df.withColumnRenamed('_c0','id')
df1 = df1.withColumnRenamed('_c1','name')
df1.show(5)
Users_cleaned = df.filter(('_c7'=='USR')&('_c8'==0)&('_c9'==0))
Users_cleaned = Users_cleaned('_c0','_c2','_c5','_c14')
Users_cleaned.show(10)
'''
#To write data in postgresql table
df.select("_c0","_c1").write \
        .mode("overwrite") \
        .option("createTableColumnTypes", "_c0 CHAR(100), _c1 CHAR(100)") \
        .jdbc("jdbc:postgresql://ec2-34-214-106-230.us-west-2.compute.amazonaws.com:5432/test_db", "git1", properties={"user":"postgres", "password":"admin"})
'''
spark.stop()