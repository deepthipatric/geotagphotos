import pandas as pd
import os
import subprocess

# Path to the CSV file and the photo directory
csv_path = r"..\location.csv"
photos_dir = r"..photofolder\photos"
exiftool_path = r"..location_of_exiftool\exiftool.exe"  

# Read the CSV file, assuming the delimiter is a comma
data = pd.read_csv(csv_path, delimiter=',')

# Remove any leading or trailing spaces from column names
data.columns = data.columns.str.strip()

# Print column names to verify they are read correctly
print("Column names:", data.columns)

# Check the first few rows to verify the data
print(data.head())
for index, row in data.iterrows():
    latitude = row['Y']
    longitude = row['X']
    photo = row['Photograph']
    
    # Construct the full path to the photo
    photo_path = os.path.join(photos_dir, photo)
    
    #  exiftool command
 # the Lat and Long is in WGS84 cordinates
    command = [
        exiftool_path,
        f"-GPSLatitude={latitude}",
        f"-GPSLatitudeRef={'N' if latitude >= 0 else 'S'}",
        f"-GPSLongitude={longitude}",
        f"-GPSLongitudeRef={'E' if longitude >= 0 else 'W'}",
        "-overwrite_original",  # Add this option to overwrite the original files to avoid creating a duplication file
        photo_path
    ]
    
    # Run the command
    subprocess.run(command)

print("Batch geotagging completed.")
