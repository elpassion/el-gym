import time

import pybullet as p
import pybullet_data

physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
p.setGravity(0, 0, -5)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [1, 1, 0.5]
cubeStartPos2 = [-1, -1, 0.5]
boxId = p.loadMJCF("ant2.xml", 0, 0)[0]
jointsNum = p.getNumJoints(boxId)

hip1 = 1
ankle1 = 3
hip2 = 6
ankle2 = 8
hip3 = 11
ankle3 = 13
hip4 = 16
ankle4 = 18
maxForce = 1000

jointInfos = []
for index in range(jointsNum):
    jointInfo = p.getJointInfo(boxId, index)
    jointInfos.append(jointInfo)
    print("jointInfo = ", jointInfo)

print(jointInfos[ankle1][9])

startStateId = p.saveState()
for i in range(1000000):

    keyboardEvents = p.getKeyboardEvents()

    def pressed(key):
        return ord(key) in keyboardEvents and keyboardEvents[ord(key)] == 1

    def released(key):
        return ord(key) in keyboardEvents and keyboardEvents[ord(key)] == 4

    if released('j'):
        p.setJointMotorControlArray(bodyUniqueId=boxId,
                                    jointIndices=[ankle1, ankle2, ankle3, ankle4],
                                    controlMode=p.POSITION_CONTROL,
                                    targetPositions=[jointInfos[ankle1][8], jointInfos[ankle2][9], jointInfos[ankle3][9], jointInfos[ankle4][8]],
                                    forces=[maxForce, maxForce,maxForce, maxForce])
    if pressed('j'):
        p.setJointMotorControlArray(bodyUniqueId=boxId,
                                    jointIndices=[ankle1, ankle2, ankle3, ankle4],
                                    controlMode=p.POSITION_CONTROL,
                                    targetPositions=[jointInfos[ankle1][9], jointInfos[ankle2][8], jointInfos[ankle3][8], jointInfos[ankle4][9]],
                                    forces=[maxForce, maxForce, maxForce, maxForce])

    if pressed('k'):
        p.setJointMotorControl2(bodyUniqueId=boxId,
                                jointIndex=ankle1,
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=jointInfos[ankle1][8],
                                force=maxForce)
    if released('k'):
        p.setJointMotorControl2(bodyUniqueId=boxId,
                                jointIndex=ankle1,
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=jointInfos[ankle1][9],
                                force=maxForce)

    if pressed('u'):
            p.setJointMotorControl2(bodyUniqueId=boxId,
                                    jointIndex=hip1,
                                    controlMode=p.VELOCITY_CONTROL,
                                    targetVelocity=-100,
                                    force=maxForce)
    if released('k'):
        p.setJointMotorControl2(bodyUniqueId=boxId,
                                jointIndex=hip1,
                                controlMode=p.VELOCITY_CONTROL,
                                targetVelocity=0,
                                force=maxForce)

    if pressed('i'):
        p.setJointMotorControl2(bodyUniqueId=boxId,
                                jointIndex=hip1,
                                controlMode=p.VELOCITY_CONTROL,
                                targetVelocity=100,
                                force=maxForce)
    if released('i'):
        p.setJointMotorControl2(bodyUniqueId=boxId,
                                jointIndex=hip1,
                                controlMode=p.VELOCITY_CONTROL,
                                targetVelocity=0,
                                force = maxForce)

    if pressed('r'):
        p.restoreState(stateId=startStateId)

    if pressed('\\'):
        p.setGravity(7, 1, -8)

    if pressed('q'):
        break

    if pressed('n'):
        boxId = p.loadMJCF("ant2.xml", 0, 0)[0]

    print("jointState ankle1 = ", p.getJointState(boxId, ankle1))
    print("jointState hip1 = ", p.getJointState(boxId, hip1))

    p.stepSimulation()
    time.sleep(1. / 240.)


