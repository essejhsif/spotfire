# Spotfire IronPython Example
# Create a data table and export the contents to an Excel file
#
# Author:   	Jesse Fish 
# Date: 		03/28/2012
# Reference: 		http://stn.spotfire.com

# Import namespaces
from Spotfire.Dxp.Data.Export import *
from Spotfire.Dxp.Application.Visuals import *
from System.IO import *

# Create table plot
visuals = Document.ActivePageReference.Visuals
tablePlot = visuals.AddNew[TablePlot]()

# Associate table plot with default data table
tablePlot.Data.DataTableReference = Document.Data.Tables.DefaultTableReference

# Create DataColumns instance and add the "LE" column to the table 
# Note: will need to do this for every column)
dataColumns = tablePlot.Data.DataTableReference.Columns
tablePlot.TableColumns.Add(dataColumns["LE"])

# Path to the Excel file to write to
fileName = "C:\\Documents and Settings\\jfish\\Desktop\\test1.xls"

# Open the stream, write to it with data from the table, close the 
# stream
stream = File.Open(fileName, FileMode.Create)
tablePlot.ExportData(DataWriterTypeIdentifiers.ExcelXlsDataWriter, stream)
stream.Close()
