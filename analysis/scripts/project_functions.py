# This fiile contains the functions used in the project
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from datetime import datetime, date

#Functions below    
def load_and_process(filename, data_type):
    """
    Load and process data as needed depending on which data was passed; india or state
    Args:
        filename(String): Name of file to be loaded
        data_type(String): india or state

    Returns:
        df(pandas.DataFrame): Data loaded into df
    """
    df=[]
    if data_type=="state":
        # Loading data by method chaining as required 
        # Statewise Dataset
        df = (pd.read_csv(filename)
                .drop(columns = ["Negative"]) # We do not need the number of people who tested negative
                .rename(columns = {"TotalSamples":"Cumulative_Tests"})# Total sample sounds confusing
                .dropna() #Dropping NA values since they are not usefull and not representative of real life data
                )
        df["Date"] = pd.to_datetime(df["Date"], yearfirst=False)
        # dates = [d for d in df["Date"]]
        # dates = [date.fromisoformat(d.replace("/","-")) for d in dates]
        # df = df.drop(columns = ["Date"])
        # df["Date"]=[0]*len(df)
        # df["Date"] = dates
    elif data_type=="india":
        df = (pd.read_csv(filename)
                .drop(columns = ["ConfirmedIndianNational", "ConfirmedForeignNational", "Sno", "Time"]) #Total in Confirmed
                .rename(columns = {"Confirmed":"Positives"})
                .dropna() #Dropping NA values since they are not usefull and not representative of real life data
            )
        df["Date"] = pd.to_datetime(df["Date"], yearfirst=False, dayfirst=True)
        # dates = [d for d in df["Date"]]
        # dates = [date.fromisoformat('2020-'+d.replace("/","-")[3:6]+d.replace("/","-")[6:]) for d in dates]
        # df = df.drop(columns = ["Date"])
        # df["Date"]=[0]*len(df)
        # df["Date"] = dates
        # df = df.sort_values("Date")# Sorting by date
    return df

def plot_correlation_matrix(df):
    """
    Plot the dataframe's correlation matrix
    Args:
        df(pandas.DataFrame): DataFrame with loaded data
    Returns:
        df(pandas.DataFrame): Data loaded into df-------------
    """
    corr = df.corr()# plot the heatmap
    return sns.heatmap(corr, xticklabels=corr.columns, 
            yticklabels=corr.columns, annot=True, 
            cmap=sns.diverging_palette(220, 20, as_cmap=True))
         
