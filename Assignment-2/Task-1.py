import os  # to deal with file io operation
import pandas as pd  # to read file

# Folder containing the CSV files
csv_folder = "./data"
output_file = "./data/task_1_merged_txt.txt"  # merged File

# Create or overwrite the text file
with open(output_file, "w", encoding="utf-8") as outfile:
    for file_name in os.listdir(csv_folder):  # loops through data folder
        if file_name.endswith(".csv"):  # picks only .csv file
            file_path = os.path.join(
                csv_folder, file_name)  # calculate file path
            # Read the CSV file
            df = pd.read_csv(file_path)  # read the filed from path
            if 'TEXT' in df.columns:  # if text coulmn exits in csv column
                # Write the 'text' column to the .txt file
                # return new series with missing values remove
                for text in df['TEXT'].dropna():
                    # output written to  merged file
                    outfile.write(text + "\n")
