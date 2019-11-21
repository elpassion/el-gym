import pybullet as p
import time
import pybullet_data
import math

physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
p.setGravity(0, 0, -10)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [1, 1, 0.5]
cubeStartPos2 = [-1, -1, 0.5]
cubeStartOrientation = p.getQuaternionFromEuler([0, 0, math.pi])
cubeStartOrientation2 = p.getQuaternionFromEuler([0, 0, 0])
boxId = p.loadURDF("r2d2.urdf", cubeStartPos, cubeStartOrientation)
boxId2 = p.loadURDF("r2d2.urdf", cubeStartPos2, cubeStartOrientation2)
jointsNum = p.getNumJoints(boxId)
print("jointsNum = ", jointsNum)

LEFT_WHEEL_ID = [6, 7]
RIGHT_WHEEL_ID = [2, 3]
GRIPPER_ID = 8
maxForce = 50

for index in range(jointsNum):
    jointInfo = p.getJointInfo(boxId, index)
    print("jointInfo = ", jointInfo)

p.setJointMotorControl2(bodyUniqueId=boxId,
                        jointIndex=GRIPPER_ID,
                        controlMode=p.VELOCITY_CONTROL,
                        targetVelocity=0,
                        force=maxForce)
p.setJointMotorControlArray(bodyUniqueId=boxId,
                            jointIndices=LEFT_WHEEL_ID,
                            controlMode=p.VELOCITY_CONTROL,
                            targetVelocities=[0, 0],
                            forces=[maxForce, maxForce])
p.setJointMotorControlArray(bodyUniqueId=boxId,
                            jointIndices=RIGHT_WHEEL_ID,
                            controlMode=p.VELOCITY_CONTROL,
                            targetVelocities=[0, 0],
                            forces=[maxForce, maxForce])

for i in range(10000):
    p.stepSimulation()
    keyboardEvents = p.getKeyboardEvents()
    print("keyboardEvents = ", keyboardEvents)
    if len(keyboardEvents) != 0:
        if 106 in keyboardEvents:
            j_event = keyboardEvents[106]
            if j_event == 1:
                p.setJointMotorControlArray(bodyUniqueId=boxId,
                                            jointIndices=LEFT_WHEEL_ID,
                                            controlMode=p.VELOCITY_CONTROL,
                                            targetVelocities=[-100, -100],
                                            forces=[maxForce, maxForce])
            if j_event == 4:
                p.setJointMotorControlArray(bodyUniqueId=boxId,
                                            jointIndices=LEFT_WHEEL_ID,
                                            controlMode=p.VELOCITY_CONTROL,
                                            targetVelocities=[0, 0],
                                            forces=[maxForce, maxForce])

                #
        if 107 in keyboardEvents:
            j_event = keyboardEvents[107]
            if j_event == 1:
                p.setJointMotorControlArray(bodyUniqueId=boxId,
                                            jointIndices=RIGHT_WHEEL_ID,
                                            controlMode=p.VELOCITY_CONTROL,
                                            targetVelocities=[-100, -100],
                                            forces=[maxForce, maxForce])
            if j_event == 4:
                p.setJointMotorControlArray(bodyUniqueId=boxId,
                                            jointIndices=RIGHT_WHEEL_ID,
                                            controlMode=p.VELOCITY_CONTROL,
                                            targetVelocities=[0, 0],
                                            forces=[maxForce, maxForce])
        if 117 in keyboardEvents:
            j_event = keyboardEvents[117]
            if j_event == 1:
                p.setJointMotorControlArray(bodyUniqueId=boxId,
                                            jointIndices=LEFT_WHEEL_ID,
                                            controlMode=p.VELOCITY_CONTROL,
                                            targetVelocities=[100, 100],
                                            forces=[maxForce, maxForce])
            if j_event == 4:
                p.setJointMotorControlArray(bodyUniqueId=boxId,
                                            jointIndices=LEFT_WHEEL_ID,
                                            controlMode=p.VELOCITY_CONTROL,
                                            targetVelocities=[0, 0],
                                            forces=[maxForce, maxForce])

                #
        if 105 in keyboardEvents:
            j_event = keyboardEvents[105]
            if j_event == 1:
                p.setJointMotorControlArray(bodyUniqueId=boxId,
                                            jointIndices=RIGHT_WHEEL_ID,
                                            controlMode=p.VELOCITY_CONTROL,
                                            targetVelocities=[100, 100],
                                            forces=[maxForce, maxForce])
            if j_event == 4:
                p.setJointMotorControlArray(bodyUniqueId=boxId,
                                            jointIndices=RIGHT_WHEEL_ID,
                                            controlMode=p.VELOCITY_CONTROL,
                                            targetVelocities=[0, 0],
                                            forces=[maxForce, maxForce])

        if 108 in keyboardEvents:
            j_event = keyboardEvents[108]
            if j_event == 1:
                p.setJointMotorControl2(bodyUniqueId=boxId,
                                        jointIndex=GRIPPER_ID,
                                        controlMode=p.VELOCITY_CONTROL,
                                        targetVelocity=-100,
                                        force=maxForce)
            if j_event == 4:
                p.setJointMotorControl2(bodyUniqueId=boxId,
                                        jointIndex=GRIPPER_ID,
                                        controlMode=p.VELOCITY_CONTROL,
                                        targetVelocity=100,
                                        force=maxForce)
        if 65295 in keyboardEvents:
            j_event = keyboardEvents[65295]
            if j_event == 1:
                p.setJointMotorControlArray(bodyUniqueId=boxId2,
                                            jointIndices=LEFT_WHEEL_ID,
                                            controlMode=p.VELOCITY_CONTROL,
                                            targetVelocities=[-100, -100],
                                            forces=[maxForce, maxForce])
            if j_event == 4:
                p.setJointMotorControlArray(bodyUniqueId=boxId2,
                                            jointIndices=LEFT_WHEEL_ID,
                                            controlMode=p.VELOCITY_CONTROL,
                                            targetVelocities=[0, 0],
                                            forces=[maxForce, maxForce])

                #
        if 65296 in keyboardEvents:
            j_event = keyboardEvents[65296]
            if j_event == 1:
                p.setJointMotorControlArray(bodyUniqueId=boxId2,
                                            jointIndices=RIGHT_WHEEL_ID,
                                            controlMode=p.VELOCITY_CONTROL,
                                            targetVelocities=[-100, -100],
                                            forces=[maxForce, maxForce])
            if j_event == 4:
                p.setJointMotorControlArray(bodyUniqueId=boxId2,
                                            jointIndices=RIGHT_WHEEL_ID,
                                            controlMode=p.VELOCITY_CONTROL,
                                            targetVelocities=[0, 0],
                                            forces=[maxForce, maxForce])
        if 65298 in keyboardEvents:
            j_event = keyboardEvents[65298]
            if j_event == 1:
                p.setJointMotorControl2(bodyUniqueId=boxId2,
                                        jointIndex=GRIPPER_ID,
                                        controlMode=p.VELOCITY_CONTROL,
                                        targetVelocity=-100,
                                        force=maxForce)
            if j_event == 4:
                p.setJointMotorControl2(bodyUniqueId=boxId2,
                                        jointIndex=GRIPPER_ID,
                                        controlMode=p.VELOCITY_CONTROL,
                                        targetVelocity=100,
                                        force=maxForce)

                    #
            print("j_event = ", j_event)
    time.sleep(1. / 240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos, cubeOrn)
p.disconnect()