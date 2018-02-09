#
# Copyright (c) 2018 <copyright holder> <email>
# 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#

from os.path import expanduser
from os.path import abspath
import ConfigParser

class ConfigHandler:
    masterListUrl = ""
    pluginsDir = ""
    pluginToInstall = ""
    
    def __init__(self, configFileName):
        print("Read ini file: "+abspath(configFileName))
        self.config = ConfigParser.RawConfigParser()
        config = self.config
        config.read(configFileName)
        if config.has_option("default","masterListUrl") and config.get("default", "masterListUrl"):
            self.masterListUrl = config.get("default","masterListUrl")
        
        self.pluginsDir = expanduser("~") + "/.test_plugins_dir"
        if config.has_option("default","pluginsDir") and config.get("default", "pluginsDir"):
            self.pluginsDir = config.get("default","pluginsDir")
            
        if config.has_option("default", "pluginToInstall") and config.get("default", "pluginToInstall"):
            self.pluginToInstall = config.get("default", "pluginToInstall")
            
        print("config: master url: " + self.masterListUrl)
        print("config: local plugins dir: " + self.pluginsDir)
