class Product:
    def __init__(self,Product_name,Price,Discount,GST,Quantity):
        self.name = Product_name
        self.price= Price
        self.discount=Discount
        self.gst=GST
        self.quantity=Quantity
    def display(self):
        print(f"Product Name : {self.name}")
        print(f"Product Price : {self.price}")
        print(f"Product Discount : {self.discount}")
        print(f"GST : {self.gst}")
        print(f"Quantity : {self.quantity}")

e1=Product("Laptop",50000,10,18,5)
e2=Product("Mobile Phone",25000,50,12,10)
e3=Product("Laptop Bag",1000,5,5,15)
e4=Product("Tablet",20000,10,18,5)
e5=Product("Ipad",55000,10,10,5)
e1.display()
e2.display()
e3.display()
e4.display()
e5.display()