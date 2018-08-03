#Average Metrics based on the grade (slope) and stage of the ride (split into three stages)

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
import pylab as plot 

rides=pd.read_csv("final_df.csv")

class Grade_Stages():
    def __init(self):
        pass
    def grade_power(self,x1):
        x1['grade_ma1']=x1['grade'].rolling(window=15).mean() #15 point moving average for the grade
        x1['grade_ma1']=x1['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x1[x1['grade_ma1']<=-6]
        velo1=grade_lowest['power'].mean()
        grade_low2=x1[(x1['grade_ma1']>-6) & (x1['grade_ma1']<=-4.5)]
        velo2=grade_low2['power'].mean()
        grade_low1=x1[(x1['grade_ma1']>-4.5) & (x1['grade_ma1']<=-3)]
        velo3=grade_low1['power'].mean()
        grade_low=x1[(x1['grade_ma1']>-3) & (x1['grade_ma1']<=-1.5)]
        velo4=grade_low['power'].mean()
        grade_avg=x1[(x1['grade_ma1']>-1.5) &(x1['grade_ma1']<=0)]
        velo5=grade_avg['power'].mean() 
        grade_high=x1[(x1['grade_ma1']>0) &(x1['grade_ma1']<=1.5)]
        velo6=grade_high['power'].mean() 
        grade_high1=x1[(x1['grade_ma1']>1.5) &(x1['grade_ma1']<=3)]
        velo7=grade_high1['power'].mean() 
        grade_high2=x1[(x1['grade_ma1']>3) &(x1['grade_ma1']<=4.5)]
        velo8=grade_high2['power'].mean() 
        grade_high3=x1[(x1['grade_ma1']>4.5) &(x1['grade_ma1']<=6)]
        velo9=grade_high3['power'].mean() 
        velo1=pd.Series(velo1)
        velo1=pd.DataFrame(velo1,columns=['velo1'])
        velo2=pd.Series(velo2)
        velo2=pd.DataFrame(velo2,columns=['velo2'])  
        velo3=pd.Series(velo3)
        velo3=pd.DataFrame(velo3,columns=['velo3'])
        velo4=pd.Series(velo4)
        velo4=pd.DataFrame(velo4,columns=['velo4'])
        velo5=pd.Series(velo5)
        velo5=pd.DataFrame(velo5,columns=['velo5'])
        velo6=pd.Series(velo6)
        velo6=pd.DataFrame(velo6,columns=['velo6'])
        velo7=pd.Series(velo7)
        velo7=pd.DataFrame(velo7,columns=['velo5'])
        velo8=pd.Series(velo8)
        velo8=pd.DataFrame(velo8,columns=['velo8'])
        velo9=pd.Series(velo9)
        velo9=pd.DataFrame(velo9,columns=['velo9'])
        df_final=pd.concat([velo1,velo2,velo3,velo4,velo5,velo6,velo7,velo8,velo9],axis=1)
        return df_final 
    def grade_velocity(self,x1):
        x1['grade_ma1']=x1['grade'].rolling(window=15).mean() #15 point moving average for the grade
        x1['grade_ma1']=x1['grade_ma1'].fillna(0) #fill na with zero 
        x1['velocity_adj']=x1['velocity']*3.6 
        grade_lowest=x1[x1['grade_ma1']<=-6]
        velo1=grade_lowest['velocity_adj'].mean()
        grade_low2=x1[(x1['grade_ma1']>-6) & (x1['grade_ma1']<=-4.5)]
        velo2=grade_low2['velocity_adj'].mean()
        grade_low1=x1[(x1['grade_ma1']>-4.5) & (x1['grade_ma1']<=-3)]
        velo3=grade_low1['velocity_adj'].mean()
        grade_low=x1[(x1['grade_ma1']>-3) & (x1['grade_ma1']<=-1.5)]
        velo4=grade_low['velocity_adj'].mean()
        grade_avg=x1[(x1['grade_ma1']>-1.5) &(x1['grade_ma1']<=0)]
        velo5=grade_avg['velocity_adj'].mean() 
        grade_high=x1[(x1['grade_ma1']>0) &(x1['grade_ma1']<=1.5)]
        velo6=grade_high['velocity_adj'].mean() 
        grade_high1=x1[(x1['grade_ma1']>1.5) &(x1['grade_ma1']<=3)]
        velo7=grade_high1['velocity_adj'].mean() 
        grade_high2=x1[(x1['grade_ma1']>3) &(x1['grade_ma1']<=4.5)]
        velo8=grade_high2['velocity_adj'].mean() 
        grade_high3=x1[(x1['grade_ma1']>4.5) &(x1['grade_ma1']<=6)]
        velo9=grade_high3['velocity_adj'].mean() 
        velo1=pd.Series(velo1)
        velo1=pd.DataFrame(velo1,columns=['velo1'])
        velo2=pd.Series(velo2)
        velo2=pd.DataFrame(velo2,columns=['velo2'])  
        velo3=pd.Series(velo3)
        velo3=pd.DataFrame(velo3,columns=['velo3'])
        velo4=pd.Series(velo4)
        velo4=pd.DataFrame(velo4,columns=['velo4'])
        velo5=pd.Series(velo5)
        velo5=pd.DataFrame(velo5,columns=['velo5'])
        velo6=pd.Series(velo6)
        velo6=pd.DataFrame(velo6,columns=['velo6'])
        velo7=pd.Series(velo7)
        velo7=pd.DataFrame(velo7,columns=['velo5'])
        velo8=pd.Series(velo8)
        velo8=pd.DataFrame(velo8,columns=['velo8'])
        velo9=pd.Series(velo9)
        velo9=pd.DataFrame(velo9,columns=['velo9'])
        df_final1=pd.concat([velo1,velo2,velo3,velo4,velo5,velo6,velo7,velo8,velo9],axis=1)
        return df_final1
    def grade_cadence(self,x1):
        x1['grade_ma1']=x1['grade'].rolling(window=15).mean() #15 point moving average for the grade
        x1['grade_ma1']=x1['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x1[x1['grade_ma1']<=-6]
        velo1=grade_lowest['cadence'].mean()
        grade_low2=x1[(x1['grade_ma1']>-6) & (x1['grade_ma1']<=-4.5)]
        velo2=grade_low2['cadence'].mean()
        grade_low1=x1[(x1['grade_ma1']>-4.5) & (x1['grade_ma1']<=-3)]
        velo3=grade_low1['cadence'].mean()
        grade_low=x1[(x1['grade_ma1']>-3) & (x1['grade_ma1']<=-1.5)]
        velo4=grade_low['cadence'].mean()
        grade_avg=x1[(x1['grade_ma1']>-1.5) &(x1['grade_ma1']<=0)]
        velo5=grade_avg['cadence'].mean() 
        grade_high=x1[(x1['grade_ma1']>0) &(x1['grade_ma1']<=1.5)]
        velo6=grade_high['cadence'].mean() 
        grade_high1=x1[(x1['grade_ma1']>1.5) &(x1['grade_ma1']<=3)]
        velo7=grade_high1['cadence'].mean() 
        grade_high2=x1[(x1['grade_ma1']>3) &(x1['grade_ma1']<=4.5)]
        velo8=grade_high2['cadence'].mean() 
        grade_high3=x1[(x1['grade_ma1']>4.5) &(x1['grade_ma1']<=6)]
        velo9=grade_high3['cadence'].mean() 
        velo1=pd.Series(velo1)
        velo1=pd.DataFrame(velo1,columns=['velo1'])
        velo2=pd.Series(velo2)
        velo2=pd.DataFrame(velo2,columns=['velo2'])  
        velo3=pd.Series(velo3)
        velo3=pd.DataFrame(velo3,columns=['velo3'])
        velo4=pd.Series(velo4)
        velo4=pd.DataFrame(velo4,columns=['velo4'])
        velo5=pd.Series(velo5)
        velo5=pd.DataFrame(velo5,columns=['velo5'])
        velo6=pd.Series(velo6)
        velo6=pd.DataFrame(velo6,columns=['velo6'])
        velo7=pd.Series(velo7)
        velo7=pd.DataFrame(velo7,columns=['velo5'])
        velo8=pd.Series(velo8)
        velo8=pd.DataFrame(velo8,columns=['velo8'])
        velo9=pd.Series(velo9)
        velo9=pd.DataFrame(velo9,columns=['velo9'])
        df_final2=pd.concat([velo1,velo2,velo3,velo4,velo5,velo6,velo7,velo8,velo9],axis=1)
        return df_final2
    def grade_heartrate(self,x1):
        x1['grade_ma1']=x1['grade'].rolling(window=15).mean() #15 point moving average for the grade
        x1['grade_ma1']=x1['grade_ma1'].fillna(0) #fill na with zero 
        grade_lowest=x1[x1['grade_ma1']<=-6]
        velo1=grade_lowest['heartrate'].mean()
        grade_low2=x1[(x1['grade_ma1']>-6) & (x1['grade_ma1']<=-4.5)]
        velo2=grade_low2['heartrate'].mean()
        grade_low1=x1[(x1['grade_ma1']>-4.5) & (x1['grade_ma1']<=-3)]
        velo3=grade_low1['heartrate'].mean()
        grade_low=x1[(x1['grade_ma1']>-3) & (x1['grade_ma1']<=-1.5)]
        velo4=grade_low['heartrate'].mean()
        grade_avg=x1[(x1['grade_ma1']>-1.5) &(x1['grade_ma1']<=0)]
        velo5=grade_avg['heartrate'].mean() 
        grade_high=x1[(x1['grade_ma1']>0) &(x1['grade_ma1']<=1.5)]
        velo6=grade_high['heartrate'].mean() 
        grade_high1=x1[(x1['grade_ma1']>1.5) &(x1['grade_ma1']<=3)]
        velo7=grade_high1['heartrate'].mean() 
        grade_high2=x1[(x1['grade_ma1']>3) &(x1['grade_ma1']<=4.5)]
        velo8=grade_high2['heartrate'].mean() 
        grade_high3=x1[(x1['grade_ma1']>4.5) &(x1['grade_ma1']<=6)]
        velo9=grade_high3['heartrate'].mean() 
        velo1=pd.Series(velo1)
        velo1=pd.DataFrame(velo1,columns=['velo1'])
        velo2=pd.Series(velo2)
        velo2=pd.DataFrame(velo2,columns=['velo2'])  
        velo3=pd.Series(velo3)
        velo3=pd.DataFrame(velo3,columns=['velo3'])
        velo4=pd.Series(velo4)
        velo4=pd.DataFrame(velo4,columns=['velo4'])
        velo5=pd.Series(velo5)
        velo5=pd.DataFrame(velo5,columns=['velo5'])
        velo6=pd.Series(velo6)
        velo6=pd.DataFrame(velo6,columns=['velo6'])
        velo7=pd.Series(velo7)
        velo7=pd.DataFrame(velo7,columns=['velo5'])
        velo8=pd.Series(velo8)
        velo8=pd.DataFrame(velo8,columns=['velo8'])
        velo9=pd.Series(velo9)
        velo9=pd.DataFrame(velo9,columns=['velo9'])
        df_final3=pd.concat([velo1,velo2,velo3,velo4,velo5,velo6,velo7,velo8,velo9],axis=1)
        return df_final3
    def power_stages_viz(self,x):
        fig1=plt.figure()
        first_third=round(0.3333*len(x)) 
        second_third=round(0.6667*len(x))
        final_third=len(x)
        first_stage=x[0:first_third]
        second_stage=x[first_third:second_third]
        third_stage=x[second_third:final_third]
        all_stages=x
        stages=Grade_Stages() 
        all_stages=stages.grade_power(all_stages)  
        stage1=stages.grade_power(first_stage)
        stage2=stages.grade_power(second_stage)
        stage3=stages.grade_power(third_stage)
        combine_stages=pd.concat([all_stages,stage1,stage2,stage3],axis=1)
        combine_stages1=combine_stages.values
        combine_stages1=combine_stages1.reshape(4,9)
        combine_stages2=pd.DataFrame(combine_stages1,columns=['-6.0','-6.0 to -4.5','-4.5 to -3.0','-3.0 to -1.5','-1.5 to 0.0','0.0 to 1.5','1.5 to 3.0','3.0 to 4.5','6.0+'])
        combine_stages2.reset_index(level=0,inplace=True)
        combine_stages3=combine_stages2
        combine_stages3.index=['average','stage one','stage two','stage three']
        combine_stages3.reset_index(level=0,inplace=True)
        combine_stages3.plot(x="level_0",y=["-6.0","-6.0 to -4.5","-4.5 to -3.0","-3.0 to -1.5","-1.5 to 0.0","0.0 to 1.5","1.5 to 3.0","3.0 to 4.5","6.0+"],kind="bar",rot=0,figsize=(12,8))
        plt.annotate('Average power and stage power over the ride',(0,0),(80,-25),xycoords='axes fraction', textcoords='offset points', va='top')
        plt.xlabel("")
        plt.ylabel("power")
        plt.title("Stage Power")
        plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0,title='moving average slope')
        legend(loc=1,title="moving average slope interval")
        plt.grid(True)
        plt.savefig("power_grade.pdf")
        plt.show()
        return fig1
    def velocity_stages_viz(self,x):
        fig2=plt.figure()
        first_third=round(0.3333*len(x)) 
        second_third=round(0.6667*len(x))
        final_third=len(x)
        first_stage=x[0:first_third]
        second_stage=x[first_third:second_third]
        third_stage=x[second_third:final_third]
        all_stages=x
        stages=Grade_Stages() 
        all_stages=stages.grade_velocity(all_stages)  
        stage1=stages.grade_velocity(first_stage)
        stage2=stages.grade_velocity(second_stage)
        stage3=stages.grade_velocity(third_stage)
        combine_stages=pd.concat([all_stages,stage1,stage2,stage3],axis=1)
        combine_stages1=combine_stages.values
        combine_stages1=combine_stages1.reshape(4,9)
        combine_stages2=pd.DataFrame(combine_stages1,columns=['-6.0','-6.0 to -4.5','-4.5 to -3.0','-3.0 to -1.5','-1.5 to 0.0','0.0 to 1.5','1.5 to 3.0','3.0 to 4.5','6.0+'])
        combine_stages2.reset_index(level=0,inplace=True)
        combine_stages3=combine_stages2
        combine_stages3.index=['average','stage one','stage two','stage three']
        combine_stages3.reset_index(level=0,inplace=True)
        combine_stages3.plot(x="level_0",y=["-6.0","-6.0 to -4.5","-4.5 to -3.0","-3.0 to -1.5","-1.5 to 0.0","0.0 to 1.5","1.5 to 3.0","3.0 to 4.5","6.0+"],kind="bar",rot=0,figsize=(12,8))
        plt.annotate('Average velocity and stage velocity over the ride',(0,0),(80,-25),xycoords='axes fraction', textcoords='offset points', va='top')
        plt.xlabel("")
        plt.ylabel("velocity (km/hr)")
        plt.title("Stage Velocity")
        plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0,title='moving average slope')
        legend(loc=1,title="moving average slope interval")
        plt.grid(True)
        plt.savefig('velo_stage.pdf')
        plt.show()
        return fig2
    def cadence_stages_viz(self,x):
        fig3=plt.figure()
        first_third=round(0.3333*len(x)) 
        second_third=round(0.6667*len(x))
        final_third=len(x)
        first_stage=x[0:first_third]
        second_stage=x[first_third:second_third]
        third_stage=x[second_third:final_third]
        all_stages=x
        stages=Grade_Stages() 
        all_stages=stages.grade_cadence(all_stages)  
        stage1=stages.grade_cadence(first_stage)
        stage2=stages.grade_cadence(second_stage)
        stage3=stages.grade_cadence(third_stage)
        combine_stages=pd.concat([all_stages,stage1,stage2,stage3],axis=1)
        combine_stages1=combine_stages.values
        combine_stages1=combine_stages1.reshape(4,9)
        combine_stages2=pd.DataFrame(combine_stages1,columns=['-6.0','-6.0 to -4.5','-4.5 to -3.0','-3.0 to -1.5','-1.5 to 0.0','0.0 to 1.5','1.5 to 3.0','3.0 to 4.5','6.0+'])
        combine_stages2.reset_index(level=0,inplace=True)
        combine_stages3=combine_stages2
        combine_stages3.index=['average','stage one','stage two','stage three']
        combine_stages3.reset_index(level=0,inplace=True)
        combine_stages3.plot(x="level_0",y=["-6.0","-6.0 to -4.5","-4.5 to -3.0","-3.0 to -1.5","-1.5 to 0.0","0.0 to 1.5","1.5 to 3.0","3.0 to 4.5","6.0+"],kind="bar",rot=0,figsize=(12,8))
        plt.annotate('Average cadence and stage cadence over the ride',(0,0),(80,-25),xycoords='axes fraction', textcoords='offset points', va='top')
        plt.xlabel("")
        plt.ylabel("cadence")
        plt.title("Stage Cadence")
        plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0,title='moving average slope')
        legend(loc=1,title="moving average slope interval")
        plt.grid(True)
        plt.savefig("cadence_stage.pdf")
        plt.show()
        return fig3
    def heartrate_stages_viz(self,x):
        fig4=plt.figure()
        first_third=round(0.3333*len(x)) 
        second_third=round(0.6667*len(x))
        final_third=len(x)
        first_stage=x[0:first_third]
        second_stage=x[first_third:second_third]
        third_stage=x[second_third:final_third]
        all_stages=x
        stages=Grade_Stages() 
        all_stages=stages.grade_heartrate(all_stages)  
        stage1=stages.grade_heartrate(first_stage)
        stage2=stages.grade_heartrate(second_stage)
        stage3=stages.grade_heartrate(third_stage)
        combine_stages=pd.concat([all_stages,stage1,stage2,stage3],axis=1)
        combine_stages1=combine_stages.values
        combine_stages1=combine_stages1.reshape(4,9)
        combine_stages2=pd.DataFrame(combine_stages1,columns=['-6.0','-6.0 to -4.5','-4.5 to -3.0','-3.0 to -1.5','-1.5 to 0.0','0.0 to 1.5','1.5 to 3.0','3.0 to 4.5','6.0+'])
        combine_stages2.reset_index(level=0,inplace=True)
        combine_stages3=combine_stages2
        combine_stages3.index=['average','stage one','stage two','stage three']
        combine_stages3.reset_index(level=0,inplace=True)
        combine_stages3.plot(x="level_0",y=["-6.0","-6.0 to -4.5","-4.5 to -3.0","-3.0 to -1.5","-1.5 to 0.0","0.0 to 1.5","1.5 to 3.0","3.0 to 4.5","6.0+"],kind="bar",rot=0,figsize=(12,8))
        plt.annotate('Average heartrate and stage heartrate over the ride',(0,0),(80,-25),xycoords='axes fraction', textcoords='offset points', va='top')
        plt.xlabel("")
        plt.ylabel("heartrate")
        plt.title("Stage Heartrate")
        plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0,title='moving average slope')
        legend(loc=1,title='moving average slope interval')
        plt.grid(True)
        plt.savefig("heartrate_stage.pdf")
        plt.show()
        return fig4
        
if __name__ == '__main__':
    s = Grade_Stages()
    s.grade_power(rides)
    s.grade_velocity(rides)
    s.grade_cadence(rides)
    plot1=s.power_stages_viz(rides)
    plot2=s.velocity_stages_viz(rides)
    plot3=s.cadence_stages_viz(rides)
    plot4=s.heartrate_stages_viz(rides)
    pp=PdfPages("grade_stages.pdf")
    pp.savefig(plot1)
    pp.savefig(plot2)
    pp.savefig(plot3) 
    pp.savefig(plot4)
    pp.close() 
