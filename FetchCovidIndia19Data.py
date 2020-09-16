import pandas as pd
from  fetchCovidIndiadata import Covid19IndiaData as Covid19
import os
import matplotlib.pyplot as plt

class CovidIndiaData( Covid19 ):
    def __init__(self):
        Covid19.__init__( self )

    def init_display(self):
        pd.set_option( 'display.max_rows', None )
        pd.set_option( 'display.max_columns', None )

    '''
    Function Name:get_statewise_data
    Argument: None
    Functionality : Takes statewise time series data (daily incremental data) from Covid19IndiaData class.                
    Ruturns: dataframe which contains per day data from total confirmed, total death, toltal recoved 
    data for covid patients in india    
    '''
    def get_statewise_data(self):
        try:
            StateWiseList = super( CovidIndiaData, self ).get_statewise_data()
            StateWiseData = pd.DataFrame( StateWiseList )
            return StateWiseData
        except:
            print("Error in getting Statewise timeseries covid19 India data  from Covid19IndiaData")

    '''
    Function Name:get_dayWise_total_data
    Functionality : Takes time series data (daily incremental data) from Covid19IndiaData class.                
    Ruturns: dataframe which contains per day data from total confirmed, total death, toltal recoved 
    data for covid patients in india    
    '''
    def get_dayWise_total_data(self):
        try:
            pd.options.display.max_columns = None
            pd.options.display.max_rows = None
            TimeSeriesList = super( CovidIndiaData, self ).get_time_series_data()
            TimeSeriesData = pd.DataFrame( TimeSeriesList )
            return TimeSeriesData[['date', 'totalconfirmed', 'totaldeceased', 'totalrecovered']]
        except:
            print("Error in getting total timeseries covid19 India data  from Covid19IndiaData")

    '''
    Function Name:get_lastWeek_total_data
    Functionality : Takes time series data (daily incrementaal data) from Covid19IndiaData.                
    Ruturns: dataframe which contains last seven days data from total confirmed, total death, toltal recoved 
    data for covid patients in india    
    '''
    def get_lastWeek_total_data(self):
        try:
            pd.options.display.max_columns = None
            pd.options.display.max_rows = None
            TimeSeriesList = super( CovidIndiaData, self ).get_time_series_data()
            TimeSeriesData = pd.DataFrame( TimeSeriesList, columns =['date', 'totalconfirmed', 'totaldeceased', 'totalrecovered'] )
            return TimeSeriesData.tail(7)
        except:
            print( "Error in getting last week total timeseries covid19 India data  from Covid19IndiaData" )

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
        try:
            pd.options.display.max_columns = None
            pd.options.display.max_rows = None
            TimeSeriesList = super( CovidIndiaData, self ).get_time_series_data()
            TimeSeriesData = pd.DataFrame( TimeSeriesList )
            return TimeSeriesData[['date', 'dailyconfirmed', 'dailydeceased', 'dailyrecovered']]
        except:
            print( "Error in getting last week timeseries covid19 India data  from Covid19IndiaData" )

    '''
    Function Name:get_daywise_lastWeek_total_data
    Functionality : Takes time series data (daily incrementaal data) from Covid19IndiaData.                
    Ruturns: dataframe which contains last seven days data from total confirmed, total death, toltal recoved 
    data for covid patients in india    
    '''
    def get_daywise_lastWeek_total_data(self):
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        try:
            TimeSeriesList = super( CovidIndiaData, self ).get_time_series_data()
            TimeSeriesData = pd.DataFrame( TimeSeriesList,
                                       columns=['date' ,'dailyconfirmed', 'dailydeceased', 'dailyrecovered'] )
            return TimeSeriesData.tail(7)
        except:
            print("Error in getting timeseries covid19 India data  from Covid19IndiaData")

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
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        TestedList = super( CovidIndiaData, self ).get_time_series_data()
        TestedData = pd.DataFrame( TestedList )
        return TestedData



def test():
    covidIndia_Data = CovidIndiaData()
    print(covidIndia_Data.get_statewise_data())



test()