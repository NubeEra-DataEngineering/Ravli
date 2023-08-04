# Databricks notebook source
access_key = "AKIAW5IZRWOYQSLAZ3SL"

secret_key = "vIPlNfMg+ON+5viuSliYKvo5boUBm7fgxhHjFMCX"

encoded_secret_key = secret_key.replace("/", "%2F")

aws_bucket_name = "bkt-ravali-04aug"

mount_name = "ravaliawss3"

dbutils.fs.mount("s3a://%s:%s@%s" % (access_key, encoded_secret_key, aws_bucket_name), "/mnt/%s" % mount_name)

display(dbutils.fs.ls("/mnt/%s" % mount_name))

# COMMAND ----------

mount_name = "ravaliawss3"

file_name="iris.csv"

df = spark.read.format("csv").load("/mnt/%s/%s" % (mount_name , file_name))

df.show()

# COMMAND ----------

strMountPointParquetFile="/mnt/%s/abc.parquet" % (mount_name)
df.write.parquet(strMountPointParquetFile)
