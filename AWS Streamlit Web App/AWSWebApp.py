import streamlit as st
import pandas as pd
import os
import boto3
from io import BytesIO
from sqlalchemy import create_engine

# Initializing the S3 client
client = boto3.client('s3')

# Function to insert DataFrame into the RDS table
def data_to_RDS(df, table_name, rds_host, db_username, db_password, db_name): # aws credentials
    engine = create_engine(f"mysql+pymysql://{db_username}:{db_password}@{rds_host}/{db_name}") # engine congiruation using aws credentials
    df.to_sql(table_name, con=engine, if_exists='append', index=False) # table creation flexibility from csv upload (pandas documentation)
    st.success(f"Data inserted into RDS table {table_name}.") 

# Function to upload file to S3 and RDS
def upload_S3_RDS(uploaded_file, bucket_name, table_name, rds_host, db_username, db_password, db_name): # aws credentials
    if uploaded_file is not None:
        file_content = uploaded_file.getvalue() # reading content into variable
        file_stream_for_s3 = BytesIO(file_content) # creating a BytesIO object from the file content for S3 bucket
        client.upload_fileobj(file_stream_for_s3, bucket_name, uploaded_file.name) # uploading file-like object to S3
        st.success(f"Uploaded {uploaded_file.name} to S3 bucket {bucket_name}.")
        file_stream_for_df = BytesIO(file_content) # create another BytesIO object for pandas reading
        df = pd.read_csv(file_stream_for_df)
        st.write("First 5 rows of DataFrame:", df.head()) # output the first few rows of the DataFrame
        if df.empty: # checking if DataFrame is empty?
            st.error("The DataFrame is empty. No data to insert into RDS.") # if empty display error
        else:
            data_to_RDS(df, table_name, rds_host, db_username, db_password, db_name) # else insert the DataFrame into the RDS table
    else:
        st.error("No file uploaded.")

# Function to list files in S3 bucket -> s3-bucket-hw7-webapp
def S3_files(bucket_name):
    s3_client = client
    response = s3_client.list_objects_v2(Bucket=bucket_name) # lets list the object within my S3 bucket
    return [file['Key'] for file in response.get('Contents', [])] # extracting file keys from response variable

def download_S3_csv(bucket_name, file_key):
    response = client.get_object(Bucket=bucket_name, Key=file_key) # getting object
    file_content = response['Body'].read() # reading object content boto3
    st.download_button(label="Download CSV", data=BytesIO(file_content), file_name=file_key, mime='text/csv')

# Function to display RDS table data
def display_RDS(table_name, rds_host, db_username, db_password, db_name): # aws credentials
    engine = create_engine(f"mysql+pymysql://{db_username}:{db_password}@{rds_host}/{db_name}") # engine configuration
    df = pd.read_sql(f"SELECT * FROM {table_name}", con=engine) # basic sql query
    st.dataframe(df)
    return df

# Function to download data as CSV from RDS table
def download_RDS_csv(df, table_name):
    csv = df.to_csv(index=False).encode('utf-8') # dataframe into csv
    st.download_button(label="Download CSV", data=csv, file_name=f"{table_name}.csv", mime='text/csv')

# My app
st.title("Streamlit AWS S3 & RDS Interaction")

# AWS credentials
# Retrieving credentials from Enviromental Variables (secure way):
rds_host = os.getenv('RDS_HOST')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
bucket_name = os.getenv('BUCKET_NAME')

# Tabs for S3 and RDS operations
tab1, tab2 = st.tabs(["S3 Operations", "RDS Operations"])

with tab1:
    st.header("AWS - S3 Bucket Operations")
    uploaded_file = st.file_uploader("Upload CSV file to S3 and it will be inserted into RDS", type=["csv"])  # file upload section / csv only!
    if uploaded_file is not None:
        table_name = uploaded_file.name.split('.')[0]  # extracted name to be used as the name for the RDS table database (HW7_db) where data from csv will be inserted
        upload_S3_RDS(uploaded_file, bucket_name, table_name, rds_host, db_username, db_password, db_name) # calling upload_S3_RDS function when file uploaded

    # List files in S3 bucket
    if st.button("Show Available Files in S3"):
        files_list = S3_files(bucket_name)
        for file_key in files_list:
            st.text(file_key)
            if st.button(f"Download '{file_key}' from S3"): # button for download process
                download_S3_csv(bucket_name, file_key) # calling the download S3 function

with tab2:
    st.header("View and Download Data from RDS")
    table_name = st.text_input("Enter the table name to fetch data from RDS") # user can enter the name of the table to see data
    if table_name: # if entered
        if st.button(f"Display {table_name} Data"): # click on button
            df = display_RDS(table_name, rds_host, db_username, db_password, db_name) # after clicking data within RDS table will be displayed
            download_RDS_csv(df, table_name) # calling the RDS download function


# References:
# Streamlit documentation: https://docs.streamlit.io/library/get-started
# text elements: https://docs.streamlit.io/library/api-reference/text
# extremely important boto3 documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
# boto3: https://medium.com/featurepreneur/boto3-aws-sdk-for-python-e7391b9901c5
# uploading file to S3: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/upload_fileobj.html
# engine configuration: https://docs.sqlalchemy.org/en/20/core/engines.html
# to_sql: https://www.w3resource.com/pandas/dataframe/dataframe-to_sql.php
# to_sql documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
# streamlit progress and status: https://docs.streamlit.io/library/api-reference/status
# working with streams regarding BytesIO: https://docs.python.org/3/library/io.html
# more streams: https://www.digitalocean.com/community/tutorials/python-io-bytesio-stringio
# donwload files from S3 bucket: https://towardsdatascience.com/how-to-upload-and-download-files-from-aws-s3-using-python-2022-4c9b787b15f2
# list_objects_v2: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_objects_v2.html
# s3 getting object: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_object.html
# S3 getting object: https://stackoverflow.com/questions/31976273/open-s3-object-as-a-string-with-boto3
# st.download: https://docs.streamlit.io/library/api-reference/widgets/st.download_button
# dataframe into csv: https://www.freecodecamp.org/news/dataframe-to-csv-how-to-save-pandas-dataframes-by-exporting/
# os.getenv: https://www.geeksforgeeks.org/python-os-getenv-method/
# st.file_uploader: https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
# st.file_uploader: https://andymcdonaldgeo.medium.com/uploading-and-reading-files-with-streamlit-92885ac3a1b6
# st.button and input: https://docs.streamlit.io/library/api-reference/widgets/st.button