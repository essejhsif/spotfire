from Spotfire.Dxp.Application.Visuals import VisualContent

tbl = currentTableVisualization.As[VisualContent]()
newtbl = Document.Data.Tables.Item[newDataTableName]
tbl.Data.DataTableReference=newtbl
tbl.AutoConfigure()
tbl.ApplyUserPreferences()
