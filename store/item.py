import csv
from sqlite3 import connect


class Item:

    #class attribute
    pay_rate = 0.8 #Pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} should be greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} should be greater than or equal to zero"

        #Assign to self object
        self.__name = name # the __ make the name attribute a private attr
        self.__price = price
        self.quantity = quantity
        
        #actions to execute
        Item.all.append(self)

    '''ENCAPSULATION'''
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        assert len(new_name) > 10, "The name is too long"
        self.__name = new_name

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, value):
        return self.__price + (self.__price * value)

    def calculate_total_price(self):
        return self.__price * self.quantity


    @classmethod
    def instantiate_from_csv(cls):
        '''
        Class methods do something that has a relationship with
        the class, but usually, those are used to manipulate  differen
        structures of data to instantiate objects from files like 
        CSV, XML, YAML etc etc
        '''
        path = r"C:\Users\LENOVO\Documents\dev\OOP_Python\store\items.csv"
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        '''
        Do something that has a relationship with the class, but 
        not something that must be unique per instance 
        '''
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.quantity})"
    
    '''ABSTRACTION'''
    def __connect(self, smtp_server):
        pass

    def __email_body(self):
        return f"""
            We have {self.__name} {self.quantity} times
        """

    def send_email(self):
        self.__connect('')
        self.__email_body()
        #send
    






#print(Item.__dict__) #All the attributes at Class level
