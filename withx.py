
class WriteFile:

    def __enter__(self):
        import sys
        self.origin_write = sys.stdout.write
        sys.stdout.write = self.monkey
        return

    def monkey(self, text):
        self.origin_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.origin_write
        return


# with WriteFile():
#     print('test')
    # f = open('../test', 'w+')
    # f.write('saf')
    # f.close()
# print('exdit')


import threading

class JustRunTimeoutCM(threading.Thread):
    """timeout之后，给上下文管理器中的，区块发送keyboard interrupt信号, 
    """
    def __init__(self, timeout=5):
        threading.Thread.__init__(self)
        self.timeout = timeout

    def run(self):
        import time
        try:
            import thread as thread
        except:
            import _thread as thread
        current_time = time.time()
        while time.time() < current_time + self.timeout:
            time.sleep(0.1)
        thread.interrupt_main()

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, *_):
        self.join()
        return exc_type is not None and issubclass(exc_type, KeyboardInterrupt)

if __name__ == '__main__':
    print('print begin.')

    with JustRunTimeoutCM(timeout=5):
        while True:
            import time
            time.sleep(1)
            print('alive...')

    print('print end.')    

