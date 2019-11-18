import gym
import time
import pybullet_envs
env = gym.make("AntBulletEnv-v0")
# env = gym.make("HalfCheetahBulletEnv-v0")
# env = gym.make("HopperBulletEnv-v0")
# env = gym.make("HumanoidBulletEnv-v0")
# env = gym.make("Walker2DBulletEnv-v0")
# env = gym.make("InvertedDoublePendulumBulletEnv-v0")
# env = gym.make("InvertedPendulumBulletEnv-v0")
# env = gym.make("MinitaurBulletEnv-v0")
# env = gym.make("RacecarBulletEnv-v0")
# env = gym.make("KukaBulletEnv-v0")
# env = gym.make("CartPoleBulletEnv-v1")
env.render(mode="human")
env.reset()
for _ in range(1000):
    env.render(mode="human")
    time.sleep(0.01)
    env.step(env.action_space.sample()) # take a random action
env.close()