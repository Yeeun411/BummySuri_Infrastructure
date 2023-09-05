import random

from model import Object
from PIL import Image

from typing import List



class ObjectSet:
    def __init__(self, type: Object):
        self.type = type
        self.objects: List[Image.Image] = []
        '''
        path = os.path.join(os.getcwd(), str(type))
        if not os.path.isdir(path):
            raise Exception('no such directory: ' + path)

        for file in os.listdir(path):
            if file.endswith('.png'):
                self.objects.append(Image.open(os.path.join(path, file)))

        self.image = self.objects[0]
        '''
    
    
    def __del__(self):
        for file in self.objects:
            file.close()
    
    def getRandom(self) -> Image.Image:
        return self.objects[random.randint(0, len(self.objects) - 1)]


class BackgroundSet(ObjectSet):
    def __init__(self):
        super().__init__(Object.Background)
    def __del__(self):
        super().__del__()

class BodySet(ObjectSet):
    def __init__(self):
        super().__init__(Object.Body)

class ClothingSet(ObjectSet):
    def __init__(self):
        super().__init__(Object.Clothing)

class FaceSet(ObjectSet):
    def __init__(self):
        super().__init__(Object.Face)

class HandSet(ObjectSet):
    def __init__(self):
        super().__init__(Object.Hand)
        
class HatSet(ObjectSet):
    def __init__(self):
        super().__init__(Object.Hat)

class HeadAccessoriesSet(ObjectSet):
    def __init__(self):
        super().__init__(Object.HeadAccessories)
