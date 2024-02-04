import os
import pandas as pd
from tqdm import tqdm
import geopandas as gpd  # Import geopandas
import matplotlib as mpl
import matplotlib.pyplot as plt
import mapclassify
from os.path import join as opj
import numpy as np
def save_imgs(csv_path, map_path, img_save_path, col_name, num_bins, selected_col):
    
    df = pd.read_csv(csv_path, index_col=[0])


    covid_map = gpd.read_file(map_path)
    covid_map = covid_map.drop(f'{selected_col}',axis=1)
    covid_map = covid_map.dropna(subset=['geometry'])
    covid_map = covid_map.drop_duplicates()
    col_name2 = set(df.columns) - set(col_name) #Preprocessing part, it could be removed in your case
    df = df.drop(col_name2, axis=1)
    scheme = mapclassify.Quantiles(df[f'{selected_col}'], k=num_bins)
    scheme_list = scheme.bins
    covid_map = covid_map[covid_map['ST_Name'].isin(col_name)]
    uni_dt = df.index
    print(len(uni_dt),"*"*50)
    
    for i in tqdm(len(uni_dt)): #Save plots by date
        try:
            covid_plot = covid_map.merge(df.iloc[i], right_on=['Countyname','ST_Name'], left_on=['Countyname','ST_Name'])
            covid_plot = covid_plot.sort_values(['dt','Countyname','ST_Name'])
            fig = plt.figure()
            ax2 = covid_plot.plot(column=f'{selected_col}', cmap='PiYG_r', scheme='user_defined', classification_kwds={'bins':scheme_list})
            ax2.set_axis_off()
            plt.savefig(opj(img_save_path,f'{uni_dt[i]}.png'), dpi=200)
            plt.clf()
            plt.close()
            
        except:
            fig = plt.figure()
            covid_plot = covid_map.merge(df[df['dt']==uni_dt[i]], right_on=['Countyname','ST_Name'], left_on=['Countyname','ST_Name'])
            covid_plot = covid_plot.sorrt_values(['dt','Countyname','ST_Name'])
            
            ax2 = covid_plot.plot(column=f'{selected_col}', cmap='PiYG_r', scheme='user_defined', classification_kwds={'bins':scheme_list})
            ax2.set_axis_off()
            plt.savefig(opj(img_save_path,f'{uni_dt[i]}.png'), dpi=200)
            plt.clf()
            plt.close()
