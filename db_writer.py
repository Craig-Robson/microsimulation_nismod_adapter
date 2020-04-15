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
year = cfg['api parameters']['year']
scale = cfg['api parameters']['scale']
data_version = cfg['api parameters']['data_version']

# read in the data files
data_location = os.path.abspath('..', 'microsimulation', 'data')
data_files = glob.glob(data_location+'.*.csv')

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

response = requests.post('%s?year=%s&scale=%s&data_version=%s' %(url, data_year, scale, data_version), auth=(username, password), data=dataframe.to_json())
