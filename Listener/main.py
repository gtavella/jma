from Listener import Listener

listen1 = Listener()


@listen1.on
def dosomething1():
  print("start do something 1")
  # listen.excurr()
  dosomething2()
  print("end do something 1")


@listen1.on
def dosomething2():
  print("start do something 2")
  dosomething3()
  print("end do something 2")


@listen1.on
def dosomething3():
  print("start do something 3")
  # listen.exmast()
  listen1.excurr()
  print("end do something 3")



def main():
  print("start main")
  dosomething1()
  print("end main")


main()
