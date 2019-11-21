import pybullet as p
import time
import pybullet_data
import math

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
for i in range(10000):
    keyboardEvents = p.getKeyboardEvents()
    print("keyboardEvents = ", keyboardEvents)
    if len(keyboardEvents) != 0:
        if 106 in keyboardEvents:
            j_event = keyboardEvents[106]
            if j_event == 4:
                p.setJointMotorControlArray(bodyUniqueId=boxId,
                                            jointIndices=[ankle1, ankle2, ankle3, ankle4],
                                            controlMode=p.POSITION_CONTROL,
                                            targetPositions=[jointInfos[ankle1][8], jointInfos[ankle2][9], jointInfos[ankle3][9], jointInfos[ankle4][8]],
                                            forces=[maxForce, maxForce,maxForce, maxForce])
            if j_event == 1:
                p.setJointMotorControlArray(bodyUniqueId=boxId,
                                            jointIndices=[ankle1, ankle2, ankle3, ankle4],
                                            controlMode=p.POSITION_CONTROL,
                                            targetPositions=[jointInfos[ankle1][9], jointInfos[ankle2][8], jointInfos[ankle3][8], jointInfos[ankle4][9]],
                                            forces=[maxForce, maxForce, maxForce, maxForce])

                #
        if 107 in keyboardEvents:
            j_event = keyboardEvents[107]
            if j_event == 1:
                p.setJointMotorControl2(bodyUniqueId=boxId,
                                        jointIndex=ankle1,
                                        controlMode=p.POSITION_CONTROL,
                                        targetPosition=-0.6,
                                        force=maxForce)
            if j_event == 4:
                p.setJointMotorControl2(bodyUniqueId=boxId,
                                        jointIndex=ankle1,
                                        controlMode=p.POSITION_CONTROL,
                                        targetPosition=0,
                                        force=maxForce)
        if 117 in keyboardEvents:
            j_event = keyboardEvents[117]
            if j_event == 1:
                p.setJointMotorControl2(bodyUniqueId=boxId,
                                        jointIndex=hip1,
                                        controlMode=p.VELOCITY_CONTROL,
                                        targetVelocity=-100,
                                        force=maxForce)
            if j_event == 4:
                p.setJointMotorControl2(bodyUniqueId=boxId,
                                        jointIndex=hip1,
                                        controlMode=p.VELOCITY_CONTROL,
                                        targetVelocity=0,
                                        force=maxForce)

                #
        if 105 in keyboardEvents:
            j_event = keyboardEvents[105]
            if j_event == 1:
                p.setJointMotorControl2(bodyUniqueId=boxId,
                                        jointIndex=hip1,
                                        controlMode=p.VELOCITY_CONTROL,
                                        targetVelocity=100,
                                        force=maxForce)
            if j_event == 4:
                p.setJointMotorControl2(bodyUniqueId=boxId,
                                        jointIndex=hip1,
                                        controlMode=p.VELOCITY_CONTROL,
                                        targetVelocity=0,
                                        force = maxForce)
        if 114 in keyboardEvents:
            j_event = keyboardEvents[114]
            if j_event == 1:
                p.restoreState(stateId=startStateId)

    print("jointState ankle1 = ", p.getJointState(boxId, ankle1))
    print("jointState hip1 = ", p.getJointState(boxId, hip1))

    p.stepSimulation()
    time.sleep(1. / 240.)
