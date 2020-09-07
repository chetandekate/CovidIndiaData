import pandas as pd
from  fetchCovidIndiadata import Covid19IndiaData as Covid19
import os

class CovidIndiaData(Covid19):
    def __init__(self):
        Covid19.__init__(self)
    def init_display(self):
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)

    def get_statewise_data(self):
        StateWiseList = super( CovidIndiaData, self).get_statewise_data()
        StateWiseData = pd.DataFrame(StateWiseList)
        return StateWiseData
    
    def get_time_series_data(self):
        TimeSeriesList = super( CovidIndiaData, self ).get_time_series_data()
        TimeSeriesData = pd.DataFrame( TimeSeriesList )
        return TimeSeriesData

    def get_tested_data(self):
        TestedList = super( CovidIndiaData, self ).get_time_series_data()
        TestedData = pd.DataFrame( TestedList )
        return TestedData

    def get_raw_data(self):
        RawList = super( CovidIndiaData, self ).get_time_series_data()
        RawData = pd.DataFrame( RawList )
        return RawData

def test():
    covidIndia_Data = CovidIndiaData()

    '''TimeSeries_data = covidIndia_Data.get_time_series_data()
    print(TimeSeries_data)

    getTested_data = covidIndia_Data.get_tested_data()
    print( getTested_data )

    getStatewise_data = covidIndia_Data.get_statewise_data()
    print(getStatewise_data)

    getRaw_data = covidIndia_Data.get_raw_data()
    print( getRaw_data )'''
    
test()