import asyncio
import json


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888,
                                                   loop=loop)
    print('Send: %r' % message)
    writer.write(json.dumps(message).encode('utf-8'))

    response = await reader.read()
    parsed_response = json.loads(response.decode('utf-8'))
    print('Received: %r' % parsed_response)
    print('Close the socket')
    writer.close()


message = [{
    "request_id": "01",
    "data": "Hub&&name&&qwe&&id&&123&&%%Device&&name&&wqe&&id&&234&&"
}, {
    "request_id": "02",
    "data": "Hub&&name&&qwe&&id&&123&&%%Device&&name&&wqe&&id&&234&&"
}, {
    "request_id": "03",
    "data": "Hub&&name&&qwe&&id&&123&&%%Device&&name&&wqe&&id&&234&&"
}]

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for item in message:
        loop.run_until_complete(tcp_echo_client(item, loop))
    loop.close()
