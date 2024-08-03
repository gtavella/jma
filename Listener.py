"""
Controls the flow.
A function can stop itself or the master.
This allows for more elegant, expressive code, 
without weird return statements or complicated 
internal state logic. 

All you need to do is decorate the interested functions
with @listen.on 

Then inside the function, simply do this:
listen.exitcurrfn = True
to exit the current function exactly at this moment.

Or use 
listen.exitmastern = True
to exit the master function, which is the 
very first function. 

This helps you control function flow without relying
on weird internal state mechanisms or complicated logic.
"""

# upon updating the exitcurrfn attribute,
# the function where this attribute is updated
# will be exited?

# the idea is not to run an infinite loop (while True), 
# but to signal when to stop the loop by raising an exception
# since an exception naturally bubbles up to be caught,
# this is the perfect situation to implement the mechanism
# whereby updating a managed attribute value will artificially 
# raise an exception, which is the only way to naturally,
# truly interrupt the program flow



class ExitCurrFn(Exception):
  def __init__(self, msg=None) -> None:
    if msg is None:
      self._errormsg = "info: exit current func"
    else:
      self._errormsg = msg

  @property
  def errormsg(self):
    return self._errormsg

  @errormsg.setter
  def errormsg(self, msg):
    self._errormsg = msg
  
  def __str__(self) -> str:
    return self._errormsg



class ExitMasterFn(Exception):
  def __init__(self, msg=None) -> None:
    if msg is None:
      self._errormsg = "info: exit master func"
    else:
      self._errormsg = msg

  @property
  def errormsg(self):
    return self._errormsg

  @errormsg.setter
  def errormsg(self, msg):
    self._errormsg = msg

  def __str__(self) -> str:
    return self._errormsg
  




class Listener:
  def __init__(self) -> None:
    self._exitcurrfn = False
    self._exitmasterfn = False
    self._master_passed = False
    # the master function
    self._masterfunc = None

  # exit current func

  @property
  def exitcurrfn(self):
    return self._exitcurrfn

  @exitcurrfn.setter
  def exitcurrfn(self, exit):
    if exit:
      raise ExitCurrFn
    self._exitcurrfn = exit

  # exit master func
  
  @property
  def exitmasterfn(self):
    return self._exitmasterfn

  @exitmasterfn.setter
  def exitmasterfn(self, exit):
    if exit:
      raise ExitMasterFn
    self._exitmasterfn = exit

  # 'event' listeners 

  def on(self, func):
    def newfunc(*args, **kw):
      # this is local, is reset for each function frame
      is_this_master = False
      currerrtype = None

      # by reference, persists across function frames
      if not self._master_passed:
          # once you set this true, it will be true
          # only for each function frame 
          is_this_master = True
          # as long as the program lives 
          self._master_passed = True

          # save the master
          self._masterfunc = func
        
      try:
        func(*args, **kw)
        
      except ExitCurrFn as e:
        currerrtype = ExitCurrFn
        self.after_exitcurrfn(func, e)
        
      except ExitMasterFn as e:
        currerrtype = ExitMasterFn
        if not is_this_master:
          raise e
        self.after_exitmasterfn(func, e)
        
      except Exception as e:
        print("another error occurred")
        
      finally:
        if is_this_master and currerrtype is ExitMasterFn:
          # print("reached master func")
          pass
          
    return newfunc

  def after_exitcurrfn(self, func, err):
    err.errormsg = f"exit current func '{func.__name__}'"
    print(err)

  def after_exitmasterfn(self, func, err):
    err.errormsg = f"exit master func '{func.__name__}'"
    print(err)


listen = Listener()



@listen.on
def dosomething1():
  print("start do something 1")
  # listen.exitcurrfn = True
  dosomething2()
  print("should not be reached in do something 1")


@listen.on
def dosomething2():
  print("start do something 2")
  # listen.exitmasterfn = True
  dosomething3()
  # listen.exitcurrfn = True
  print("should not be reached in do something 2")



@listen.on
def dosomething3():
  print("start do something 3")
  listen.exitmasterfn = True
  listen.exitcurrfn = True
  print("should not be reached in do something 3")

# be careful when applying 
# listen.exitcurrfn = True
# to a function that is not being listened to
# in the sense, where there's not @listen.on
# if you apply listen.exitcurrfn = True
# on such an undecorated function, 
# the last decorated function will be 
# considered as the current on



def main():
  print("start main")
  dosomething1()
  print("end main")


main()
