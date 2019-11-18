import gym
env = gym.make('CartPole-v0')
aspace = env.action_space
ospace = env.observation_space
print("Action space is {}".format(aspace))
print("Observation space is {}".format(ospace))
for i_episode in range(20):
    observation = env.reset()
    for t in range(1000):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()
