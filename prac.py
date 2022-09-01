class Mobile:
    def __init__(self,model,camera):
        self.model=model
        self.camera=camera
      # in the above example model and camera are the properties and values are which passed to the __init__ method.
    def make_call(self,number):
        print("calling.....{}".format(number))

    def update_obj(self, model):
        self.model = model
        #In OOP terminology, properties are referred as attributes actions are referred as methods
mobile_obj = Mobile("iPhone 12 Pro", "12 MP")
mobile_obj.make_call(9876543210)
print(mobile_obj.camera)
mobile_obj.update_obj("iphone13")
print(mobile_obj.model)#to update the given model in the above update_obj function