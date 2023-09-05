import sys

sys.path.append("./src")

from model import Team
from compositor import ImageCompositor, BummyImageCompositor, SuriImageCompositor


if __name__ == '__main__':

    if len(sys.argv) != 3:
        raise Exception('argument count and team is required')

    if sys.argv[0] != "main.py":
        raise Exception('run main.py on generator directory')

    key, count = sys.argv[1].split('=')
    if key != "count":
        raise Exception('first argument key is to be count')

    if not count.isdigit():
        raise Exception('first argument value is to be integer')
    
    key, team = sys.argv[2].split('=')
    if key != "team":
        raise Exception('second argument key is to be team')
    
    compositor: ImageCompositor
    if team == str(Team.bummy):
        compositor = BummyImageCompositor()
    elif team == str(Team.suri):
        compositor = SuriImageCompositor()
    else:
        raise Exception('second argument value is to be bummy or suri')
    
    for i in range(int(count)):
        compositor.generate().save(f'../asset/{i}.png')