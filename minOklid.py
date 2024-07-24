# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:10:43 2024

@author: Melike
"""

import math

# Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Öklid Mesafesi İçin Fonksiyon Tanımlama
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum Mesafenin Bulunması
min_distance = min(distances)

# Sonucun Yazdırılması
print("Minimum Öklid Mesafesi:", min_distance)
