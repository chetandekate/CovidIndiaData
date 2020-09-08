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
                                       columns=['date' ,'dailyconfirmed', 'dailydeceased', 'dailyrecovered'] )
        #TimeSeriesData.id = pd.to_( pf.id )
        TimeSeriesData.dailyconfirmed = pd.to_numeric( TimeSeriesData.dailyconfirmed )
        TimeSeriesData.dailydeceased = pd.to_numeric( TimeSeriesData.dailydeceased )
        TimeSeriesData.dailyrecovered = pd.to_numeric( TimeSeriesData.dailyrecovered )
        TimeSeriesData_LstWeek = TimeSeriesData.tail(7)

        #plt.xticks(rotation=90)
        plt.plot( TimeSeriesData_LstWeek.date, TimeSeriesData_LstWeek.dailyconfirmed, color='orange', label='Daily Confirmed' )
        plt.plot( TimeSeriesData_LstWeek.date, TimeSeriesData_LstWeek.dailydeceased, color='red', label='Daily Death' )
        plt.plot( TimeSeriesData_LstWeek.date, TimeSeriesData_LstWeek.dailyrecovered, color='green', label='Daily Recovered' )
        #plt.style()
        plt.legend(loc=6)
        plt.show()

        #my_plot = TimeSeries_Data_totals.plot( kind='bar')
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
    covidIndia_Data.get_daywise_lastWeek_total_data()

    '''
    
    print(TimeSeries_data)'''


test()