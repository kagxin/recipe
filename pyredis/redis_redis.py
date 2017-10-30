import redis


def handler(message):
    print(message)

def handler2(message):
    print('msg2:{}'.format(message))

if __name__ == '__main__':

    r = redis.Redis(host='localhost', port=6379, db=0)
    p = r.pubsub()
    p.subscribe(**{'channel1': handler})
    # p.subscribe(**{'channel1': handler2})


    thread = p.run_in_thread(sleep_time=0.001)

    r.publish('channel1', 'this will reach the listener')

