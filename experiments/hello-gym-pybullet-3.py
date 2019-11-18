import gym
import time
import pybullet_envs
env = gym.make("HumanoidBulletEnv-v0")
aspace = env.action_space
ospace = env.observation_space
print("Action space is {}".format(aspace))
print("Observation space is {}".format(ospace))
env.render(mode="human")
env.reset()
while True:
    env.render(mode="human")
    time.sleep(0.01)
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
env.close()