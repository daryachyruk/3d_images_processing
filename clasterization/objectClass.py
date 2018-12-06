class MyObject:
    square = perimeter = compactness = index = claster = None

    def __init__(self, index, square, perimetr):
        self.index = index
        self.square = square
        self.perimeter = perimetr

    def CalcCompactness(self):
        self.compactness = self.square**2/self.perimeter/1000
        #self.compactness = self.perimeter**2/self.square
        if self.compactness > 25:
            self.compactness = self.compactness * 100
        self.compactness = round(self.compactness, 3)
        return

    def set_claster(self, numb_claster):
        self.claster = numb_claster
        return

    def get_claster(self):
        return self.claster
