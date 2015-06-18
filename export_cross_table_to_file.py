from System.IO import Path, File, StreamWriter
from Spotfire.Dxp.Application.Visuals import CrossTablePlot
 
#Temp file for storing the cross table data
tempFolder = Path.GetTempPath()
tempFilename = Path.GetTempFileName()

#Export CrossTable data to the temp file
writer = StreamWriter(tempFilename)
vTable.As[CrossTablePlot]().ExportText(writer)

print tempFilename
