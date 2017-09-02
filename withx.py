
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


with WriteFile():
    print('test')
    # f = open('../test', 'w+')
    # f.write('saf')
    # f.close()

# print('exdit')