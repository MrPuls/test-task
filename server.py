import asyncio
from random import randint
from helpers import parse_request


async def handle_echo(reader, writer):
    data = await reader.read(120)
    message = data.decode('utf-8')
    address = writer.get_extra_info('peername')
    print("Received %r from %r" % (message, address))
    parsed_message = parse_request(message)
    await asyncio.sleep(randint(1, 5))
    print("Send: %r" % parsed_message)
    writer.write(parsed_message.encode('utf-8'))
    await writer.drain()
    writer.close()
    print("writer closed")


loop = asyncio.get_event_loop()
coroutine = asyncio.start_server(handle_echo, '127.0.0.1', 8888, loop=loop)
server = loop.run_until_complete(coroutine)

print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

