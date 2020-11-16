# This fiile contains the functions used in the project
import pandas as pd
import numpy as np

def load_and_process(filename, data_type):
    """
    Load and process data as needed depending on which data was passed; india or state
    Args:
        filename(String): Name of file to be loaded
        data_type(String): india or state

    Returns:
        df(pandas.DataFrame): Data loaded into df
    """
    try:

        if data_type=="india":
            # Loading data by method chaining as required 
            # Statewise Dataset
            df = (pd.read_csv(directory+files[0])
                    .drop(columns = "Negative") # We do not need the number of people who tested negative
                    .rename(columns = {"TotalSamples":"Cumulative_Tests"})# Total sample sounds confusing
                    .sort_values("Date")# Sorting by date
                    .dropna() #Dropping NA values since they are not usefull and not representative of real life data
                    )
        elif:
            df = (pd.read_csv(directory+files[2])
                    .drop(columns = ["ConfirmedIndianNational", "ConfirmedForeignNational"]) #Total in Confirmed
                    .rename(columns = {"Confirmed":"Positives"})
                    .sort_values("Date") # Sorting by date
                    .dropna()
                    )
        return df
    except:
        return "Please make sure argument for data_type is 'india' or 'state'. Try again."
         
