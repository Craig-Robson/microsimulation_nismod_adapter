"""
file patterns
household_microsynth
    hh_LADCODE_SCALE_2011.csv
microsynth - microsynth
    ????
microsynth - ssm
    ssm_LADCODE_SCALE_ppp_YEAR.csv
microsynth - assignment
    ass_LADCODE_SCALE_YEAR.csv
    ass_hh_LADCODE_SCALE_YEAR.csv
"""
import pandas
import requests
import os, configparser
import glob

# read in the config details
cfg = configparser.ConfigParser()
cfg.read(os.path.abspath(os.path.join(os.path.dirname(''), 'config.ini')))

# url/api details
# these should be loaded from a config file
url = cfg['api']['url']
username = cfg['api']['username']
password = cfg['api']['password']

# data details
scale = cfg['api parameters']['scale']
data_version = cfg['api parameters']['data_version']

# read in the data files
data_location = os.path.abspath('..', 'microsimulation', 'data')

# get only the data files for the final hh assignment
data_files = glob.glob(data_location+'.ass_hh_*.csv')

# loop through all data files
for file_path in data_files:
    # create dataframe with data
    data_frame = pandas.read_csv(file_path)

    # get the metadata for the file
    file_str = file_path.split('/')[0]
    file_str.split('_')

    # get data values
    data_lad = file_str[1]
    data_year = file_str[-1]
    data_scale = file_str[-2]

    # push data to database
    response = requests.post('%s?year=%s&scale=%s&data_version=%s' %(url, data_year, data_scale, data_version), auth=(username, password), data=data_frame.to_json())
