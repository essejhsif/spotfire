from Spotfire.Dxp.Application.Visuals import VisualContent
from System import Guid

page = Application.Document.ActivePageReference

#Get the filtering scheme used on this page
filteringSchemeRef = page.FilterPanel.FilteringSchemeReference

#Get the name of the filtering scheme on the active page
for filteringScheme in Document.FilteringSchemes:
 filteringSelection = filteringScheme.FilteringSelectionReference
 if filteringScheme == filteringSchemeRef: 
  filteringSchemeName = filteringSelection.Name

content="<STRONG>Filtering Scheme:</STRONG> " + filteringSchemeName

filterPanel = page.FilterPanel
filterPanel.InteractiveSearchPattern = "status:m"

for filters in filterPanel.FiltersMatchingSearchPattern:
 print filters.FilterReference.ToString()

for tableGroup in filterPanel.TableGroups :
 print tableGroup.ToString()
 tableGroup.Expanded=True
 for filterGroup in tableGroup.SubGroups :
  print filterGroup.ToString()
  print filterGroup.Expanded
  filterGroup.Visible=False
  if (filterGroup.Expanded == False):
      filterGroup.Expanded = True
  else:
   filterGroup.Expanded = False

for tableGroup in filterPanel.TableGroups:
 isMod=0
 str="<p>"
 if filterPanel.TableGroups.Count > 1:
  str+="<b>"+tableGroup.FilterCollectionReference.DataTableReference.Name+":</b><br>"
 for fh in tableGroup.FilterHandles:
  if fh.FilterReference.Modified:
   isMod=-1
   str+=fh.FilterReference.ToString()
   str+="<br>"
 for subGroup in tableGroup.SubGroups:
  for fh in subGroup.FilterHandles:
   if fh.FilterReference.Modified:
    isMod=-1
    str+=fh.FilterReference.ToString()
    str+="<br>"
 str+="</p>"
 if isMod==-1:
  content+=str  

ta=vTextArea.As[VisualContent]()
if(ta.HtmlContent is None):
 ta.HtmlContent = " "

if (ta.HtmlContent.find("<SPAN id=fs>")==-1):
  ta.HtmlContent=="<SPAN id=fs>"+ta.HtmlContent
final=ta.HtmlContent.split("<SPAN id=fs>")[0]+"<SPAN id=fs>"+content+"</SPAN>"
ta.HtmlContent=final

#Reset filter panel search and navigate to the Filter Settings Page
filterPanel.InteractiveSearchPattern = ""