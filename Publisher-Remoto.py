import asyncio
from nats.aio.client import Client as NATS
from stan.aio.client import Client as STAN
from datetime import datetime


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


    # First connect to NATS, then start session with NATS Streaming.
    #await nc.connect(io_loop=loop)
    await sc.connect("vsblty-cluster", "client-Miajil-dev", nats=nc)

    # Periodically send a message
    i = 1
    while True:
        Objeto = '{"detections": [ { “Temperature”:”98.6”, "FaceDetector": { "confidence": 0.9998735189437866, "image_id": 0.0, "label": 1, "position": [ 132, 41], "size": [ 222, 303 ] }, "LandmarksDetector": { "left_eye": [ 134, 147], "left_lip_corner": [136, 242], "nose_tip": [210,204],"right_eye": [ 300,145],"right_lip_corner": [ 307, 240]}, "PoseEstimator": { "ypr": [-3.50416898727417, 3.2856898307800293, -0.45209193229675293 ]}, “FrameTimestamp”:UTC Time}'
        now = datetime.now()
        mensaje = str(" - " + str(i) + " Item - : " + str(now))
        #mensaje = str(Objeto)
        await sc.publish("greetings-Mijail", bytes(mensaje, 'utf8'))
        i +=1
        await asyncio.sleep(1, loop=loop)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.run_forever()