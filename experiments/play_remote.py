import gym, time
from experiments.events import EventProvider

action = 0
env = gym.make('Pong-ram-v0')
env.reset()


def run():
    global action
    with EventProvider('2') as provider:
        while True:
            env.render()
            env.step(action)

            event = provider.pop_event()
            if event:
                value = event['value']
                if value == 'p:top':
                    step_action(2)
                if value == 'p:bottom':
                    step_action(3)
                if value == 'r:top' or value == 'r:bottom':
                    step_action(0)

            time.sleep(0.07)


def step_action(action_key):
    global action
    action = action_key
    env.step(action)


run()
