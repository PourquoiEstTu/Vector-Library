from vectorClass import Vector as v

class DimensionError(Exception) :
    pass

class SingleVectorError(Exception) :
    def __init__(self) :
        super().__init__("If you enter a single vector into a Matrix object, do not put it inside a list. Instead, just enter it by itself without square brackets. You may also enter it as a standalone vector (i.e. using the vector class) if that is what you need.")

class Matrix(v) :
    def __init__(self, l) :
        """ This is a class for doing Matrix operations with vectors. 
        The arguments for the initialization should be a single vector object or
        a list of vector objects. """
       
        #case of a matrix with a single vector
        if isinstance(l, v) :
            self.matrix = l
            self.oneDimMatrix = True
        else :

            #checks whether l is a list
            if type(l) != list :
                raise TypeError

            if len(l) == 0 :
                self.matrix = l
                self.emptyMatrix = True
            else :

                #checks whether the members of l are vectors 
                for i in range( len(l) ) :
                    if not ( isinstance(l[i], v) ) :
                        raise TypeError

                #checks to see if a single vector was entered inside a list. 
                #this check is done after the loop so that it is confirmed that
                # vectors have actually been entered.
                if len(l) == 1 :
                    raise SingleVectorError
        
                #checks if all the vectors are the same size
                first_elem_size = l[0].dim()
                for i in range(1, len(l) ) :
                    if l[i].dim() != first_elem_size :
                        raise DimensionError

                self.matrix = l
                self.oneDimMatrix = False
    
    def coordDim(self) :
        """Returns the dimension of the matrix in a tuple. The first value is the number of rows. The second number is the number of columns. For a more English/math representation, call strDim() instead."""

        if self.oneDimMatrix == True :
            return ( self.matrix.dim(), 1 )

        return ( self.matrix[0].dim(), len(self.matrix) )

    def longDim(self) :
        """Returns the dimension of the matrix in a longer, more detailed form. """

        return "This is a " + str( self.coordDim()[0] ) + " row by " + str( self.coordDim()[1] ) + " column matrix."

    def dim(self) :
        """Returns the dimension of the matrix in standard mathematical notation where the first number signifies rows and the second signifies columns."""

        return str( self.coordDim()[0] ) + "\u00D7" + str( self.coordDim()[1] )

    def __getitem__(self, x, y) :
        if (x < 0) or (x >= self.coordDim()[1] ) :
            raise IndexError 
        if (y < 0 ) or (y >= self.coordDim()[0]) :
            raise IndexError

    def __mul__(self, other) :
        if (not (isinstance(other, Matrix)) ) :
            raise TypeError

        if self.coordDim()[1] != other.coordDim()[0] :
            print("For matrix multiplication, the number of columns in the first matrix must be the same as the number of rows in the secondmatrix.")
            raise DimensionError

        new = Matrix([])
