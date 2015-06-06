from Spotfire.Dxp.Data import DataColumn, TagsColumn
from Spotfire.Dxp.Data import DataPropertyClass, DataType, DataValueCursor, IDataColumn, IndexSet
from Spotfire.Dxp.Data import RowSelection 
  
# Tag the marked rows
markedRowSelection = Document.ActiveMarkingSelectionReference.GetSelection(Document.ActiveDataTableReference)
table = Document.ActiveDataTableReference
myTagColumn = table.Columns.Item["Decision"].As[TagsColumn]()

selectRows = IndexSet(table.RowCount, True)
myTagColumn.Tag("No", RowSelection(selectRows))
myTagColumn.Tag("Yes", markedRowSelection )
