import asyncio
from nats.aio.client import Client as NATS
from stan.aio.client import Client as STAN
from datetime import datetime

# Numero Random
import random2
# GUID
import uuid 
# Request
import requests
import json

Url = "http://100.97.218.207:5080/FaceDetetion"

async def error_cb(e):
    print("Error:", e)


async def run(loop):
    nc = NATS()
    sc = STAN()
    #r = requests.get(Url)
    #print (r.json())
    options = {
        "servers": ["nats://192.168.100.228:4222"],
        "io_loop": loop,
        "error_cb": error_cb
    }

    await nc.connect(**options)


    # First connect to NATS, then start session with NATS Streaming.
    #await nc.connect(io_loop=loop)
    await sc.connect("vsblty-cluster", "client-Miajil-dev", nats=nc)

    # Periodically send a message
    i = 1
    while True:

        r = requests.get(Url)
        #encoded respuesta
        data_string = json.dumps(r.json())

        #now = datetime.now()
        #mensaje = str(" - " + str(i) + " Item - : " + str(now) + " Data: - " + str(decoded))
        mensaje = data_string
        #mensaje = str(Objeto)
        await sc.publish("greetings-Mijail", bytes(mensaje, 'utf8'))
        i +=1
        await asyncio.sleep(1, loop=loop)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.run_forever()