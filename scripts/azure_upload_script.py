# This script will upload E-commerce Sales Dataset from kaggle api to our azure container retail-data, bronze folder:

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from io import open
import kaggle
import os


def upload_to_azure():
    # store your real kaggel username and key to your environment or store them to default location;
    #  ~/.kaggle/kaggle.json
    #  alternatively if using docker, store the secrets in .env file though not recommended in a production environmnent.

    os.environ["KAGGLE_USERNAME"] = "username"
    os.environ["KAGGLE_KEY"] = "key"

    kaggle.api.authenticate()

    # Download latest version of our retail sales data
    kaggle.api.dataset_download_files(
        "thedevastator/unlock-profits-with-e-commerce-sales-data",
        path="./mydata",
        unzip=True,
    )

    # Azure authentication
    credential = DefaultAzureCredential()

    # azure blob connection string
    connect_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = "retail-data"
    bronze_folder = "bronze/"  # this is our bronze directory in our container

    # upload kaggle data to our blob storage
    for filename in os.listdir("./mydata"):
        filepath = os.path.join("./mydata", filename)
        if filename.endswith(".csv"):
            with open(filepath, "rb") as csv_data:
                blob_path = os.path.join(bronze_folder, filename)
                blob_client = blob_service_client.get_blob_client(
                    container=container_name, blob=blob_path
                )
                blob_client.upload_blob(data=csv_data, overwrite=True)
                print(
                    f"Uploaded {filename} to Azure Blob Storage under {bronze_folder}"
                )

    # # uncomment to clean up the downloaded dataset directory in our local environment
    # import shutil
    # shutil.rmtree('./data')


if __name__ == "__main__":
    upload_to_azure()
