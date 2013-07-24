# Spotfire IronPython Example
# Automatically create a bar chart Example
#
# Author: Jesse Fish 
# Date: 03/28/2012
# Reference: http://stn.spotfire.com

from Spotfire.Dxp.Application.Visuals import *

# Create a new bar chart
visuals = Document.ActivePageReference.Visuals
visual = visuals.AddNew[BarChart]()

# Set the underlying data table to the default data table in document
visual.Data.DataTableReference = Document.Data.Tables.DefaultTableReference

# Set the x,y axis with respective columns from dataset
visual.YAxis.Expression = "Sum([Y Axis Column])"
visual.XAxis.Expression = "[X Axis Column]"

# Set the color axis with the Color Axis Column from the dataset
visual.ColorAxis.Expression = "[Color Axis Column]"
