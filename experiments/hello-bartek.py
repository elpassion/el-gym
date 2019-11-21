import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
p.setGravity(0, 0, -10)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [0, 1, 1]
cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
boxId = p.loadMJCF("mjcf/ant.xml", -5, 0)[0]
boxId2 = p.loadMJCF("mjcf/ant.xml", 0, 0)[0]
boxId = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)
print("boxId = ", boxId)
jointsNum = p.getNumJoints(boxId)
print("jointsNum = ", jointsNum)
for index in range(jointsNum):
    jointInfo = p.getJointInfo(boxId, index)
    print("jointInfo = ", jointInfo)
#
# maxForce = 1
# p.setJointMotorControl2(bodyUniqueId=boxId,
#                         jointIndex=3,
#                         controlMode=p.VELOCITY_CONTROL,
#                         targetVelocity=-100,
#                         force=maxForce)
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
# p.setJointMotorControl2(bodyUniqueId=boxId,
#                         jointIndex=8,
#                         controlMode=p.VELOCITY_CONTROL,
#                         targetVelocity=-10,
#                         force=maxForce)

for i in range(10000):
    # if i == 500:
    #     p.setJointMotorControl2(bodyUniqueId=boxId,
    #                             jointIndex=8,
    #                             controlMode=p.TORQUE_CONTROL,
    #                             targetVelocity=10,
    #                             force=maxForce)
    p.stepSimulation()
    time.sleep(1. / 240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos, cubeOrn)
p.disconnect()
