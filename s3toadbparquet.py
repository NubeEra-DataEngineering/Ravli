# Databricks notebook source
s3_path ='s3://bkt-ravali-04aug/userdata1.parquet'
df = spark.read.format("parquet").load("s3://bkt-ravali-04aug/userdata1.parquet")
df.show()
