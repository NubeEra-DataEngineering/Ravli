# Databricks notebook source
df_remote_table= (spark.read
                  .format("sqlserver")
                  .option("host","streamingdatabaseserver.database.windows.net")
                  .option("port","1433")
                  .option("user","admin123")
                  .option("password","Ravali123")
                  .option("database","streamingdatabase")
                  .option("dbtable","dbo.iris_data")
                  .load())

# COMMAND ----------

df_remote_table.show(10)
