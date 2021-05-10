import matplotlib.pyplot as plt
from matplotlib import collections
import numpy as np
np.random.seed(42)


class Point:
   def __init__(self, x= 0, y= 0):
      self.x = x
      self.y = y
   
   def getCoordinate(self):
      return [self.x, self.y]
   
   @classmethod
   def genPoints(cls, point_array):
      points_list = []
      for i in range(len(point_array[0])):
         points_list.append(cls(point_array[0,i], point_array[1,i]))
      return points_list 
   
   def __str__(self):
      return "Point.x= {}, Point.y= {}".format(str(self.x), str(self.y))
   
   # calculate cross product 2D
   def isCounterClockwise(self, other1, other2): # self->other1 * other1->other2 (* : cross product)
      area = (other1.x - self.x) * (other2.y - other1.y) - (other2.x - other1.x) * (other1.y - self.y) 
      if (area < 0): return -1   # clockwise
      if (area > 0): return 1    # counter-clockwise
      return 0 
   
def getSlope(point1, point2):
   if (point1.x == point2.x) and (point1.y >= point2.y): return float('inf')
   elif (point1.x == point2.x) and (point1.y < point2.y): return float('-inf')
   else:
      return 1.0 * (point2.y-point1.y)/(point2.x-point1.x)

def main():
   NUM_POINTS = 10   # the number of random coor_points
   MAX_COOR_VAL = 300  # the maximum coordinary' value 
   coor_points = np.random.randint(low= 0, high= MAX_COOR_VAL, size= (2, NUM_POINTS))
   points_ary = Point().genPoints(coor_points)

   points_ary.sort(key=lambda p : [p.x, p.y]) # default: sorting a list in increasing 
   convex_hull = [] # stack contain the result
   convex_hull.append(points_ary.pop(0)) # đưa phần tử khởi tạo đầu tiên vào stack (chắc chắn nằm trong convex hull stack)
   print("first point: ", convex_hull[0])

   points_ary.sort(key= lambda p: (getSlope(convex_hull[0], p), -p.x)) # thứ tự ưu tiên: các điểm từ dưới lên trên theo counterclockwise, các điểm ở xa nếu góc trùng
   convex_hull.append(points_ary.pop(0)) # đưa phần tử tiếp theo của mảng (sau khi sắp xếp theo góc theo counterclockwise) vào stack 
   
   for p in points_ary: 
      # pop the last point from the stack if we turn clockwise to reach this point
      # p : điểm hiện tại đang xét
      """
      while để tạo so sánh đệ quy giữa các node 
      kiểm tra len(convex_hull) > 1: phần tử khởi tạo thứ 2 có thể ko nằm trong convex hull stack
      """
      top = convex_hull[-1] # get top in this stack
      pre_top = convex_hull[-2] # get a previous top in this stack
      while len(convex_hull) > 1 and pre_top.isCounterClockwise(top, p) < 0:
         convex_hull.pop()
         top = convex_hull[-1] # update top in this stack
         pre_top = convex_hull[-2] # update a previous top in this stack
      convex_hull.append(p)

   # create a collection of lines
   collec_lines = [] 
   for i in range(len(convex_hull)):
      collec_lines.append(convex_hull[i].getCoordinate())
   collec_lines.append(convex_hull[0].getCoordinate())
      # print(convex_hull[i])

   # plotting the graph
   plt.subplot(121)
   plt.scatter(coor_points[0], coor_points[1])
   plt.subplot(122)
   plt.scatter(coor_points[0], coor_points[1])
   xs, ys = zip(*collec_lines)
   plt.plot(xs, ys, color='green', marker='v', 
            linestyle='dashed', linewidth=2, markersize=10)
   plt.show()


if __name__ == "__main__":
   main()