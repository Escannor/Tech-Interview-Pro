class Point:
    '''Object Point'''
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

def Solution(listPoints):
    '''Return de max Distance, and de pair of points'''
    maxX=minX=maxY=minY = listPoints[0]

    #print(maxX.name,minX.name,maxY.name,minY.name)
    for point in listPoints:
        if point.x > maxX.x:
            maxX = point
        if point.x < minX.x:
            minX = point
        if point.y > maxY.y:
            maxY = point
        if point.x < minY.y:
            maxX = point
        
    A = maxX
    B = minX
    maxDistance = 0
    listCompare = [(maxX,minX), (maxX,maxY), (maxX,minY), (minX,maxY), (minX,minY),(maxY,minY)]
    for compare in listCompare:
        
        newDistance = Distance(compare[0],compare[1])
        if maxDistance < newDistance:
            maxDistance = newDistance
            A,B = compare

    return maxDistance,A,B

def Distance(A,B):
    X = abs(A.x-B.x)
    Y = abs(A.y-B.y)
    return ( (X**2) + (Y**2) )**(1/2)
    

A = Point('A',-10,7)
B = Point('B',-9,-6)
C = Point('C',7,5)
D = Point('D',-10,-7)

listPoints = [A,B,C,D]

output = Solution(listPoints)
print("La distancia mas larga es de: "+str(output[0]))
print("Los puntos que la conforman son: " +output[1].name+ ", "+output[2].name)

