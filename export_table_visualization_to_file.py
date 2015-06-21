from System.IO import Path, File, StreamWriter
from Spotfire.Dxp.Application.Visuals import TablePlot
 
#Temp file for storing the table data
tempFolder = Path.GetTempPath()
tempFilename = Path.GetTempFileName()

#Export table data to the temp file
writer = StreamWriter(tempFilename)
vTable.As[TablePlot]().ExportText(writer)

print tempFilename
