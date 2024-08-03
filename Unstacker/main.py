from Unstacker import Unstacker

unstacker = Unstacker()


def cool_decorator(func):
  def newfunc(*args, **kw):
    print("in decorator, before")
    func(*args, **kw)
    print("in decorator, after")
  return newfunc


@unstacker.add
def dosomething1():
  print("start 1")
  # bstack.resume_master()
  dosomething2()
  print("end 1")


@unstacker.add
def dosomething2():
  print("start 2")
  # bstack.resume_master()
  dosomething3()
  print("end 2")



@unstacker.add
def dosomething3():
  print("start 3")
  # bstack.back(10)
  dosomething4()
  # bstack.resume_master()
  # bstack.exit_current()
  # bstack.exit_current()
  print("end 3")


@unstacker.add
def dosomething4():
  print("start 4")
  dosomething5()
  # bstack.back(3)
  # bstack.exit_master()
  # bstack.resume_master()
  # bstack.exit_current()
  # bstack.exit_current()
  print("end 4")


@unstacker.add
# @cool_decorator
def dosomething5():
  print("start 5")
  # unstacker.back(1)
  dosomething6()
  # bstack.back(3)
  # bstack.resume_master()
  # bstack.exit_current()
  # bstack.exit_current()
  print("end 5")


@unstacker.add
def dosomething6():
  print("start 6")
  # unstacker.back(3)
  dosomething7()
  # unstacker.exit_master()
  # unstacker.resume_master()
  # bstack.exit_current()
  # bstack.exit_current()
  print("end 6")


@unstacker.add
def dosomething7():
  print("start 7")
  print("end 7")


def main():
  print("start main")
  dosomething1()
  print("end main")


main()
