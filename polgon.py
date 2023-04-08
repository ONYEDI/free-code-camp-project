#__________________parent class rectangle______________________
# creating the parent class for the child class 

class Rectangle:

    # The class for all rectangle attribute

    def __init__(self,width,height) -> None:
        
        self.width = width
        self.height = height
    
    # function for setting the width for the rectangle
    def set_width(self):
        return self.width
    
    # works as the set_width function
    def set_height(self):
        return self.height
    
    #function to calculate the area of the rectangle
    def get_area(self):
        return (self.width*self.height)

    # perimeter function 
    def get_perimeter(self):
        return(2*self.width + self.height)
    
    #function to get the diagonal of the rectangle
    def get_diagonal(self):
        return(float(((self.width**2) + (self.height**2))**.5))

    # get_picture function is to print the width and height using *
    def get_picture(self):

        # whenever the height value is greater than 50 
        if self.height > 50:
            print("Too big for picture")
        else:
            for i in range(self.height):
                printing = print("*"*self.width)
                

    #the function is going to return the number of time that the new
    # shape is going to fit into the old shape without rotation
    def get_amount_inside(self,width,height):

        #using interger divsion to get how many times that it is going to fit
        module_1 = self.set_width() %  width
        module_2 = self.set_height() % height
        if self.get_area() > (width*height):
            if module_1 > module_2:
               num_inside = module_2
            else :
                num_inside = module_1
        else:
            print("The shape can not fit ")
        return num_inside

#_________________________the child class of rectangle class_____________________________________

class square(Rectangle):

    # square class is a subclass of the rectangle class
    #creating the initialization method
    def __init__(self,width,height,side) -> None:
        Rectangle.__init__(self,width,height) 
        self.side = side
    
    # the ser_side function is going to set the sides of the square object to be equal to side
    def set_side(self):
        side =self.width =self.height
        return side


# testing thr polgon project here
t = Rectangle(9,4)
t.set_width ()
t.set_height()
t.get_area()
print(t.get_area())
t.get_picture()
print(t.get_diagonal)



        
