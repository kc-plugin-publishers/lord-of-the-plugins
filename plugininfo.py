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
import xml.etree.ElementTree as ET
import xml.etree.ElementTree
class Plugininfo:
    def __init__(self, infoFile):
        self.pluginInfoFile = infoFile
        tree = ET.parse(infoFile)
        self.root = tree.getroot()
        #ET.dump(tree)
        self.versionElement = self.findElement("version") #there can be many, for now we select the first one
        self.name = self.findText("name")
        #self.shortDescription = self.findText("shortDescription")
        
        # use the first "version" element
        self.zipFileSource = self.findText("zipFileSource", root=self.versionElement)
        self.fileSources = self.findallTexts("source", root=self.versionElement)
        print("init plugininfo")
        print("name:"+self.name)
        print("zip:"+self.zipFileSource)
        

    def getName(self):
        return self.name
    
    def getSourceFiles(self):
        return self.fileSources
    
    def getFiles(self):
        sourceDestPairs = []
        elements = self.findallElements("file", self.versionElement)
        for f in elements:
            sourceDestPairs.append( (f.find("source").text, f.find("destination").text) )
        return sourceDestPairs
        
    def getZipFile(self):
        return self.zipFileSource
    
    def findText(self, elementName, root=None):
        if root is None: root = self.root
        return self.findElement(elementName, root).text.strip()

    def findElement(self, elementName, root=None):
        if root is None: root = self.root
        return root.find(elementName)

    def findallElements(self, elementName, root=None):
        if root is None: root = self.root
        elements = []
        for elem in root.iter(elementName):
            elements.append(elem)
        return elements

    def findallTexts(self, elementName, root=None):
        if root is None: root = self.root
        tagTexts = []
        for elem in root.iter(elementName):
            tagTexts.append(elem.text.strip())
        return tagTexts
