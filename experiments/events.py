import asyncio
import json
import threading
from contextlib import ContextDecorator

import websockets

class EventProvider(ContextDecorator):
    def __init__(self):
        self.events = []
        self.socket = None
        self.stopped = False

    async def fetch_events(self):
        uri = 'wss://api.asapdeploy.com/ws/commands/'
        async with websockets.connect(uri) as socket:
            print('Connected!')
            while not self.stopped:
                received = await socket.recv()
                value = json.loads(received.decode('utf-8'))
                print(f'Received {value}')
                self.events.append(value)

    def __enter__(self):
        def do_work():
            loop = asyncio.new_event_loop()
            loop.run_until_complete(self.fetch_events())

        thread = threading.Thread(target=do_work)
        thread.start()
        return self

    def __exit__(self, *exc):
        self.stopped = True
        return False

    def pop_event(self):
        if self.events:
            return self.events.pop(0)
        return None
