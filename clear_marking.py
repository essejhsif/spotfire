from Spotfire.Dxp.Data import DataManager 
from Spotfire.Dxp.Data import IndexSet 
from Spotfire.Dxp.Data import RowSelection 

marking=Application.GetService[DataManager]().Markings[markingName]
selectRows = IndexSet(dataTable.RowCount, False)
marking.SetSelection(RowSelection(selectRows),dataTable)
