from Spotfire.Dxp.Data import DataProperty 
from Spotfire.Dxp.Data import DataType 
from Spotfire.Dxp.Data import DataPropertyClass 

propName  = "myDocumentProperty2" 
attr   = DataProperty.DefaultAttributes 
prop   = DataProperty.CreateCustomPrototype(propName, DataType.String, attr) 

Document.Data.Properties.AddProperty(DataPropertyClass.Document, prop) 

prop.Value  = "myDocumentPropertyValue"
