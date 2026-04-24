class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        x=-1
        i=len(self.prices)-1
        while i>=0:
            if self.prices[i][0]>price:
                x=max(x,self.prices[i][1])
            if self.prices[i][0]<price:
                break
            i -= 1
        #i is either -1 ie a decreasing series or the largest price that is smaller than price
        if i==-1:
            self.prices[:] = [(price,len(self.prices))] +self.prices
            return len(self.prices)-x-1
        self.prices[:] = self.prices[:i+1]+[(price,len(self.prices))]+self.prices[i+1:]
        return len(self.prices)-x-1
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)