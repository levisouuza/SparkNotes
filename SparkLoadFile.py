# File location and type

from pyspark.sql import SparkSession

def CreateDataframe(appName, location, file_type):
  spark = SparkSession.builder.appName(appName).getOrCreate()

  file_location = location
  file_type = file_type

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
  
  return df

def CreateTableParquet(dataframe, table_name_tmp):
  
  try:
    # Create a view or table
    temp_table_name = table_name_tmp

    dataframe.createOrReplaceTempView(table_name_tmp)

    permanent_table_name = table_name_tmp

    df.write.format("parquet").saveAsTable(permanent_table_name)
  except:
    print('Create table is failed!')
  
