import numpy as np
import stravalib as strava
import seaborn as sns
import pandas as pd 

rides2=pd.read_csv("ride_current.csv") #sample ride data

rides2['ma_filter_slope']=rides2.grade.rolling(window=30).mean() #rollling 30-second moving average 
rides2.ma_filter_slope.describe()
idx=rides2['ma_filter_slope'].values>1
#count number of up-hill sections over the ride
rides2['idx_up']=rides2['ma_filter_slope'].values>2.5 
hills_boolean=rides2.idx_up.values 
#find indexes (for uphill start and uphill end)
df=rides2.idx_up
df=df.astype(int)
df=pd.DataFrame(df)
df_prev = df.shift(1)['idx_up']
df_next = df.shift(-1)['idx_up']
df_next2 = df.shift(-2)['idx_up']
df.loc[(df_prev != 1) & (df['idx_up'] == 1) & (df_next == 1), 'start'] = 1
df.loc[(df['idx_up'] != 0) & (df_next == 0) & (df_next2 == 0), 'end'] = 1
df.fillna(0, inplace=True)
df = df.astype(int)
#combine dataframes 
rest=pd.concat([rides2,df],axis=1)
rest = rest.loc[:,~rest.columns.duplicated()]

class Ride_Analysis():
    def __init__(self):
        pass

    #this function measures the percentage of the time that the rider is going uphill compared to being in a "rest" state (downhill or flat grade)
    def uphill_pct(self):
        rest_sub=rest[["start","end","idx_up"]]
        rest_sub1=rest_sub[(rest_sub.start==1) | (rest_sub.end==1)]
        up_start=[] #counting the start and end point of an uphill 
        for i,row in rest_sub1.iterrows():
            up_start.append(i)
        #append time 0 as a starting point for the ride
        time_zero=0
        up_start=[time_zero]+up_start 
        #time spent on uphills and "rest" sections
        time_diff=np.diff(up_start)
        #a.select every 2nd value (for time spent on uphills) >2.5 grade
        uphill_time=time_diff[1::2] #start at the first index 
        #b. time spent in "rest" sections
        rest_time=time_diff[0::2]
        #account for last section of the ride 
        final_rest=up_start[-1]
        final_rest=rest.shape[0]-final_rest 
        final_rest=np.append(rest_time,final_rest) #append last section of the ride to rest time
        final_rest=np.array(final_rest)
        #calculate percentage in rest state vs. percentage in uphill state?
        uphill_count=uphill_time.sum() 
        rest_count=final_rest.sum() 
        uphill_pct=uphill_count/(uphill_count+rest_count)*100
        rest_pct=rest_count/(uphill_count+rest_count)*100
        uphill_pct=round(uphill_pct,2)
        rest_pct=round(rest_pct,2)

        print("The cyclist is riding uphill {0:.10f}".format(uphill_pct) + "%" + " of the time over the ride.")
        print("The cyclist is in a rest state {0:.10f}".format(rest_pct) + "%" + " of the time over the ride.")

    #calculating the cyclist's power output on uphills 
    def uphill_metrics(self):
        uphill_metrics=rest[rest.idx_up==True]
        power_avg=uphill_metrics.power.mean() 
        velocity_avg=uphill_metrics.velocity.mean()
        cadence_avg=uphill_metrics.cadence.mean() 

        uphill_columns=[]
        def test_iterrow(df):
            for (i,row) in df.iterrows():
                if row['idx_up']==True:
                    uphill_columns.append(row)
        test_iterrow(rest)
        uphill_columns1=pd.DataFrame(uphill_columns)

        #difference between indexes
        uphill_columns1['time_diff']=uphill_columns1['time'] - uphill_columns1['time'].shift(1)
        uphill_cols=uphill_columns1['time_diff']
        uphill_cols=pd.DataFrame(uphill_cols)

        #find hill intervals in the dataframe 
        uphsi=[]
        local=[]
        for idx in range(uphill_cols['time_diff'].values.shape[0]):
            aux=uphill_cols["time_diff"].values[idx]
            if aux>1 and np.isfinite(aux):
                uphsi.append(local)
                local=[uphill_cols.iloc[idx]]
            else:
                local.append(uphill_cols.iloc[idx])

        hills=uphsi
        hill_index=[]
        for i in range(0,len(hills)):
            values=hills[i]
            hill_index.append(values)

        # hill 1 
        hills1=hills[0]
        hills1=pd.DataFrame(hills1)
        hills1.reset_index(level=0,inplace=True)
        hills1.columns=['index','time_diff']
        rest1=rest 
        rest1.reset_index(level=0,inplace=True)
        hill1=pd.merge(hills1,rest1,on="index")
        hill1_avg=hill1[["power","velocity","cadence","heartrate"]].mean() 
        hill1_avg=np.array(hill1_avg)

        # hill 10
        hills10=hills[9]
        hills10=pd.DataFrame(hills10)
        hills10.reset_index(level=0,inplace=True)
        rest1=rest 
        rest1.reset_index(level=0,inplace=True)
        hills10=pd.merge(hills10,rest1,on="index")
        hill10_avg=hills10[["power","velocity","cadence","heartrate"]].mean() 
        hill10_avg=np.array(hill10_avg)

        #
        print("The average power on the cyclist's first hill {0:.10f}".format(hill1_avg[0])+ " watts.")
        print("The average power on the cyclist's tenth hill {0:.10f}".format(hill10_avg[0])+ " watts.")


if __name__ =='__main__':
    rides=Ride_Analysis()
    rest_uphill=rides.uphill_pct() #measures uphill vs. "rest" percentages 
    uphill_metrcs=rides.uphill_metrics() #power output on uphills 


