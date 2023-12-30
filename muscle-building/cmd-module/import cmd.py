import cmd

class MyCmd(cmd.Cmd):
  intro = "__Welcome to My Command Line Shell__"
  prompt = "==> "
  def do_quit(self, arg):
    exit(1)

MyCmd().cmdloop()

