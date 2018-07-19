#Average Metrics based on the grade (slope) and stage of the ride (split into three stages)
class Average_Velo_Metrics_S1():
    def __init__(self):
        pass

    def average_velo_stage_one(self,x):
        fig=plt.figure()
        x=frank_rides[0:2500]
        x['grade_ma1']=x['grade'].rolling(window=20).mean() #20 point moving average for the grade
        x['grade_ma1']=x['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x[x['grade_ma1']<-6]
        velo1=grade_lowest['velocity'].mean()
        grade_low2=x[(x['grade_ma1']>-6) & (x['grade_ma1']<=-4.5)]
        velo111=grade_low2['velocity'].mean()
        grade_low1=x[(x['grade_ma1']>-4.5) & (x['grade_ma1']<=-3)]
        velo11=grade_low1['velocity'].mean()
        grade_low=x[(x['grade_ma1']>-3) & (x['grade_ma1']<=-1.5)]
        velo2=grade_low['velocity'].mean()
        grade_avg=x[(x['grade_ma1']>-1.5) &(x['grade_ma1']<=0)]
        velo3=grade_avg['velocity'].mean() 
        grade_high=x[(x['grade_ma1']>0) &(x['grade_ma1']<=1.5)]
        velo4=grade_high['velocity'].mean() 
        grade_high1=x[(x['grade_ma1']>1.5) &(x['grade_ma1']<=3)]
        velo5=grade_high1['velocity'].mean() 
        grade_high2=x[(x['grade_ma1']>3) &(x['grade_ma1']<=4.5)]
        velo6=grade_high2['velocity'].mean() 
        grade_high3=x[(x['grade_ma1']>4.5) &(x['grade_ma1']<=6)]
        velo7=grade_high3['velocity'].mean() 
        plt.plot([-7.5,-6],[velo1,velo1],linewidth=2)
        plt.plot([-6,-4.5],[velo111,velo111],linewidth=2)
        plt.plot([-4.5,-3],[velo11,velo11],linewidth=2)
        plt.plot([-3,-1.5],[velo2,velo2],linewidth=2)
        plt.plot([-1.5,0],[velo3,velo3],linewidth=2)
        plt.plot([0,1.5],[velo4,velo4],linewidth=2)
        plt.plot([1.5,3],[velo5,velo5],linewidth=2)
        plt.plot([3,4.5],[velo6,velo6],linewidth=2)
        plt.plot([4.5,6],[velo7,velo7],linewidth=2)
        plt.xlabel('grade moving average (stage one)') 
        plt.ylabel('velocity (m/s)')
        plt.plot() 
        plt.show() 
        return fig 

class Average_Velo_Metrics_S2():
    def __init__(self):
        pass

    def average_velo_stage_two(self,x):
        fig=plt.figure()
        x=frank_rides[2501:5000]
        x['grade_ma1']=x['grade'].rolling(window=20).mean() #20 point moving average for the grade
        x['grade_ma1']=x['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x[x['grade_ma1']<-6]
        velo1=grade_lowest['velocity'].mean()
        grade_low2=x[(x['grade_ma1']>-6) & (x['grade_ma1']<=-4.5)]
        velo111=grade_low2['velocity'].mean()
        grade_low1=x[(x['grade_ma1']>-4.5) & (x['grade_ma1']<=-3)]
        velo11=grade_low1['velocity'].mean()
        grade_low=x[(x['grade_ma1']>-3) & (x['grade_ma1']<=-1.5)]
        velo2=grade_low['velocity'].mean()
        grade_avg=x[(x['grade_ma1']>-1.5) &(x['grade_ma1']<=0)]
        velo3=grade_avg['velocity'].mean() 
        grade_high=x[(x['grade_ma1']>0) &(x['grade_ma1']<=1.5)]
        velo4=grade_high['velocity'].mean() 
        grade_high1=x[(x['grade_ma1']>1.5) &(x['grade_ma1']<=3)]
        velo5=grade_high1['velocity'].mean() 
        grade_high2=x[(x['grade_ma1']>3) &(x['grade_ma1']<=4.5)]
        velo6=grade_high2['velocity'].mean() 
        grade_high3=x[(x['grade_ma1']>4.5) &(x['grade_ma1']<=6)]
        velo7=grade_high3['velocity'].mean() 
        plt.plot([-7.5,-6],[velo1,velo1],linewidth=2)
        plt.plot([-6,-4.5],[velo111,velo111],linewidth=2)
        plt.plot([-4.5,-3],[velo11,velo11],linewidth=2)
        plt.plot([-3,-1.5],[velo2,velo2],linewidth=2)
        plt.plot([-1.5,0],[velo3,velo3],linewidth=2)
        plt.plot([0,1.5],[velo4,velo4],linewidth=2)
        plt.plot([1.5,3],[velo5,velo5],linewidth=2)
        plt.plot([3,4.5],[velo6,velo6],linewidth=2)
        plt.plot([4.5,6],[velo7,velo7],linewidth=2)
        plt.xlabel('grade moving average (stage two)') 
        plt.ylabel('velocity (m/s)')
        plt.plot() 
        plt.show() 
        return fig

class Average_Velo_Metrics_S3():
    def __init__(self):
        pass
    def average_velo_stage_three(self,x):
        fig=plt.figure()
        x=frank_rides[5001:10000]
        x['grade_ma1']=x['grade'].rolling(window=20).mean() #20 point moving average for the grade
        x['grade_ma1']=x['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x[x['grade_ma1']<-6]
        velo1=grade_lowest['velocity'].mean()
        grade_low2=x[(x['grade_ma1']>-6) & (x['grade_ma1']<=-4.5)]
        velo111=grade_low2['velocity'].mean()
        grade_low1=x[(x['grade_ma1']>-4.5) & (x['grade_ma1']<=-3)]
        velo11=grade_low1['velocity'].mean()
        grade_low=x[(x['grade_ma1']>-3) & (x['grade_ma1']<=-1.5)]
        velo2=grade_low['velocity'].mean()
        grade_avg=x[(x['grade_ma1']>-1.5) &(x['grade_ma1']<=0)]
        velo3=grade_avg['velocity'].mean() 
        grade_high=x[(x['grade_ma1']>0) &(x['grade_ma1']<=1.5)]
        velo4=grade_high['velocity'].mean() 
        grade_high1=x[(x['grade_ma1']>1.5) &(x['grade_ma1']<=3)]
        velo5=grade_high1['velocity'].mean() 
        grade_high2=x[(x['grade_ma1']>3) &(x['grade_ma1']<=4.5)]
        velo6=grade_high2['velocity'].mean() 
        grade_high3=x[(x['grade_ma1']>4.5) &(x['grade_ma1']<=6)]
        velo7=grade_high3['velocity'].mean() 
        plt.plot([-7.5,-6],[velo1,velo1],linewidth=2)
        plt.plot([-6,-4.5],[velo111,velo111],linewidth=2)
        plt.plot([-4.5,-3],[velo11,velo11],linewidth=2)
        plt.plot([-3,-1.5],[velo2,velo2],linewidth=2)
        plt.plot([-1.5,0],[velo3,velo3],linewidth=2)
        plt.plot([0,1.5],[velo4,velo4],linewidth=2)
        plt.plot([1.5,3],[velo5,velo5],linewidth=2)
        plt.plot([3,4.5],[velo6,velo6],linewidth=2)
        plt.plot([4.5,6],[velo7,velo7],linewidth=2)
        plt.xlabel('grade moving average (stage three)') 
        plt.ylabel('velocity (m/s)')
        plt.plot() 
        plt.show() 
        return fig
    

avg_velo_metrics_s1=Average_Velo_Metrics_S1()
avg_velo_metrics_s1.average_velo_stage_one(frank_rides)

avg_velo_metrics_s2=Average_Velo_Metrics_S2()
avg_velo_metrics_s2.average_velo_stage_two(frank_rides)

avg_velo_metrics_s3=Average_Velo_Metrics_S3()
avg_velo_metrics_s3.average_velo_stage_three(frank_rides)



class Average_Power_Metrics_S1():
    def __init__(self):
        pass

    def average_power_stage_one(self,x):
        fig=plt.figure()
        x=frank_rides[0:2500]
        x['grade_ma1']=x['grade'].rolling(window=20).mean() #20 point moving average for the grade
        x['grade_ma1']=x['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x[x['grade_ma1']<-6]
        velo1=grade_lowest['power'].mean()
        grade_low2=x[(x['grade_ma1']>-6) & (x['grade_ma1']<=-4.5)]
        velo111=grade_low2['power'].mean()
        grade_low1=x[(x['grade_ma1']>-4.5) & (x['grade_ma1']<=-3)]
        velo11=grade_low1['power'].mean()
        grade_low=x[(x['grade_ma1']>-3) & (x['grade_ma1']<=-1.5)]
        velo2=grade_low['power'].mean()
        grade_avg=x[(x['grade_ma1']>-1.5) &(x['grade_ma1']<=0)]
        velo3=grade_avg['power'].mean() 
        grade_high=x[(x['grade_ma1']>0) &(x['grade_ma1']<=1.5)]
        velo4=grade_high['power'].mean() 
        grade_high1=x[(x['grade_ma1']>1.5) &(x['grade_ma1']<=3)]
        velo5=grade_high1['power'].mean() 
        grade_high2=x[(x['grade_ma1']>3) &(x['grade_ma1']<=4.5)]
        velo6=grade_high2['power'].mean() 
        grade_high3=x[(x['grade_ma1']>4.5) &(x['grade_ma1']<=6)]
        velo7=grade_high3['power'].mean() 
        plt.plot([-7.5,-6],[velo1,velo1],linewidth=2)
        plt.plot([-6,-4.5],[velo111,velo111],linewidth=2)
        plt.plot([-4.5,-3],[velo11,velo11],linewidth=2)
        plt.plot([-3,-1.5],[velo2,velo2],linewidth=2)
        plt.plot([-1.5,0],[velo3,velo3],linewidth=2)
        plt.plot([0,1.5],[velo4,velo4],linewidth=2)
        plt.plot([1.5,3],[velo5,velo5],linewidth=2)
        plt.plot([3,4.5],[velo6,velo6],linewidth=2)
        plt.plot([4.5,6],[velo7,velo7],linewidth=2)
        plt.xlabel('grade moving average (stage one)') 
        plt.ylabel('power')
        plt.plot() 
        plt.show() 
        return fig 

class Average_Power_Metrics_S2():
    def __init__(self):
        pass

    def average_power_stage_two(self,x):
        fig=plt.figure()
        x=frank_rides[2501:5000]
        x['grade_ma1']=x['grade'].rolling(window=20).mean() #20 point moving average for the grade
        x['grade_ma1']=x['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x[x['grade_ma1']<-6]
        velo1=grade_lowest['power'].mean()
        grade_low2=x[(x['grade_ma1']>-6) & (x['grade_ma1']<=-4.5)]
        velo111=grade_low2['power'].mean()
        grade_low1=x[(x['grade_ma1']>-4.5) & (x['grade_ma1']<=-3)]
        velo11=grade_low1['power'].mean()
        grade_low=x[(x['grade_ma1']>-3) & (x['grade_ma1']<=-1.5)]
        velo2=grade_low['power'].mean()
        grade_avg=x[(x['grade_ma1']>-1.5) &(x['grade_ma1']<=0)]
        velo3=grade_avg['power'].mean() 
        grade_high=x[(x['grade_ma1']>0) &(x['grade_ma1']<=1.5)]
        velo4=grade_high['power'].mean() 
        grade_high1=x[(x['grade_ma1']>1.5) &(x['grade_ma1']<=3)]
        velo5=grade_high1['power'].mean() 
        grade_high2=x[(x['grade_ma1']>3) &(x['grade_ma1']<=4.5)]
        velo6=grade_high2['power'].mean() 
        grade_high3=x[(x['grade_ma1']>4.5) &(x['grade_ma1']<=6)]
        velo7=grade_high3['power'].mean() 
        plt.plot([-7.5,-6],[velo1,velo1],linewidth=2)
        plt.plot([-6,-4.5],[velo111,velo111],linewidth=2)
        plt.plot([-4.5,-3],[velo11,velo11],linewidth=2)
        plt.plot([-3,-1.5],[velo2,velo2],linewidth=2)
        plt.plot([-1.5,0],[velo3,velo3],linewidth=2)
        plt.plot([0,1.5],[velo4,velo4],linewidth=2)
        plt.plot([1.5,3],[velo5,velo5],linewidth=2)
        plt.plot([3,4.5],[velo6,velo6],linewidth=2)
        plt.plot([4.5,6],[velo7,velo7],linewidth=2)
        plt.xlabel('grade moving average (stage two)') 
        plt.ylabel('power')
        plt.plot() 
        plt.show() 
        return fig

class Average_Power_Metrics_S3():
    def __init__(self):
        pass
    def average_power_stage_three(self,x):
        fig=plt.figure()
        x=frank_rides[5001:10000]
        x['grade_ma1']=x['grade'].rolling(window=20).mean() #20 point moving average for the grade
        x['grade_ma1']=x['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x[x['grade_ma1']<-6]
        velo1=grade_lowest['power'].mean()
        grade_low2=x[(x['grade_ma1']>-6) & (x['grade_ma1']<=-4.5)]
        velo111=grade_low2['power'].mean()
        grade_low1=x[(x['grade_ma1']>-4.5) & (x['grade_ma1']<=-3)]
        velo11=grade_low1['power'].mean()
        grade_low=x[(x['grade_ma1']>-3) & (x['grade_ma1']<=-1.5)]
        velo2=grade_low['power'].mean()
        grade_avg=x[(x['grade_ma1']>-1.5) &(x['grade_ma1']<=0)]
        velo3=grade_avg['power'].mean() 
        grade_high=x[(x['grade_ma1']>0) &(x['grade_ma1']<=1.5)]
        velo4=grade_high['power'].mean() 
        grade_high1=x[(x['grade_ma1']>1.5) &(x['grade_ma1']<=3)]
        velo5=grade_high1['power'].mean() 
        grade_high2=x[(x['grade_ma1']>3) &(x['grade_ma1']<=4.5)]
        velo6=grade_high2['power'].mean() 
        grade_high3=x[(x['grade_ma1']>4.5) &(x['grade_ma1']<=6)]
        velo7=grade_high3['power'].mean() 
        plt.plot([-7.5,-6],[velo1,velo1],linewidth=2)
        plt.plot([-6,-4.5],[velo111,velo111],linewidth=2)
        plt.plot([-4.5,-3],[velo11,velo11],linewidth=2)
        plt.plot([-3,-1.5],[velo2,velo2],linewidth=2)
        plt.plot([-1.5,0],[velo3,velo3],linewidth=2)
        plt.plot([0,1.5],[velo4,velo4],linewidth=2)
        plt.plot([1.5,3],[velo5,velo5],linewidth=2)
        plt.plot([3,4.5],[velo6,velo6],linewidth=2)
        plt.plot([4.5,6],[velo7,velo7],linewidth=2)
        plt.xlabel('grade moving average (stage three)') 
        plt.ylabel('power')
        plt.plot() 
        plt.show() 
        return fig

avg_power_metrics_s1=Average_Power_Metrics_S1()
avg_power_metrics_s1.average_power_stage_one(frank_rides)

avg_power_metrics_s2=Average_Power_Metrics_S2()
avg_power_metrics_s2.average_power_stage_two(frank_rides)

avg_power_metrics_s3=Average_Power_Metrics_S3()
avg_power_metrics_s3.average_power_stage_three(frank_rides)


class Average_Cadence_Metrics_S1():
    def __init__(self):
        pass

    def average_cadence_stage_one(self,x):
        fig=plt.figure()
        x=frank_rides[0:2500]
        x['grade_ma1']=x['grade'].rolling(window=20).mean() #20 point moving average for the grade
        x['grade_ma1']=x['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x[x['grade_ma1']<-6]
        velo1=grade_lowest['cadence'].mean()
        grade_low2=x[(x['grade_ma1']>-6) & (x['grade_ma1']<=-4.5)]
        velo111=grade_low2['cadence'].mean()
        grade_low1=x[(x['grade_ma1']>-4.5) & (x['grade_ma1']<=-3)]
        velo11=grade_low1['cadence'].mean()
        grade_low=x[(x['grade_ma1']>-3) & (x['grade_ma1']<=-1.5)]
        velo2=grade_low['cadence'].mean()
        grade_avg=x[(x['grade_ma1']>-1.5) &(x['grade_ma1']<=0)]
        velo3=grade_avg['cadence'].mean() 
        grade_high=x[(x['grade_ma1']>0) &(x['grade_ma1']<=1.5)]
        velo4=grade_high['cadence'].mean() 
        grade_high1=x[(x['grade_ma1']>1.5) &(x['grade_ma1']<=3)]
        velo5=grade_high1['cadence'].mean() 
        grade_high2=x[(x['grade_ma1']>3) &(x['grade_ma1']<=4.5)]
        velo6=grade_high2['cadence'].mean() 
        grade_high3=x[(x['grade_ma1']>4.5) &(x['grade_ma1']<=6)]
        velo7=grade_high3['cadence'].mean() 
        plt.plot([-7.5,-6],[velo1,velo1],linewidth=2)
        plt.plot([-6,-4.5],[velo111,velo111],linewidth=2)
        plt.plot([-4.5,-3],[velo11,velo11],linewidth=2)
        plt.plot([-3,-1.5],[velo2,velo2],linewidth=2)
        plt.plot([-1.5,0],[velo3,velo3],linewidth=2)
        plt.plot([0,1.5],[velo4,velo4],linewidth=2)
        plt.plot([1.5,3],[velo5,velo5],linewidth=2)
        plt.plot([3,4.5],[velo6,velo6],linewidth=2)
        plt.plot([4.5,6],[velo7,velo7],linewidth=2)
        plt.xlabel('grade moving average (stage one)') 
        plt.ylabel('cadence')
        plt.plot() 
        plt.show() 
        return fig
    
class Average_Cadence_Metrics_S2():
    def __init__(self):
        pass

    def average_cadence_stage_two(self,x):
        fig=plt.figure()
        x=frank_rides[2501:5000]
        x['grade_ma1']=x['grade'].rolling(window=20).mean() #20 point moving average for the grade
        x['grade_ma1']=x['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x[x['grade_ma1']<-6]
        velo1=grade_lowest['cadence'].mean()
        grade_low2=x[(x['grade_ma1']>-6) & (x['grade_ma1']<=-4.5)]
        velo111=grade_low2['cadence'].mean()
        grade_low1=x[(x['grade_ma1']>-4.5) & (x['grade_ma1']<=-3)]
        velo11=grade_low1['cadence'].mean()
        grade_low=x[(x['grade_ma1']>-3) & (x['grade_ma1']<=-1.5)]
        velo2=grade_low['cadence'].mean()
        grade_avg=x[(x['grade_ma1']>-1.5) &(x['grade_ma1']<=0)]
        velo3=grade_avg['cadence'].mean() 
        grade_high=x[(x['grade_ma1']>0) &(x['grade_ma1']<=1.5)]
        velo4=grade_high['cadence'].mean() 
        grade_high1=x[(x['grade_ma1']>1.5) &(x['grade_ma1']<=3)]
        velo5=grade_high1['cadence'].mean() 
        grade_high2=x[(x['grade_ma1']>3) &(x['grade_ma1']<=4.5)]
        velo6=grade_high2['cadence'].mean() 
        grade_high3=x[(x['grade_ma1']>4.5) &(x['grade_ma1']<=6)]
        velo7=grade_high3['cadence'].mean() 
        plt.plot([-7.5,-6],[velo1,velo1],linewidth=2)
        plt.plot([-6,-4.5],[velo111,velo111],linewidth=2)
        plt.plot([-4.5,-3],[velo11,velo11],linewidth=2)
        plt.plot([-3,-1.5],[velo2,velo2],linewidth=2)
        plt.plot([-1.5,0],[velo3,velo3],linewidth=2)
        plt.plot([0,1.5],[velo4,velo4],linewidth=2)
        plt.plot([1.5,3],[velo5,velo5],linewidth=2)
        plt.plot([3,4.5],[velo6,velo6],linewidth=2)
        plt.plot([4.5,6],[velo7,velo7],linewidth=2)
        plt.xlabel('grade moving average (stage one)') 
        plt.ylabel('cadence')
        plt.plot() 
        plt.show() 
        return fig

class Average_Cadence_Metrics_S3():
    def __init__(self):
        pass

    def average_cadence_stage_three(self,x):
        fig=plt.figure()
        x=frank_rides[5001:10000]
        x['grade_ma1']=x['grade'].rolling(window=20).mean() #20 point moving average for the grade
        x['grade_ma1']=x['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x[x['grade_ma1']<-6]
        velo1=grade_lowest['cadence'].mean()
        grade_low2=x[(x['grade_ma1']>-6) & (x['grade_ma1']<=-4.5)]
        velo111=grade_low2['cadence'].mean()
        grade_low1=x[(x['grade_ma1']>-4.5) & (x['grade_ma1']<=-3)]
        velo11=grade_low1['cadence'].mean()
        grade_low=x[(x['grade_ma1']>-3) & (x['grade_ma1']<=-1.5)]
        velo2=grade_low['cadence'].mean()
        grade_avg=x[(x['grade_ma1']>-1.5) &(x['grade_ma1']<=0)]
        velo3=grade_avg['cadence'].mean() 
        grade_high=x[(x['grade_ma1']>0) &(x['grade_ma1']<=1.5)]
        velo4=grade_high['cadence'].mean() 
        grade_high1=x[(x['grade_ma1']>1.5) &(x['grade_ma1']<=3)]
        velo5=grade_high1['cadence'].mean() 
        grade_high2=x[(x['grade_ma1']>3) &(x['grade_ma1']<=4.5)]
        velo6=grade_high2['cadence'].mean() 
        grade_high3=x[(x['grade_ma1']>4.5) &(x['grade_ma1']<=6)]
        velo7=grade_high3['cadence'].mean() 
        plt.plot([-7.5,-6],[velo1,velo1],linewidth=2)
        plt.plot([-6,-4.5],[velo111,velo111],linewidth=2)
        plt.plot([-4.5,-3],[velo11,velo11],linewidth=2)
        plt.plot([-3,-1.5],[velo2,velo2],linewidth=2)
        plt.plot([-1.5,0],[velo3,velo3],linewidth=2)
        plt.plot([0,1.5],[velo4,velo4],linewidth=2)
        plt.plot([1.5,3],[velo5,velo5],linewidth=2)
        plt.plot([3,4.5],[velo6,velo6],linewidth=2)
        plt.plot([4.5,6],[velo7,velo7],linewidth=2)
        plt.xlabel('grade moving average (stage one)') 
        plt.ylabel('cadence')
        plt.plot() 
        plt.show() 
        return fig

avg_cadence_metrics_s1=Average_Cadence_Metrics_S1()
avg_cadence_metrics_s1.average_cadence_stage_one(frank_rides)

avg_cadence_metrics_s2=Average_Cadence_Metrics_S2()
avg_cadence_metrics_s2.average_cadence_stage_two(frank_rides)

avg_cadence_metrics_s3=Average_Cadence_Metrics_S3()
avg_cadence_metrics_s3.average_cadence_stage_three(frank_rides)
    


class Average_Heartrate_Metrics_S1():
    def __init__(self):
        pass

    def average_heartrate_stage_one(self,x):
        fig=plt.figure()
        x=frank_rides[0:2500]
        x['grade_ma1']=x['grade'].rolling(window=20).mean() #20 point moving average for the grade
        x['grade_ma1']=x['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x[x['grade_ma1']<-6]
        velo1=grade_lowest['heartrate'].mean()
        grade_low2=x[(x['grade_ma1']>-6) & (x['grade_ma1']<=-4.5)]
        velo111=grade_low2['heartrate'].mean()
        grade_low1=x[(x['grade_ma1']>-4.5) & (x['grade_ma1']<=-3)]
        velo11=grade_low1['heartrate'].mean()
        grade_low=x[(x['grade_ma1']>-3) & (x['grade_ma1']<=-1.5)]
        velo2=grade_low['heartrate'].mean()
        grade_avg=x[(x['grade_ma1']>-1.5) &(x['grade_ma1']<=0)]
        velo3=grade_avg['heartrate'].mean() 
        grade_high=x[(x['grade_ma1']>0) &(x['grade_ma1']<=1.5)]
        velo4=grade_high['heartrate'].mean() 
        grade_high1=x[(x['grade_ma1']>1.5) &(x['grade_ma1']<=3)]
        velo5=grade_high1['heartrate'].mean() 
        grade_high2=x[(x['grade_ma1']>3) &(x['grade_ma1']<=4.5)]
        velo6=grade_high2['heartrate'].mean() 
        grade_high3=x[(x['grade_ma1']>4.5) &(x['grade_ma1']<=6)]
        velo7=grade_high3['heartrate'].mean() 
        plt.plot([-7.5,-6],[velo1,velo1],linewidth=2)
        plt.plot([-6,-4.5],[velo111,velo111],linewidth=2)
        plt.plot([-4.5,-3],[velo11,velo11],linewidth=2)
        plt.plot([-3,-1.5],[velo2,velo2],linewidth=2)
        plt.plot([-1.5,0],[velo3,velo3],linewidth=2)
        plt.plot([0,1.5],[velo4,velo4],linewidth=2)
        plt.plot([1.5,3],[velo5,velo5],linewidth=2)
        plt.plot([3,4.5],[velo6,velo6],linewidth=2)
        plt.plot([4.5,6],[velo7,velo7],linewidth=2)
        plt.xlabel('grade moving average (stage one)') 
        plt.ylabel('heartrate')
        plt.plot() 
        plt.show() 
        return fig

class Average_Heartrate_Metrics_S2():
    def __init__(self):
        pass

    def average_heartrate_stage_two(self,x):
        fig=plt.figure()
        x=frank_rides[2501:5000]
        x['grade_ma1']=x['grade'].rolling(window=20).mean() #20 point moving average for the grade
        x['grade_ma1']=x['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x[x['grade_ma1']<-6]
        velo1=grade_lowest['heartrate'].mean()
        grade_low2=x[(x['grade_ma1']>-6) & (x['grade_ma1']<=-4.5)]
        velo111=grade_low2['heartrate'].mean()
        grade_low1=x[(x['grade_ma1']>-4.5) & (x['grade_ma1']<=-3)]
        velo11=grade_low1['heartrate'].mean()
        grade_low=x[(x['grade_ma1']>-3) & (x['grade_ma1']<=-1.5)]
        velo2=grade_low['heartrate'].mean()
        grade_avg=x[(x['grade_ma1']>-1.5) &(x['grade_ma1']<=0)]
        velo3=grade_avg['heartrate'].mean() 
        grade_high=x[(x['grade_ma1']>0) &(x['grade_ma1']<=1.5)]
        velo4=grade_high['heartrate'].mean() 
        grade_high1=x[(x['grade_ma1']>1.5) &(x['grade_ma1']<=3)]
        velo5=grade_high1['heartrate'].mean() 
        grade_high2=x[(x['grade_ma1']>3) &(x['grade_ma1']<=4.5)]
        velo6=grade_high2['heartrate'].mean() 
        grade_high3=x[(x['grade_ma1']>4.5) &(x['grade_ma1']<=6)]
        velo7=grade_high3['heartrate'].mean() 
        plt.plot([-7.5,-6],[velo1,velo1],linewidth=2)
        plt.plot([-6,-4.5],[velo111,velo111],linewidth=2)
        plt.plot([-4.5,-3],[velo11,velo11],linewidth=2)
        plt.plot([-3,-1.5],[velo2,velo2],linewidth=2)
        plt.plot([-1.5,0],[velo3,velo3],linewidth=2)
        plt.plot([0,1.5],[velo4,velo4],linewidth=2)
        plt.plot([1.5,3],[velo5,velo5],linewidth=2)
        plt.plot([3,4.5],[velo6,velo6],linewidth=2)
        plt.plot([4.5,6],[velo7,velo7],linewidth=2)
        plt.xlabel('grade moving average (stage two)') 
        plt.ylabel('heartrate')
        plt.plot() 
        plt.show() 
        return fig

class Average_Heartrate_Metrics_S3():
    def __init__(self):
        pass

    def average_heartrate_stage_three(self,x):
        fig=plt.figure()
        x=frank_rides[5001:10000]
        x['grade_ma1']=x['grade'].rolling(window=20).mean() #20 point moving average for the grade
        x['grade_ma1']=x['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x[x['grade_ma1']<-6]
        velo1=grade_lowest['heartrate'].mean()
        grade_low2=x[(x['grade_ma1']>-6) & (x['grade_ma1']<=-4.5)]
        velo111=grade_low2['heartrate'].mean()
        grade_low1=x[(x['grade_ma1']>-4.5) & (x['grade_ma1']<=-3)]
        velo11=grade_low1['heartrate'].mean()
        grade_low=x[(x['grade_ma1']>-3) & (x['grade_ma1']<=-1.5)]
        velo2=grade_low['heartrate'].mean()
        grade_avg=x[(x['grade_ma1']>-1.5) &(x['grade_ma1']<=0)]
        velo3=grade_avg['heartrate'].mean() 
        grade_high=x[(x['grade_ma1']>0) &(x['grade_ma1']<=1.5)]
        velo4=grade_high['heartrate'].mean() 
        grade_high1=x[(x['grade_ma1']>1.5) &(x['grade_ma1']<=3)]
        velo5=grade_high1['heartrate'].mean() 
        grade_high2=x[(x['grade_ma1']>3) &(x['grade_ma1']<=4.5)]
        velo6=grade_high2['heartrate'].mean() 
        grade_high3=x[(x['grade_ma1']>4.5) &(x['grade_ma1']<=6)]
        velo7=grade_high3['heartrate'].mean() 
        plt.plot([-7.5,-6],[velo1,velo1],linewidth=2)
        plt.plot([-6,-4.5],[velo111,velo111],linewidth=2)
        plt.plot([-4.5,-3],[velo11,velo11],linewidth=2)
        plt.plot([-3,-1.5],[velo2,velo2],linewidth=2)
        plt.plot([-1.5,0],[velo3,velo3],linewidth=2)
        plt.plot([0,1.5],[velo4,velo4],linewidth=2)
        plt.plot([1.5,3],[velo5,velo5],linewidth=2)
        plt.plot([3,4.5],[velo6,velo6],linewidth=2)
        plt.plot([4.5,6],[velo7,velo7],linewidth=2)
        plt.xlabel('grade moving average (stage three)') 
        plt.ylabel('heartrate')
        plt.plot() 
        plt.show() 
        return fig

avg_heartrate_metrics_s1=Average_Heartrate_Metrics_S1()
avg_heartrate_metrics_s1.average_heartrate_stage_one(frank_rides)

avg_heartrate_metrics_s2=Average_Heartrate_Metrics_S2()
avg_heartrate_metrics_s2.average_heartrate_stage_two(frank_rides)

avg_heartrate_metrics_s3=Average_Heartrate_Metrics_S3()
avg_heartrate_metrics_s3.average_heartrate_stage_three(frank_rides)