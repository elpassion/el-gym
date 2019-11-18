import pybullet_envs.bullet as bullet

env = bullet.minitaur_gym_env.MinitaurBulletEnv(render=True)
# env = bullet.racecarGymEnv.RacecarGymEnv(isDiscrete=False, renders=True)

env.reset()
for _ in range(1000):
    env.step(env.action_space.sample()) # take a random action
env.close()