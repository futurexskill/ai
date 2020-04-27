# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:40:43 2020

@author: futur
"""
print("Program ")


import os
import sys

# NOTE: Please change the folder paths to your current setup.
#Windows
print("Program started")
if sys.platform.startswith('win'):
    print("Windows")
    #Where you have the code
    os.chdir("C:\spark\src")
    #Where you installed spark.    
    os.environ['SPARK_HOME'] = 'C:\spark\spark-2.4.3-bin-hadoop2.6'
#other platforms - linux/mac
else:
    print("Linux")
    os.chdir("/spark/src")
    os.environ['SPARK_HOME'] = '/spark/spark-2.4.3-bin-hadoop2.6'

os.curdir

print("set directory")


# Create a variable for our root path
SPARK_HOME = os.environ['SPARK_HOME']

#Chehck if the files actually exist

sys.path.insert(0,os.path.join(SPARK_HOME,"python"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib","pyspark.zip"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib","py4j-0.10.7-src.zip"))

print("creating spark session")

from pyspark.sql import SparkSession
#spark = SparkSession.builder.appName('SparkDemo').getOrCreate()
spark = SparkSession.builder.appName('SparkDFExample').getOrCreate()
print("creating dataframe")
df = spark.createDataFrame([{"Google": "Colab","Spark": "Scala"} ,{"Google": "Dataproc","Spark":"Python"}])
print("DataFrame Created")

df.show()