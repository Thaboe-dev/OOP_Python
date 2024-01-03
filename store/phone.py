from item import Item

'''INHERITANCE'''
class Phone(Item):
    
    def __init__(self, name: str, price: float, quantity: int, serial: str, broken_phones = 0):
        #Call to the Constructor of the Super Class
        super().__init__(
            name, price, quantity
        )
        
        #Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} should be greater or equal to zero"
       
        #Assign to self object
        self.broken_phones = broken_phones




