
import re
import os
import sys
import boto3 as bt3
import s3fs
import pandas as pd
import qgrid

from pyspark import *
from pyspark.sql import *
from IPython.display import display

pd.set_option('display.max_columns', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', -1)

# ====================================
# Data Loading

s3 = bt3.resource('s3')
my_bucket = s3.Bucket('a_s3_bucket')
s3_loc = 's3://a_s3_bucket'
data_loc_list = ['path/to/folder/',
  ]

# Visual list of files
ls_loc = []
ls_file = []
for data_loc in data_loc_list:
  for obj in my_bucket.objects.filter(Prefix=data_loc):
    print(obj.key)
    file = s3_loc + obj.key
    ls_file.append(file)
  print(data_loc + '\n')
print("number of files:" + str(len(ls_file)))

spark = SparkSession.builder.appName('TC-APP1').master('local[*]') \
.config('spark.sql.hive.convertMetastoreParquet', 'false') \
.config('spark.sql.hive.caseSensitiveInferenceMode', 'NEVER_INFER') \
.config(fs.s3a.server-side-encryption-algorithm', 'SSE-KMS') \
.config(fs.s3a.server-side-encryption.key', 'alias/s3_encryption_key') \
.enableHiveSupport() \
.getOrCreate()

spark.sql("CREATE DATABASE IF NOT EXISTS dbpega COMMENT 'This is DB for pega data' ").show()
spark.sql("DESCRIBE DATABASE EXTENDED dbpega ").show()

v_source_file_loc_path = ["s3://a_s3_bucket/path/to/folder/"]

df_target1 = spark.read.format("parquet").load(v_source_file_loc_path)
df_target1.printSchema()

# Temp tables are more resistant to a shared hive tables - avoids tampering
df_target1.registerTempTable("t_check_attrib")

df_target1.columns
display(df_target1.columns)
