import pandas as pd
import matplotlib.pyplot as plt
import os

directory_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def create_dataframes()->dict:
    dataframes = {}
    
    folder_path = os.path.join(directory_path, 'Data')
    
    for filename in os.listdir(folder_path):
        current_file_path = os.path.join(folder_path, filename)
        new_df = pd.read_csv(current_file_path)
        
        file_parts = filename.split('_')
        name = file_parts[1]
        
        dataframes[name] = new_df
        
    return dataframes


def melt_dataframes(dataframes:dict):
    ''' This function melts all the month columns into one single date column for easier visualization
    '''