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

How to use:
- Since there's only one master function, I can avoid 
decorating all other functions
- However if I want to exit the current function,
you must decorate it. If you do not decorate it, 
when you listen.excurr() you will effectively exit the last
function. So running listen.excurr() on an undecorated function
is equivalent to applying listen.excurr() to the last correctly
decorated function
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

# be careful when applying 
# listen.exitcurrfn = True
# to a function that is not being listened to
# in the sense, where there's not @listen.on
# if you apply listen.exitcurrfn = True
# on such an undecorated function, 
# the last decorated function will be 
# considered as the current on


class Listener:
  def __init__(self) -> None:
    self._master_passed = False

  # exit current func

  def excurr(self):
    raise ExitCurrFn

  def exmast(self):
    raise ExitMasterFn


  # 'event' listeners 

  def on(self, func):
    def newfunc(*args, **kw):
      # is the current function the master function?
      # this is local, is reset for each function frame
      is_master = False
      currerrtype = None
      # if the master has not passed, then 
      # this function is exactly the master
      # it also means that the master has just passed
      # by reference, persists across function frames
      if not self._master_passed:
          # once you set this true, it will be true
          # only for each function frame 
          is_master = True
          # as long as the program lives 
          self._master_passed = True

      try:
        func(*args, **kw)

      except ExitCurrFn as e:
        currerrtype = ExitCurrFn
        self.after_exitcurrfn(func, e)

      except ExitMasterFn as e:
        currerrtype = ExitMasterFn
        # re-raising the error means exiting any
        # function frame (including) the master function frame
        if not is_master:
          raise e
        self.after_exitmasterfn(func, e)

      except Exception as e:
        print("another error occurred")

      finally:
        if is_master and currerrtype is ExitMasterFn:
          # print("reached master func")
          pass

    return newfunc

  def after_exitcurrfn(self, func, err):
    return
    err.errormsg = f"[exit current func '{func.__name__}']"
    print(err)

  def after_exitmasterfn(self, func, err):
    return
    err.errormsg = f"[exit master func '{func.__name__}']"
    print(err)





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
