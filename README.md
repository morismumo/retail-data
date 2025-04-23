This project aims to process retail-data sourced from Kaggle. All code is in the scripts folder.
Several steps are applied including uploading the data to azure cloud, data cleaning, and storage in a database.
To keep the project's cost low, the use of opensource technology was preferred.

Bash code;

1. To remove non csv files within the folder
find . -type f -not -name "*.csv" -delete

2. Renaming csv files by replacing every space " " occurence with an underscore _
sudo apt install rename && rename "s/ /_/g" *