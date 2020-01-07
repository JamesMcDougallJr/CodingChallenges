"""
Sort a list of points by distance from (0,0)
"""
def sortByDistance(points):
  return sorted(points, key=lambda point: point[0]**2 + point[1]**2)

def sortByXThenY(points):
  return sorted(points)

if __name__ == '__main__':
  pointList = [(1,1), (10,5), (2,4), (3,7), (7,3), (8,2)]
  print("Sorted by distance from (0,0): " + str(sortByDistance(pointList)))
  print("Sorted by X then Y: " + str(sortByXThenY(pointList)))