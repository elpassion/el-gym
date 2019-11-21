import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
p.setGravity(0, 0, -10)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [0, 0, 0.5]
cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
boxId = p.loadURDF("r2d2.urdf", cubeStartPos, cubeStartOrientation)
jointsNum = p.getNumJoints(boxId)
print("jointsNum = ", jointsNum)

LEFT_WHEEL_ID = [6, 7]
RIGHT_WHEEL_ID = [2, 3]
GRIPPER_ID = 8
maxForce = 10

for index in range(jointsNum):
    jointInfo = p.getJointInfo(boxId, index)
    print("jointInfo = ", jointInfo)

    p.setJointMotorControl2(bodyUniqueId=boxId,
                            jointIndex=3,
                            controlMode=p.VELOCITY_CONTROL,
                            targetVelocity=-100,
                            force=maxForce)
    # p.setJointMotorControl2(bodyUniqueId=boxId,
    #                         jointIndex=2,
    #                         controlMode=p.VELOCITY_CONTROL,
    #                         targetVelocity=-100,
    #                         force=maxForce)
    # p.setJointMotorControl2(bodyUniqueId=boxId,
    #                         jointIndex=6,
    #                         controlMode=p.VELOCITY_CONTROL,
    #                         targetVelocity=-100,
    #                         force=maxForce)
    # p.setJointMotorControl2(bodyUniqueId=boxId,
    #                         jointIndex=7,
    #                         controlMode=p.VELOCITY_CONTROL,
    #                         targetVelocity=-100,
    #                         force=maxForce)

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

                    #
            print("j_event = ", j_event)
    time.sleep(1. / 240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos, cubeOrn)
p.disconnect()