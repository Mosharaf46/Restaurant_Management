class order:
    def __init__(self):
        self.items={}
    
    def add_item(self,item):
        if item in self.items:
            self.items[item]+=item.quantity  #jodi item ta cart a already thake
        else:
            self.items[item]=item.quantity   # jodi cart a item ti na thake
            
    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)
    @property
    def total_price(self):
        return sum(item.price*quantity for item,quantity in self.items.items())
        # sm=0
        # for item in self.items:
        #     sm+=(item.price*item.quantity)
        # return sm
    
    def clear(self):
        self.items={}