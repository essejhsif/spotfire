from Spotfire.Dxp.Application.Visuals import TablePlot, TablePlotColumnSortMode

toTableSort = vTable.As[TablePlot]();
todataColumn = toTableSort.Data.DataTableReference.Columns[sortColumn];
toTableSort.SortInfos.Clear();
toTableSort.SortInfos.Add(todataColumn, TablePlotColumnSortMode.Ascending);
