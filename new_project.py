import math

class Point :
   def __init__(self,x=0,y=0) :
    self.ptx=x 
    self.pty=y 

   def gitpt(self):
    print(f"the point x ={self.ptx},the point y={self.pty}")

   def dis_to_origin(self):

    dist=math.sqrt(int(self.ptx)**2+int(self.pty)**2) #dist to get the sqear root for the sum of sqear to the points

    forma= "{:.2f}".format(dist) #cuz the method sqrt return a folot num so , this line to print just 2 decimal numbers
    
    print(f"the distance to origin is {forma}")

   def reflect(self,o):
    o =str(o).lower()
    if o =="x":
        self.ptx=self.ptx*-1
    elif o=="y":
        self.pty=self.pty*-1
    else :
        print("pleas inter x for reflect on X axis , and Y for reflect on Y axis")
    print((self.ptx,self.pty))



point_one=Point(x=2,y=4)

# point_one.dis_to_origin()

point_one.reflect("y")
