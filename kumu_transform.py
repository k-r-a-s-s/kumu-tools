import pandas as pd
"""
Kevin Rassool
July 2023

This script takes the Kumu file and transforms it into a merged format, where each element has a list of connections.
This can be useful for an import in to greenrope, airtable, or for a more general analysis.
Currently, this is a proof of concept for a one way transformation, but could be very easily extended to be a two way transformation by reversing.
I do not have access to greenrope, nor any information on how the data (CSVs) is stored in greenrope
...so this is a proof of concept, with simple tweaks required to push/pull the correct fields for greenrope.
"""

### Options ###
file_path = 'kumu-krass-australia-policy.xlsx'

# airtable/other spreadhsheet export options
airtable_output = True # if false, will keep as lists, if true, will convert to strings for airtable import
comma_replace_string = '-' # if airtable_output is true, this string will replace any commas in the data, as this will cause issues with airtable import

### End Options ###


### Start Script ###
all_sheets = pd.read_excel(file_path, sheet_name=None)

elements_sheet_name = "Elements"
connections_sheet_name = "Connections"

df_ele = pd.read_excel(file_path, sheet_name=elements_sheet_name, skiprows=0)
df_con = pd.read_excel(file_path, sheet_name=connections_sheet_name, skiprows=0)

if airtable_output:
    # remove any commas in the elements "label" column, as this will cause issues with airtable import
    # remove any commas in the connections "to and "from" column, as this will cause issues with airtable import
    df_ele['Label'] = df_ele['Label'].apply(lambda x: x.replace(',', comma_replace_string))
    df_con['From'] = df_con['From'].apply(lambda x: x.replace(',', comma_replace_string))
    df_con['To'] = df_con['To'].apply(lambda x: x.replace(',', comma_replace_string))

# flatten the connections sheet, so that each row "From" is a "labal", and they are not repeated.
# then take the strings in the "To" column and combine them into a list, and add that list to the row.
df_con_flat = df_con.groupby('From').agg({'To': lambda x: list(x)}).reset_index()

# merge the elements and connections sheets, so that each element has a list of connections, don't keep the "From" column
df_merged = pd.merge(df_ele, df_con_flat, left_on='Label', right_on='From', how='left')
df_merged = df_merged.drop(columns=['From'])

# rename the columns to be more descriptive
df_merged = df_merged.rename(columns={'Label': 'Name', 'To': 'Connections'})

if airtable_output:
    # convert the list of connections to a string, for airtable import
    # ignore the NaN values
    df_merged['Connections'] = df_merged['Connections'].apply(lambda x: ', '.join(x) if type(x) == list else x)

# save the merged file to csv
df_merged.to_csv('kumu-krass-australia-policy-merged.csv', index=False)
