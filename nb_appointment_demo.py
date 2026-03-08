#!/usr/bin/env python
# coding: utf-8

# ## nb_appointment_demo
# 
# null

# In[2]:


from pyspark.sql import functions as F

bronze_path = "Files/bronze/appointment/appointment_demo.ndjson"

df_raw = spark.read.json(bronze_path)

display(df_raw)
df_raw.printSchema()


# In[3]:


df_raw.write.mode("overwrite").saveAsTable("bronze_appointments")


# In[6]:


df_silver = df_raw.select(
    F.col("id").alias("appointment_id"),
    F.col("resourceType").alias("resource_type"),
    F.col("status"),
    F.col("description"),
    F.to_timestamp("start").alias("start_time"),
    F.to_timestamp("end").alias("end_time"),
    F.to_timestamp("meta.lastUpdated").alias("last_updated"),
    F.col("participant")[0]["actor"]["display"].alias("provider_name"),
    F.col("participant")[1]["actor"]["display"].alias("patient_name"),
    F.col("participant")[0]["status"].alias("provider_status"),
    F.col("participant")[1]["status"].alias("patient_status"),
    F.col("serviceCategory")[0]["coding"][0]["code"].alias("service_category_code"),
    F.col("serviceCategory")[0]["coding"][0]["display"].alias("service_category"),
    F.col("appointmentType")["coding"][0]["code"].alias("appointment_type_code"),
    F.col("appointmentType")["coding"][0]["display"].alias("appointment_type"),
    F.col("reasonCode")[0]["text"].alias("reason_text")
)

display(df_silver)


# In[7]:


df_silver.write.mode("overwrite").saveAsTable("silver_appointments")


# In[8]:


df_gold = (
    df_silver
    .groupBy("service_category", "status")
    .count()
    .orderBy("service_category", "status")
)

display(df_gold)


# In[9]:


df_gold.write.mode("overwrite").saveAsTable("gold_appointment_summary")

