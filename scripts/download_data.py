import kaggle
import os


def download_to_local():
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


if __name__ == "__main__":
    download_to_local()
