import pandas as pd
import os
import time
from prefect import task, flow, get_run_logger
from prefect.utilities.annotations import quote
from prefect_aws.s3 import S3Bucket
from generate_fake_data import create_data_set
from prefect.utilities.annotations import quote


@task
def read_data_file(file_name="fake_data.csv"):
    start_time = time.time()
    df = pd.read_csv(file_name)

    elapsed_time = time.time() - start_time
    print(f"Time taken to read CSV into DataFrame: {elapsed_time:.4f} seconds")
    return df


@task
def dataframe_to_dict(df):
    start_time = time.time()
    data_dict = df.to_dict("records")
    elapsed_time = time.time() - start_time
    print(f"Time taken to convert DataFrame to dictionary: {elapsed_time:.4f} seconds")
    start_between_time = time.time()
    return [data_dict, start_between_time]


@task
def format_payload(data_dict) -> list:
    """Formats the raw response by cleaning the payload header"""
    start_time = time.time()
    elapsed_time = time.time() - data_dict[1]
    print(f"💥 Time taken between tasks: {elapsed_time:.4f} seconds")
    strings = []
    data_dict = data_dict[0]
    for i in range(len(data_dict)):
        strings.append(data_dict[i]["string"])
    elapsed_time = time.time() - start_time
    print(f"Time taken to convert DataFrame to dictionary: {elapsed_time:.4f} seconds")


@flow(log_prints=True, result_storage=S3Bucket.load("result-storage"))
def data_processing_flow(file_name):
    start_time = time.time()
    df = read_data_file.submit(file_name=file_name)
    data_dict = dataframe_to_dict.submit(df)
    # Large gap in time between tasks
    cleaned = format_payload.submit(quote(data_dict.result()))


if __name__ == "__main__":
    data_processing_flow("med_fake_data.csv")
