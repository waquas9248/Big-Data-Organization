# Create SparkSession
from pyspark.sql import SparkSession
from pyspark.sql.functions import when
from pyspark.sql.functions import sum
import time

start = time.time()
spark:SparkSession = SparkSession.builder.master("local[1]").appName("ParseData").getOrCreate()

dataframe = spark.read.csv("/mnt/disks/Disk1/sql/tables/TotalSet.csv")
dataframe.createOrReplaceTempView("dataset")
spark.sql("SELECT sum(case when _c4='Person' then 1 else 0 end) as PersonCount,sum(case when _c4='Sky' then 1 else 0 end) as SkyCount,sum(case when _c4='Tree' then 1 else 0 end) as TreeCount FROM dataset;").show()


print("Program Elapsed Time")
print(time.time() - start, "seconds")