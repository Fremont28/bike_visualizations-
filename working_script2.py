import stravalib as strava 
import units
import matplotlib.pyplot as plotlib 
import numpy as np
import pandas as pd 
import seaborn as sns
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import seaborn as sns 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_pdf import PdfPages

"""
This script runs visualiations on the collected Strava data from csv files and 
outputs how the rider is performing on uphills and downhills. In addition,
the script also compares the rider's current power, velocity, and cadence against 
his ride history. 

"""

#import sample csv files 
frank_rides=pd.read_csv("final_df.csv")
ride_history=pd.read_csv("magnes_data4.csv")

class Bike_Visualizations():
    def __init__(self):
        pass
    #3-D ride profile 
    def ride_profile(self,x):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x['lat'], x['long'], x['altitude']) 
        ax.view_init(60, 190)
        plt.xlabel('longitude')
        plt.ylabel('latitude')
        zLabel = ax.set_zlabel('altitude (m)', linespacing=3.9)
        plt.grid(True)
        #plt.show()
        plt.annotate('Altitude profile of the ride',(0,0),(65,-25),
        xycoords='axes fraction', textcoords='offset points', va='top')
        return fig 
    #summary (average) ride chart 
    def avg_score(self,x):
        fig=plt.figure()
        for i in range(0,len(x)):
            avg_scores=x.mean()
            avg_df=pd.DataFrame(avg_scores,columns=['avg'])
            avg_df=avg_df.drop(['time','long','lat','grade','power'])
            avg_df.reset_index(level=0,inplace=True)
        sns.barplot(x="index",y="avg",data=avg_df)
        plt.xlabel('')
        plt.ylabel('')
        plt.title('Average Metrics')
        plt.annotate('Average metrics over the ride',(0,0),(65,-25),
        xycoords='axes fraction', textcoords='offset points', va='top')
        plt.grid('True')
        #plt.show() 
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
        plt.annotate('Maximum metrics over the ride',(0,0),(65,-25),
        xycoords='axes fraction', textcoords='offset points', va='top')
        plt.grid(True)
        #plt.show() 
        return fig 
    #minimum ride chart (set min values for cadence, power)
    """def min_score(self,x):
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
        plt.grid(True)
        #plt.show() 
        return fig"""
    #elevation gain over the ride
    def altitude_gain(self,x):
        fig=plt.figure()
        for i in range(0,len(x)):
            diff=x.set_index('time').diff()
            diff_altitude=diff['altitude'].sum() 
            diff_altitude=pd.DataFrame([diff_altitude],columns=['altitude_change'])
            diff_altitude.reset_index(level=0,inplace=True)
        sns.barplot(x="index",y="altitude_change",data=diff_altitude)
        plt.xlabel('Slope Change')
        plt.ylabel('')
        plt.title('Slope Change Over the Ride')
        plt.grid(True)
        #plt.annotate('Slope change over the ride', (0,0), (85, -50), xycoords='axes fraction', textcoords='offset points', va='top')
        #plt.show() 
        return fig 
    #speed scatterplot 
    def speed_scatter(self,x):
        fig=plt.figure() 
        x1=x[x>0]
        x1['velocity']=x1['velocity']*3.6 
        sns.regplot(x1['time'],x1['velocity'],fit_reg=False)
        plt.xlabel('time (seconds)')
        plt.ylabel('velocity (km/hr)')
        plt.title('Time vs. Velocity')
        plt.grid(True)
        plt.annotate('velocity vs. time over the ride', (0,0), (85, -30), xycoords='axes fraction', textcoords='offset points', va='top')
        #plt.show() 
        return fig 
    #heartrate scatterplot 
    def heartrate_scatter(self,x):
        fig=plt.figure() 
        x1=x[x>0]
        sns.regplot(x1['time'],x1['heartrate'],fit_reg=False)
        plt.xlabel('time (seconds)')
        plt.ylabel('heartrate (BPM)')
        plt.title('Time vs. Heartrate')
        plt.grid(True)
        plt.annotate('heartrate vs. time over the ride', (0,0), (85, -30), xycoords='axes fraction', textcoords='offset points', va='top')
        #plt.show()  
        return fig
    #velocity vs.cadence
    def velo_cadence(self,x):
        fig=plt.figure() 
        x1=x[x>0]
        x1['velocity']=x1['velocity']*3.6 
        sns.regplot(x1['cadence'],x1['velocity'],fit_reg=False)
        plt.xlabel('cadence')
        plt.ylabel('velocity (km/hr)')
        plt.title('Cadence vs. Velocity')
        plt.grid(True)
        plt.annotate('cadence vs. time over the ride', (0,0), (85, -30), xycoords='axes fraction', textcoords='offset points', va='top')
        #plt.show()
        return fig 
    #power histogram 
    def power_hist(self,x):
        fig=plt.figure() 
        sns.distplot(x['power'],bins=100)
        plt.xlabel('Power')
        plt.ylabel('Frequency')
        plt.title('Power Histogram')
        plt.grid(True)
        #plt.show() 
        return fig 
    #cadence histogram
    def cadence_hist(self,x):
        fig=plt.figure() 
        sns.distplot(x["cadence"],bins=100)
        plt.xlabel('Cadence')
        plt.ylabel('Frequency')
        plt.title('Cadence Histogram')
        plt.grid(True)
        #plt.show() 
        return fig 
    #velocity histogram 
    def velocity_hist(self,x):
        fig=plt.figure() 
        x['velocity']=x['velocity']*3.6 
        sns.distplot(x["velocity"],bins=100)
        plt.xlabel('Velocity (km/hr)')
        plt.ylabel('Frequency')
        plt.title('Velocity Histogram')
        plt.grid(True)
        #plt.show() 
        return fig 
    #grade vs. time 
    def grade_time(self,x):
        fig=plt.figure() 
        sns.regplot(x['time'],x['grade'],fit_reg=False)
        plt.xlabel('time')
        plt.ylabel('grade')
        plt.grid(True)
        plt.title('Time vs. Grade')
        #plt.show()
        return fig 
    #how frequently rider acheives a high energy state on the uphill (riding faster than average velocity)
    def velocity_score_uphill(self,x): 
        fig=plt.figure() 
        pos_high_velo=[]
        pos_avg_velo=[]
        pos_velo_low=[]
        x=x[x['grade']>0] 
        #slope percentiles 
        df_slope=x['grade']
        df_slope=np.asarray(df_slope)
        df_slope_high=np.percentile(df_slope,80)
        df_slope_avg=np.percentile(df_slope,50)
        df_slope=np.asarray(df_slope)
        df_slope=df_slope.tolist()
        #velocity percentiles
        df_velo=x['velocity']*3.6
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
        plt.annotate('Percentage rider is cycling faster than his average uphill velocity', (0,0), (50, -25), xycoords='axes fraction', textcoords='offset points', va='top')
        plt.title('Uphill High Velocity')
        plt.grid(True)
        #plt.show() 
        return fig 
    def velocity_score_downhill(self,x):
        fig=plt.figure() 
        neg_high_velo=[]
        neg_avg_velo=[]
        neg_velo_low=[]
        x=x[x['grade']<=0] 
        #slope percentiles 
        df_slope=x['grade']
        df_slope=np.asarray(df_slope)
        df_slope_high=np.percentile(df_slope,80)
        df_slope_avg=np.percentile(df_slope,50)
        df_slope=np.asarray(df_slope)
        df_slope=df_slope.tolist()
        #velocity percentiles
        df_velo=x['velocity']*3.6 
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
        plt.annotate('Percentage rider is cycling faster than his average downhill velocity', (0,0), (50, -25), xycoords='axes fraction', textcoords='offset points', va='top')
        plt.title('Downhill High Velocity')
        plt.grid(True)
        #plt.show() 
        return fig 
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
            if (slope<=df_slope_high and velocity>df_velo_low):
                pos_high_velo.append(velocity)
            if (slope>=df_slope_avg and slope<df_slope_high) and (velocity<=df_velo_avg): 
                pos_avg_velo.append(velocity)
            if (slope<df_slope_avg):
                pos_velo_low.append(velocity)
        high_energy_count=len(pos_high_velo)+len(pos_avg_velo)+len(pos_velo_low)
        total_count=len(df_velo)
        uphill_energy=high_energy_count/total_count
        uphill_energy=pd.DataFrame([uphill_energy],columns=['high_energy'])
        sns.barplot(y="high_energy",data=uphill_energy)
        plt.xlabel('')
        plt.ylabel('')
        plt.annotate('Percentage rider is cycling slower than his average uphill velocity', (0,0), (50, -25), xycoords='axes fraction', textcoords='offset points', va='top')
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
            if (slope<=df_slope_high and velocity>df_velo_low):
                neg_high_velo.append(velocity)
            if (slope>=df_slope_avg and slope<df_slope_high) and (velocity<=df_velo_avg): 
                neg_avg_velo.append(velocity)
            if (slope<df_slope_avg):
                neg_velo_low.append(velocity)
        high_energy_count=len(neg_high_velo)+len(neg_avg_velo)+len(neg_velo_low)
        total_count=len(df_velo)
        downhill_energy=high_energy_count/total_count
        downhill_energy=pd.DataFrame([downhill_energy],columns=['high_energy'])
        sns.barplot(y="high_energy",data=downhill_energy)
        plt.annotate('Percentage rider is cycling faster than his average downhill velocity', (0,0), (50, -25), xycoords='axes fraction', textcoords='offset points', va='top')
        plt.xlabel('')
        plt.ylabel('')
        plt.title('Downhill Low Velocity Score')
        plt.grid(True)
        #plt.show() 
        return fig
    def max_scores(self,df,df1): #df=past rides, df1=current ride
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(10,5))
        max_velo=df['velocity'].max()
        #max_velo_km=3.6*max_velo
        max_velo1=df1['velocity'].max()
        percent_velo=max_velo/max_velo1
        percent_velo=pd.Series(percent_velo) 
        percent_velo=pd.DataFrame(percent_velo,columns=['percent of maximum velocity'])
        max_hr=df['heartrate'].max()
        percent_hr=(df1['heartrate'].max())/max_hr
        percent_hr=pd.Series(percent_hr)
        percent_hr=pd.DataFrame(percent_hr,columns=['percent of maximum heartrate'])
        max_cadence=df['moving1'].max()
        percent_cadence=(df1['cadence'].max())/max_cadence
        percent_cadence=pd.Series(percent_cadence)
        percent_cadence=pd.DataFrame(percent_cadence,columns=['percent of maximum cadence'])
        df_max=pd.concat([percent_velo,percent_hr],axis=1)
        df_max1=pd.concat([df_max,percent_cadence],axis=1)
        df_max2=df_max1.T
        df_max2.columns=['max_value']
        df_max2.reset_index(level=0,inplace=True)
        sns.barplot(x='index',y='max_value',data=df_max2)
        plt.xlabel("")
        plt.ylabel("Percent of Maximum")
        plt.title("")
        plt.grid(True)
        plt.annotate('Comparing the maximum metric relative to the maximum metric of past rides',(0,0),(65,-25),
        xycoords='axes fraction', textcoords='offset points', va='top')
        #plt.show() 
        return fig
    def avg_scores(self,df,df1): #df=past rides, df1=current ride
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(10,5))
        mean_velo=df['velocity'].mean()
        #mean_velo_km=3.6*mean_velo
        mean_velo1=df1['velocity'].mean()
        percent_velo=mean_velo/mean_velo1
        percent_velo=pd.Series(percent_velo) 
        percent_velo=pd.DataFrame(percent_velo,columns=['percent of average velocity'])
        mean_hr=df['heartrate'].mean()
        percent_hr=(df1['heartrate'].mean())/mean_hr
        percent_hr=pd.Series(percent_hr)
        percent_hr=pd.DataFrame(percent_hr,columns=['percent of average heartrate'])
        mean_cadence=df['moving1'].mean()
        percent_cadence=(df1['cadence'].mean())/mean_cadence
        percent_cadence=pd.Series(percent_cadence)
        percent_cadence=pd.DataFrame(percent_cadence,columns=['percent of average cadence'])
        df_mean=pd.concat([percent_velo,percent_hr],axis=1)
        df_mean1=pd.concat([df_mean,percent_cadence],axis=1)
        df_mean2=df_mean1.T
        df_mean2.columns=['avg_value']
        df_mean2.reset_index(level=0,inplace=True)
        sns.barplot(x='index',y='avg_value',data=df_mean2)
        plt.xlabel("")
        plt.ylabel("Percent of Average")
        plt.title("")
        plt.grid(True)
        plt.annotate('Comparing the average metric relative to the average metrics of past rides',(0,0),(65,-25),
        xycoords='axes fraction', textcoords='offset points', va='top')
        #plt.show() 
        return fig

if __name__ == '__main__':
    s = Bike_Visualizations() 
    #plot1=s.velocity_score_uphill1(frank_rides)
    #plot2=s.altitude_gain(frank_rides)
    plot3=s.avg_score(frank_rides)
    plot4=s.max_score(frank_rides)
    #plot5=s.min_score(frank_rides)
    plot6=s.altitude_gain(frank_rides)
    plot7=s.speed_scatter(frank_rides)
    plot8=s.heartrate_scatter(frank_rides)
    plot9=s.velo_cadence(frank_rides)
    plot10=s.power_hist(frank_rides)
    plot11=s.cadence_hist(frank_rides)
    plot12=s.velocity_hist(frank_rides)
    plot13=s.grade_time(frank_rides)
    plot14=s.velocity_score_uphill(frank_rides)
    plot15=s.velocity_score_downhill(frank_rides)
    #plot16=s.velocity_score_uphill1(frank_rides)
    #plot17=s.velocity_score_downhill1(frank_rides)
    plot18=s.max_scores(ride_history,frank_rides)
    plot19=s.avg_scores(ride_history,frank_rides)
    plot20=s.ride_profile(frank_rides)
    pp=PdfPages("coca_fernet.pdf")
    #pp.savefig(plot1)
    #pp.savefig(plot2)
    pp.savefig(plot3) 
    pp.savefig(plot4)
    #pp.savefig(plot5)
    pp.savefig(plot6)
    pp.savefig(plot7)
    pp.savefig(plot8)
    pp.savefig(plot9)
    pp.savefig(plot10)
    pp.savefig(plot11)
    pp.savefig(plot12)
    pp.savefig(plot13)
    pp.savefig(plot14)
    pp.savefig(plot15)
    #pp.savefig(plot16)
    #pp.savefig(plot17)
    pp.savefig(plot18)
    pp.savefig(plot19)
    pp.savefig(plot20)
    pp.close() 
















