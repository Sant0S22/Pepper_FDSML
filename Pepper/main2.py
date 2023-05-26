import naoqi
from naoqi import ALProxy
import sys
import numpy as np
import cv2

ip_addr = "192.168.69.60"
port_num = 9559


# Ottenere il servizio di mappatura
mapping_service = ALProxy("ALNavigation", ip_addr, port_num)

# Avviare la mappatura
mapping_service.startMapping(0.1)

# Fare muovere il robot per mappare l'ambiente
robot_movement_service = ALProxy("ALRobotPosture")
robot_movement_service.goToPosture("StandInit", 0.5)

# Fermare la mappatura
mapping_service.stopMapping()

# Ottenere la mappa
map_data = mapping_service.getMapsList()

# Disegnare la mappa
visualization_service = ALProxy("ALVisualization")
visualization_service.show(map_data[0])
