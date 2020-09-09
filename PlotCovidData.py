import pandas as pd
from  FetchCovidIndia19Data import CovidIndiaData as CovidIndData
import os
import matplotlib.pyplot as plt

class PlotCovidIndiaData( CovidIndData ):
    
    def __init__(self):
        CovidIndData.__init__( self )
        print("PlotCovidIndiaData :: constructor Called")

    def init_display(self):
        pd.set_option( 'display.max_rows', None )
        pd.set_option( 'display.max_columns', None )
        
    def plot_daywise_lastWeek_total_data(self,day=7,type='line'):
        print("Inside : plot_daywise_lastWeek_total_data")
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        
        Plot_weeklyDaywise_Data = super( PlotCovidIndiaData, self ).get_daywise_lastWeek_total_data()

        plt.style.use( plt.style.available[9] )
        plt.xlabel( "DATE" )

        Plot_weeklyDaywise_Data.dailyconfirmed = pd.to_numeric( Plot_weeklyDaywise_Data.dailyconfirmed )
        Plot_weeklyDaywise_Data.dailydeceased = pd.to_numeric( Plot_weeklyDaywise_Data.dailydeceased )
        Plot_weeklyDaywise_Data.dailyrecovered = pd.to_numeric( Plot_weeklyDaywise_Data.dailyrecovered )

        plt.plot( Plot_weeklyDaywise_Data.date, Plot_weeklyDaywise_Data.dailyconfirmed, color='orange',
                  label='Daily Confirmed' )
        plt.plot( Plot_weeklyDaywise_Data.date, Plot_weeklyDaywise_Data.dailydeceased, color='red', label='Daily Death' )
        plt.plot( Plot_weeklyDaywise_Data.date, Plot_weeklyDaywise_Data.dailyrecovered, color='green',
                  label='Daily Recovered' )
        
        plt.legend( loc=6 )
        plt.show()
    
    def plot_daywise_lastWeek_data(self,day=7):
        print( "Inside : plot_daywise_lastWeek_data" )
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None

        Plot_weeklyDaywise_Data = super( PlotCovidIndiaData, self ).get_lastWeek_total_data()
        print(Plot_weeklyDaywise_Data)
        plt.style.use( plt.style.available[9] )
        #plt.xlabel( "DATE" )

        Plot_weeklyDaywise_Data.totalconfirmed = pd.to_numeric( Plot_weeklyDaywise_Data.totalconfirmed )
        Plot_weeklyDaywise_Data.totaldeceased = pd.to_numeric( Plot_weeklyDaywise_Data.totaldeceased )
        Plot_weeklyDaywise_Data.totalrecovered = pd.to_numeric( Plot_weeklyDaywise_Data.totalrecovered )

        plt.plot( Plot_weeklyDaywise_Data.date, Plot_weeklyDaywise_Data.totalconfirmed, color='orange',
                  label='Daily Confirmed' )
        plt.plot( Plot_weeklyDaywise_Data.date, Plot_weeklyDaywise_Data.totaldeceased, color='red',
                  label='Daily Death' )
        plt.plot( Plot_weeklyDaywise_Data.date, Plot_weeklyDaywise_Data.totalrecovered, color='green',
                  label='Daily Recovered' )

        plt.legend( loc=6 )
        plt.show()
    

