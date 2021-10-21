#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 18:37:34 2021

@author: sundharalagumalai
"""
# Import neccessary libraries
import pyspark as pys
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
from pyspark.sql import Row
from pyspark.sql.functions import split

# Setup spark session

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example").getOrCreate()
    #.config("spark.some.config.option", "some-value") \


# Read system log file as csv
# df = pd.read_csv('systemlog.csv')
df = pd.read_csv('eventlog.csv')
df.head(10)
