from cmd import Cmd

class MyCMD(Cmd):
    prompt = '(cmd)'
    intro = 'just for test cmd!'
    
    def do_foo(self, args):
        print(args)

    def do_show(self, arg):
        """just show xiaoming name or age.
           show name 
           show age
        """
        data = {'name':'xiaoming', 'age':123}
        if arg in data.keys():
            print(data[arg])
    def complete_show(self, text, line, begidx, endidx):
        print(text, line, begidx, endidx)
        if not text:
            context = ['foo', 'show']
        elif text == 's':
            context = ['show']
        elif text == 'f':
            context = ['foo']
        return context
            

    def do_help(self, arg):
        super().do_help(arg)
        print('you can:\n    ?show')

    def do_shell(self, arg):
        print('do shell!{}'.format(arg))
        
    def do_bye(self, arg):
        pass

if __name__ == '__main__':

    MyCMD().cmdloop()

