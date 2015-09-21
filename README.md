# Spotfire IronPython Scripts

## Overview 

According to the Spotfire Technology Network, Spotfire's IronPython scripts are "modern, expressive and has access to the full public Spotfire automation API. Scripts are executed from an action control in the HTML text area. This also enables the use of scripting in the TIBCO Spotfire Web Player. 

To create an analyses containing IronPython scripts, the analyst needs the Author Scripts license function. 

Scripts in analysis files that are shared via the library by licensed script authors are considered as trusted. For security reasons you should always examine and approve a script that is not listed as trusted before executing it.

## Examples

This repository holds IronPython scripts for use within the Spotfire application. The following examples are available as individual modules within this repository as well. 

For more information on how to run IronPython scripts within the Spotfire client/Web Player, please see the Spotfire Technology Network: http://stn.spotfire.com

Please note that these examples can be used stand-alone or collectively within an analysis file. I am a former professional services employee of Spotfire/TIBCO and if you have any other questions about Spotfire,  IronPython scripts or custom integrations with the Spotfire suite, please contact me: jessefish [at] gmail [dot] com 

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

```
from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Data.Import import *

#### Create Data Manager object
dataManager = Document.Data

#### Point to a Data Table (e.g. 'Data Table Name') and refresh it
dataTableName = dataManager.Tables["Data Table Name"]
dataTableName.Refresh()
```

### Change Underling Datatable for Visualization

```
from Spotfire.Dxp.Application.Visuals import VisualContent

tbl = currentTableVisualization.As[VisualContent]()
newtbl = Document.Data.Tables.Item[newDataTableName]
tbl.Data.DataTableReference=newtbl
tbl.AutoConfigure()
tbl.ApplyUserPreferences()
```

### Change Active Page

```
Document.ActivePageReference = Document.Pages[2]
```

### Change URL Collaboration Panel

```
import clr
clr.AddReference ( "System" )
import System
from System import Uri
import Spotfire.Dxp.Application

for panel in Application.Document.ActivePageReference.Panels:
 if panel.Title == "Collaboration":
  panel.Url = Uri ( "http://www.google.com" )
```

### Clear All Markings 

```
from Spotfire.Dxp.Data import DataManager 
from Spotfire.Dxp.Data import IndexSet 
from Spotfire.Dxp.Data import RowSelection 

marking=Application.GetService[DataManager]().Markings[markingName]
selectRows = IndexSet(dataTable.RowCount, False)
marking.SetSelection(RowSelection(selectRows),dataTable)
```

### Clear Document Property

```
from Spotfire.Dxp.Data import DataProperty 
from Spotfire.Dxp.Data import DataType 
from Spotfire.Dxp.Data import DataPropertyClass 

propName  = "myDocumentProperty2" 
attr   = DataProperty.DefaultAttributes 
prop   = DataProperty.CreateCustomPrototype(propName, DataType.String, attr) 

Document.Data.Properties.AddProperty(DataPropertyClass.Document, prop) 

prop.Value  = "myDocumentPropertyValue"
```

### Get Current Username

```
from System.Threading import Thread 
print Thread.CurrentPrincipal.Identity.Name 
```

### Loop Through Pages 
```
for page in Application.Document.Pages:
  print page.Title
````

###Mark Rows
```
from Spotfire.Dxp.Application.Visuals import TablePlot

targetViz = markingViz.As[TablePlot]();

rowSelection = targetViz.Data.DataTableReference.Select(selectStatement);

targetViz.Data.MarkingReference.SetSelection(rowSelection, targetViz.Data.DataTableReference);
```

###Perform Operations on Columns in a Graphical Table
```
from Spotfire.Dxp.Application.Visuals.Miniatures import GraphicalTable
from Spotfire.Dxp.Application.Visuals import VisualTypeIdentifiers

for col in gtable.As[GraphicalTable]().Columns: 
 #Calculated Value Columns
 if col.Visualization.TypeId == VisualTypeIdentifiers.CalculatedValueMiniatureVisualization:
  try:
   vExp = col.Visualization.ValueAxis.Expression
  except:
   0

 #Icon Columns
 if col.Visualization.TypeId == VisualTypeIdentifiers.IconMiniatureVisualization:
  try:   
   vExp = col.Visualization.IconAxis.Expression
  except:
   0

 #Sparkline Columns
 if col.Visualization.TypeId == VisualTypeIdentifiers.SparklineMiniatureVisualization:
  try:   
   vExp = col.Visualization.YAxis.Expression
  except:
   0

 #Bullet Graph Columns
 if col.Visualization.TypeId == VisualTypeIdentifiers.BulletGraphMiniatureVisualization:
  try:   
   vExp = col.Visualization.ValueAxis.Expression
  except:
   0

 try:
  col.Title = vExp
 except:
  0
```


