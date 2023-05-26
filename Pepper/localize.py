import naoqi
from naoqi import ALProxy
import sys


def main(navigation_service):
    """
    This example uses localization methods.
    """

    #METTI TUTTO SU TRY FINALLY CON STOPEXPLORATION NEL FINALLY

    # Get the services ALNavigation and ALMotion.
    navigation_service.stopLocalization()
    # Load a previously saved exploration
    #exploration_file = "Map_Lab.explo"
    exploration_file = "Corridoio.explo"
    navigation_service.loadExploration(exploration_file)

    # Relocalize the robot and start the localization process.
    guess = [3., 0., 0] # assuming the robot is not far from the place where
                     # he started the loaded exploration.
    navigation_service.relocalizeInMap(guess)
    navigation_service.startLocalization()

    # Navigate to another place in the map
    navigation_service.navigateToInMap([0., 0., 0.])

    # Check where the robot arrived
    position = navigation_service.getRobotPositionInMap()
    print(len(position))
    for i in range(0,len(position)):
        print(i,position[i])

    print "I reached: " + str(navigation_service.getRobotPositionInMap()[0])

    # Stop localization
    navigation_service.stopLocalization()

if __name__ == "__main__":
    ip_addr = "192.168.137.104"
    port_num = 9559

    # Ottenere il servizio di mappatura
    mapping_service = ALProxy("ALNavigation", ip_addr, port_num)
    main(mapping_service)