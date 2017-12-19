# Every file in this package is imported so that no file is read runtime.
# This should make on-the-fly deleting/installing this package with itself possible.
from downloader import Downloader             #downloads files behind urls
from zipfilehandler import ZipFileHandler     #encapsulates a downloaded .zip file
from plugininfo import Plugininfo             #encapsulates a .plugininfo file
from localfilehandler import LocalFileHandler #saves/removes local files

class LordOfThePluginsAction():
    def __init__(self):
        #def defaults(self):
        self.name = "LordOfThePlugins"
        self.category = "Metaplugin"
        self.description = "A plugin manager which installs, updates and removes plugins"
        
        #------USE THE CONFIG FILE TO CONFIGURE PLUGIN LIST URL AND TO-BE-INSTALLED PLUGIN--------
        self.configFileName = "lord_of_the_plugins.ini" # FILE IN CWD OR GIVE THE WHOLE PATH
        
        self.masterListUrl = "https://github.com/kc-plugin-publishers/kc-plugins-master-list/archive/master.zip" #can be overriden in ini conf file, see above
        self.pluginsDir = "~/.test_plugins_dir" # see above
        self.pluginToInstall = "SimplePluginExample" # see above
        
    def Run(self):
        print("Running LordOfThePlugins")
        
        self.initConfig()
        
        downloader = Downloader()
        masterListZip = downloader.retrieve(self.masterListUrl)
        print(masterListZip)
        self.handleMasterList(masterListZip)
        
    def initConfig(self):
        from os.path import expanduser
        from os.path import abspath
        import ConfigParser
        
        configFile = self.configFileName
        print("Read ini file: "+abspath(configFile))
        config = ConfigParser.RawConfigParser()
        config.read(configFile)
        if config.has_option("default","masterListUrl") and config.get("default", "masterListUrl"):
            self.masterListUrl = config.get("default","masterListUrl")
        
        self.pluginsDir = expanduser("~") + "/.test_plugins_dir"
        if config.has_option("default","pluginsDir") and config.get("default", "pluginsDir"):
            self.pluginsDir = config.get("default","pluginsDir")
            
        if config.has_option("default", "pluginToInstall") and config.get("default", "pluginToInstall"):
            self.pluginToInstall = config.get("default", "pluginToInstall")
            
        print(self.masterListUrl)
        print(self.pluginsDir)
        
    #read and handle the zip file which has the plugininfo files
    def handleMasterList(self, masterListZip):   
        zipFileHandler = ZipFileHandler(masterListZip)
        infoFilesList = zipFileHandler.getPlugininfoFileList()
        
        #return
        
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
    action = LordOfThePluginsAction()
    action.Run()
