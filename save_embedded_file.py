# Spotfire IronPython Example
# Set a file as embedded and save to a specified path within
# the Spotfire Library.
#
# Author:   	Jesse Fish 
# Date: 		03/28/2012
# Reference: 		http://stn.spotfire.com

# Import namespaces
from Spotfire.Dxp.Application import DocumentSaveSettings
from Spotfire.Dxp.Framework.Library import *

# Set the folder path and file name
folderName = "/Spotfire Test Folder/Reports"
fileName = "Test File"

# Set up the LibraryMangager and ensure that we can 
# access the folder path specified
libraryManager = Document.GetService(LibraryManager)
success, libraryFolder = libraryManager.TryGetItem(folderName, LibraryItemType.Folder)

# Embed the data
Document.Data.SaveSettings.EmbedAllSourceData = 1

# Save the document back to the Library
Application.SaveAs(libraryFolder, fileName, LibraryItemMetadataSettings(), DocumentSaveSettings())
