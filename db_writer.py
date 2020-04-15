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

for file_path in data_files:
    data_frame = pandas.read_csv(file_path)

response = requests.post('%s?year=%s&scale=%s&data_version=%s' %(url, year, scale, data_version), auth=(username, password), data=dataframe.to_json())
