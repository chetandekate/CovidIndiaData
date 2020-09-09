from  PlotCovidData import PlotCovidIndiaData as CovidIndiaStat
import os
class Test(CovidIndiaStat):
    def __init__(self):
        CovidIndiaStat.__init__( self )
    def main(self):
        CovidIndia_Stat = CovidIndiaStat()
        switcher = {
                1: 'Get Last 7 days data',
                2: 'Get Last 7 days Incremential data'
        }

        op=switcher.get( 1, "Invalid Option, Please Enter Valid Options" )
        print(op)
        if op == 1:
                print("Get Last 7 days data")
                super( CovidIndiaStat, self ).plot_daywise_lastWeek_total_data()
                #CovidIndia_Stat.plot_daywise_lastWeek_data()
        elif op == 2:
                print( "Get Last 7 days Incremental data" )
                CovidIndia_Stat = CovidIndiaStat()
                CovidIndia_Stat.plot_daywise_lastWeek_total_data()
        else:
                exit()
def test():
    test_data=Test()
    test_data.main()

test()