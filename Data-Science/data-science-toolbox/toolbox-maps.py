# coding: utf-8
# Requires the following packages:
import numpy as np
import pandas as pd
import postcodes


def get_coordinate(postcode, coordinate_type, postcodes_df):
    "Takes a postcode, a coordinate type ('lat' or 'lng') and gives back the coordinate"
    # Is postcode in df ?
    try:
        coordinate = postcodes_df.loc[postcode][coordinate_type]
        return coordinate
    except KeyError:
        # If not: Is in the postcodes database?
        info = postcodes.get(postcode)
        if pd.isnull(info):
            print("Postcode %d does not exist" %postcode)
            return np.nan
        else:
            coordinate = info['geo'][coordinate_type]
            return coordinate


def get_coordinates_both(postcode, postcodes_df):
    "Takes a postcode, and gives back the lat and lng coordinates"
    # Is postcode empty entry?
    if pd.isnull(postcode):
        return np.nan, np.nan
    # Is postcode in df ?
    try:
        coordinate = postcodes_df.loc[postcode]
        return coordinate['lat'], coordinate['lng']
    except KeyError:
        # If not: Is in the postcodes database?
        try:
            info = postcodes.get(postcode)
            if pd.isnull(info):
                print("Postcode %s does not exist" %postcode)
                return np.nan, np.nan
            else:
                coordinate = info['geo']
                return coordinate['lat'], coordinate['lng']
        except AttributeError:
            print("There might have been a problem connecting to the postcode database.                    Are you sure, you are connected to the internet?")
            return np.nan, np.nan


def reformat_postcode_df(xcel_filepath='../gingerbread_mnt/aux_data/ukpostcodes.csv'):
    "Takes xcel file from xcel filepath and reformats the resulting dataframe to have     two columns (lat and lng) and the postcodes as index."
    postcodes_csv = pd.read_csv(xcel_filepath)
    
    # reformat into a df, where the postcode is the index
    postcodes_df = pd.DataFrame(postcodes_csv[['latitude', 'longitude']].values,                                 index = postcodes_csv['postcode'].values,                                 columns=['lat', 'lng'])
    return postcodes_df 


def find_longs_lats(df, postcodes_df):
    "Takes dataframe df, that has column Postcodes and inserts columns         Longitudinal and Latitudinal from dataframe postcodes_df"
        
    postcode_column = df.columns.get_loc("Postcode") 
    
    my_series = df['Postcode'].apply(lambda x: get_coordinates_both(x, postcodes_df))
    
    lats = my_series.apply(pd.Series)[0].values
    lngs = my_series.apply(pd.Series)[1].values
    
    df.insert(postcode_column+1, 'Latitudinal', lats)
    df.insert(postcode_column+2, 'Longitudinal', lngs)


def insert_lats_lngs_into_df(df_pkl_filepath,ukpostcodes_xcel_filepath):
    "Loads a pickled dataframe from df_pkl_filename with Column Postcodes and \
     adds columns Longitudinal and Latitudinal, based on spreadsheet at ukpostcodes_xcel_filepath. \
     Returns new dataframe and saves it to old_fileame_with_lats_lngs.pkl. \
     Usage: insert_lats_lngs_into_df(df_pkl_filepath,ukpostcodes_xcel_filepath)"
    df = pd.read_pickle(df_pkl_filepath)
    my_postcodes_df = reformat_postcode_df(ukpostcodes_xcel_filepath)
    find_longs_lats(df, my_postcodes_df)
    new_filename = df_pkl_filepath.split('/')[-1].split('.')[0] + '_with_lats_lngs' + '.pkl'
    new_filepath = ('/').join(df_pkl_filepath.split('/')[:-1] + [new_filename])
    df.to_pickle(new_filepath)
    print("The new datafame has been saved as %s" %new_filepath)
    return df
