import sys
import subprocess
import numpy as np
import stravalib as strava
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as pltlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import pylab 
from mpl_toolkits.mplot3d import Axes3D
import units
import os 
from matplotlib.backends.backend_pdf import PdfPages

pltlib.rc("font", family = "serif", size = 26)

#sample data 
frank_rides=pd.read_csv("final_df.csv")
ride_history1=pd.read_csv("ride_history.csv")

class Metrics_Viz():
    def __init__(self):
        pass

    #time vs. altitude
    def time_altitude(self,frank_rides):
        fig=plt.figure() 
        fig,ax=plt.subplots(figsize=(12,8))
        time_10s=frank_rides.rolling(window=10).mean() 
        alt_max=frank_rides['altitude'].max()
        time_id=frank_rides.ix[frank_rides.velocity.idxmax(),'time']
        alt_mean=frank_rides['altitude'].mean()
        x=time_10s['time']
        y=time_10s['velocity']
        plt.plot(x,y,linestyle="-")
        plt.axhline(y=alt_mean, xmin=0, xmax=1.0, color='red',linestyle="--")
        plt.grid(True)
        pltlib.xlabel('Time (s)')
        pltlib.ylabel('Altitude (m)')
        pltlib.text(time_id,alt_max,"{:.1f} m".format(alt_max),va='bottom',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        pltlib.text(3500,alt_mean,"{:.1f} m".format(alt_mean),va='bottom',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        plt.savefig("time_alt.pdf")
        return fig 
    #time vs. velocity
    def velo_time(self,frank_rides):
        fig=plt.figure() 
        fig,ax=plt.subplots(figsize=(12,8))
        velo_max=frank_rides['velocity'].max()
        time_id=frank_rides.ix[frank_rides.velocity.idxmax(),'time']
        velo_mean=frank_rides['velocity'].mean()
        x=frank_rides['time']
        y=frank_rides['velocity']
        plt.plot(x,y,linestyle="-")
        plt.axhline(y=velo_mean, xmin=0, xmax=1.0, color='red',linestyle="--")
        plt.grid(True)
        pltlib.xlabel('Time (s)')
        pltlib.ylabel('Velocity (km/h)')
        pltlib.text(time_id,velo_max,"{:.1f} km/h".format(velo_max),va='bottom',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        pltlib.text(3500,velo_mean,"{:.1f} km/h".format(velo_mean),va='top',ha='right',bbox={'facecolor':'w','edgecolor':'black'})
        plt.savefig( "velocity_scatter.pdf")
        return fig 
    #time vs. heartrate 
    def hr_time(self,frank_rides):
        fig=plt.figure() 
        fig,ax=plt.subplots(figsize=(12,8))
        hr_max=frank_rides['heartrate'].max()
        time_id=frank_rides.ix[frank_rides.velocity.idxmax(),'time']
        hr_mean=frank_rides['heartrate'].mean()
        x=frank_rides['time']
        y=frank_rides['heartrate']
        plt.plot(x,y,linestyle="-")
        plt.axhline(y=hr_mean, xmin=0, xmax=1.0, color='red',linestyle="--")
        pltlib.xlabel('Time (s)')
        pltlib.ylabel('Heartrate (bpm)')
        pltlib.text(time_id,hr_max,"{:.1f} bpm".format(hr_max),va='bottom',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        pltlib.text(3500,hr_mean,"{:.1f} bpm".format(hr_mean),va='top',ha='right',bbox={'facecolor':'w','edgecolor':'black'})
        plt.grid(True)
        plt.savefig("heartrate_scatter.pdf")
        return fig 
    #time vs. cadence 
    def cad_time(self,frank_rides):
        fig=plt.figure() 
        fig,ax=plt.subplots(figsize=(12,8))
        avg_cad=frank_rides['cadence'].mean()
        sns.regplot(x=frank_rides['cadence'],y=frank_rides['velocity'],fit_reg=False)
        pltlib.xlabel('Cadence (rpm)')
        pltlib.ylabel('Velocity (km/h)')
        plt.grid(True)
        plt.savefig("cadence_scatter.pdf")
        return fig 
    #time vs. grade (slope)
    def grade_time(self,frank_rides):
        fig=plt.figure() 
        fig,ax=plt.subplots(figsize=(12,8))
        grade_max=frank_rides['grade'].max()
        time_id=frank_rides.ix[frank_rides.velocity.idxmax(),'grade']
        grade_mean=frank_rides['grade'].mean()
        x=frank_rides['time']
        y=frank_rides['grade']
        plt.plot(x,y,linestyle="-")
        plt.axhline(y=grade_mean, xmin=0, xmax=1.0, color='red',linestyle="--")
        pltlib.xlabel('Time (s)')
        pltlib.ylabel('Grade')
        pltlib.text(time_id,grade_max,"{:.1f}".format(grade_max),va='bottom',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        pltlib.text(3500,grade_mean,"{:.1f}".format(grade_mean),va='top',ha='right',bbox={'facecolor':'w','edgecolor':'black'})
        plt.grid(True)
        plt.title('Time vs. Grade')
        plt.savefig("slope_scatter.pdf")
        return fig 
    #cadence histogram 
    def cad_time1(self,frank_rides):
        fig=plt.figure() 
        fig,ax=plt.subplots(figsize=(12,8))
        plt.hist(frank_rides['cadence'], bins=[-30,1,30,60,90,120,150,180]) #intervals of 50 
        locs,strings=pltlib.xticks()
        pltlib.xticks(locs[1:])
        avg_cad=frank_rides['cadence'].mean() 
        sd=frank_rides['cadence'].std()
        sd_high=avg_cad+sd
        sd_low=avg_cad-sd 
        plt.axvline(avg_cad,color="blue",linestyle='solid', linewidth=2) #average bar
        plt.axvline(sd_high,color="red",linestyle='solid', linewidth=2) #sd bars
        plt.axvline(sd_low,color="red",linestyle='solid', linewidth=2) #sd bars
        pltlib.text(sd_low,1000,"{:.1f} rpm".format(sd_low),va='bottom',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        pltlib.text(sd_high,1000,"{:.1f} rpm".format(sd_high),va='bottom',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        pltlib.text(avg_cad,2000,"{:.1f} rpm".format(avg_cad),va='bottom',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        pltlib.xlabel('Cadence (rpm)')
        pltlib.ylabel('Frequency (s)')
        plt.title('Cadence Histogram')
        plt.grid(True)
        plt.savefig("cadence_hist.pdf")
        return fig 
    #power histogram 
    def power_time(self,frank_rides):
        fig=plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        plt.hist(frank_rides['power'], bins=[-50,1, 50, 100, 150, 200, 250,300])
        locs,strings=pltlib.xticks()
        pltlib.xticks(locs[1:])
        mean_power=frank_rides['power'].mean() 
        sd=frank_rides['power'].std()
        sd_high=mean_power+sd
        sd_low=mean_power-sd 
        plt.axvline(mean_power,color="blue",linestyle='solid', linewidth=2) #average bar
        plt.axvline(sd_high,color="red",linestyle='solid', linewidth=2) #sd bars
        plt.axvline(sd_low,color="red",linestyle='solid', linewidth=2) #sd bars
        pltlib.text(sd_low,1000,"{:.1f} w".format(sd_low),va='bottom',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        pltlib.text(sd_high,1000,"{:.1f} w".format(sd_high),va='bottom',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        pltlib.text(mean_power,2000,"{:.1f} w".format(mean_power),va='top',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        pltlib.xlabel('Power (w)')
        pltlib.ylabel('Frequency (s)')
        plt.title('Power Histogram')
        plt.grid(True)
        plt.savefig("power_hist.pdf")
        return fig 
    #velocity histogram 
    def velo_hist(self,frank_rides): 
        fig=plt.figure() 
        fig,ax=plt.subplots(figsize=(12,8))
        plt.hist(frank_rides['velocity'], bins=[0, 10, 20, 30, 40, 50, 60]) #intervals of 10 
        avg_velo=frank_rides['velocity'].mean() 
        sd=frank_rides['velocity'].std()
        sd_high=avg_velo+sd
        sd_low=avg_velo-sd 
        plt.axvline(avg_velo,color="blue",linestyle='solid', linewidth=2) #average bar
        plt.axvline(sd_high,color="red",linestyle='solid', linewidth=2) #sd bars
        plt.axvline(sd_low,color="red",linestyle='solid', linewidth=2) #sd bars
        pltlib.text(sd_low,1000,"{:.1f} km/h".format(sd_low),va='bottom',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        pltlib.text(sd_high,1000,"{:.1f} km/h".format(sd_high),va='bottom',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        pltlib.text(avg_velo,2000,"{:.1f} km/h".format(avg_velo),va='bottom',ha='left',bbox={'facecolor':'w','edgecolor':'black'})
        pltlib.xlabel('Velocity (km/h)')
        pltlib.ylabel('Frequency (s)')
        plt.title('Velocity Histogram') 
        plt.grid(True)
        plt.savefig("velocity_hist.pdf")
        return fig 
    #uphill velocity 
    def uphill(self,frank_rides):
        fig=plt.figure() 
        fig,ax=plt.subplots(figsize=(12,8))
        slope=frank_rides['grade']
        slope=pd.DataFrame(slope)
        rides=frank_rides
        p=slope.grade>0
        c=p.cumsum()
        uphill_count=c-c.mask(p).ffill().fillna(0).astype(int)
        uphill_count=pd.DataFrame(uphill_count)
        p1=slope.grade<0
        c1=p1.cumsum()
        downhill_count=c1-c1.mask(p1).ffill().fillna(0).astype(int)
        downhill_count=pd.DataFrame(downhill_count)
        up_down=pd.concat([uphill_count,downhill_count],axis=1)
        up_down.columns=['uphill_count','downhill_count']
        rides1=pd.concat([rides,up_down],axis=1)
        rides1.describe() 
        rides1.uphill_count.max() 
        rides1.downhill_count.max() 
        #average velocity on long-hills, medium hills, and short hills
        #long uphills
        long_uphills=rides1[rides1['uphill_count']>30] #greater than 30 seconds 
        long_uphills_av=long_uphills.velocity.mean()
        long_uphills_av=pd.Series(long_uphills_av) 
        long_uphills_av=pd.DataFrame(long_uphills_av,columns=['Velocity (km/h) Long Hills'])
        #medium uphills
        medium_uphills=rides1[(rides1['uphill_count']<=30) & (rides1['uphill_count']>15)]
        medium_uphills_av=medium_uphills.velocity.mean()
        medium_uphills_av=pd.Series(medium_uphills_av) 
        medium_uphills_av=pd.DataFrame(medium_uphills_av,columns=['Velocity (km/h) Medium Hills'])
        #short uphills 
        short_uphills=rides1[rides1.uphill_count <=15] #less than 15 seconds 
        short_uphills_av=short_uphills.velocity.mean()
        short_uphills_av=pd.Series(short_uphills_av) 
        short_uphills_av=pd.DataFrame(short_uphills_av,columns=['Velocity (km/h) Short Hills'])
        final_uphill_velo=pd.concat([long_uphills_av,medium_uphills_av,short_uphills_av],axis=1)
        final_uphill_velo.columns=['Long Hills','Medium Hills','Short Hills']
        final_uphill_velo1=final_uphill_velo.T 
        final_uphill_velo1.reset_index(level=0,inplace=True)
        final_uphill_velo1.columns=['uphill_stage','velocity']
        #bar plot 
        sns.set(style="whitegrid")
        flatui = ["#9b59b6", "#3498db", "#e74c3c"]
        sns.barplot(x="uphill_stage",y="velocity",data=final_uphill_velo1,palette=flatui)
        pltlib.xlabel('')
        pltlib.ylabel('Average Velocity (km/h)')
        plt.tick_params(axis='x', which='major')
        plt.title('Velocity On Uphill Time Intervals') 
        plt.grid(True)
        plt.savefig("uphill_score.pdf")
        return fig 
    #downhill velocity 
    def downhill(self,frank_rides):
        fig=plt.figure() 
        fig,ax=plt.subplots(figsize=(12,8))
        slope=frank_rides['grade']
        slope=pd.DataFrame(slope)
        rides=frank_rides
        rides['velocity']=rides['velocity']
        p=slope.grade<0
        c=p.cumsum()
        uphill_count=c-c.mask(p).ffill().fillna(0).astype(int)
        uphill_count=pd.DataFrame(uphill_count)
        p1=slope.grade<0
        c1=p1.cumsum()
        downhill_count=c1-c1.mask(p1).ffill().fillna(0).astype(int)
        downhill_count=pd.DataFrame(downhill_count)
        up_down=pd.concat([uphill_count,downhill_count],axis=1)
        up_down.columns=['uphill_count','downhill_count']
        rides1=pd.concat([rides,up_down],axis=1)
        rides1.describe() 
        rides1.uphill_count.max() 
        rides1.downhill_count.max() 
        #average velocity on long-hills, medium hills, and short hills
        #long uphills
        long_downhills=rides1[rides1['downhill_count']>30] #greater than 30 seconds 
        long_downhills_av=long_downhills.velocity.mean()
        long_downhills_av=pd.Series(long_downhills_av) 
        long_downhills_av=pd.DataFrame(long_downhills_av,columns=['Velocity (km/H) Long Hills'])
        #medium uphills
        medium_downhills=rides1[(rides1['downhill_count']<=30) & (rides1['uphill_count']>15)]
        medium_downhills_av=medium_downhills.velocity.mean()
        medium_downhills_av=pd.Series(medium_downhills_av) 
        medium_downhills_av=pd.DataFrame(medium_downhills_av,columns=['Velocity (Km/H) Medium Hills'])
        #short uphills 
        short_downhills=rides1[rides1.downhill_count <=15] #less than 15 seconds 
        short_downhills_av=short_downhills.velocity.mean()
        short_downhills_av=pd.Series(short_downhills_av) 
        short_downhills_av=pd.DataFrame(short_downhills_av,columns=['Velocity (Km/H) Short Hills'])
        final_downhill_velo=pd.concat([long_downhills_av,medium_downhills_av,short_downhills_av],axis=1)
        final_downhill_velo.columns=['Long Hills','Medium Hills','Short Hills']
        final_downhill_velo1=final_downhill_velo.T 
        final_downhill_velo1.reset_index(level=0,inplace=True)
        final_downhill_velo1.columns=['uphill_stage','velocity']
        #bar plot 
        sns.set(style="whitegrid")
        flatui = ["#9b59b6", "#3498db", "#e74c3c"]
        sns.barplot(x="uphill_stage",y="velocity",data=final_downhill_velo1,palette=flatui)
        pltlib.xlabel('Velocity (km/h)')
        pltlib.ylabel('Average Velocity (Km/h)')
        plt.tick_params(axis='x', which='major')
        plt.title('Velocity On Downhill Time Intervals')
        plt.grid(True)
        plt.savefig("downhill_score.pdf")
        return fig 

    def power_hist1(self,ride_history1,frank_rides):
        #overlay power histogram
        fig=plt.figure() 
        fig,ax=plt.subplots(figsize=(12,8))
        plt.hist(ride_history1['power'], bins=[-50,1,50,100,150,200,250,300],color="darkgray",edgecolor="black",label="Ride History") #intervals of 50 
        plt.hist(frank_rides['power'], bins=[-50,1,50,100,150,200,250,300],alpha=0.5,color="orange",label="Ride Current") #intervals of 50 
        locs,strings=pltlib.xticks()
        pltlib.xticks(locs[1:])
        pltlib.xlabel('Power (w)')
        pltlib.ylabel('Frequency (s)')
        plt.legend() 
        plt.savefig("power_double.pdf")
        return fig 
    def velo_hist1(self,ride_history1,frank_rides):
        #overlay velocity histogram 
        fig = plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        plt.hist(ride_history1['velocity'], bins=[0, 10, 20, 30, 40, 50, 60],color="darkgray",edgecolor="black",label="Ride History") #intervals of 10
        plt.hist(frank_rides['velocity'], bins=[0, 10, 20, 30, 40, 50, 60],alpha=0.5,color="orange",label="Ride Current")
        plt.legend()
        pltlib.xlabel('Velocity (km/h)')
        pltlib.ylabel('Frequency (s)')
        plt.savefig("velo_double.pdf")
        return fig 
    def cad_hist1(self,ride_history1,frank_rides):
        #overlay cadence histogram 
        fig = plt.figure() 
        fig,ax=plt.subplots(figsize=(12,8))
        plot1=plt.hist(ride_history1['cadence'], bins=[-30,1,30,60,90,120,150,180],facecolor="darkgray",edgecolor='black',label="Ride History") #intervals of 30 
        plot2=plt.hist(frank_rides['cadence'], bins=[-30,1,30,60,90,120,150,180],alpha=0.5,color="orange",label="Ride Current")
        locs,strings=pltlib.xticks()
        pltlib.xticks(locs[1:])
        pltlib.xlabel('Cadence (rpm)')
        pltlib.ylabel('Frequency (s)')
        plt.legend()
        plt.savefig("cad_double.pdf")
        return fig 
    def hr_hist1(self,ride_history1,frank_rides): 
        #overlay heartrate histogram 
        fig = plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        pylab.xlim(50,250)
        plt.hist(ride_history1['heartrate'], bins=5,color="darkgray",label="Ride History") 
        plt.hist(frank_rides['heartrate'], bins=5,alpha=0.5,color="orange",label="Ride Current")
        pltlib.xlabel('Heartrate (rpm)')
        pltlib.ylabel('Frequency (s)')
        plt.legend() 
        plt.savefig("hr_double.pdf")
        return fig 
    def peak_power(self,frank_rides):
        #peak power over time intervals 5s, 10s, 30s, 60s, 5m, 10m, 30m, 60m
        fig = plt.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        p1=frank_rides['power'].rolling(window=5).mean()
        p1=pd.DataFrame(p1,columns=['power'])
        p1=p1.max() 
        p1=pd.Series(p1)
        p1=pd.DataFrame(p1,columns=['power'])
        p1.reset_index(level=0,inplace=True)
        p1.columns=['index','power_5s']
        p2=frank_rides['power'].rolling(window=10).mean()
        p2=pd.DataFrame(p2,columns=['power'])
        p2=p2.max() 
        p2=pd.Series(p2)
        p2=pd.DataFrame(p2,columns=['power'])
        p2.reset_index(level=0,inplace=True)
        p2.columns=['index','power_10s']
        p3=frank_rides['power'].rolling(window=30).mean()
        p3=pd.DataFrame(p3,columns=['power'])
        p3=p3.max() 
        p3=pd.Series(p3)
        p3=pd.DataFrame(p3,columns=['power'])
        p3.reset_index(level=0,inplace=True)
        p3.columns=['index','power_30s']
        p4=frank_rides['power'].rolling(window=60).mean()
        p4=pd.DataFrame(p4,columns=['power'])
        p4=p4.max() 
        p4=pd.Series(p4)
        p4=pd.DataFrame(p4,columns=['power'])
        p4.reset_index(level=0,inplace=True)
        p4.columns=['index','power_60s']
        p5=frank_rides['power'].rolling(window=300).mean()
        p5=pd.DataFrame(p5,columns=['power'])
        p5=p5.max() 
        p5=pd.Series(p5)
        p5=pd.DataFrame(p5,columns=['power'])
        p5.reset_index(level=0,inplace=True)
        p5.columns=['index','power_5m']
        p6=frank_rides['power'].rolling(window=600).mean()
        p6=pd.DataFrame(p6,columns=['power'])
        p6=p6.max() 
        p6=pd.Series(p6)
        p6=pd.DataFrame(p6,columns=['power'])
        p6.reset_index(level=0,inplace=True)
        p6.columns=['index','power_10m']
        p7=frank_rides['power'].rolling(window=1800).mean()
        p7=pd.DataFrame(p7,columns=['power'])
        p7=p7.max() 
        p7=pd.Series(p7)
        p7=pd.DataFrame(p7,columns=['power'])
        p7.reset_index(level=0,inplace=True)
        p7.columns=['index','power_30m']
        p8=frank_rides['power'].rolling(window=3600).mean()
        p8=pd.DataFrame(p8,columns=['power'])
        p8=p8.max() 
        p8=pd.Series(p8)
        p8=pd.DataFrame(p8,columns=['power'])
        p8.reset_index(level=0,inplace=True)
        p8.columns=['index','power_60m']
        combo_power=pd.concat([p1,p2,p3,p4,p5,p6,p7,p8],axis=1)
        combo_power.columns=['index','5s','index','10s','index','30s','index','60s','index','5m','index','10m','index','30m','index','60m']
        combo_power1=combo_power[['5s','10s','30s','60s','5m','10m','30m','60m']]
        combo_power2=combo_power1.T 
        combo_power2.reset_index(level=0,inplace=True)
        combo_power2.columns=['index','power (watts)']
        sns.barplot(x="index",y="power (watts)", data=combo_power2,palette="Reds_d") 
        plt.xlabel('Time Interval (s)') 
        plt.tick_params(axis='x', which='major')
        plt.tick_params(axis='x', which='minor')
        pltlib.ylabel('Maximum Power (w)')
        pltlib.title('Peak Power Profile')
        plt.savefig("peak_power1.pdf")
        return fig 
    #power on different grade (slope) intervals 
    def ride_stage(self,frank_rides):
        frank_rides['grade_ma1']=frank_rides['grade'].rolling(window=15).mean() #15 point moving average for the grade
        frank_rides['grade_ma1']=frank_rides['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=frank_rides[frank_rides['grade_ma1']<=-6]
        first_third=round(0.3333*len(grade_lowest))
        second_third=round(0.6667*len(grade_lowest))
        final_third=len(grade_lowest)
        first_stage=grade_lowest[0:first_third]
        second_stage=grade_lowest[first_third:second_third]
        third_stage=grade_lowest[second_third:final_third]
        all_stages1=grade_lowest
        #stage 1
        p1=first_stage['power'].mean()
        p1=pd.Series(p1)
        p1=pd.DataFrame(p1,columns=['stage_1'])
        p1.reset_index(level=0,inplace=True)
        p2=second_stage['power'].mean()
        p2=pd.Series(p2)
        p2=pd.DataFrame(p2,columns=['stage_2'])
        p2.reset_index(level=0,inplace=True)
        p3=third_stage['power'].mean()
        p3=pd.Series(p3)
        p3=pd.DataFrame(p3,columns=['stage_3'])
        p3.reset_index(level=0,inplace=True)
        p1_mean=all_stages1['power'].mean()
        #stage 2
        grade_lowest=frank_rides[(frank_rides['grade_ma1']<-4) & (frank_rides['grade_ma1']>-6)]
        first_third=round(0.3333*len(grade_lowest))
        second_third=round(0.6667*len(grade_lowest))
        final_third=len(grade_lowest)
        first_stage=grade_lowest[0:first_third]
        second_stage=grade_lowest[first_third:second_third]
        third_stage=grade_lowest[second_third:final_third]
        all_stages2=grade_lowest
        p4=first_stage['power'].mean()
        p4=pd.Series(p4)
        p4=pd.DataFrame(p4,columns=['stage_1'])
        p4.reset_index(level=0,inplace=True)
        p5=second_stage['power'].mean()
        p5=pd.Series(p5)
        p5=pd.DataFrame(p5,columns=['stage_2'])
        p5.reset_index(level=0,inplace=True)
        p6=third_stage['power'].mean()
        p6=pd.Series(p6)
        p6=pd.DataFrame(p6,columns=['stage_3'])
        p6.reset_index(level=0,inplace=True)
        p2_mean=all_stages2['power'].mean()
        #stage 3 
        grade_lowest=frank_rides[(frank_rides['grade_ma1']< -2) & (frank_rides['grade_ma1']>-4)]
        first_third=round(0.3333*len(grade_lowest))
        second_third=round(0.6667*len(grade_lowest))
        final_third=len(grade_lowest)
        first_stage=grade_lowest[0:first_third]
        second_stage=grade_lowest[first_third:second_third]
        third_stage=grade_lowest[second_third:final_third]
        all_stages3=grade_lowest
        p7=first_stage['power'].mean()
        p7=pd.Series(p7)
        p7=pd.DataFrame(p7,columns=['stage_1'])
        p7.reset_index(level=0,inplace=True)
        p8=second_stage['power'].mean()
        p8=pd.Series(p8)
        p8=pd.DataFrame(p8,columns=['stage_2'])
        p8.reset_index(level=0,inplace=True)
        p9=third_stage['power'].mean()
        p9=pd.Series(p9)
        p9=pd.DataFrame(p9,columns=['stage_3'])
        p9.reset_index(level=0,inplace=True)
        p3_mean=all_stages3['power'].mean()
        #stage 4
        grade_lowest=frank_rides[(frank_rides['grade_ma1']< 0) & (frank_rides['grade_ma1']>-2)]
        first_third=round(0.3333*len(grade_lowest))
        second_third=round(0.6667*len(grade_lowest))
        final_third=len(grade_lowest)
        first_stage=grade_lowest[0:first_third]
        second_stage=grade_lowest[first_third:second_third]
        third_stage=grade_lowest[second_third:final_third]
        all_stages4=grade_lowest
        p10=first_stage['power'].mean()
        p10=pd.Series(p10)
        p10=pd.DataFrame(p10,columns=['stage_1'])
        p10.reset_index(level=0,inplace=True)
        p11=second_stage['power'].mean()
        p11=pd.Series(p11)
        p11=pd.DataFrame(p11,columns=['stage_2'])
        p11.reset_index(level=0,inplace=True)
        p12=third_stage['power'].mean()
        p12=pd.Series(p12)
        p12=pd.DataFrame(p12,columns=['stage_3'])
        p12.reset_index(level=0,inplace=True)
        p4_mean=all_stages4['power'].mean()
        #stage 5
        grade_lowest=frank_rides[(frank_rides['grade_ma1']< 2) & (frank_rides['grade_ma1']>0)]
        first_third=round(0.3333*len(grade_lowest))
        second_third=round(0.6667*len(grade_lowest))
        final_third=len(grade_lowest)
        first_stage=grade_lowest[0:first_third]
        second_stage=grade_lowest[first_third:second_third]
        third_stage=grade_lowest[second_third:final_third]
        all_stages5=grade_lowest
        p13=first_stage['power'].mean()
        p13=pd.Series(p13)
        p13=pd.DataFrame(p13,columns=['stage_1'])
        p13.reset_index(level=0,inplace=True)
        p14=second_stage['power'].mean()
        p14=pd.Series(p14)
        p14=pd.DataFrame(p14,columns=['stage_2'])
        p14.reset_index(level=0,inplace=True)
        p15=third_stage['power'].mean()
        p15=pd.Series(p15)
        p15=pd.DataFrame(p15,columns=['stage_3'])
        p15.reset_index(level=0,inplace=True)
        p5_mean=all_stages5['power'].mean()
        #stage 6 
        grade_lowest=frank_rides[(frank_rides['grade_ma1']< 4) & (frank_rides['grade_ma1']>2)]
        first_third=round(0.3333*len(grade_lowest))
        second_third=round(0.6667*len(grade_lowest))
        final_third=len(grade_lowest)
        first_stage=grade_lowest[0:first_third]
        second_stage=grade_lowest[first_third:second_third]
        third_stage=grade_lowest[second_third:final_third]
        all_stages6=grade_lowest
        p16=first_stage['power'].mean()
        p16=pd.Series(p16)
        p16=pd.DataFrame(p16,columns=['stage_1'])
        p16.reset_index(level=0,inplace=True)
        p17=second_stage['power'].mean()
        p17=pd.Series(p17)
        p17=pd.DataFrame(p17,columns=['stage_2'])
        p17.reset_index(level=0,inplace=True)
        p18=third_stage['power'].mean()
        p18=pd.Series(p18)
        p18=pd.DataFrame(p18,columns=['stage_3'])
        p18.reset_index(level=0,inplace=True)
        p6_mean=all_stages6['power'].mean()
        #stage 7
        grade_lowest=frank_rides[(frank_rides['grade_ma1']< 6) & (frank_rides['grade_ma1']>4)]
        first_third=round(0.3333*len(grade_lowest))
        second_third=round(0.6667*len(grade_lowest))
        final_third=len(grade_lowest)
        first_stage=grade_lowest[0:first_third]
        second_stage=grade_lowest[first_third:second_third]
        third_stage=grade_lowest[second_third:final_third]
        all_stages7=grade_lowest
        p19=first_stage['power'].mean()
        p19=pd.Series(p19)
        p19=pd.DataFrame(p19,columns=['stage_1'])
        p19.reset_index(level=0,inplace=True)
        p20=second_stage['power'].mean()
        p20=pd.Series(p20)
        p20=pd.DataFrame(p20,columns=['stage_2'])
        p20.reset_index(level=0,inplace=True)
        p21=third_stage['power'].mean()
        p21=pd.Series(p21)
        p21=pd.DataFrame(p21,columns=['stage_3'])
        p21.reset_index(level=0,inplace=True)
        p7_mean=all_stages7['power'].mean()
        #stage 8
        grade_lowest=frank_rides[frank_rides['grade_ma1']> 6]
        first_third=round(0.3333*len(grade_lowest))
        second_third=round(0.6667*len(grade_lowest))
        final_third=len(grade_lowest)
        first_stage=grade_lowest[0:first_third]
        second_stage=grade_lowest[first_third:second_third]
        third_stage=grade_lowest[second_third:final_third]
        all_stages8=grade_lowest
        p22=first_stage['power'].mean()
        p22=pd.Series(p22)
        p22=pd.DataFrame(p22,columns=['stage_1'])
        p22.reset_index(level=0,inplace=True)
        p23=second_stage['power'].mean()
        p23=pd.Series(p23)
        p23=pd.DataFrame(p23,columns=['stage_2'])
        p23.reset_index(level=0,inplace=True)
        p24=third_stage['power'].mean()
        p24=pd.Series(p24)
        p24=pd.DataFrame(p24,columns=['stage_3'])
        p24.reset_index(level=0,inplace=True)
        p8_mean=all_stages8['power'].mean()
        c1=pd.concat([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24],axis=1)
        c1=c1[["stage_1","stage_2","stage_3"]]
        c1=c1.T 
        c1.columns=['power (watts)']
        c1.reset_index(level=0,inplace=True)
        c1.columns=['Ride Stage','power (watts)']
        sample_slope=np.array([['< -6'],['> -6 to < -4'],[' > -4 to < -2'],[' > -2 to < 0'],['> 0 to < 2'],['>2 to < 4'],['>4 to < 6'],[' > 6'],['< -6'],['> -6 to < -4'],[' > -4 to < -2'],[' > -2 to < 0'],['> 0 to < 2'],['>2 to < 4'],['>4 to < 6'],[' > 6'],['< -6'],['> -6 to < -4'],[' > -4 to < -2'],[' > -2 to < 0'],['> 0 to < 2'],['>2 to < 4'],['>4 to < 6'],[' > 6']])
        sample_slope=pd.DataFrame(sample_slope,columns=['slope'])
        c1=pd.concat([c1,sample_slope],axis=1)
        fig = pltlib.figure()
        fig,ax=plt.subplots(figsize=(12,8))
        ax=sns.barplot(x="slope",y="power (watts)",hue="Ride Stage",data=c1)
        plt.axhline(y=p8_mean, xmin=0.87, xmax=0.99, color='darkblue')
        plt.axhline(y=p7_mean, xmin=0.75, xmax=0.87, color='darkblue')
        plt.axhline(y=p6_mean, xmin=0.63, xmax=0.75, color='darkblue')
        plt.axhline(y=p5_mean, xmin=0.51, xmax=0.63, color='darkblue')
        plt.axhline(y=p4_mean, xmin=0.39, xmax=0.51, color='darkblue')
        plt.axhline(y=p3_mean, xmin=0.27, xmax=0.39, color='darkblue')
        plt.axhline(y=p2_mean, xmin=0.13, xmax=0.27, color='darkblue')
        plt.axhline(y=p1_mean, xmin=0.01, xmax=0.13, color='darkblue')
        plt.setp(ax.get_legend().get_texts()) 
        plt.setp(ax.get_legend().get_title()) 
        pltlib.xlabel('Slope Interval')
        pltlib.ylabel('Power (w)')
        plt.tick_params(axis='x', which='major') 
        plt.savefig("power_stages1.pdf")
        return fig 

if __name__ == '__main__':
    s = Metrics_Viz() 
    plot1=s.time_altitude(frank_rides)
    plot2=s.velo_time(frank_rides)
    plot3=s.hr_time(frank_rides)
    plot4=s.cad_time(frank_rides)
    plot5=s.grade_time(frank_rides)
    plot6=s.cad_time1(frank_rides)
    plot7=s.power_time(frank_rides)
    plot8=s.velo_hist(frank_rides)
    plot9=s.uphill(frank_rides)
    plot10=s.downhill(frank_rides)
    plot11=s.power_hist1(ride_history1,frank_rides)
    plot12=s.cad_hist1(ride_history1,frank_rides)
    plot13=s.hr_hist1(ride_history1,frank_rides) 
    plot14=s.peak_power(frank_rides)
    plot15=s.ride_stage(frank_rides)
    pp=PdfPages("alps_riding.pdf")
    pp.savefig(plot1) 
    pp.savefig(plot2)
    pp.savefig(plot3)
    pp.savefig(plot4)
    pp.savefig(plot5)
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
    pp.close() 
