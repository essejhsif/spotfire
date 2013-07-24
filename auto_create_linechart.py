# Spotfire IronPython Example
# Automatically create a line chart
#
# Author:   Jesse Fish 
# Date: 	03/28/2012
# Reference: 	http://stn.spotfire.com

from Spotfire.Dxp.Application.Visuals import *

# Create a new line chart
visuals = Document.ActivePageReference.Visuals
visual = visuals.AddNew[LineChart]()

# Set the underlying data table to the default data table in document
visual.Data.DataTableReference = Document.Data.Tables.DefaultTableReference

# Set the x,y axis with respective columns from data set
visual.XAxis.Expression = "[X Axis Column]"
visual.YAxis.Expression = "Sum([Y Axis Column])"
