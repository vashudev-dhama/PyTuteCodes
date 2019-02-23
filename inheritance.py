class Parent():

    def __init__(self, last_name, eye_color):
        print("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
    
    def show_info(self):
        print("last name:"+self.last_name)
        print("eye color:"+self.eye_color)

class Child(Parent):

    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor called")
        #fetching the parent class properties
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

    #method overriding
    def show_info(self):
        print("last name:"+self.last_name)
        print("eye color:"+self.eye_color)
        print("toys:"+self.number_of_toys)
    
child1 = Child("Cyrus","Blue","5")
child1.show_info()