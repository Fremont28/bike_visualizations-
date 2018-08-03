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
ride_history1=pd.read_csv("aug_magnes.csv")
ride_history1=ride_history1.dropna()

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
        plt.close()
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
        plt.close()
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
        plt.close()
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
        plt.close()
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
        plt.close()
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
        plt.close()
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
        plt.close()
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
        plt.close()
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
        plt.close()
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
        plt.close()
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
        plt.close()
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
            if (slope<df_slope_avg):
                pos_velo_low.append(velocity)
        high_energy_count=len(pos_high_velo)+len(pos_avg_velo)+len(pos_velo_low)
        total_count=len(df_velo)
        uphill_energy=high_energy_count/total_count
        uphill_energy=pd.DataFrame([uphill_energy],columns=['high_energy'])
        sns.barplot(y="high_energy",data=uphill_energy)
        plt.xlabel('')
        plt.ylabel('')
        #plt.annotate('Percentage rider is cycling faster than his average uphill velocity', (0,0), (50, -25), xycoords='axes fraction', textcoords='offset points', va='top')
        plt.title('Uphill High Velocity')
        plt.grid(True)
        #plt.show() 
        plt.close()
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
            if (slope<df_slope_avg):
                neg_velo_low.append(velocity)
        high_energy_count=len(neg_high_velo)+len(neg_avg_velo)+len(neg_velo_low)
        total_count=len(df_velo) 
        downhill_energy=high_energy_count/total_count
        downhill_energy=pd.DataFrame([downhill_energy],columns=['high_energy'])
        sns.barplot(y="high_energy",data=downhill_energy)
        plt.xlabel('')
        plt.ylabel('')
        #plt.annotate('Percentage rider is cycling faster than his average downhill velocity', (0,0), (50, -25), xycoords='axes fraction', textcoords='offset points', va='top')
        plt.title('Downhill High Velocity')
        plt.grid(True)
        #plt.show() 
        plt.close()
        return fig 
    def max_velocity(self,df,df1):
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        max_velo_rides=df['velocity'].max()*3.6
        max_velo_rides=pd.Series(max_velo_rides)
        max_velo_rides=pd.DataFrame(max_velo_rides,columns=['max_velo_history'])
        max_velo_rides.reset_index(level=0,inplace=True)
        max_current_velo=df1['velocity'].max()*3.6
        max_current_velo=pd.Series(max_current_velo) 
        max_current_velo=pd.DataFrame(max_current_velo,columns=['max_velo_current'])
        max_current_velo.reset_index(level=0,inplace=True)
        sns.barplot(x='index',y='max_velo_history',data=max_velo_rides,color="red",label="max velocity ride history")
        sns.barplot(x='index',y='max_velo_current',data=max_current_velo,color="blue",label="max velocity current ride")
        plt.xlabel("")
        plt.ylabel("Velocity (km/hr)")
        plt.title("Comparing Current Maximum Velocity to Past Maximum Velocity")
        plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0) 
        plt.grid(True)
        #plt.show()
        plt.close()
        return fig 
    def max_power(self,df,df1):
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        max_power_rides=df['power'].max()
        max_power_rides=pd.Series(max_power_rides)
        max_power_rides=pd.DataFrame(max_power_rides,columns=['max_power_history'])
        max_power_rides.reset_index(level=0,inplace=True)
        max_current_power=df1['power'].max()
        max_current_power=pd.Series(max_current_power) 
        max_current_power=pd.DataFrame(max_current_power,columns=['max_power_current'])
        max_current_power.reset_index(level=0,inplace=True)
        sns.barplot(x='index',y='max_power_history',data=max_power_rides,color="red",label="max power ride history")
        sns.barplot(x='index',y='max_power_current',data=max_current_power,color="blue",label="max power current ride")
        plt.xlabel("")
        plt.ylabel("Power")
        plt.title("Comparing Current Maximum Power Output to Past Maximum Power Output")
        plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0) 
        plt.grid(True) 
        #plt.show()
        plt.close()
        return fig 
    def max_cadence(self,df,df1):
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        max_cadence_rides=df['cadence'].max()
        max_cadence_rides=pd.Series(max_cadence_rides)
        max_cadence_rides=pd.DataFrame(max_cadence_rides,columns=['max_cadence_history'])
        max_cadence_rides.reset_index(level=0,inplace=True)
        max_current_cadence=df1['cadence'].max()
        max_current_cadence=pd.Series(max_current_cadence) 
        max_current_cadence=pd.DataFrame(max_current_cadence,columns=['max_cadence_current'])
        max_current_cadence.reset_index(level=0,inplace=True)
        sns.barplot(x='index',y='max_cadence_history',data=max_cadence_rides,color="red",label="max cadence ride history")
        sns.barplot(x='index',y='max_cadence_current',data=max_current_cadence,color="blue",label="max cadence current ride")
        plt.xlabel("")
        plt.ylabel("Cadence")
        plt.title("Comparing Current Maximum Cadence to Past Maximum Cadence")
        plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0) 
        plt.grid(True)
        #plt.show()
        plt.close()
        return fig 
    def max_heartrate(self,df,df1):
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        max_heartrate_rides=df['heartrate'].max()
        max_heartrate_rides=pd.Series(max_heartrate_rides)
        max_heartrate_rides=pd.DataFrame(max_heartrate_rides,columns=['max_heartrate_history'])
        max_heartrate_rides.reset_index(level=0,inplace=True)
        max_current_heartrate=df1['heartrate'].max()
        max_current_heartrate=pd.Series(max_current_heartrate) 
        max_current_heartrate=pd.DataFrame(max_current_heartrate,columns=['max_heartrate_current'])
        max_current_heartrate.reset_index(level=0,inplace=True)
        sns.barplot(x='index',y='max_heartrate_history',data=max_heartrate_rides,color="red",label="max heartrate ride history")
        sns.barplot(x='index',y='max_heartrate_current',data=max_current_heartrate,color="blue",label="max heartrate current ride")
        plt.xlabel("")
        plt.ylabel("Heartrate")
        plt.title("Comparing Current Maximum Heartrate to Past Maximum Heartrate")
        plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0) 
        plt.grid(True)
        #plt.show()
        plt.close()
        return fig 
    def avg_velocity(self,df,df1):
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        mean_velo_rides=df['velocity'].mean()*3.6
        mean_velo_rides=pd.Series(mean_velo_rides)
        mean_velo_rides=pd.DataFrame(mean_velo_rides,columns=['mean_velo_history'])
        mean_velo_rides.reset_index(level=0,inplace=True)
        mean_current_velo=df1['velocity'].max()*3.6
        mean_current_velo=pd.Series(mean_current_velo) 
        mean_current_velo=pd.DataFrame(mean_current_velo,columns=['mean_velo_current'])
        mean_current_velo.reset_index(level=0,inplace=True)
        sns.barplot(x='index',y='mean_velo_current',data=mean_current_velo,color="blue",label="average velocity current ride")
        sns.barplot(x='index',y='mean_velo_history',data=mean_velo_rides,color="red",label="average velocity ride history")
        plt.xlabel("")
        plt.ylabel("Velocity (km/hr)")
        plt.title("Comparing Current Average Velocity to Past Average Velocity")
        plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0) 
        plt.grid(True)
        #plt.show()
        plt.close()
        return fig 
    def avg_power(self,df,df1):
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        mean_power_rides=df['power'].mean()
        mean_power_rides=pd.Series(mean_power_rides)
        mean_power_rides=pd.DataFrame(mean_power_rides,columns=['max_power_history'])
        mean_power_rides.reset_index(level=0,inplace=True)
        mean_current_power=frank_rides['power'].mean()
        mean_current_power=pd.Series(mean_current_power) 
        mean_current_power=pd.DataFrame(mean_current_power,columns=['max_power_current'])
        mean_current_power.reset_index(level=0,inplace=True)
        sns.barplot(x='index',y='max_power_current',data=mean_current_power,color="blue",label="average power current ride")
        sns.barplot(x='index',y='max_power_history',data=mean_power_rides,color="red",label="average power ride history")
        plt.xlabel("")
        plt.ylabel("Power")
        plt.title("Comparing Current Average Power Output to Past Average Power Output")
        plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0) 
        plt.grid(True) 
        #plt.show()
        plt.close()
        return fig 
    def avg_cadence(self,df,df1):
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        mean_cadence_rides=df['cadence'].mean()
        mean_cadence_rides=pd.Series(mean_cadence_rides)
        mean_cadence_rides=pd.DataFrame(mean_cadence_rides,columns=['mean_cadence_history'])
        mean_cadence_rides.reset_index(level=0,inplace=True)
        mean_current_cadence=df1['cadence'].mean()
        mean_current_cadence=pd.Series(mean_current_cadence) 
        mean_current_cadence=pd.DataFrame(mean_current_cadence,columns=['mean_cadence_current'])
        mean_current_cadence.reset_index(level=0,inplace=True)
        sns.barplot(x='index',y='mean_cadence_current',data=mean_current_cadence,color="blue",label="average cadence current ride")
        sns.barplot(x='index',y='mean_cadence_history',data=mean_cadence_rides,color="red",label="average cadence ride history")
        plt.xlabel("")
        plt.ylabel("Cadence")
        plt.title("Comparing Current Average Cadence to Past Average Cadence")
        plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0) 
        plt.grid(True)
        #plt.show()
        plt.close()
        return fig 
    def avg_heartrate(self,df,df1):
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        mean_heartrate_rides=df['heartrate'].mean()
        mean_heartrate_rides=pd.Series(mean_heartrate_rides)
        mean_heartrate_rides=pd.DataFrame(mean_heartrate_rides,columns=['mean_heartrate_history'])
        mean_heartrate_rides.reset_index(level=0,inplace=True)
        mean_current_heartrate=df1['heartrate'].max()
        mean_current_heartrate=pd.Series(mean_current_heartrate) 
        mean_current_heartrate=pd.DataFrame(mean_current_heartrate,columns=['mean_heartrate_current'])
        mean_current_heartrate.reset_index(level=0,inplace=True)
        sns.barplot(x='index',y='mean_heartrate_current',data=mean_current_heartrate,color="blue",label="average heartrate current ride")
        sns.barplot(x='index',y='mean_heartrate_history',data=mean_heartrate_rides,color="red",label="average heartrate ride history")
        plt.xlabel("")
        plt.ylabel("Heartrate")
        plt.title("Comparing Current Average Heartrate to Past Average Heartrate")
        plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0) 
        plt.grid(True)
        #plt.show()
        plt.close()
        return fig
    def max_power1(self,df):
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        power_sub=df['power']
        power_sub=pd.DataFrame(power_sub)
        max_power=power_sub.sort_values('power',ascending=False)
        max_power=max_power[0:5]
        ax=sns.swarmplot(y="power",data=max_power)
        plt.xlabel('power')
        plt.title('Maximum Power Output')
        plt.annotate('5-point maximum power output', (0,0), (220, -30), xycoords='axes fraction', textcoords='offset points', va='top')
        #plt.show() 
        plt.close()
        return fig 
    def max_velocity1(self,df):
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        velo_sub=df['velocity']*3.6
        velo_sub=pd.DataFrame(velo_sub)
        max_velo=velo_sub.sort_values('velocity',ascending=False)
        max_velo=max_velo[0:5]
        ax=sns.swarmplot(y="velocity",data=max_velo)
        plt.xlabel('velocity (km/hr)')
        plt.title('Maximum Velocity Output')
        plt.annotate('5-point maximum velocity output', (0,0), (220, -30), xycoords='axes fraction', textcoords='offset points', va='top')
        #plt.show() 
        plt.close()
        return fig 
    def max_heartrate1(self,df):
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        heartrate_sub=df['heartrate']
        heartrate_sub=pd.DataFrame(heartrate_sub)
        max_heartrate=heartrate_sub.sort_values('heartrate',ascending=False)
        max_heartrate=max_heartrate[0:5]
        ax=sns.swarmplot(y="heartrate",data=max_heartrate)
        plt.xlabel('heartrate')
        plt.title('Maximum Heartrate Output')
        plt.annotate('5-point maximum heartrate output', (0,0), (220, -30), xycoords='axes fraction', textcoords='offset points', va='top')
        #plt.show() 
        plt.close()
        return fig 
    def max_cadence1(self,df):
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        cadence_sub=df['cadence']
        cadence_sub=pd.DataFrame(cadence_sub)
        max_cadence=cadence_sub.sort_values('cadence',ascending=False)
        max_cadence=max_cadence[0:5]
        ax=sns.swarmplot(y="cadence",data=max_cadence)
        plt.xlabel('cadence')
        plt.title('Maximum Cadence Output')
        plt.annotate('5-point maximum cadence output', (0,0), (220, -30), xycoords='axes fraction', textcoords='offset points', va='top')
        #plt.show() 
        plt.close()
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
    #plot18=s.max_scores(ride_history1,frank_rides)
    #plot19=s.avg_scores(ride_history1,frank_rides)
    plot20=s.ride_profile(frank_rides)
    plot21=s.max_power(ride_history1,frank_rides)
    plot22=s.max_velocity(ride_history,frank_rides) 
    plot23=s.max_cadence(ride_history1,frank_rides)
    plot24=s.max_heartrate(ride_history1,frank_rides)
    plot25=s.avg_power(ride_history1,frank_rides)
    plot26=s.avg_velocity(ride_history,frank_rides) 
    plot27=s.avg_cadence(ride_history1,frank_rides)
    plot28=s.avg_heartrate(ride_history1,frank_rides)
    plot29=s.max_power1(frank_rides)
    plot30=s.max_velocity1(frank_rides)
    plot31=s.max_cadence1(frank_rides)
    plot32=s.max_heartrate1(frank_rides)
    pp=PdfPages("sample_pdf.pdf")
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
    #pp.savefig(plot18)
    #pp.savefig(plot19)
    pp.savefig(plot20)
    pp.savefig(plot21)
    pp.savefig(plot22)
    pp.savefig(plot23)
    pp.savefig(plot24)
    pp.savefig(plot25)
    pp.savefig(plot26)
    pp.savefig(plot27)
    pp.savefig(plot28)
    pp.savefig(plot29)
    pp.savefig(plot30)
    pp.savefig(plot31)
    pp.savefig(plot32)
    pp.close() 






