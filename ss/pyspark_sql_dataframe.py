# -*- coding: utf-8 -*-
"""pyspark_sql_dataframe.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qPjF_1qI1bjjIyOnaeoSOGIEzZHfBJ_G
"""

!wget https://downloads.apache.org/spark/spark-3.1.1/spark-3.1.1-bin-hadoop2.7.tgz
!tar -xvf spark-3.1.1-bin-hadoop2.7.tgz
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.1.1-bin-hadoop2.7"
!pip install findspark
import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()

!wget https://raw.githubusercontent.com/futurexskill/bidata/master/retailstore.csv

!ls

customer_df = spark.read.csv("retailstore.csv",header=True)

type(customer_df)

customer_df.show()

customer_df.show(3)

customer_df.describe().show()

country_df = customer_df.select("country")

type(country_df)

country_df.show()

customer_df.groupBy("country").count().show()

customer_df.groupBy("gender").count().show()

customer_df.createOrReplaceTempView("customer")

results = spark.sql("select * from customer")

type(results)

new_results = spark.sql("select * from customer where age>22")

new_results.show()

filtered_df = customer_df.filter('age>22')

filtered_df.show()

customer_df.groupBy("gender").agg({"salary": "avg", "age": "max"}).show()

customer_df.select(["age","salary"]).show()

customer_df.withColumn('doublesalary',customer_df['salary']*2).show()

customer_df.show()

new_customer_df = customer_df.withColumn('doublesalary',customer_df['salary']*2)

new_customer_df.show()

from pyspark.sql.functions import lit
customer_df.withColumn("new_col",lit("A")).show()

customer_df.withColumnRenamed('salary', 'income').show()

customer_df.filter("salary > 30000").select('age').show()

spark.sql("select age from customer where salary > 30000").show()

customer_df.filter("salary > 30000").select('age','country').show()

spark.sql("select age,country from customer where salary > 30000").show()

customer_df.filter("salary > 30000 and salary < 40000 ").select('age','country').show()

spark.sql("select age,country from customer where salary > 30000 and salary < 40000").show()

from pyspark.sql.functions import countDistinct, avg,stddev

customer_df.select(countDistinct("country")).show()

customer_df.select(countDistinct("country").alias("Distinct Countries")).show()

customer_df.select(avg('salary')).show()

customer_df.select(avg('age')).show()

customer_df.select(stddev("salary")).show()

customer_df.select(stddev("age")).show()

from pyspark.sql.functions import format_number

salary_std = customer_df.select(stddev("salary").alias('std'))

salary_std.show()

salary_std.select(format_number('std',2)).show()

customer_df.orderBy("salary").show()

from pyspark.sql.functions import col
customer_df.orderBy(col("salary").desc()).show()

from pyspark.sql.functions import col
customer_df.orderBy(col("salary").asc()).show()

new_df = customer_df.drop("purchased")

new_df.show()

customer_df.na.drop().show()

customer_df.na.fill('NEW VALUE').show()

