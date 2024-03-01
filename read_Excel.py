import pandas as pd
import base_page as BasePage



def ReadExcel():

    # Read Excel file and store the dataframe variable in df
    df = pd.read_excel("files\\challenge.xlsx")

    # Use the first column as the key and the next 10 columns as values
    key_column = df.columns[0]
    value_columns = df.columns[1:]

    #Create a dictionary with key-Value pairs.
    
    key_value_dict = df.set_index(key_column)[value_columns].to_dict(orient="index")


    # Extract the value from the first column and convert it to a list

    alistofkeycolumn = df.iloc[:,0].to_list()

    print("List from the first column")
    print(alistofkeycolumn)

    desired_key = "John"

    column_Value1 = BasePage.getDesiredKeyAndColumn(key_value_dict,
        desired_key,
        "Address")
    print(column_Value1)

    return key_value_dict, alistofkeycolumn



