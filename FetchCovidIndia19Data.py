import pandas as pd
from  fetchCovidIndiadata import Covid19IndiaData as Covid19
import os


class CovidIndiaData( Covid19 ):
    def __init__(self):
        Covid19.__init__( self )

    def init_display(self):
        pd.set_option( 'display.max_rows', None )
        pd.set_option( 'display.max_columns', None )

    def get_statewise_data(self):
        StateWiseList = super( CovidIndiaData, self ).get_statewise_data()
        StateWiseData = pd.DataFrame( StateWiseList )
        return StateWiseData

    '''
    Function Name:get_dayWise_total_data
    Functionality : Takes time series data (daily incremental data) from Covid19IndiaData class.                
    Ruturns: dataframe which contains per day data from total confirmed, total death, toltal recoved 
    data for covid patients in india    
    '''
    def get_dayWise_total_data(self):
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        TimeSeriesList = super( CovidIndiaData, self ).get_time_series_data()
        TimeSeriesData = pd.DataFrame( TimeSeriesList )
        return TimeSeriesData[['date', 'totalconfirmed', 'totaldeceased', 'totalrecovered']]

    '''
    Function Name:get_lastWeek_total_data
    Functionality : Takes time series data (daily incrementaal data) from Covid19IndiaData.                
    Ruturns: dataframe which contains last seven days data from total confirmed, total death, toltal recoved 
    data for covid patients in india    
    '''
    def get_lastWeek_total_data(self):
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        TimeSeriesList = super( CovidIndiaData, self ).get_time_series_data()
        TimeSeriesData = pd.DataFrame( TimeSeriesList, columns =['date', 'totalconfirmed', 'totaldeceased', 'totalrecovered'] )
        return TimeSeriesData.tail(7)

    '''
    Function Name:get_last30days_total_data
    Functionality : Takes time series data (daily incremental data) from Covid19IndiaData.                
    Ruturns: dataframe which contains last 30 days data from total confirmed, total death, toltal recoved 
    data for covid patients in india    
    '''
    def get_last30days_total_data(self):
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        TimeSeriesList = super( CovidIndiaData, self ).get_time_series_data()
        TimeSeriesData = pd.DataFrame( TimeSeriesList,
                                       columns=['date', 'totalconfirmed', 'totaldeceased', 'totalrecovered'] )
        return TimeSeriesData.tail(30)

    '''
    Function Name:get_dayWise_data
    Functionality : Takes time series data (daily data) from Covid19IndiaData.                
    Ruturns: dataframe which contains per day data from total confirmed, total death, toltal recoved 
    data for covid patients in india    
    '''
    def get_dayWise_data(self):
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        TimeSeriesList = super( CovidIndiaData, self ).get_time_series_data()
        TimeSeriesData = pd.DataFrame( TimeSeriesList )
        return TimeSeriesData[['date', 'dailyconfirmed', 'dailydeceased', 'dailyrecovered']]

    '''
    Function Name:get_daywise_lastWeek_total_data
    Functionality : Takes time series data (daily incrementaal data) from Covid19IndiaData.                
    Ruturns: dataframe which contains last seven days data from total confirmed, total death, toltal recoved 
    data for covid patients in india    
    '''
    def get_daywise_lastWeek_total_data(self):
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        TimeSeriesList = super( CovidIndiaData, self ).get_time_series_data()
        TimeSeriesData = pd.DataFrame( TimeSeriesList,
                                       columns=['date', 'dailyconfirmed', 'dailydeceased', 'dailyrecovered'] )
        return TimeSeriesData.tail( 7 )

    '''
    Function Name:get_last30days_total_data
    Functionality : Takes time series data (daily  data) from Covid19IndiaData.                
    Ruturns: dataframe which contains last 30 days data from total confirmed, total death, toltal recoved 
    data for covid patients in india    
    '''
    def get_daywise_last30days_total_data(self):
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        TimeSeriesList = super( CovidIndiaData, self ).get_time_series_data()
        TimeSeriesData = pd.DataFrame( TimeSeriesList,
                                       columns=['date', 'dailyconfirmed', 'dailydeceased', 'dailyrecovered'] )
        return TimeSeriesData.tail( 30 )

    def get_tested_data(self):
        TestedList = super( CovidIndiaData, self ).get_time_series_data()
        TestedData = pd.DataFrame( TestedList )
        return TestedData

    def get_raw_data(self):
        RawList = super( CovidIndiaData, self ).get_daywise_last30days_total_data()
        RawData = pd.DataFrame( RawList )
        return RawData


def test():
    covidIndia_Data = CovidIndiaData()
    TimeSeries_data = covidIndia_Data.get_last30days_total_data()
    print(TimeSeries_data)

test()