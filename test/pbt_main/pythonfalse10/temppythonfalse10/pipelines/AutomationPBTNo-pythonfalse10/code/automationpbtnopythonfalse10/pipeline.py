from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from automationpbtnopythonfalse10.config.ConfigStore import *
from automationpbtnopythonfalse10.functions import *
from prophecy.utils import *
from automationpbtnopythonfalse10.graph import *

def pipeline(spark: SparkSession) -> None:
    df_s3_source_dataset = s3_source_dataset(spark)
    create_lookup_table(spark, df_s3_source_dataset)
    df_reformatted_customer_data = reformatted_customer_data(spark, df_s3_source_dataset)
    df_print_success_message = print_success_message(spark, df_reformatted_customer_data)
    df_select_from_temp_view = select_from_temp_view(spark, df_s3_source_dataset)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("AutomationPBT-pythonfalse10").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/AutomationPBTNo-pythonfalse10")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/AutomationPBTNo-pythonfalse10", config = Config)(
        pipeline
    )

if __name__ == "__main__":
    main()
