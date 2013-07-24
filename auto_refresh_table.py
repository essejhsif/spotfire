# Spotfire IronPython Example
# Automatically refresh a data table
#
# Author:   Jesse Fish 
# Date: 	03/28/2012
# Reference: 	http://stn.spotfire.com

# Import needed namespaces
from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Data.Import import *

# Create Data Manager object
dataManager = Document.Data

# Point to a Data Table (e.g. 'Data Table Name') and refresh it
dataTableName = dataManager.Tables["Data Table Name"]
dataTableName.Refresh()
