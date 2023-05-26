import naoqi
from naoqi import ALProxy
import sys
import numpy
import cv2

ip_addr = "192.168.69.60"
port_num = 9559

mapping_service = ALProxy("ALNavigation", ip_addr, port_num)

error_code = mapping_service.explore(2)
if error_code != 0:
    print "Exploration failed."
    # Saves the exploration on disk
path = mapping_service.saveExploration()
print("Percorso " + path)


result_map = mapping_service.getMetricalMap()
map_width = result_map[1]
map_height = result_map[2]
img = numpy.array(result_map[4]).reshape(map_width, map_height)
img = (100 - img) * 2.55 # from 0..100 to 255..0
img = numpy.array(img, numpy.uint8)
cv2.imshow("mammt", img)
cv2.waitKey(0)
cv2.imwrite("mappa.png", img)