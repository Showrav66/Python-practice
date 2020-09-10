class EcommerceA():

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def daraz(self):
        print(self.brand, self.model)

    def evaly(self):
        print(self.brand, self.model)

#inheritance
class EcommerceC(EcommerceA):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.brand = brand
        self.model = model

    def Alibaba(self):
        print(self.brand, self.model)

    def Amazon(self):
        print(self.brand, self.model)


mobile1 = EcommerceC('Samsung', 'sm-g360h')
mobile2 = EcommerceC('Redmi', 'note 7 pro')
mobile2.Alibaba()
mobile1.Amazon()