# this app will generate clean csv data and also filter data from may 23rd to june 3rd
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd

# continue the code here...