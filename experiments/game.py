import time

import pybullet as p
import pybullet_data
from typing import NamedTuple


class Player(NamedTuple):
    id: int
    name: str
    todo: list = []
    isBorn: bool = False
    isDead: bool = False


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


def move(players):
    print(players) #FIXME: remove
    global jointInfos
    for player in players.values():
        for command in player.todo:
            if command == "jump":
                p.setJointMotorControlArray(bodyUniqueId=player.id,
                                            jointIndices=[ANKLE1, ANKLE2, ANKLE3, ANKLE4],
                                            controlMode=p.POSITION_CONTROL,
                                            targetPositions=[jointInfos[ANKLE1][9], jointInfos[ANKLE2][8],
                                                             jointInfos[ANKLE3][8], jointInfos[ANKLE4][9]],
                                            forces=[MAX_FORCE, MAX_FORCE, MAX_FORCE, MAX_FORCE])
            if command == "rest":
                p.setJointMotorControlArray(bodyUniqueId=player.id,
                                            jointIndices=[ANKLE1, ANKLE2, ANKLE3, ANKLE4],
                                            controlMode=p.POSITION_CONTROL,
                                            targetPositions=[jointInfos[ANKLE1][8], jointInfos[ANKLE2][9],
                                                             jointInfos[ANKLE3][9], jointInfos[ANKLE4][8]],
                                            forces=[MAX_FORCE, MAX_FORCE, MAX_FORCE, MAX_FORCE])
            if command == "onelegdown":
                p.setJointMotorControl2(bodyUniqueId=player.id,
                                        jointIndex=ANKLE1,
                                        controlMode=p.POSITION_CONTROL,
                                        targetPosition=jointInfos[ANKLE1][8],
                                        force=MAX_FORCE)
            if command == "onelegup":
                p.setJointMotorControl2(bodyUniqueId=player.id,
                                    jointIndex=ANKLE1,
                                    controlMode=p.POSITION_CONTROL,
                                    targetPosition=jointInfos[ANKLE1][9],
                                    force=MAX_FORCE)

            if command == "onelegleft":
                p.setJointMotorControl2(bodyUniqueId=player.id,
                                        jointIndex=HIP1,
                                        controlMode=p.VELOCITY_CONTROL,
                                        targetVelocity=-100,
                                        force=MAX_FORCE)
            if command == "onelegright":
                p.setJointMotorControl2(bodyUniqueId=player.id,
                                        jointIndex=HIP1,
                                        controlMode=p.VELOCITY_CONTROL,
                                        targetVelocity=100,
                                        force=MAX_FORCE)
            if command == "onelegrest":
                p.setJointMotorControl2(bodyUniqueId=player.id,
                                        jointIndex=HIP1,
                                        controlMode=p.VELOCITY_CONTROL,
                                        targetVelocity=0,
                                        force=MAX_FORCE)
        player.todo.clear()


def pressed(key):
    global keyboardEvents
    return ord(key) in keyboardEvents and keyboardEvents[ord(key)] == 1


def released(key):
    global keyboardEvents
    return ord(key) in keyboardEvents and keyboardEvents[ord(key)] == 4


def main():
    global jointInfos
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -5)
    p.loadURDF("plane.urdf")
    masterId = p.loadMJCF("ant2.xml", 0, 0)[0]


    for index in range(p.getNumJoints(masterId)):
        jointInfo = p.getJointInfo(masterId, index)
        jointInfos.append(jointInfo)
        print("jointInfo = ", jointInfo)

    startStateId = p.saveState()

    players = {"Master": Player(masterId, "Master")}

    while True:

        move(players)

        global keyboardEvents
        keyboardEvents = p.getKeyboardEvents()

        if pressed('j'): players["Master"].todo.append("jump")
        if released('j'): players["Master"].todo.append("rest")
        if pressed('k'): players["Master"].todo.append("onelegdown")
        if released('k'): players["Master"].todo.append("onelegup")
        if pressed('u'): players["Master"].todo.append("onelegleft") #FIXME: or right??
        if released('u'): players["Master"].todo.append("onelegrest")
        if pressed('i'): players["Master"].todo.append("onelegright") #FIXME: or left??
        if released('i'): players["Master"].todo.append("onelegrest")

        if pressed('r'):
            p.restoreState(stateId=startStateId)

        if pressed('\\'):
            p.setGravity(7, 1, -8)

        if pressed('q'):
            break

        if pressed('n'):
            masterId = p.loadMJCF("ant2.xml", 0, 0)[0]

        print("jointState ankle1 = ", p.getJointState(masterId, ANKLE1))
        print("jointState hip1 = ", p.getJointState(masterId, HIP1))

        p.stepSimulation()
        time.sleep(1. / 240.)


if __name__ == '__main__':
    main()
