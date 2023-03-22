#  File: Hull.py

#  Description: prints vertices of the convex hull, extreme left point clockwise around the convex hull and convex hull area 

#  Student Name: K. Amber Vasquez

#  Student UT EID: kav835

#  Partner Name: Nicole Estabrook

#  Partner UT EID: nae588

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created:

#  Date Last Modified: 10/30/2020

import sys
import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

def det (p, q, r):
    # p[0], p[1]
    # q[0], q[1]
    # r[0], r[1]
    determinant = p.x*q.y + q.x*r.y + r.x*p.y - (p.y*q.x + q.y*r.x + r.y*p.x)
    return determinant

def convex_hull (sorted_points):
    n = len(sorted_points)
    upper_hull = []
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])
    for i in range(2, n, 1):
        upper_hull.append(sorted_points[i])
        determinant = det(upper_hull[-3], upper_hull[-2], upper_hull[-1])
        while len(upper_hull) >= 3 and determinant >= 0:
            del upper_hull[-2]
            if len(upper_hull) >= 3:
                determinant = det(upper_hull[-3], upper_hull[-2], upper_hull[-1])
            else:
                continue

    lower_hull = []
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])
    for i in range (n-2, -1, -1):
        lower_hull.append(sorted_points[i])
        determinant = det(lower_hull[-3], lower_hull[-2],lower_hull[-1])
        while len(lower_hull) >= 3 and determinant >= 0:
            del (lower_hull[-2])
            if len(lower_hull) >= 3:
                determinant = det(lower_hull[-3], lower_hull[-2], lower_hull[-1])
            else:
                continue

    del lower_hull[0]
    del lower_hull[-1]
    convex_hull = []
    for point in upper_hull:
        convex_hull.append(point)
    for point in lower_hull:
        convex_hull.append(point)

    return convex_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
    # area = (1/2) * abs (det)
    n = len(convex_poly)

    pos_det = 0
    for i in range(n):
        if i < n-1:
            pos_det += convex_poly[i].x * convex_poly[i+1].y
        elif i == n-1:
            pos_det += convex_poly[i].x * convex_poly[0].y

    neg_det = 0
    for i in range(n):
        if i < n-1:
            neg_det += convex_poly[i+1].x * convex_poly[i].y
        else:
            neg_det += convex_poly[0].x * convex_poly[i].y

    det = pos_det - neg_det
    area = 0.5 * abs(det)

    return area

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    # write your own test cases
    pass

    return "all test cases passed"

def selection_sort (pointList):
    #x = point[0]
    for x in range (len(pointList) - 1):     # find the minimum     
        min = pointList[x]    
        minIdx = x   # what does this mean 
        for j in range (x + 1, len(pointList)):   # what does j sort through, is j the next x in the list? 
            if (pointList[j] < min):         
                min = pointList[j]
                minIdx = j  

        pointList[minIdx] = pointList[x]     
        pointList[x] = min

    return pointList

def main():

    pointList = []

    # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int(line)

    # read data from standard input
    for i in range (num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int (line[0])
        y = int (line[1])
        pointList.append (Point (x, y))
    
    # sort the list according to x-coordinates
    sorted_points = selection_sort(pointList)
    
    # get the convex hull
    hull = convex_hull(sorted_points)	

    # run your test cases

    # print your results to standard output

    # print the convex hull
    print("Convex Hull")
    for point in hull:
        print(point)

    # get the area of the convex hull
    area = area_poly(hull)

    # print the area of the convex hull
    print("\nArea of Convex Hull = " + str(area))

if __name__ == "__main__":
    main()

