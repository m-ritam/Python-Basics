import pandas as pd

# Reading the Excel file
Sample_Loan_Data = pd.read_excel("Sample_Loan_Data.xlsx")

print(Sample_Loan_Data) # View the data

#print(Sample_Loan_Data["Exposure"]) # only select a column named ' Exposure'

#print(Sample_Loan_Data[["Exposure","Customer_ID"]]) #  select 2 column

#print(Sample_Loan_Data.loc[3])   #Select the 4th row (index = 3)

#print(Sample_Loan_Data.iloc[3]) #Select the 4th row using iloc

#print(Sample_Loan_Data.loc[2:5]) # Rows 2 to 5 (inclusive)Includes both 2 and 5

#print(Sample_Loan_Data.iloc[2:6]) #Rows 2 to 5 -End value (6) is excluded

#print(Sample_Loan_Data.columns) # print all column names

#print(Sample_Loan_Data.dtypes) #View Data Types of all columnswise

#print(Sample_Loan_Data.shape) #size of data- znumber of rows, columns

#print(Sample_Loan_Data["Product"].unique()) #unique values in producs column

#print(Sample_Loan_Data["Product"].value_counts()) #how many times a value appears in product

#print(Sample_Loan_Data.sort_values(by="Exposure", ascending=False)) #SORTING by Exposure

#print(Sample_Loan_Data[(Sample_Loan_Data["Exposure"] > 7000000) & (Sample_Loan_Data["DPD"] > 30)])

#print(Sample_Loan_Data.groupby("Region")["Exposure"].sum()) #region wise sum of exposure