#how does rider's velocity compare on long uphill ride vs. short uphill? 
#how does rider's velocity compare on long downhill vs. short downhill?

class Stage_Stretch():
    def __init__(self):
        pass
    
    def uphill_long_short(self,x):
        x['grade_diff']=x['grade'].diff()
        x['up_down']=np.where(x['grade_diff']>0,'uphill','downhill')
        x['count'] = x.groupby((x['up_down'] != x['up_down'].shift(1)).cumsum()).cumcount()+1
        #long hill climbs
        long_hill=x[(x['count']>=15) & (x['up_down']=="uphill")]
        short_hill=x[(x['count']<=5) & (x['up_down']=="uphill")]
        long_hill_velo=long_hill['velocity'].mean()
        short_hill_velo=short_hill['velocity'].mean()
        return long_hill_velo, short_hill_velo 

    def downhill_long_short(self,x):
        x['grade_diff']=x['grade'].diff()
        x['up_down']=np.where(x['grade_diff']>0,'uphill','downhill')
        x['count'] = x.groupby((x['up_down'] != x['up_down'].shift(1)).cumsum()).cumcount()+1
        #downhill runs
        long_downhill=x[(x['count']>=15) & (x['up_down']=="downhill")]
        short_downhill=x[(x['count']<=5) & (x['up_down']=="downhill")]
        long_downhill_velo=long_downhill['velocity'].mean()
        short_downhill_velo=short_downhill['velocity'].mean()
        return long_downhill_velo, short_downhill_velo 

stage=Stage_Stretch()
stage.uphill_long_short(df)
stage.downhill_long_short(df)