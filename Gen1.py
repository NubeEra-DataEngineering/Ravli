# Databricks notebook source
storage_account="saravaliver1"
container_name="input"
source_url="wasbs://{0}@{1}.blob.core.windows.net".format(container_name,storage_account)
accesskey="ldV/Uqla5A21XllFZzOceorhMayuXJW8fP70rTxHS8P9sTdK1NZtnbMFhqtS8vYzzav3mE77yXsI+AStSVo7gQ=="
print(source_url)
mount_point_url="/mnt/dataset17"
extra_configs_key=f"fs.azure.account.key.{storage_account}.blob.core.windows.net"
extra_configs_value=accesskey
extra_configs_dict={extra_configs_key:extra_configs_value}


# COMMAND ----------

dbutils.fs.mount(source=source_url,
                 mount_point=mount_point_url,
                 extra_configs=extra_configs_dict)
