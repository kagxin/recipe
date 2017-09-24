import asyncio
import os


def reader(fd):

    data = f_instance.read(1024)
    print(data)

fd = open('/tmp/my_fifo')

loop = asyncio.get_event_loop()
loop.add_reader(fd, reader, fd)
loop.run_forever()
f.close()
loop.close()
    
    
