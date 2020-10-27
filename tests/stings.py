
#Here are the instructions to install Drivers
#1. After the download is completed go to where you saved the folder.
#(By default everything you download from the Internet is saved to the Downloads folder)
#2. Right click on the folder and choose ''Extract All'' and then choose ''Extract'' again.
#4. Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below:
#*setup application
#*Asussetup
#*pnpinstal64
#*pnputil
#*Igxpin
#5. Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the set up.
#•	Find how many times the word Drivers is used
#•	How long in your Strint
#•	Replace Extract with EXTRACT
#•	Replace setup or Setup with SETUP
#•	Find  ‘4’

#Here are the instructions to install Drivers
#1. After the download is completed go to where you saved the folder.
#(By default everything you download from the Internet is saved to the Down 
String="Here are the instructions to install Drivers 1. After the download is completed go to where you saved the folder.(By default everything you download from the Internet is saved to the Downloads folder)Right click on the folder and choose ''Extract All'' and then choose ''Extract'' again.4. Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below:*setup application *Asussetup *pnpinstal64 *pnputil *Igxpin"


print( )
print(String.replace('Extract','EXTRACT'))
print( )
print(String.replace('Setup','SETUP'))
print( )
print(String.find(4))
print( )
