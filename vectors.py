#!/usr/bin/python3
# By Joseph Pitts

import math
    
class vector2D(object):
    def __init__(self, x_coord, y_coord):
        super().__init__()
        self.x = x_coord
        self.y = y_coord      

    def set(self, x_coord, y_coord):     
        """Sets the x, y component of the vector.    
        >>> v = vector2D(10, 20)  

        >>> v.set(20, 24)
        >>> print(v.x)
        20
        >>> print(v.y)
        24
        """

        self.x = x_coord
        self.y = y_coord     

    def copy(self):
        """Return a copy of the vector.   
        >>> v = vector2D(10, 20)  
        >>> c = v.copy()
        >>> print(c.x)
        10
        >>> print(c.y)
        20
        """
        return vector2D(self.x ,self.y)

    def add(self, x_coord, y_coord):
        """Adds x and y components to the vector.
        >>> v = vector2D(10, 20)  

        >>> v.add(10, 6)
        >>> print(v.x)
        20
        >>> print(v.y)
        26
        """
        self.x += x_coord
        self.y += y_coord

    def addVector2D(self, vec):
        """Adds one vector to the other.
        >>> v = vector2D(10, 20)  
        >>> v2 = vector2D(10, 6) 
        >>> v.addVector2D(v2)
        >>> print(v.x)
        20
        >>> print(v.y)
        26
        """
        if repr(vec) == "Vector2D":
            self.add(vec.x, vec.y)
        else:
            raise AttributeError("vector2D.addVector2D requires a 2DVector!")

    def sub(self, x_coord, y_coord):
        """Subtacts x and y components.
        >>> v = vector2D(10, 20)  
        >>> v.sub(10, 6)
        >>> print(v.x)
        0
        >>> print(v.y)
        14
        """
        self.x -= x_coord
        self.y -= y_coord

    def subVector2D(self, vec):
        """Subtacts one vector from the other.
        >>> v = vector2D(10, 20)  
        >>> v2 = vector2D(10, 6)  
        >>> v.subVector2D(v2)
        >>> print(v.x)
        0
        >>> print(v.y)
        14
        """
        if repr(vec) == "Vector2D":
            self.sub(vec.x, vec.y)
        else:
            raise AttributeError("vector2D.subVector2D requires a 2DVector!")

    def mult(self, x_coord, y_coord):
        """ Multiples the x and y components by the supplied coords.
        >>> v = vector2D(10, 20)  
        >>> v.mult(10, 6)
        >>> print(v.x)
        100
        >>> print(v.y)
        120
        """
        self.x *= x_coord
        self.y *= y_coord

    def multVector2D(self, vec):
        """ Multiples two vectors together.
        >>> v = vector2D(10, 20)  
        >>> v2 = vector2D(10, 6) 
        >>> v.multVector2D(v2)
        >>> print(v.x)
        100
        >>> print(v.y)
        120
        """
        if repr(vec) == "Vector2D":
            self.mult(vec.x, vec.y)
        else:
            raise AttributeError("vector2D.multVector2D requires a 2DVector!")

    def div(self, x_coord, y_coord):
        """ Divides the x and y components by the supplied coords.
        >>> v = vector2D(10, 20)  
        >>> v.div(10, 2)
        >>> print(v.x)
        1.0
        >>> print(v.y)
        10.0
        """
        self.x /= x_coord
        self.y /= y_coord

    def divVector2D(self, vec):
        """ Divides two vectors x and y components.
        >>> v = vector2D(10, 20) 
        >>> v2 = vector2D(10, 2)  
        >>> v.divVector2D(v2)
        >>> print(v.x)
        1.0
        >>> print(v.y)
        10.0
        """
        if repr(vec) == "Vector2D":
            self.div(vec.x, vec.y)
        else:
            raise AttributeError("vector2D.divVector2D requires a 2DVector!")

    def mag(self):
        """	Calculates the magnitude (length) of the vector.
        >>> v = vector2D(3, 4)  
        >>> v.mag()
        5.0
        """
        return round(math.sqrt(
            (self.x * self.x) +
            (self.y * self.y)
            ), 10)

    def magSq(self):
        """	Calculates the squared magnitude (length) of the vector (Faster)
        >>> v = vector2D(3, 4)  
        >>> v.magSq()
        25
        """
        return (
            (self.x * self.x) +
            (self.y * self.y)
            )
	
    def dot(self, x_coord, y_coord):
        """	Calculates the dot product between the vector and an x and y coordinate.
        >>> v = vector2D(3, 4)  
        >>> v.dot(3, 79)
        325
        """
        return (self.x * x_coord) + (self.y * y_coord)

    def dotVector2D(self, vec):
        """	Calculates the dot product between two vectors.
        >>> v = vector2D(3, 4)  
        >>> v2 = vector2D(3, 79)
        >>> v.dotVector2D(v2)
        325
        """
        if repr(vec) == "Vector2D":
             return self.dot(vec.x, vec.y)
        else:
            raise AttributeError("vector2D.dotVector2D requires a 2DVector!")

    def dist(self, x_coord, y_coord):
        """	Calculates the distance between the Vector and a point.
        >>> v = vector2D(3, 4)        
        >>> v.dist(10, 6)
        7.2801098893
        """
        a = x_coord - self.x
        b = y_coord - self.y
        return round(math.sqrt((a*a)+(b*b)), 10)

    def distVector2D(self, vec):
        """	Calculates the distance between two Vectors.
        >>> v = vector2D(3, 4)  
        >>> v2 = vector2D(10, 6)      
        >>> v.distVector2D(v2)
        7.2801098893
        """
        if repr(vec) == "Vector2D":            
            return self.dist(vec.x, vec.y)
        else:
            raise AttributeError("vector2D.distVector2D requires a 2DVector!")

    def normalise(self, mag_limit = 1):
        """	Normalise the vector to a magnitude of mag_limit.
        >>> v = vector2D(4, 7)        
        >>> v.normalise()
        >>> print(v)
        (0.49613893835674455, 0.868243142124303)

        >>> v = vector2D(4, 7)        
        >>> v.normalise(5)
        >>> print(v)
        (2.480694691783723, 4.341215710621515)
        """
        m = self.mag()
        sf = (m / mag_limit)
        self.div(sf, sf)

    def heading(self):
        """	Calculates the heading of the Vector
        >>> v = vector2D(3, 4)  
        >>> v.heading()
        0.927295218
        """
        return round(math.atan(self.y / self.x), 10)

    def rotate(self, angle):
        """	Rotates the Vector by an angle given in radians.
        >>> v = vector2D(3, 4)  
        >>> v.rotate(1.57)
        >>> print(v)
        (-3.9976097516, 3.0031843556)
        """
        theta = angle        
        cs = math.cos(theta)
        sn = math.sin(theta)
        px = self.x * cs - self.y * sn
        py = self.x * sn + self.y * cs
        self.x = round(px, 10)
        self.y = round(py, 10)


    def angleBetween(self, x_coord, y_coord):
        """	Calculates the angle in radians between the Vector and a point.
        >>> v = vector2D(3, 4)  
        >>> v.angleBetween(24, 4)       
        0.7233555441
        """
        dp = self.dot(x_coord, y_coord)
        m1 = self.mag()
        m2 = vector2D(x_coord, y_coord).mag()
        return round(dp / (m1*m2),10)

    def angleBetweenVector2D(self, vec):
        """	Calculates the angle in radians between the Vector and a point.
        >>> v = vector2D(3, 4)  
        >>> v2 = vector2D(24, 4)
        >>> v.angleBetweenVector2D(v2)       
        0.7233555441
        """ 
        if repr(vec) == "Vector2D":
             return self.angleBetween(vec.x, vec.y)
        else:
            raise AttributeError("vector2D.angleBetweenVector2D requires a 2DVector!")    


    def lerp(self, x_coord, y_coord, amnt):
        """ Linear interpolate the vector to a coord pair
        >>> v = vector2D(3, 4) 
        >>> v.lerp(6, 3, 0.5)
        >>> print(v)
        (4.5, 3.5)
        """
        if amnt < 0 or amnt > 1:
            raise AttributeError("Lerp ammount must be between 0 and 1!")
        else:
            self.x = (1 - amnt) * self.x + amnt * x_coord
            self.y = (1 - amnt) * self.y + amnt * y_coord

    def lerpVector2D(self, vec, amnt):
        """ Linear interpolate the vector to another vector
        >>> v = vector2D(3, 4) 
        >>> v2 = vector2D(6, 3) 
        >>> v.lerpVector2D(v2, 0.5)
        >>> print(v)
        (4.5, 3.5)
        """
        if repr(vec) == "Vector2D":
             return self.lerp(vec.x, vec.y, amnt)
        else:
            raise AttributeError("vector2D.lerpVector2D requires a 2DVector!")  

    def array(self):
        """ Return an array 
        >>> v = vector2D(3, 4) 
        >>> v.array()
        [3, 4]
        """
        return [self.x, self.y]


    def __eq__(self, value):
        try:
            return self.x == value.x and self.y == value.y
        except:
            return False

    def __ne__(self, value):
        try:
            return self.x != value.x or self.y != value.y
        except:
            return True
                
    def __repr__(self):
        return "Vector2D"

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)



    
class vector3D(object):
    def __init__(self, x_coord, y_coord, z_coord):
        super().__init__()
        self.x = x_coord
        self.y = y_coord 
        self.z = z_coord   

    def set(self, x_coord, y_coord, z_coord):     
        """Sets the x, y component of the vector.    
        >>> v = vector3D(10, 20, 30)  

        >>> v.set(20, 24, 26)
        >>> print(v.x)
        20
        >>> print(v.y)
        24
        >>> print(v.z)
        26
        """

        self.x = x_coord
        self.y = y_coord     
        self.z = z_coord

    def copy(self):
        """Return a copy of the vector.   
        >>> v = vector3D(10, 20, 30)  
        >>> c = v.copy()
        >>> print(c.x)
        10
        >>> print(c.y)
        20
        >>> print(c.z)
        30
        """
        return vector3D(self.x ,self.y, self.z)

    def add(self, x_coord, y_coord, z_coord):
        """Adds x, y and x components to the vector.
        >>> v = vector3D(10, 20, 30)  

        >>> v.add(10, 6, 4)
        >>> print(v.x)
        20
        >>> print(v.y)
        26
        >>> print(v.z)
        34
        """
        self.x += x_coord
        self.y += y_coord
        self.z += z_coord

    def addVector3D(self, vec):
        """Adds one vector to the other.
        >>> v = vector3D(10, 20, 30)  
        >>> v2 = vector3D(10, 6, 4) 
        >>> v.addVector3D(v2)
        >>> print(v.x)
        20
        >>> print(v.y)
        26
        >>> print(v.z)
        34
        """
        if repr(vec) == "Vector3D":
            self.add(vec.x, vec.y, vec.z)
        else:
            raise AttributeError("vector3D.addVector3D requires a 3DVector!")

    def sub(self, x_coord, y_coord, z_coord):
        """Subtacts x, y and z components.
        >>> v = vector3D(10, 20, 30)  
        >>> v.sub(10, 6, 4)
        >>> print(v.x)
        0
        >>> print(v.y)
        14
        >>> print(v.z)
        26
        """
        self.x -= x_coord
        self.y -= y_coord
        self.z -= z_coord

    def subVector3D(self, vec):
        """Subtacts one vector from the other.
        >>> v = vector3D(10, 20, 30)  
        >>> v2 = vector3D(10, 6, 4)  
        >>> v.subVector3D(v2)
        >>> print(v.x)
        0
        >>> print(v.y)
        14
        >>> print(v.z)
        26
        """
        if repr(vec) == "Vector3D":
            self.sub(vec.x, vec.y, vec.z)
        else:
            raise AttributeError("vector3D.subVector3D requires a 3DVector!")

    def mult(self, x_coord, y_coord, z_coord):
        """ Multiples the x, y and z components by the supplied coords.
        >>> v = vector3D(10, 20, 30)  
        >>> v.mult(10, 6, 4)
        >>> print(v.x)
        100
        >>> print(v.y)
        120
        >>> print(v.z)
        120
        """
        self.x *= x_coord
        self.y *= y_coord
        self.z *= z_coord

    def multVector3D(self, vec):
        """ Multiples two vectors together.
        >>> v = vector3D(10, 20, 30)  
        >>> v2 = vector3D(10, 6, 4) 
        >>> v.multVector3D(v2)
        >>> print(v.x)
        100
        >>> print(v.y)
        120
        >>> print(v.z)
        120
        """
        if repr(vec) == "Vector3D":
            self.mult(vec.x, vec.y, vec.z)
        else:
            raise AttributeError("vector3D.multVector3D requires a 3DVector!")

    def div(self, x_coord, y_coord, z_coord):
        """ Divides the x, y and z components by the supplied coords.
        >>> v = vector3D(10, 20, 30)  
        >>> v.div(10, 2, 3)
        >>> print(v.x)
        1.0
        >>> print(v.y)
        10.0
        >>> print(v.z)
        10.0
        """
        self.x /= x_coord
        self.y /= y_coord
        self.z /= z_coord

    def divVector3D(self, vec):
        """ Divides two vectors x, y and z components.
        >>> v = vector3D(10, 20, 30) 
        >>> v2 = vector3D(10, 2, 3)  
        >>> v.divVector3D(v2)
        >>> print(v.x)
        1.0
        >>> print(v.y)
        10.0
        >>> print(v.z)
        10.0
        """
        if repr(vec) == "Vector3D":
            self.div(vec.x, vec.y, vec.z)
        else:
            raise AttributeError("vector3D.divVector3D requires a 3DVector!")

    def mag(self):
        """	Calculates the magnitude (length) of the vector.
        >>> v = vector3D(3, 4, 12)  
        >>> v.mag()
        13.0
        """
        return round(math.sqrt(
            (self.x * self.x) +
            (self.y * self.y) +
            (self.z * self.z) 
            ), 10)

    def magSq(self):
        """	Calculates the squared magnitude (length) of the vector (Faster)
        >>> v = vector3D(3, 4 ,12)  
        >>> v.magSq()
        169
        """
        return (
            (self.x * self.x) +
            (self.y * self.y)+
            (self.z * self.z)
            )
	
    def dot(self, x_coord, y_coord, z_coord):
        """	Calculates the dot product between the vector and an x, y and z coordinate.
        >>> v = vector3D(3, 4, 5)  
        >>> v.dot(3, 79, 24)
        445

        >>> v = vector3D(1, 0, 0)  
        >>> v.dot(1, 0, 0)
        1

        """
        return (self.x * x_coord) + (self.y * y_coord) + (self.z * z_coord)

    def dotVector3D(self, vec):
        """	Calculates the dot product between two vectors.
        >>> v = vector3D(3, 4, 5)  
        >>> v2 = vector3D(3, 79, 24)
        >>> v.dotVector3D(v2)
        445
        """
        if repr(vec) == "Vector3D":
             return self.dot(vec.x, vec.y, vec.z)
        else:
            raise AttributeError("vector3D.dotVector3D requires a 3DVector!")

    def dist(self, x_coord, y_coord, z_coord):
        """	Calculates the distance between the Vector and a point.
        >>> v = vector3D(3, 4, 5)        
        >>> v.dist(10, 6, 4)
        7.3484692283
        """
        a = x_coord - self.x
        b = y_coord - self.y
        c = z_coord - self.z
        return round(math.sqrt((a*a)+(b*b)+(c*c)), 10)

    def distVector3D(self, vec):
        """	Calculates the distance between two Vectors.
        >>> v = vector3D(3, 4, 5)  
        >>> v2 = vector3D(10, 6, 4)      
        >>> v.distVector3D(v2)
        7.3484692283
        """
        if repr(vec) == "Vector3D":            
            return self.dist(vec.x, vec.y, vec.z)
        else:
            raise AttributeError("vector3D.distVector3D requires a 3DVector!")

    def normalise(self, mag_limit = 1):
        """	Normalise the vector to a magnitude of mag_limit.
        >>> v = vector3D(4, 7, 9)        
        >>> v.normalise()
        >>> print(v)
        (0.33104235544079846, 0.5793241220213973, 0.7448452997417965)

        >>> v = vector3D(4, 7, 9)        
        >>> v.normalise(5)
        >>> print(v)
        (1.655211777203992, 2.8966206101069862, 3.7242264987089824)

        """
        m = self.mag()
        sf = (m / mag_limit)
        self.div(sf, sf, sf)    

    def angleBetween(self, x_coord, y_coord, z_coord):
        """	Calculates the angle in radians between the Vector and a point.
        >>> v = vector3D(2, 4 ,6)  
        >>> v.angleBetween(0, 5, 10)       
        0.9561828875
        """
        dp = self.dot(x_coord, y_coord, z_coord)
        m1 = self.mag()
        m2 = vector3D(x_coord, y_coord, z_coord).mag()
        return round(dp / (m1*m2),10)

    def angleBetweenVector3D(self, vec):
        """	Calculates the angle in radians between the Vector and a point.
        >>> v = vector3D(2, 4, 6)  
        >>> v2 = vector3D(0, 5, 10)
        >>> v.angleBetweenVector3D(v2)       
        0.9561828875
        """ 
        if repr(vec) == "Vector3D":
             return self.angleBetween(vec.x, vec.y, vec.z)
        else:
            raise AttributeError("vector3D.angleBetweenVector3D requires a 3DVector!")    


    def lerp(self, x_coord, y_coord, z_coord, amnt):
        """ Linear interpolate the vector to a coord pair
        >>> v = vector3D(3, 4, 5) 
        >>> v.lerp(6, 3, 1, 0.5)
        >>> print(v)
        (4.5, 3.5, 3.0)
        """
        if amnt < 0 or amnt > 1:
            raise AttributeError("Lerp ammount must be between 0 and 1!")
        else:
            self.x = self.x * amnt + x_coord * (1-amnt)
            self.y = self.y * amnt + y_coord * (1-amnt)
            self.z = self.z * amnt + z_coord * (1-amnt)

    def lerpVector3D(self, vec, amnt):
        """ Linear interpolate the vector to another vector
        >>> v = vector3D(3, 4, 5) 
        >>> v2 = vector3D(6, 3, 1) 
        >>> v.lerpVector3D(v2, 0.5)
        >>> print(v)
        (4.5, 3.5, 3.0)
        """
        if repr(vec) == "Vector3D":
             return self.lerp(vec.x, vec.y, vec.z, amnt)
        else:
            raise AttributeError("vector3D.lerpVector3D requires a 3DVector!")  

    def array(self):
        """ Return an array 
        >>> v = vector3D(3, 4, 5) 
        >>> v.array()
        [3, 4, 5]
        """
        return [self.x, self.y, self.z]


    def __eq__(self, value):
        try:
            return self.x == value.x and self.y == value.y and self.y == value.z
        except:
            return False

    def __ne__(self, value):
        try:
            return self.x != value.x or self.y != value.y or self.z != value.z
        except:
            return True
                
    def __repr__(self):
        return "Vector3D"

    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)


if __name__ == "__main__":
    import doctest
    doctest.testmod()