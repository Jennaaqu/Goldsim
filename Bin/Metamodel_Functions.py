#24/06/2021 - This function solves the Lotka-Volterra system

# Import libraries
#++++++++++++++++++++++++++++++++
import numpy as np
from scipy.integrate import odeint
import math
from scipy.integrate import solve_ivp
import pandas as pd
from decimal import Decimal
import matplotlib.pyplot as plt
import seaborn as sns
#++++++++++++++++++++++++++++++++

#Index. Functions in this file
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#0.0. A function that solves logistic Lotka-Volterra model
#0.1. A function that solves Marisa's model 
#0.2. LHS-related. Splits any parameter range in equally distributed intervals
#0.3. Latin Hypercube Sampling (LHS)
#0.4. Define interval for experimental measurement
#0.5. Create a dataframe with measurement data on Hyperion
#0.6. Convert dictionary of solutions of dynamic model to dataframe
#0.7. Create dictionary of per capita rates (aka bioprocesses)
#0.8. Find thresholds in a list or vector
#0.9. Find critical concentrations of predation and burst
#0.11. Log sample a dataframe to plot a light svg heatmap
#0.12. Compute mean relative errors of simplified model
#0.11. A header for initial configurations of lotka-volterra dynamics
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#0. FUNCTIONS.
#0.0. Solution to Lotka-Volterra
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Solve_Lotka_Volterra(Parameters, Initial_Conditions, time_vector, step):
    
    r=Parameters['r'];K=Parameters['K'];d=Parameters['d']
    c=Parameters['c'];m=Parameters['m']
    #0.1. Lotka-Volterra system
    #=================================================    
    def Lotka_Volterra(t,y):

        return [r*(1-(y[0]/float(K)))*y[0] - d*y[0]*y[1],
                c*d*y[0]*y[1] - m*y[1]]

    #Breaking condition for sensitive bacteria. Bottom
    def Min_Volume_B(t,y):
        return y[0] - 1
    Min_Volume_B.terminal=True
    Min_Volume_B.direction = 1
    #=================================================

    #0.2. MODEL SOLUTION
    #================================================================
    Events_Model=Min_Volume_B
    y0=[Initial_Conditions[0], Initial_Conditions[1] ]

    #0.2.1. Solver
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    sol_LV=solve_ivp(Lotka_Volterra,[time_vector[0],time_vector[-1]],y0,\
    method='RK45',dense_output=True,events=Events_Model,max_step=step)
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    #0.2.2. Change time vector in case event triggered
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    try:
        final_t=sol_LV.t_events[0][0]
        time=time_vector[:int(time_vector[-1])]
        print('Event found')
    except IndexError:
        pass
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    return sol_LV
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#0.1. Solution to Experimental System
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Solve_Experiment_Induction(Parameters, Initial_Conditions, time_vector, step):
    r=Parameters['r']
    K=Parameters['K']
    mu=Parameters['mu']
    c=Parameters['c']
    m=Parameters['m']

    #0.1. Induction system
    #=================================================
    def Experiment_Induction(t,y):
        
        return [r*(1-(y[0]/float(K)))*y[0] - mu*y[0],
                c*mu*y[0] - m*y[1]]
    
    #Breaking conditions for sensitive bacteria. Bottom
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def Min_Volume_L(t,y):
        return y[0] - 1
    Min_Volume_L.terminal=False
    Min_Volume_L.direction = 1
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #=================================================

    #0.2. MODEL SOLUTION
    #====================================================================
    Events_Model=[]
    y0=[Initial_Conditions[0], Initial_Conditions[1] ]
    
    #0.2.1. Solver
    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    sol_Exp=solve_ivp(Experiment_Induction,[time_vector[0],time_vector[-1]],y0,\
    method='RK45',dense_output=True,events=Events_Model,max_step=step)
    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    #0.2.2. Change time vector in case event triggered
    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    try:
        final_t=sol_Exp.t_events[0][0]
        time=time_vector[:int(time_vector[-1])]
        print('Event found')
    except IndexError:
        pass
    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    return sol_Exp
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    
#0.2. Split range of parameters in equispaced or logspaced intervals
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def LHS_intervals(min_value,max_value,Samples_fun,Logarithmic=0):
    interval=np.linspace(min_value, max_value, Samples_fun+1)
    
    if Logarithmic==1:
        interval=np.logspace(np.log10(min_value), np.log10(max_value),\
                             num=Samples_fun+1, endpoint=True, base=10)
        
    return interval 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#0.3. Latin_Hypercube_Sampling
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
#Ranges_Parameters: a dictionary where keys are names of parameters and values
#are a list of two elements: mimimum and maxium value of the interval
def LHS(Ranges_Parameters, Sampling_Points, Seed):
    np.random.seed(Seed)

    #A dictionary that gives an id from 1 to N to each interval
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    Ids_Intervals={}  
    for Parameter in Ranges_Parameters:
        
        Min_Value=Ranges_Parameters[Parameter][0]
        Max_Value=Ranges_Parameters[Parameter][1]
        vector_interval=LHS_intervals(Min_Value, Max_Value, Sampling_Points)

        #Condition for logarithmic sampling
        #---------------------------------------------------------------------
        Min_o_magnitude=np.log10(Min_Value)     
        Max_o_magnitude=np.log10(Max_Value)
        
        Delta_Orders_of_Magnitude=\
                    abs(abs(np.log10(Max_Value)) - abs(np.log10(Min_Value)))
        
        if Delta_Orders_of_Magnitude>=2:
            vector_interval=LHS_intervals(Min_Value, Max_Value, Sampling_Points,Logarithmic=1) 
        #---------------------------------------------------------------------

        for i in range(len(vector_interval)-1):
            try:
                Ids_Intervals[Parameter][i]=\
                                    [vector_interval[i],vector_interval[i+1]]
            except KeyError:
                Ids_Intervals[Parameter]=\
                                    {i:[vector_interval[i],vector_interval[i+1]]}
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    #Randomly choose intervals for the parameters
    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    Samples={}
    for parameter in Ranges_Parameters:
        Samples[parameter]=\
        list(np.random.choice(Sampling_Points,Sampling_Points,replace=False))
    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    #Uniformly choose random values within intervals and store them in dictionary
    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    counter_samples=0
    Latin_Hypercube_Sampling={}

    for parameter in Samples:
        for interval in Samples[parameter]:
            #Interval minimum
            Min_value=Ids_Intervals[parameter][interval][0]
            #Interval maximum
            Max_value=Ids_Intervals[parameter][interval][1]
            #Uniformly choose random value
            parameter_value=np.random.uniform(Min_value,Max_value)

            #Store value in dictionary
            #---------------------------------------------------------------------
            try:
                Latin_Hypercube_Sampling[counter_samples][parameter]=\
                                                    parameter_value
            except KeyError:
                Latin_Hypercube_Sampling[counter_samples]=\
                                            {parameter:parameter_value}
            #--------------------------------------------------------------------
            counter_samples+=1
            if counter_samples==Sampling_Points:
                counter_samples=0
    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    return Latin_Hypercube_Sampling
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#0.4. Measurement Interval
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#This function gives you the experimental interval/span of time given a desired
#measurement time
def Measurement_Interval_fun(measurement_time,measure_error, time_vector):

    Initial_time=measurement_time - measure_error
    Final_time=measurement_time + measure_error

#Look for the chunk of time vector corresponding to the initial and final times
    Measure_Interval=[time_vector[np.abs(time_vector - Initial_time).argmin() :\
                                  np.abs(time_vector - Final_time).argmin()]][0]
    
    return Measure_Interval

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#0.5. Snapshots to Dataframe
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Given data of multiple measurement experiments, produce a dataframe with
#information about time experiments and measurements
def Snapshots_to_Dataframe(Experiments_Dict_var, Solutions_Dict_var, time_var, Measure_time_var):
    
    List_df=[]
    for Experiment_Number in Experiments_Dict_var:
        for Measurement in Experiments_Dict_var[Experiment_Number]:
            #Save snapshots of the model to list for Dataframe
            Times_Snapshot=Experiments_Dict_var[Experiment_Number][Measurement]
            counter_time=0
            for key1 in Solutions_Dict_var:
                for key2 in Solutions_Dict_var[key1]:
                    time_experiment=Times_Snapshot[counter_time]
                    index=np.where(time_var==time_experiment)
                    
                    List_df.append([Measure_time_var,Experiment_Number,Measurement
,time_var[index][0],Solutions_Dict_var[key1][key2][index][0],key2,key1])
                    counter_time+=1
                    
    Snapshot_df_var=pd.DataFrame(List_df,columns=["Theoretic Time","Experiment","Measurement","Time","Concentration","Bioagent","Type"])
    return Snapshot_df_var 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#0.6. Solutions to dataframe
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#This function converts a dictionary of solutions of a dynamic system of ODEs
#into a dataframe

def Solutions_to_Dataframe(Solutions_Dict_var,time_var):
    
    List_df=[]
    
    for key1 in Solutions_Dict_var:
        for key2 in Solutions_Dict_var[key1]:
            for snapshot in zip(Solutions_Dict_var[key1][key2],time_var):
                
                List_df.append([snapshot[1],snapshot[0],key2,key1])
                
    Solutions_df_var=pd.DataFrame(List_df,columns=[\
                "Time","Concentration", "Bioagent","Type"])
    
    return Solutions_df_var  
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#0.7. Extract per capita rates from Lotka-Volterra
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def PerCapita_Rates_LV(Concentrations, Time, Parameters, TimeScale='r'):
    r=Parameters['r'];K=Parameters['K'];c=Parameters['c']
    d=Parameters['d'];m=Parameters['m']

    Bioprocesses={'Growth':[], 'Infection':[], 'Burst':[], 'Decay':[]}

    for (Bacteria,Phage) in zip(Concentrations[0],Concentrations[1]):

        #Compute global and per capita rates
        #............................................................
        Growth_t=(r*(Bacteria))
        Normalized_Growth_t=Growth_t/(Bacteria*r)
        
        Infection_t=(d*Bacteria*Phage)
        Normalized_Infection_t=Infection_t/(Bacteria*r)
        
        Burst_t=(c*d*Bacteria*Phage)
        Normalized_Burst_t=Burst_t/(Phage*r)
        
        Decay_t=(m*Phage)
        Normalized_Decay_t=Decay_t/(Phage*r)

        #Argument if the timescale is not only r
        if TimeScale=='m' or TimeScale=='both':
            Normalized_Growth_t=Growth_t/(Bacteria*m)
            Normalized_Infection_t=Infection_t/(Bacteria*m)
            Normalized_Burst_t=Burst_t/(Phage*m)
            Normalized_Decay_t=Decay_t/(Phage*m)
        #............................................................

        #Append per capita rates to dictionary
        #......................................................................
        Bioprocesses['Growth'].append(Normalized_Growth_t)
        Bioprocesses['Infection'].append(Normalized_Infection_t)
        Bioprocesses['Burst'].append(Normalized_Burst_t)
        Bioprocesses['Decay'].append(Normalized_Decay_t)
        #......................................................................

        #Update previous-step concentrations for rates
        #.......................
        Bacteria_0=Bacteria
        Phage_0=Phage
        #.......................

    return Bioprocesses
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#8. Find thresholds in a list
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Threshold_Finder(Vector, Threshold):
    
    Indices_Threshold=np.where(np.sign(Vector[:-1]-Threshold)!=\
    np.sign(Vector[1:] - Threshold) )[0] + 1
    
    return Indices_Threshold
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#9. Find Criticals
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Find_Criticals(df_fun, epsilon_value, dominant):
    
    #BURST
    #...............................................................
    #Critical indices for burst
    Per_Capita_Burst=df_fun['Per_Capita_Burst'].to_numpy()
    Critical_Ind_Burst=Threshold_Finder(Per_Capita_Burst, epsilon_value)
    #Critical concentrations
    CritConc_Burst=[];Critical_Times_Burst=[]
    for index in Critical_Ind_Burst:
        CritConc_Burst.append(df_fun.iloc[index]['Bacterial_Concentration'])
    #...............................................................

    #INFECTION
    #...............................................................
    #Critical indices 
    Per_Capita_Inf=df_fun['Per_Capita_Predation'].to_numpy()
    Critical_Ind_Inf=Threshold_Finder(Per_Capita_Inf, epsilon_value)
    #Critical concentration
    CritConc_Inf=[];Critical_Times_Infection=[]
    for index in Critical_Ind_Inf:
        CritConc_Inf.append(df_fun.iloc[index]['Phage_Concentration'])
    #...............................................................

    #SAVE DATA
    #...............................................................
    Critical_Indices={'Burst':Critical_Ind_Burst,'Predation':Critical_Ind_Inf}
    Critical_Concentrations={'Burst':CritConc_Burst,'Predation':CritConc_Inf}
    #...............................................................
    return Critical_Indices, Critical_Concentrations
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#10. Extract Active processes
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Get_Active_Bioprocesses(Dataframe,epsilon_fun):

    #New dataframe
    Binary_Dataframe = pd.DataFrame(columns =Dataframe.columns.tolist())
    
    for process in Dataframe.columns.tolist():
        Binary_Dataframe[process]=(Dataframe[process] < epsilon_fun).astype(int)
        Binary_Dataframe[process]=(Dataframe[process] >=epsilon_fun).astype(int)

    #Sum columns
    Binary_Dataframe['Total']=Binary_Dataframe.sum(axis=1)

    #Extract information
    Total_Active_Bioprocesses=Binary_Dataframe["Total"].values.tolist()
        
    return Total_Active_Bioprocesses
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#11. Logarithmic sampling of dataframe
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Log_Sampling_Vector_fun(vector,Orders_of_Magnitude,First_Order):
    #Find where the vector crosses the first order of magnitude
    Threshold_First_Order=Threshold_Finder(vector,First_Order)
    Threshold_First_Order=Threshold_First_Order[0]

    #Fill the first order of sampling vector with all points from original vector
    First_Order_Vector=vector[:Threshold_First_Order]
    #All orders of magnitude have the same number of points
    Points_per_order=len(First_Order_Vector)

    #Run over higher order of magnitude and save log vectors
    Log_Sampling_Vectors=[]
    for Order in range(First_Order,Orders_of_Magnitude):
        #Find threshold of Nth order of magnitude
        Threshold_N_Order=Threshold_Finder(vector,10**Order)
        Threshold_N_Order=Threshold_N_Order[0]
        #Get original full vector between orders of magnitude
        N_Order_Vector=vector[Threshold_First_Order:Threshold_N_Order]
        #Sample original full vector with an increasing step
        Sampling_Step=int(0.1*(Points_per_order-1)*(10**(Order-1)))
        N_Order_Sampling=N_Order_Vector[0::Sampling_Step]
        #Save Nth order vector to list of lists 
        Log_Sampling_Vectors.append(N_Order_Sampling)

        #Define starting point for the next order of magnitude
        Threshold_First_Order=Threshold_N_Order

    #Sample vector with the remainings of the last order of magnitude
    #For instance, if your tf is 400 you dont have a full order of magnitude
    Last_Order=vector[Threshold_First_Order:]
    Last_Order_Sampling=Last_Order[0::Sampling_Step*10]

    #Concatenate all vectors of all orders of magnitude
    Log_Sampling_Vector_fun=np.concatenate((\
    First_Order_Vector,Log_Sampling_Vectors[0],Log_Sampling_Vectors[1],Last_Order_Sampling),axis=0)

    return Log_Sampling_Vector_fun
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#10. Relative errors of simplified dynamics
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Rel_Error_Fun(True_Dynamics_Vec,Model_Dynamics_Vec):
    
    Bacteria_True=True_Dynamics_Vec[0];Bacteria_Model=Model_Dynamics_Vec[0]
    Rel_Err_B=[]
    for (BT, BM) in zip(Bacteria_True, Bacteria_Model):
        Relative_Error_B_i=(np.absolute(BT-BM))/BT
        Rel_Err_B.append(Relative_Error_B_i)

    Rel_Err_P=[]
    Phage_True=True_Dynamics_Vec[1];Phage_Model=Model_Dynamics_Vec[1]
    for (PT, PM) in zip(Phage_True, Phage_Model):
        Relative_Error_P_i=(np.absolute(PT-PM))/PT
        Rel_Err_P.append(Relative_Error_P_i)

    Rel_Error=[np.mean((bacteria,phage)) for (bacteria,phage) in zip(Rel_Err_B,Rel_Err_P)]
    #Mean values
    #----------------------------------------------------------------------
    Mean_Rel_Error_Bacteria=np.mean(Rel_Err_B)
    Mean_Rel_Error_Phage=np.mean(Rel_Err_P)
    Mean_Rel_Error=np.mean([Mean_Rel_Error_Phage,Mean_Rel_Error_Bacteria])
    #----------------------------------------------------------------------
    
    return Rel_Error, Rel_Err_B, Rel_Err_P
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#10. Initial parameters, concentrations and final time for dominant timescale
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Initial_Configuration(Dominant_Timescale):
    #Scale independent parameters
    K=1e7;c=150;Volume=1
    if Dominant_Timescale=='r':
        r=0.9;m=2.8e-3;d=3e-8;
        y0=[1e3,1e4]
        time_0=0;time_f=14
        
    elif Dominant_Timescale=='m':
        r=3.7e-5;m=0.1;d=1e-10
        Bcrit=m/(c*d);Pcrit=m/d
        time_0=0.1;time_f=260
        y0=[10*Bcrit,1]
        
    elif Dominant_Timescale=='mr_Equ':
        d=3e-8;m=0.1
        r=m
        Bcrit=r/(c*d);Pcrit=r/d
        y0=[1.2*Bcrit,0.8*Pcrit]
        time_0=0;time_f=200

    elif Dominant_Timescale=='mr_Disequ':
        rmin=0.01;rmax=0.169;
        d=3e-8;m=0.1
        r=m
        Bcrit=r/(c*d);Pcrit=r/d
        y0=[2*Bcrit,0.5*Pcrit]
        time_0=0;time_f=200
        
    elif Dominant_Timescale=='mr_m':
        r=0.05;m=0.1;3e-8
        Bcrit=m/(c*d);Pcrit=m/d
        y0=[5*Bcrit,5*Pcrit]
        time_0=0;time_f=200
        
    elif Dominant_Timescale=='mr_r':
        r=0.5;m=0.1;3e-8

        Bcrit=r/(c*d);Pcrit=r/d
        y0=[2*Bcrit,0.75*Pcrit]
        time_0=0;time_f=200

    Parameters={'r':r,'d':d,'c':c,'m':m,'K':K}

    return Parameters,y0,time_0,time_f
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
