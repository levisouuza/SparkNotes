# File location and type

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('LoadFile').getOrCreate()

file_location = "/FileStore/tables/cruise_ship_info.csv"
file_type = "csv"

# CSV options
infer_schema = "True"
first_row_is_header = "True"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

# Show dataframe
df.show()
