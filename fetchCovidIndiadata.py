import urllib.request as request
from urllib.error import URLError, HTTPError
import urllib
import json

class Covid19IndiaData():
    """
    Covid19IndiaData class implements all the functionality to fetch data of India Covid19 data
    """
    __CODECACHE__ = None

    def __init__(self):
        self._Covid19India_data_url = "https://api.covid19india.org/data.json"
        self._Covid19India_data=dict()

    '''
    Function Name: fetch_Covid19India_json_data
    Agrument: none
    Functionality : Reads the JSON data from the url and convert it to Python dictonary
    Return: Python Dictonary which contains consolidate covid data for INDIA.
    '''
    def fetch_Covid19India_json_data(self):
        try:
            covid19Url = request.urlopen(self._Covid19India_data_url)
        except HTTPError as e:
            print( 'The server couldn\'t fulfill the request.' )
            print( 'Error code: ', e.code )
        except URLError as e:
            print( 'We failed to reach a server.' )
            print( 'Reason: ', e.reason )
        else:
                if covid19Url.getcode() == 200:
                    data = covid19Url.read()
                    return json.loads( data )
                else:
                    print( "Recieved Error, Cannot parse Code :",str(covid19Url.getcode()))

    '''
    Function Name: get_state_data
    Argumet: State Name
    Functionality: Reads the JSON data from the url and convert it to Python dictonary
    Return: Covid 19 date for the mentioned INDIAN state
    '''
    def get_state_data(self,state):
        StateWisedata = self.fetch_Covid19India_json_data()
        for stateData in StateWisedata["statewise"]:
            if (stateData["state"] == state):
                return stateData

    '''
    Function Name: get_statewise_data
    Argumet: None
    Functionality: Reads the JSON data from the url and convert it to Python dictonary
    Return: Covid 19 date for the each state in INDIA
    '''
    def get_statewise_data(self):
        StateWisedata = self.fetch_Covid19India_json_data()
        return StateWisedata['statewise']

    '''
    Function Name: get_time_series_data
    Argumet: None
    Functionality: Reads the JSON data from the url and convert it to Python dictonary
    Return: Covid 19 dictonary which contains Times Series 
    (sequence of numerical data points in successive order) date, statewise and consolidate for INDIA
    '''
    def get_time_series_data(self):
        TimeSeriesdata = self.fetch_Covid19India_json_data()
        return TimeSeriesdata['cases_time_series']

    '''
    Function Name: get_tested_data
    Argumet: None
    Functionality: Reads the JSON data from the url and convert it to Python dictonary
    Return: Consolidate Covid 19 data in form of python dictonary 
    '''
    def get_tested_data(self):
        Testeddata = self.fetch_Covid19India_json_data()
        return Testeddata['tested']

    def get_raw_data(self):
        Rawdata = self.fetch_Covid19India_json_data()
        return Rawdata
