import time

import pybullet as p
import pybullet_data

from experiments.events import EventProvider


def main():
    physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
    p.setGravity(0, 0, -10)
    planeId = p.loadURDF("plane.urdf")
    cubeStartPos = [0, 0, 1]
    cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
    boxId = p.loadURDF("r2d2.urdf", cubeStartPos, cubeStartOrientation)
    # boxId2 = p.loadMJCF("ant2.xml", 0, 0)
    # boxId3 = p.loadMJCF("ant2.xml", 0, 0)
    # boxId5 = p.loadMJCF("mjcf/swimmer.xml", 0, 0)

    with EventProvider() as provider:
        for i in range(10000):
            event = provider.pop_event()
            if event:
                command = event['value']
                print(f'Received command: {command}')
            p.stepSimulation()
            time.sleep(1. / 240.)
    p.disconnect()

if __name__ == '__main__':
    main()

