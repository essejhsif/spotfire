from Spotfire.Dxp.Application.Visuals import TablePlot

targetViz = markingViz.As[TablePlot]();

rowSelection = targetViz.Data.DataTableReference.Select(selectStatement);

targetViz.Data.MarkingReference.SetSelection(rowSelection, targetViz.Data.DataTableReference);
