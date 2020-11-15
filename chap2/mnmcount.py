import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import count

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print(f"Usage: mnmcount {sys.stderr}")
        sys.exit(-1)

    spark = SparkSession.builder.appName("PythonMnMCount").getOrCreate()

    mnm_file = sys.argv[1]

    mnm_df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(mnm_file)

    count_mnm_df = mnm_df.select("State", "Color", "Count").groupBy("State", "Color").agg(count("Count").alias("Total")).orderBy("Total", ascending=False)

    count_mnm_df.show(n=60, truncate=False)
    print(f"Total Rows = {count_mnm_df.count()}")

    spark.stop()