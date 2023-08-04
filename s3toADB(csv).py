# Databricks notebook source
s3_path = 's3://bkt-ravali-04aug/iris.csv'
df = spark.read.format("csv").load("s3://bkt-ravali-04aug/iris.csv")

# COMMAND ----------

df.show()

# COMMAND ----------

df.write.parquet('s3://bkt-ravali-04aug/iris.parquet')
