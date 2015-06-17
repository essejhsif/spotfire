import clr
clr.AddReference ( "System" )
import System
from System import Uri
import Spotfire.Dxp.Application

for panel in Application.Document.ActivePageReference.Panels:
 if panel.Title == "Collaboration":
  panel.Url = Uri ( "http://www.google.com" )