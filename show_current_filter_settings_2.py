from Spotfire.Dxp.Application.Visuals import VisualContent
from System import Guid

page = Application.Document.ActivePageReference


#Get the filtering scheme used on this page
filteringSchemeRef = page.FilterPanel.FilteringSchemeReference

filterPanel = page.FilterPanel

#Now set the filtering scheme to that of the originating page
filterPanel.FilteringSchemeReference = filteringSchemeRef

for filteringScheme in Document.FilteringSchemes:
 filteringSelection = filteringScheme.FilteringSelectionReference
 if filteringScheme == filteringSchemeRef: 
  filteringSchemeName = filteringSelection.Name

content="<STRONG>Filtering Scheme:</STRONG> " + filteringSchemeName + "<BR><BR>"

filterPanel.InteractiveSearchPattern = "status:m"
for filters in filterPanel.FiltersMatchingSearchPattern:
 content += filters.FilterReference.ToString() + "<BR>"


ta=vTextArea.As[VisualContent]()
if(ta.HtmlContent is None):
 ta.HtmlContent = " "

if (ta.HtmlContent.find("<SPAN id=fs>")==-1):
  ta.HtmlContent=="<SPAN id=fs>"+ta.HtmlContent
final=ta.HtmlContent.split("<SPAN id=fs>")[0]+"<SPAN id=fs>"+content+"</SPAN>"
ta.HtmlContent=final

filterPanel.InteractiveSearchPattern = ""