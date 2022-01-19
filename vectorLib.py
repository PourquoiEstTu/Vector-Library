class Vector() :
    def __init__(self, l) :
        if type(l) != list :
            raise TypeError
        for item in l :
            if type(item) not in (int, float) :
                raise TypeError
        self.vector = l
    
    def dim(self) :
        return len(self.vector)
    
    def __getitem__(self, i) :
        if (i < 1 == True) or (i > len(self.vector) == True) :
            raise IndexError
        
        return self.vector[i - 1]
    
    def __setitem__(self, i, x) :
        if (i < 1 == True) or (i > len(self.vector) == True) :
            raise IndexError
        self.vector[i - 1] = x
        
    def __add__(self, other) :
        if (isinstance(other, Vector) != True) or (other.dim() != self.dim()) :
            raise ValueError
        
        newVector = Vector([])
        for item in range(1, self.dim() + 1) :
            newVector.vector.append(self[item] + other[item]) 
        return newVector
            
    def __mul__(self, other) :
        newVector = Vector([])
        if (type(other) not in (int, float)) and (isinstance(other, Vector) != True) :
            raise AssertionError
            
        if type(other) in (int, float) :
            for item in range(1, self.dim() + 1) :
                newVector.vector.append(self[item] * other)
                #print(item)
            return newVector
        else :
            if other.dim() != self.dim() :
                raise ValueError
            else :
                dotProduct = 0 
                for item in range(1, self.dim() + 1) :
                    dotProduct += self[item] * other[item]
                    #print(dotProduct)
                return dotProduct
            
    def __rmul__(self, other) :
        return self.__mul__(other)
    
    def __str__(self) :
        return "Vector: " + str(self.vector)