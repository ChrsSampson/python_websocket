import os
import uuid
import json

class Storage:
    def __init__(self, dir, entity):
        self.path = dir
        self.entity = entity
        self.bucket = {}
        # init file
        self.writeFile()

    def createId(self):
        return uuid.uuid4()

    def hasStorage(self, dir):
        exists = os.path.exists(dir)
        return exists

    def serialize(self, data):
        return json.dumps(data)

    def writeFile(self):
        cdir = os.getcwd()
        checkDir = f'{self.path}/{self.entity}.json'
        hasStorage = self.hasStorage(checkDir)
        if(hasStorage != True):
            # file needs to be created - write blank file
            with open(checkDir, 'w') as fp:
                str = self.serialize([])
                fp.write(str)
        else :
            with open(checkDir, 'w') as fp:
                str = self.serialize(self.bucket)
                fp.write(str)

    def readFile(self):
        pass

    def add(self, value):
        pass

    def remove(self, id):
        pass

    def getAll(self):
        pass