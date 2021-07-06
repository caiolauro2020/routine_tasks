import os
import glob
import pandas as pd
dir_path = r'insert_directory_path'
os.chdir(dir_path)
file_extension = ".csv"
#list al files contained in given directory
all_filenames = [i for i in glob.glob(f"*{file_extension}")]
#concatenate all files in a single dataframe
df = pd.concat([pd.read_csv(file, delimiter= ';') for file in all_filenames])
#create excel file with created dataframe
df.to_excel(r'insert.xlsx_path')
