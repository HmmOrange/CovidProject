import matplotlib
import matplotlib.pyplot as plt
import numpy    
class Pie:
    def __init__(self, activeCases, totalRecovered, totalDeaths):
        self.activeCases = activeCases
        self.totalRecovered = totalRecovered
        self.totalDeaths = totalDeaths
    def pieChart(self):
        data = numpy.array([self.activeCases, self.totalRecovered, self.totalDeaths])
        colors = ["#ffd800", "#ffa575", "#000000"]
        
        plt.figure(figsize = (5, 4), facecolor = "#f0f0f0")
        plt.pie(data, colors = colors, autopct = '%.2f%%', pctdistance = 1.3)
        plt.legend(loc = "upper left", labels = ["Active Cases", "Total Recovered", "Total Deaths"])
        try:
            plt.savefig('./static/potato.png')
        except:
            plt.savefig('../Bot/potato.png')
        plt.clf()
        plt.close()
