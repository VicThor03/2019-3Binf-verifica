class Locker:
    def __init__(self, position,material,width ,height,depth,private_key):
        self.position = position
        self.material = material
        self.width  = width 
        self.height = height
        self.depth = depth
        self.private_key = private_key
        self.bulky_width = width > 200
        self.code_is_valid = code_is_valid
        self.is_bulky = ((width*height*depth/1000000)) > 2.0
       


          
