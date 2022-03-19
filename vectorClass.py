class Vector() :
    def __init__(self, l) :
        """ A vector class for doing simple and common vector operations. 
        The input for initialization is a list of integers or floats."""

        if type(l) != list :
            raise TypeError
        for item in l :
            if type(item) not in (int, float) :
                raise TypeError
        self.vector = l
    
    def dim(self) :
        """ Returns the dimension of the vector or in other words, 
        the length of the list of numbers."""

        return len(self.vector)
    
    def __getitem__(self, i) :
        """Retrieves elements from a vector exactly
        like how you can with lists."""

        if (i < 0 == True) or (i >= len(self.vector) == True) :
            raise IndexError
        
        return self.vector[i]
    
    def __setitem__(self, i, x) :
        """Allows you to change the element of the vector in the i-th position
        that you select. """

        if (i < 0 == True) or (i >= len(self.vector) == True) :
            raise IndexError
        self.vector[i] = x
        
    def __add__(self, other) :
        """Adds vectors of like (the same) dimensions together."""
        if (isinstance(other, Vector) != True) or (other.dim() != self.dim()) :
            raise ValueError
        
        newVector = Vector([])
        for item in range(self.dim()) :
            newVector.vector.append(self[item] + other[item]) 
        return newVector
            
    def __mul__(self, other) :
        """Depending on whether the argument 'other' (the argument in the brackets
        of the method when called on a vector) is a scalar number or another vector,
        either does scalar multiplication on a vector or takes the dot product of two 
        vectors respectively."""

        newVector = Vector([])
        if (type(other) not in (int, float)) and (isinstance(other, Vector) != True) :
            raise AssertionError
            
        if type(other) in (int, float) :
            for item in range(self.dim()) :
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
        """Same as the __mul__ method."""

        return self.__mul__(other)
    
    def __str__(self) :
        return "Vector: " + str(self.vector)


