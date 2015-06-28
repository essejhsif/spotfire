from Spotfire.Dxp.Data import DataValueCursor

myLatCursor = DataValueCursor.CreateFormatted(Document.Data.Tables["mydatatable"].Columns["latitude"])
myLongCursor = DataValueCursor.CreateFormatted(Document.Data.Tables["mydatatable"].Columns["longitude"])

markedRows = Document.Data.Markings["Marking"].GetSelection(Document.Data.Tables["mydatatable"]).AsIndexSet()
for row in Document.Data.Tables["mydatatable"].GetRows(markedRows, myLatCursor):
  Document.Properties['refLat'] = myLatCursor.CurrentValue

for row in Document.Data.Tables["mydatatable"].GetRows(markedRows, myLongCursor):
  Document.Properties['refLong'] = myLongCursor.CurrentValue
