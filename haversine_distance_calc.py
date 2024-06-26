import sys
import time
from time import sleep
from pyspark.sql import SparkSession
from pyspark.sql.functions import array, col, concat_ws

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception("Requires input and output paths.")
    
    inputPath = sys.argv[1]
    outputPath = sys.argv[2]

    spark = SparkSession.builder.getOrCreate()
    
    # Register the UDF
    spark.udf.registerJavaFunction("computeHaversine", "com.example.haversinedistance.HaversineDistance", None)
    
    # Read the input data
    #df = spark.read.csv(inputPath, header=True, inferSchema=True)
    df = spark.read.parquet(inputPath)
    
    # Compute the haversine distance using the UDF
    df = df.filter("lat1 is not NULL and lon1 is not NULL and lat2 is not NULL and lon2 is not NULL")
    df = df.selectExpr('lat1', 'lon1', 'lat2', 'lon2', 'computeHaversine(lon1, lat1, lon2, lat2) as distance')
    df = df.sort(col("distance"))
    
    # Write the output data
    start_time = time.time()
    #df.write.mode("overwrite").csv(outputPath, header=True)
    df.write.mode("overwrite").parquet(outputPath)
    end_time = time.time()
    
    print(f"==> Processing took {round(end_time - start_time, 2)} seconds")
    sleep(1000)
    spark.stop()
