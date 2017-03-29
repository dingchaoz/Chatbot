import pandas as pd 

cols = pd.read_csv('FDW_Columns_201703150802.csv')
fdwFilter = [x.startswith('FDW') for x in cols.TABSCHEMA]
fdwCols = cols[fdwFilter]

#len(set(fdwCols.TABSCHEMA)): 354, there are 354 unique fdw schemas
#len(set(fdwCols.TABNAME)): 13246, there are 13246 unique tables
#fdwCols.shape: 563072, there are + 500k columns

##### Approach is to show all unique fdw tables and schemas in one question
##### When asked will all columns needed or not, show the specific selected tables' columns
##### using python script

tables = pd.read_csv('FDW_Tables_201703141418.csv')


## Rename col names
colNames = tables.columns
colNames = colNames[1:]
colNames.insert(0,'TABSCHEMA')
tables.columns = colNames

## Select only schema and tables names
tables = tables.iloc[:,:2]
fdwFilter = [x.startswith('FDW') for x in tables.TABSCHEMA]
tables = tables[fdwFilter]
tables.to_csv('FDW_TABLE_SCHEMA_NAMES.csv',index = None)
