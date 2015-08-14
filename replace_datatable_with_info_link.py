from System import Array,Guid,String,Object
from Spotfire.Dxp.Data.Import import InformationLinkDataSource, InformationLinkParameter

ilDataSource = InformationLinkDataSource(myGUID)

Document.Data.Tables[myDataTable].ReplaceData(ilDataSource)

