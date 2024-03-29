import time

import pybullet as p
import pybullet_data

from experiments.events import EventProvider


class Player:
    id: int
    todo: list
    isBorn: bool
    isDead: bool

    def __init__(self):
        self.id = None
        self.todo = []
        self.isBorn = False
        self.isDead = False



HIP1 = 1
ANKLE1 = 3
HIP2 = 6
ANKLE2 = 8
HIP3 = 11
ANKLE3 = 13
HIP4 = 16
ANKLE4 = 18
MAX_FORCE = 1000

keyboardEvents = {}
jointInfos = []
anklesMaxPositions = {}
anklesMinPositions = {}
hipMinPositions = {}
hipMaxPositions = {}


def move_position(playerId, jointIndices, targetPositions):
    p.setJointMotorControlArray(bodyUniqueId=playerId,
                                jointIndices=jointIndices,
                                controlMode=p.POSITION_CONTROL,
                                targetPositions=targetPositions,
                                forces=[MAX_FORCE]*len(jointIndices))


def move_velocity(playerId, jointIndices, targetVelocity):
    p.setJointMotorControlArray(playerId,
                            jointIndices=jointIndices,
                            controlMode=p.VELOCITY_CONTROL,
                            targetVelocities=[targetVelocity] * len(jointIndices),
                            forces=[MAX_FORCE]*len(jointIndices))


def doCommand(playerid, command):
    if command == "first_ankles_go":
        move_position(playerid, [ANKLE1, ANKLE3], [anklesMinPositions[ANKLE1], anklesMinPositions[ANKLE3]])
    if command == "first_ankles_stop":
        move_position(playerid, [ANKLE1, ANKLE3], [anklesMaxPositions[ANKLE1], anklesMaxPositions[ANKLE3]])
    if command == "second_ankles_go":
        move_position(playerid, [ANKLE2, ANKLE4], [anklesMinPositions[ANKLE2], anklesMinPositions[ANKLE4]])
    if command == "second_ankles_stop":
        move_position(playerid, [ANKLE2, ANKLE4], [anklesMaxPositions[ANKLE2], anklesMaxPositions[ANKLE4]])
    if command == "first_hips_go":
        move_position(playerid, [HIP1, HIP3], [hipMinPositions[HIP1], hipMinPositions[HIP3]])
    if command == "first_hips_stop":
        move_position(playerid, [HIP1, HIP3], [hipMaxPositions[HIP1], hipMaxPositions[HIP3]])
    if command == "first_hips_0":
        move_position(playerid, [HIP1, HIP3], [0, 0])
    if command == "second_hips_go":
        move_position(playerid, [HIP2, HIP4], [hipMinPositions[HIP2], hipMinPositions[HIP4]])
    if command == "second_hips_stop":
        move_position(playerid, [HIP2, HIP4], [hipMaxPositions[HIP2], hipMaxPositions[HIP4]])
    if command == "second_hips_0":
        move_position(playerid, [HIP2, HIP4], [0, 0])

    if command in ["p:top:left", "p:top", "p:left", "p:center"]: move_velocity(playerid, [ANKLE2], -100)
    if command in ["r:top:left", "r:top", "r:left", "r:center"]: move_velocity(playerid, [ANKLE2], 100)

    if command in ["p:top:right", "p:top", "p:right", "p:center"]: move_velocity(playerid, [ANKLE1], 100)
    if command in ["r:top:right", "r:top", "r:right", "r:center"]: move_velocity(playerid, [ANKLE1], -100)

    if command in ["p:bottom:left", "p:bottom", "p:left", "p:center"]: move_velocity(playerid, [ANKLE3], -100)
    if command in ["r:bottom:left", "r:bottom", "r:left", "r:center"]: move_velocity(playerid, [ANKLE3], 100)
    if command in ["p:bottom:right", "p:bottom", "p:right", "p:center"]: move_velocity(playerid, [ANKLE4], 100)
    if command in ["r:bottom:right", "r:bottom", "r:right", "r:center"]: move_velocity(playerid, [ANKLE4], -100)


def updateEnv(players):
    global jointInfos
    for (name, player) in players.items():
        if player.isDead:
            if player.id is not None:
                p.removeBody(player.id)
                player.id = None
        elif not player.isBorn:
            player.id = p.loadMJCF("ant2.xml", 0, 0)[0]
            player.isBorn = True
        else:
            for command in player.todo: doCommand(player.id, command)
            player.todo.clear()


def pressed(key):
    global keyboardEvents
    return ord(key) in keyboardEvents and keyboardEvents[ord(key)] == 1


def released(key):
    global keyboardEvents
    return ord(key) in keyboardEvents and keyboardEvents[ord(key)] == 4


def main():
    global jointInfos
    global anklesMinPositions
    global anklesMaxPositions
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -6)
    p.loadURDF("sphere2.urdf", globalScaling=29, useFixedBase=1, basePosition=[0, 0, -14.1])

    startStateId = p.saveState()

    players = {"Master": Player()}
    updateEnv(players)

    for index in range(p.getNumJoints(players["Master"].id)):
        jointInfo = p.getJointInfo(players["Master"].id, index)
        jointInfos.append(jointInfo)

    anklesMinPositions[ANKLE1] = jointInfos[ANKLE1][9]
    anklesMinPositions[ANKLE2] = jointInfos[ANKLE2][8]
    anklesMinPositions[ANKLE3] = jointInfos[ANKLE3][8]
    anklesMinPositions[ANKLE4] = jointInfos[ANKLE4][9]
    anklesMaxPositions[ANKLE1] = jointInfos[ANKLE1][8]
    anklesMaxPositions[ANKLE2] = jointInfos[ANKLE2][9]
    anklesMaxPositions[ANKLE3] = jointInfos[ANKLE3][9]
    anklesMaxPositions[ANKLE4] = jointInfos[ANKLE4][8]
    hipMinPositions[HIP1] = jointInfos[HIP1][9]
    hipMinPositions[HIP2] = jointInfos[HIP2][8]
    hipMinPositions[HIP3] = jointInfos[HIP3][8]
    hipMinPositions[HIP4] = jointInfos[HIP4][9]
    hipMaxPositions[HIP1] = jointInfos[HIP1][8]
    hipMaxPositions[HIP2] = jointInfos[HIP2][9]
    hipMaxPositions[HIP3] = jointInfos[HIP3][9]
    hipMaxPositions[HIP4] = jointInfos[HIP4][8]


    with EventProvider() as provider:
        p.setRealTimeSimulation(True)
        while True:

            updateEnv(players)

            event = provider.pop_event()
            if event:
                command = event['value']
                print(f'Received command: {command}')
                if event["name"] not in players:
                    players[event["name"]] = Player()
                else:
                    players[event["name"]].todo.append(event["value"])

            global keyboardEvents
            keyboardEvents = p.getKeyboardEvents()

            if pressed('1'): players["Master"].todo.append("first_ankles_go")
            if released('1'): players["Master"].todo.append("first_ankles_stop")
            if pressed('2'): players["Master"].todo.append("first_hips_go")
            if released('2'): players["Master"].todo.append("first_hips_0")
            if pressed('3'): players["Master"].todo.append("first_hips_stop")
            if released('3'): players["Master"].todo.append("first_hips_0")
            if pressed('4'): players["Master"].todo.append("second_ankles_go")
            if released('4'): players["Master"].todo.append("second_ankles_stop")
            if pressed('5'): players["Master"].todo.append("second_hips_go")
            if released('5'): players["Master"].todo.append("second_hips_0")
            if pressed('6'): players["Master"].todo.append("second_hips_stop")
            if released('6'): players["Master"].todo.append("second_hips_0")
            if pressed('j'): players["Master"].todo.append("p:left")
            if released('j'): players["Master"].todo.append("r:left")
            if pressed('k'): players["Master"].todo.append("p:center")
            if released('k'): players["Master"].todo.append("r:center")
            if pressed('l'): players["Master"].todo.append("p:right")
            if released('l'): players["Master"].todo.append("r:right")
            if pressed('i'): players["Master"].todo.append("p:top")
            if released('i'): players["Master"].todo.append("r:top")
            if pressed('m'): players["Master"].todo.append("p:bottom")
            if released('m'): players["Master"].todo.append("r:bottom")
            if pressed('d'): players["Master"].isDead = True

            if pressed('r'):
                for player in players.values(): player.isDead = True
                updateEnv(players)
                p.restoreState(stateId=startStateId)

            if pressed('\\'):
                p.setGravity(7, 1, -8)

            if pressed('q'):
                break

            if pressed('n'):
                if "Master" in players:
                    players["Master"].isDead = True
                    updateEnv(players)
                players["Master"] = Player()

            time.sleep(1. / 240.)


if __name__ == '__main__':
    main()
    p.disconnect()
