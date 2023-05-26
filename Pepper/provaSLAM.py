import naoqi as qi

# IP del robot Pepper
IP = "192.168.250.60"

# Porta di connessione
PORT = 9559

# Connessione al robot
session = qi.Session()
session.connect("tcp://" + IP + ":" + str(PORT))

# Ottenere il servizio di mappatura
mapping_service = session.service("ALMapping")

# Avviare la mappatura
mapping_service.startMapping(0.1)

# Fare muovere il robot per mappare l'ambiente
robot_movement_service = session.service("ALRobotPosture")
robot_movement_service.goToPosture("StandInit", 0.5)

# Fermare la mappatura
mapping_service.stopMapping()

# Ottenere la mappa
map_data = mapping_service.getMapsList()

# Disegnare la mappa
visualization_service = session.service("ALVisualization")
visualization_service.show(map_data[0])
