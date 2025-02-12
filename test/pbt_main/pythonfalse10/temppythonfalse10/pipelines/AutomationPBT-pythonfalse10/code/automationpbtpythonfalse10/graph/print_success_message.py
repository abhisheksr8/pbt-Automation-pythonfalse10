from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from automationpbtpythonfalse10.config.ConfigStore import *
from automationpbtpythonfalse10.functions import *

def print_success_message(spark: SparkSession, in0: DataFrame) -> DataFrame:
    print("Successfully Executed Son.")
    out0 = in0

    return out0
