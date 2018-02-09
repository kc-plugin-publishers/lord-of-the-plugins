from backend.downloader import Downloader                       #downloads files behind urls
from backend.zipfilehandler import ZipFileHandler               #encapsulates a downloaded .zip file
from backend.plugininfo import Plugininfo                       #encapsulates a .plugininfo file
from backend.localfilehandler import LocalFileHandler           #saves/removes local files
from backend.confighandler import ConfigHandler                 #reads, writes and stores configuration
from backend.plugininfocollection import PlugininfoCollection   #keeps all plugininfos from a repository


class LordOfThePluginsCli():
    """The command line interface main class for the Plugin Manager."""
    def __init__(self, configFileName):
        #def defaults(self):
        
        #------USE THE CONFIG FILE TO CONFIGURE PLUGIN LIST URL AND TO-BE-INSTALLED PLUGIN--------
        if (configFileName):
            self.configFileName = configFileName
        else:
            self.configFileName = "lord_of_the_plugins.ini" # FILE IN CWD OR GIVE THE WHOLE PATH
            import os
            import sys
            cwd = os.path.dirname(os.path.abspath(__file__))
            self.configFileName = cwd + "/lord_of_the_plugins.ini"
            
        
        self.masterListUrl = "https://github.com/kc-plugin-publishers/kc-plugins-master-list/archive/master.zip" #can be overriden in ini conf file, see above
        self.pluginsDir = "~/.test_plugins_dir" # see above
        self.pluginToInstall = "SimplePluginExample" # see above
        
    def Run(self):
        print("Running LordOfThePlugins")
        
        self.initConfig()
        
        downloader = Downloader()
        masterListZip = downloader.retrieve(self.config.masterListUrl)
        print(masterListZip)
        self.handleMasterList(masterListZip)
        
    def initConfig(self):
        self.config = ConfigHandler(self.configFileName)
        self.masterListUrl = self.config.masterListUrl
        self.pluginsDir = self.config.pluginsDir
        self.pluginToInstall = self.config.pluginToInstall
        
    #read and handle the zip file which has the plugininfo files
    def handleMasterList(self, masterListZip):   
        zipFileHandler = ZipFileHandler(masterListZip)
        infoCollection = PlugininfoCollection(zipFileHandler)
        infoFilesList = infoCollection.getInfoFileNames()
        
        for infoFileName in infoFilesList:
            print(infoFileName)
            infoFile = zipFileHandler.getFile(infoFileName)
            #print(infoFile)
            pluginInfo = Plugininfo(infoFile)
            print(pluginInfo.getName())
            if pluginInfo.getName() == self.pluginToInstall:
                print("Found the plugin to install!")
                self.installPluginZip(pluginInfo)

    #(re)install plugin if it's found in the master list
    def installPluginZip(self, pluginInfo):
        downloader = Downloader()
        pluginPackageZip = downloader.retrieve(pluginInfo.getZipFile())
        zipFileHandler = ZipFileHandler(pluginPackageZip)
        
        sourceDestList = pluginInfo.getFiles()
        print(sourceDestList)
        fileHandler = LocalFileHandler(self.pluginsDir)
        fileHandler.uninstallPlugin(pluginInfo)
        
        for sourceFileName, destPath in sourceDestList:
            print(sourceFileName + destPath)
            installableFile = zipFileHandler.getFile(sourceFileName)
            fileHandler.installFile(destPath, installableFile)
            
            
if __name__ == "__main__":
    cli = LordOfThePluginsCli(None)
    cli.Run()
