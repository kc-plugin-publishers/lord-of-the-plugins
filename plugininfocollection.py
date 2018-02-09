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

from zipfilehandler import ZipFileHandler

class PlugininfoCollection:
    """Interface to all plugininfo files in one repository.
    Is used to return lists, trees etc.
    """
    infoFileNames = []
    
    def __init__(self, zipFileHandler):
        """Takes a zip file which is a plugininfo repository."""
        self.zipFileHandler = zipFileHandler
        
        
    def getInfoFileNames(self):
        fileList = []
        allFiles = self.zipFileHandler.getFileNameList()
        for fname in allFiles:
            print(fname)
            if fname.endswith(".plugininfo"):
                fileList.append(fname)
        return fileList
    
    def getInfoTree(self):
        # TODO
        return "Info tree not implemented yet"
