import pandas as pd
import datetime
def check_gas_testing_time_compliance() -> bool:
    # Put your code here
    periodic_gas_read_df = pd.read_csv("periodical_gas_reading.csv", header=None)
    entrant_gas_read_df = pd.read_csv("entrant_gas_reading.csv", header=None)
     
    column1 = entrant_gas_read_df[1]  
    column2 = entrant_gas_read_df[2]      
  
    Compliant = []             
    timestamp_list  = pd.date_range(column1[1] , column2[1] , freq="30min")   
    start_time = timestamp_list[0]                        
    for i in range(1,timestamp_list.size): 
        column0 = periodic_gas_read_df[0]
        Compliant_per = False
        for j in range(1, column0.size): 
            gas_read = pd.Timestamp(column0[j])       
            if (gas_read > start_time and gas_read <= timestamp_list[i]):
                Compliant_per = True          
        start_time = timestamp_list[i]
        Compliant.append(Compliant_per)
    if True in Compliant:
        return True
    return False


if __name__ == "__main__":
    if check_gas_testing_time_compliance():
        print("Compliant")
    else:
        print("Not Compliant")
