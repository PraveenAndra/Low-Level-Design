from abc import ABC,abstractmethod

class FileSystem(ABC):
    @abstractmethod
    def getPath(self):
        pass
    @abstractmethod
    def getSize(self):
        pass
    @abstractmethod
    def getExtension(self):
        pass

class File(FileSystem):
    def __init__(self,name,size=0,extension=None):
        self.name=name
        self.size=size
        self.extension=extension
    def getPath(self):
        return "/"+self.name
    def getSize(self):
        return self.size
    def getExtension(self):
        return self.extension
class Folder(FileSystem):
    def __init__(self,name,size=0):
        self.name=name
        self.size=size
        self.extension=None
        self.children=[]
    def getPath(self):
        return "/"+self.name
    def getSize(self):
        return self.size
    def getExtension(self):
        return self.extension
    def addChild(self,child: FileSystem):
        self.children.append(child)
        self.size += child.getSize()
class Criteria(ABC):
    @abstractmethod
    def getMatch(self, component: FileSystem):
        pass
class SizeCriteria(Criteria):
    def __init__(self,minSize):
        self.minSize=minSize
    def getMatch(self, component: FileSystem):
        return component.getSize() > self.minSize

class ExtensionCriteria(Criteria):
    def __init__(self,extension):
        self.extension=extension
    def getMatch(self, component: FileSystem):
        return component.getExtension()==self.extension

class Library:
    def __init__(self,root):
        self.root=root

    def find_files(self,criteria):
        result=[]
        self._search(criteria,result,self.root)
        return result
    def _search(self,criteria: Criteria,result,curr: FileSystem):
        if isinstance(curr,Folder):
            for child in curr.children:
                self._search(criteria,result,child)
        else:
            if all(criterion.getMatch(curr) for criterion in criteria):
                result.append(curr.name)

file1 = File("file1",12,"xml")
file2 = File("file2",7,"pdf")
file3 = File("file3",8,"txt")
folder1 = Folder("folder1")
folder1.addChild(file1)
folder1.addChild(file2)
folder2 = Folder("folder2")
folder2.addChild(file3)
root = Folder("root")
root.addChild(folder1)
library = Library(root)
sizeCriteria = SizeCriteria(6)
xmlCriteria = ExtensionCriteria("xml")
print(library.find_files([sizeCriteria,xmlCriteria]))



