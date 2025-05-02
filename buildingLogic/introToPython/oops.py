class vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
        print("The vehicle is created")
        
    def moves(self):
        print("The vehicle moves")
    def get_make_model(self):
        print(f"i'AM A {self.make} {self.model}.")
        
mycar=vehicle('TESLA' ,'MODEL S')
mycar.moves()
mycar.get_make_model()
mycar2=vehicle('BMW' ,'X5')
mycar2.moves()
mycar2.get_make_model()

class Airplane(vehicle):
    def __init__(self,make,model,faa_id):
        super().__init__(make,model)
        self.faa_id=faa_id
    
    def moves(self):
        print("flies along")

class Truck(vehicle):
    def moves(self):
        print("drives along")

class GolfCart(vehicle):
    pass

cessna=Airplane('CESSNA','172','mjnfn-0890808')
ce=Truck('Cesin','192')
ces=GolfCart('yamaha','162')

cessna.moves()
cessna.get_make_model()

ces.moves()
ces.get_make_model()

ce.moves()
ce.get_make_model()

#abilty to respond/behave diffrently in response to the same input messages
#classes-bluprints
#objects -instances of classes

print('\n \n')
for v in (mycar,mycar2,cessna,ce,ces):
    v.moves()
    v.get_make_model()
