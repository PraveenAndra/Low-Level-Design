from abc import ABC, abstractmethod
class FileSystem(ABC):
    @abstractmethod
    def getPath(self):
        pass
    @abstractmethod
    def getSize(self):
        pass

class File(FileSystem):
    def __init__(self,name, size):
        self.name = name
        self.size = size
    def getPath(self):
        return "/"+self.name
    def getSize(self):
        return self.size
class Folder(FileSystem):
    def __init__(self,name,size=0):
        self.name = name
        self.size = size
        self.children = set()
    def getSize(self):
        return self.size
    def getPath(self):
        return "/"+self.name
    def addFile(self,file: FileSystem):
        self.children.add(file)
        self.size += file.getSize()

file1 = File("file1", 10)
file2 = File("file2", 20)
file3 = File("file3", 30)
folder1 = Folder("folder1")
folder1.addFile(file1)
folder1.addFile(file2)
folder2 = Folder("folder2")
folder2.addFile(file3)
print(folder1.getSize())
print(folder2.getSize())
print(file1.getPath())