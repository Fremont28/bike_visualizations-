#7/14/18
#import libraries
#code for creating bike performance visualizations
#based on the rider's cadence, power, velocity, and heartrate 
import stravalib as strava 
import units
import matplotlib.pyplot as plotlib 
import numpy as np
import pandas as pd 
import seaborn as sns
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import seaborn as sns 
from matplotlib.backends.backend_pdf import PdfPages
from latex import build_pdf

#import sample csv 
bike_rides=pd.read_csv("final_df.csv")

class Bike_Visualizations():
    def __init__(self):
        pass
    #3-D ride profile 
    def ride_profile(self,x):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x['lat'], x['long'], x['altitude'],c=x['power']) 
        ax.view_init(60, 190)
        plt.xlabel('longitude')
        plt.ylabel('latitude')
        zLabel = ax.set_zlabel('altitude (m)', linespacing=3.9)
        legend=['power']
        plt.legend(legend)
        plt.show()
        return fig 
    #summary (average) ride chart 
    def avg_score(self,x):
        fig=plt.figure()
        for i in range(0,len(x)):
            avg_scores=x.mean()
            avg_df=pd.DataFrame(avg_scores,columns=['avg'])
            avg_df=avg_df.drop(['time','long','lat','grade'])
            avg_df.reset_index(level=0,inplace=True)
        sns.barplot(x="index",y="avg",data=avg_df)
        plt.xlabel('')
        plt.ylabel('')
        plt.title('Average Metrics')
        plt.show() 
        return fig 
    #maximum ride chart
    def max_score(self,x):
        fig=plt.figure()
        for i in range(0,len(x)):
            max_scores=x.max()
            max_df=pd.DataFrame(max_scores,columns=['max'])
            max_df=max_df.drop(['time','long','lat','grade','heartrate'])
            max_df.reset_index(level=0,inplace=True)
        sns.barplot(x="index",y="max",data=max_df)
        plt.xlabel('')
        plt.ylabel('')
        plt.title('Maximum Metrics')
        plt.show() 
        return fig 
    #minimum ride chart (set min values for cadence, power)
    def min_score(self,x):
        fig=plt.figure()
        for i in range(0,len(x)):
            min_scores=x.min()
            min_df=pd.DataFrame(min_scores,columns=['min'])
            min_df=min_df.drop(['time','long','lat','grade','heartrate'])
            min_df.reset_index(level=0,inplace=True)
        sns.barplot(x="index",y="min",data=min_df)
        plt.xlabel('')
        plt.ylabel('')
        plt.title('Minimum Metrics')
        plt.show() 
        return fig 
    #elevation (+/-) gain over the ride
    def altitude_gain(self,x):
        fig=plt.figure()
        for i in range(0,len(x)):
            diff=x.set_index('time').diff()
            diff_altitude=diff['altitude'].sum() 
            diff_altitude=pd.DataFrame([diff_altitude],columns=['altitude_change'])
            diff_altitude.reset_index(level=0,inplace=True)
        sns.barplot(x="index",y="altitude_change",data=diff_altitude)
        plt.xlabel('Elevation Change')
        plt.ylabel('')
        plt.title('')
        plt.show() 
        return fig 

class Bike_Visualizations1():
    def __init__(self):
            pass
    #speed vs. time scatterplot 
    def speed_scatter(self,x):
        fig=plt.figure() 
        sns.regplot(x['time'],x['velocity'],fit_reg=False)
        plt.xlabel('time (seconds)')
        plt.ylabel('velocity (m/s)')
        plt.title('Time vs. Velocity')
        plt.show() 
        return fig 
    #heartrate vs. time scatterplot 
    def heartrate_scatter(self,x):
        fig=plt.figure() 
        sns.regplot(x['time'],x['velocity'],fit_reg=False)
        plt.xlabel('time (seconds)')
        plt.ylabel('heartrate (BPM)')
        plt.title('Time vs. Heartrate')
        plt.show()  
        return fig
    #velocity vs. cadence
    def velo_cadence(self,x):
        fig=plt.figure() 
        sns.regplot(x['cadence'],x['velocity'],fit_reg=False)
        plt.xlabel('cadence')
        plt.ylabel('velocity (m/s)')
        plt.title('Cadence vs. Velocity')
        plt.show()
        return fig 
       
class Bike_Visualizations2():
    def __init__(self):
        pass 
    #power histogram 
    def power_hist(self,x):
        fig=plt.figure() 
        sns.distplot(x['power'],bins=100)
        plt.xlabel('Power')
        plt.ylabel('Frequency')
        plt.title('Power Histogram')
        plt.show() 
        return fig 
    #cadence histogram
    def cadence_hist(self,x):
        fig=plt.figure() 
        sns.distplot(x["cadence"],bins=100)
        plt.xlabel('Cadence')
        plt.ylabel('Frequency')
        plt.title('Cadence Histogram')
        plt.show() 
        return fig 
    #velocity histogram 
    def velocity_hist(self,x):
        fig=plt.figure() 
        sns.distplot(x["velocity"],bins=100)
        plt.xlabel('Velocity')
        plt.ylabel('Frequency')
        plt.title('Velocity Histogram')
        plt.show() 
        return fig 
    #grade vs. time 
    def grade_time(self,x):
        fig=plt.figure() 
        sns.regplot(x['time'],x['grade'],fit_reg=False)
        plt.xlabel('time')
        plt.ylabel('grade')
        plt.title('Time vs. Grade')
        plt.show()
        return fig 
    #joint plot (grade vs. velocity)
    def joint_plot(self,df):
        fig=plt.figure()
        sns.axes_style('white')
        sns.jointplot(df["grade"],df["velocity"],data=df,kind="hex")
        plt.show() 
        return fig 

#energy states (based on velocity and slope)
class High_Energy_State():
    def __init__(self):
        pass
    
    #how frequently rider acheives a high energy state on the uphill 
    def velocity_score_uphill(self,x): #grade,velocity 
        fig=plt.figure() 
        pos_high_velo=[]
        pos_avg_velo=[]
        pos_velo_low=[]
        #slope percentiles 
        df_slope=x['grade']
        df_slope=np.asarray(df_slope)
        df_slope_high=np.percentile(df_slope,80)
        df_slope_avg=np.percentile(df_slope,50)
        df_slope=np.asarray(df_slope)
        df_slope=df_slope.tolist()
        #velocity percentiles
        df_velo=x['velocity']
        df_velo=np.asarray(df_velo)
        df_velo_high=np.percentile(df_velo,85)
        df_velo_high1=np.percentile(df_velo,70)
        df_velo_avg=np.percentile(df_velo,50)
        df_velo=np.asarray(df_velo)
        df_velo=df_velo.tolist() 
        for i in range(0,len(df_slope)):
            slope=df_slope[i]
            velocity=df_velo[i]
            if (slope>=df_slope_high and velocity>=df_velo_avg):
                pos_high_velo.append(velocity)
            if (slope>=df_slope_avg and slope<df_slope_high) and (velocity>=df_velo_high1): 
                pos_avg_velo.append(velocity)
            if (slope<df_slope_avg and velocity>df_velo_high):
                pos_velo_low.append(velocity)
        high_energy_count=len(pos_high_velo)+len(pos_avg_velo)+len(pos_velo_low)
        total_count=len(df_velo)
        uphill_energy=high_energy_count/total_count
        uphill_energy=pd.DataFrame([uphill_energy],columns=['high_energy'])
        sns.barplot(y="high_energy",data=uphill_energy)
        plt.xlabel('')
        plt.ylabel('')
        plt.figtext(0.95, 0.02, 'Percentage rider is cycling faster than his average velocity on uphill', horizontalalignment='right')
        plt.title('Uphill High Velocity')
        plt.grid(True)
        plt.show() 
        return fig 

    def velocity_score_downhill(self,x):
        fig=plt.figure() 
        neg_high_velo=[]
        neg_avg_velo=[]
        neg_velo_low=[]
        #slope percentiles 
        df_slope=x['grade']
        df_slope=np.asarray(df_slope)
        df_slope_high=np.percentile(df_slope,80)
        df_slope_avg=np.percentile(df_slope,50)
        df_slope=np.asarray(df_slope)
        df_slope=df_slope.tolist()
        #velocity percentiles
        df_velo=x['velocity']
        df_velo=np.asarray(df_velo)
        df_velo_high=np.percentile(df_velo,85)
        df_velo_high1=np.percentile(df_velo,70)
        df_velo_avg=np.percentile(df_velo,50)
        df_velo=np.asarray(df_velo)
        df_velo=df_velo.tolist() 
        for i in range(0,len(df_slope)):
            slope=df_slope[i]
            velocity=df_velo[i]
            if (slope>=df_slope_high and velocity>=df_velo_avg):
                neg_high_velo.append(velocity)
            if (slope>=df_slope_avg and slope<df_slope_high) and (velocity>=df_velo_high1): 
                neg_avg_velo.append(velocity)
            if (slope<df_slope_avg and velocity>df_velo_high):
                neg_velo_low.append(velocity)
        high_energy_count=len(neg_high_velo)+len(neg_avg_velo)+len(neg_velo_low)
        total_count=len(df_velo) 
        downhill_energy=high_energy_count/total_count
        downhill_energy=pd.DataFrame([downhill_energy],columns=['high_energy'])
        sns.barplot(y="high_energy",data=downhill_energy)
        plt.xlabel('')
        plt.ylabel('')
        plt.figtext(0.95, 0.02, 'Percentage rider is cycling faster than his average velocity on downhill', horizontalalignment='right')
        plt.title('Downhill High Velocity')
        plt.grid(True)
        plt.show() 
        return fig 

class Low_Energy_State():
    def __init__(self):
        pass 
    def velocity_score_uphill1(self,x):
        fig=plt.figure() 
        pos_high_velo=[]
        pos_avg_velo=[]
        pos_velo_low=[]
        #slope percentiles 
        df_slope=x['grade']
        df_slope=np.asarray(df_slope)
        df_slope_high=np.percentile(df_slope,80)
        df_slope_avg=np.percentile(df_slope,50)
        df_slope_low=np.percentile(df_slope,30)
        df_slope=np.asarray(df_slope)
        df_slope=df_slope.tolist()
        #velocity percentiles
        df_velo=x['velocity']
        df_velo=np.asarray(df_velo)
        df_velo_high=np.percentile(df_velo,85)
        df_velo_high1=np.percentile(df_velo,70)
        df_velo_avg=np.percentile(df_velo,50)
        df_velo_low=np.percentile(df_velo,30)
        df_velo=np.asarray(df_velo)
        df_velo=df_velo.tolist() 
        for i in range(0,len(df_slope)):
            slope=df_slope[i]
            velocity=df_velo[i]
            if (slope>=df_slope_high and velocity<=df_velo_low):
                pos_high_velo.append(velocity)
            if (slope>=df_slope_avg and slope<df_slope_high) and (velocity<=df_velo_avg): 
                pos_avg_velo.append(velocity)
            if (slope<df_slope_avg and velocity<=df_velo_high1):
                pos_velo_low.append(velocity)
        high_energy_count=len(pos_high_velo)+len(pos_avg_velo)+len(pos_velo_low)
        total_count=len(df_velo)
        uphill_energy=high_energy_count/total_count
        uphill_energy=pd.DataFrame([uphill_energy],columns=['high_energy'])
        sns.barplot(y="high_energy",data=uphill_energy)
        plt.xlabel('')
        plt.ylabel('')
        plt.figtext(0.95, 0.02, 'Percentage rider is cycling slower than his average velocity on uphill', horizontalalignment='right')
        plt.title('Uphill Low Velocity Score')
        plt.grid(True)
        plt.show() 
        return fig 

    def velocity_score_downhill1(self,x):
        fig=plt.figure() 
        neg_high_velo=[]
        neg_avg_velo=[]
        neg_velo_low=[]
        #slope percentiles 
        df_slope=x['grade']
        df_slope=np.asarray(df_slope)
        df_slope_high=np.percentile(df_slope,80)
        df_slope_avg=np.percentile(df_slope,50)
        df_slope_low=np.percentile(df_slope,30)
        df_slope=np.asarray(df_slope)
        df_slope=df_slope.tolist()
        #velocity percentiles
        df_velo=x['velocity']
        df_velo=np.asarray(df_velo)
        df_velo_high=np.percentile(df_velo,85)
        df_velo_high1=np.percentile(df_velo,70)
        df_velo_avg=np.percentile(df_velo,50)
        df_velo_low=np.percentile(df_velo,40)
        df_velo=np.asarray(df_velo)
        df_velo=df_velo.tolist() 
        for i in range(0,len(df_slope)):
            slope=df_slope[i]
            velocity=df_velo[i]
            if (slope>=df_slope_high and velocity<=df_velo_low):
                neg_high_velo.append(velocity)
            if (slope>=df_slope_avg and slope<df_slope_high) and (velocity<=df_velo_avg): 
                neg_avg_velo.append(velocity)
            if (slope<df_slope_avg and velocity<df_velo_high1):
                neg_velo_low.append(velocity)
        high_energy_count=len(neg_high_velo)+len(neg_avg_velo)+len(neg_velo_low)
        total_count=len(df_velo)
        downhill_energy=high_energy_count/total_count
        downhill_energy=pd.DataFrame([downhill_energy],columns=['high_energy'])
        sns.barplot(y="high_energy",data=downhill_energy)
        plt.figtext(0.95, 0.02,'Percentage rider is cycling slower than his average velocity on downhill', horizontalalignment='right')
        plt.xlabel('')
        plt.ylabel('')
        plt.title('Downhill Low Velocity Score')
        plt.grid(True)
        plt.show() 
        return fig

#calling the functions 
viz=Bike_Visualizations() 
plotx=viz.avg_score(bike_rides)
plotx1=viz.altitude_gain(bike_rides)
plotx2=viz.ride_profile(bike_rides)
plotx3=viz.max_score(bike_rides)
pp=PdfPages('plots1.pdf')
pp.savefig(plotx)
pp.savefig(plotx1)
pp.savefig(plotx2)
pp.savefig(plotx3)
pp.close()

viz1=Bike_Visualizations1() 
plot1=viz1.heartrate_scatter(bike_rides)
plot2=viz1.speed_scatter(bike_rides)
plot3=viz1.velo_cadence(bike_rides)
pp=PdfPages('plots2.pdf')
pp.savefig(plot1)
pp.savefig(plot2)
pp.savefig(plot3)
pp.close()

viz2=Bike_Visualizations2()
plot1=viz2.power_hist(bike_rides)
plot2=viz2.cadence_hist(bike_rides)
plot3=viz2.velocity_hist(bike_rides)
plot4=viz2.grade_time(bike_rides)
plot5=viz2.joint_plot(bike_rides)
pp=PdfPages('plots3.pdf')
pp.savefig(plot1)
pp.savefig(plot2)
pp.savefig(plot3)
pp.savefig(plot4)
pp.savefig(plot5)
pp.close()

energy_high=High_Energy_State()
plotx1=energy_high.velocity_score_uphill(bike_rides)
plotx2=energy_high.velocity_score_downhill(bike_rides)
pp=PdfPages("energy_high1.pdf")
pp.savefig(plotx1)
pp.savefig(plotx2)
pp.close() 

energy_low=Low_Energy_State()
plotx1=energy_low.velocity_score_downhill1(bike_rides)
plotx2=energy_low.velocity_score_uphill1(bike_rides)
pp=PdfPages("energy_low1.pdf")
pp.savefig(plotx1)
pp.savefig(plotx2)
pp.close() 