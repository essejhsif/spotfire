# Spotfire IronPython Scripts

## Overview 
According to the Spotfire Technology Network, Spotfire's IronPython scripts are "modern, expressive and has access to the full public Spotfire automation API. Scripts are executed from an action control in the HTML text area. This also enables the use of scripting in the TIBCO Spotfire Web Player.To create an analyses containing IronPython scripts, the analyst needs the Author Scripts license function. Scripts in analysis files that are shared via the library by licensed script authors are considered as trusted. For security reasons you should always examine and approve a script that is not listed as trusted before executing it.

## Examples

This repository holds IronPython scripts for use within the Spotfire application. For more information on how to run IronPython scripts within the Spotfire application, please see the Spotfire Technology Network: http://stn.spotfire.com

### Auto Create Barchart

```
from Spotfire.Dxp.Application.Visuals import *

##### Create a new bar chart
visuals = Document.ActivePageReference.Visuals
visual = visuals.AddNew[BarChart]()

##### Set the underlying data table to the default data table in document
visual.Data.DataTableReference = Document.Data.Tables.DefaultTableReference

##### Set the x,y axis with respective columns from dataset
visual.YAxis.Expression = "Sum([Y Axis Column])"
visual.XAxis.Expression = "[X Axis Column]"

##### Set the color axis with the Color Axis Column from the dataset
visual.ColorAxis.Expression = "[Color Axis Column]"
```

### Auto Create Linechart

```
from Spotfire.Dxp.Application.Visuals import *

##### Create a new line chart
visuals = Document.ActivePageReference.Visuals
visual = visuals.AddNew[LineChart]()

##### Set the underlying data table to the default data table in document
visual.Data.DataTableReference = Document.Data.Tables.DefaultTableReference

##### Set the x,y axis with respective columns from data set
visual.XAxis.Expression = "[X Axis Column]"
visual.YAxis.Expression = "Sum([Y Axis Column])"
```

### Auto Refresh Datatable

### Change Underling Datatable for Visualization

