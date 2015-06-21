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