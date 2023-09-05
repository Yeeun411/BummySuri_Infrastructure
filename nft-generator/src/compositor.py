import os

from model import Team
from objectset import ObjectSet, BackgroundSet, BodySet, ClothingSet, FaceSet, HandSet, HatSet, HeadAccessoriesSet
from PIL import Image
from functools import reduce
from typing import List




class ImageCompositor:
    def __init__(self, team: Team):
        self.team = team
        dir = os.path.join(os.getcwd(), str(team))
        if not os.path.isdir(dir):
            raise Exception('no such directory: ' + dir)        
        os.chdir(dir)
        
        self.objectList: List[ObjectSet] = []
    
    def generate(self):
        itemList: List[Image.Image] = [obj.getRandom() for obj in self.objectList]
        return reduce(Image.alpha_composite, itemList)



class BummyImageCompositor(ImageCompositor):
    def __init__(self):
        super().__init__(Team.bummy)
                
        self.objectList: list[ObjectSet] = [
            BackgroundSet(),
            BodySet(),
            ClothingSet(),
            FaceSet(),
            HandSet(),
            HatSet(),
            HeadAccessoriesSet()
        ]
        
class SuriImageCompositor(ImageCompositor):
    def __init__(self):
        super().__init__(Team.suri)

        self.objectList: list[ObjectSet] = [
            BackgroundSet(),
            BodySet(),
            ClothingSet(),
            FaceSet(),
            HandSet(),
            HatSet()
        ]
