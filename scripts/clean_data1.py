import os
import re
import pathlib
import pandas as pd
from pathlib import Path

path1 = Path("./mydata/bronze")
path2 = Path('./mydata/silver')
def remove_non_csv_files():
    """
    remove all non csv files in this bronze directory
    """
    try:
        
        if not path1.is_dir():
            print(f"Error: {path1} not a directrory")
            return

        for file_path in path1.iterdir():
            if file_path.is_file():
                pattern = ".csv$"
                if not re.search(pattern, file_path.name):
                    try:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                    except OSError as e:
                        print(f"Error deleting {file_path: {e}}")

    except Exception as x:
        print("Error occured: {x}")

def rename_filenames():
    """
        renaming filenames by replacing space with underscore
    """
    try:
        
        if not path1.is_dir():
            print(f"Error: {path1} not a directrory")
            return

        for file_path in path1.iterdir():
            if file_path.is_file():
                old_name = str(file_path)  # converting the full path as a string
                new_name = re.sub(r"[\s]", "_", old_name)  # replacing spaces with underscores
                if old_name != new_name:
                    try:
                        os.rename(old_name, new_name)  # Renaming the file
                        print(f"Renamed: {old_name} to {new_name}")
                    except OSError as e:
                        print(f"Error renaming {old_name}: {e}")

    except Exception as x:
        print(f"Error occured: {x}")

def rename_csv_headers():
    numfiles = []
    filenames = os.listdir(path1)

    for filename in filenames:
        if filename.endswith('.csv'):
            numfiles.append(filename)

    for i in numfiles:
        file1 = os.path.join(path1, i)
        file2 = os.path.join(path2, i)
        try:

            df = pd.read_csv(file1, header=0, encoding='utf-8')
            # column operations; lowercase, replace space with underscore, & replacing hyphen with underscore
            df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('-','_').str.capitalize()
            df.to_csv(file2, index=False)

        except Exception as e:
            print(f"An error occured processing {file1}: {e}")

if __name__ == "__main__":
    # remove_non_csv_files()
    # rename_filenames()
    rename_csv_headers()