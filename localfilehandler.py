#
# Copyright (c) 2017 Eeli Kaikkonen <email>
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
import os

class LocalFileHandler:

    def __init__(self, pluginsDir):
        self.pluginsDir = os.path.expanduser(pluginsDir)
        print("Plugins directory: "+self.pluginsDir)
        

    def uninstallPlugin(self, plugininfo):
        print("uninstall TBD")
    
    def installFile(self, destPath, fileObject):
        wholeDestPath = self.pluginsDir + "/" + destPath
        print("Saving file to "+ wholeDestPath)
        destDir = os.path.dirname(wholeDestPath)
        print(destDir)
        print("exists? "+ str(os.path.exists(destDir)))
        if not os.path.exists(destDir):
            os.makedirs(destDir)
        
        outf = open(wholeDestPath, "w")
        outf.write(fileObject.read())
        
