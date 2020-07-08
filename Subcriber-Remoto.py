import asyncio
from nats.aio.client import Client as NATS
from stan.aio.client import Client as STAN

async def error_cb(e):
    print("Error:", e)

async def run(loop):
    nc = NATS()
    sc = STAN()

    options = {
        "servers": ["nats://192.168.100.228:4222"],
        "io_loop": loop,
        "error_cb": error_cb
    }

    await nc.connect(**options)

    # Start session with NATS Streaming cluster using
    # the established NATS connection.
    #await nc.connect(io_loop=loop)
    await sc.connect("vsblty-cluster", "client-1235487854", nats=nc)

    # Example async subscriber
    async def cb(msg):
        print("Received a message (seq={}): {}".format(msg.seq, msg.data))

    # Subscribe to get all messages from the beginning.
    await sc.subscribe("greetings-Mijail", start_at='first', cb=cb)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.run_forever()