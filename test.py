from  PlotCovidData import PlotCovidIndiaData as CovidIndiaStat
import os
class Test(CovidIndiaStat):
    def __init__(self):
        CovidIndiaStat.__init__( self )
    def main(self):
        CovidIndia_Stat = CovidIndiaStat()
        
        op=int(input("Enter Your Options...\n"
                     "1: 'Get Last 7 days data'\n"
                     "2: 'Get Last 7 days Incremential data'"))
        if op == 1:
                CovidIndia_Stat.plot_daywise_lastWeek_data()
        elif op == 2:
                CovidIndia_Stat.plot_daywise_lastWeek_total_data()
        else:
                exit()
def test():
    test_data=Test()
    test_data.main()

test()