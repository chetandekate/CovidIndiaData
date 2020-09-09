import urllib.request as request
import urllib
import json
"""from dictor import dictor"""
class Covid19IndiaData():
    """
    Covid19IndiaData class implements all the functionality to fetch data of India Covid19 data
    """
    __CODECACHE__ = None

    def __init__(self):
        self._Covid19India_data_url = "https://api.covid19india.org/data.json"
        self._Covid19India_data=dict()

    def fetch_Covid19India_json_data(self):
        covid19Url = request.urlopen(self._Covid19India_data_url)
        if covid19Url.getcode() == 200:
            data = covid19Url.read()
            #get_covid19_json( data )
            return json.loads( data )
        else:
            print( "Recieved Error, Cannot parse Code :",str(covid19Url.getcode()))

    def get_state_today_data(self,state):
        StateWisedata = self.fetch_Covid19India_json_data()
        for stateData in StateWisedata["statewise"]:
            if (stateData["state"] == state):
                return stateData

    def get_statewise_data(self):
        StateWisedata = self.fetch_Covid19India_json_data()
        return StateWisedata['statewise']

    def get_time_series_data(self):
        TimeSeriesdata = self.fetch_Covid19India_json_data()
        return TimeSeriesdata['cases_time_series']

    def get_tested_data(self):
        Testeddata = self.fetch_Covid19India_json_data()
        return Testeddata['tested']

    def get_raw_data(self):
        Rawdata = self.fetch_Covid19India_json_data()
        return Rawdata

def main():
    test = Covid19IndiaData()
    '''StateWise = test.get_statewise_data()
    for state in StateWise:
        print(state)
    print(test.get_time_series_data())
    print( test.get_tested_data())
    print(test.get_raw_data())'''


main()


