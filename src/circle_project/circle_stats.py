import math

def radius_sum(r1, r2):
    return r1 + r2

def euclid_distance(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    distance = math.sqrt(x*x + y*y)
    return distance

def has_intersection(circle_1, circle_2):
   x1, y1, r1 = circle_1["x"], circle_1["y"], circle_1["r"]
   x2, y2, r2 = circle_2["x"], circle_2["y"], circle_2["r"]

   d = euclid_distance(x1, y1, x2, y2)
   r = radius_sum(r1, r2)
   if d > r:
       return {"intersects" : False, "intersections_count" : 0}
   elif d == r:
       return {"intersects" : True, "intersections_count" : 1}
   else:
       return {"intersects" : True, "intersetions_count" : 2}