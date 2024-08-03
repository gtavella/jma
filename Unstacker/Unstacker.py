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


class Unstacker:
  def __init__(self) -> None:
    self._master_passed = False
    self.func_count = 0

  # exit current func

  def exit_current(self):
    """
    Exit current function.
    """
    raise ExitCurrFn

  def exit_master(self):
    """
    Exit from master function.
    """
    raise ExitMasterFn

  def resume_master(self):
    """
    Go to master function.
    In the sense, resume where master 
    function left off.
    """
    raise ResumeMasterFn

  def back(self, offset: int):
    """
    Go to master function.
    In the sense, resume where master 
    function left off.
    """
    self.back_offset = offset
    self.set_start_idx = False
    raise BackOffset


  # 'event' listeners 

  def add(self, func):
    def newfunc(*args, **kw):
      # is the current function the master function?
      # this is local, is reset for each function frame
      # why two variables? because one is local 
      # and will be the real value
      # the other is global, represents the global state
      # not the local state
      func_idx = self.func_count
      self.func_count += 1
      
      currerrtype = None
      
      try:
        func(*args, **kw)

      

      except ExitCurrFn as e:
        currerrtype = ExitCurrFn
        self.after_exitcurrfn(func, e)

      
      except BackOffset as e:
        currerrtype = BackOffset
        # self.after_gomastfn(func, e)
        """
        master:  master master1 master2
        index :     0      1        2
        re-raising the exception from the n-th
        function to the second function included, 
        which in turn will generate the last exception
        and 'cancel the frame' of function 1, thus
        effectively leaving frame of function 1 only,
        which is another way of saying "resume from function 1"
        """
        # this only runs once and captures the funcion index
        # of the caller, so that it provides the starting index
        if not self.set_start_idx:
          self.start_func_idx = func_idx
        self.set_start_idx = True
        
        while ((func_idx >= self.start_func_idx - self.back_offset + 2) 
               and func_idx >= 1):
          raise e

        currerrtype = BackOffset

  
      except ResumeMasterFn as e:
        currerrtype = ResumeMasterFn
        # self.after_gomastfn(func, e)
        """
        master:  master master1 master2
        index :     0      1        2
        re-raising the exception from the n-th
        function to the second function included, 
        which in turn will generate the last exception
        and 'cancel the frame' of function 1, thus
        effectively leaving frame of function 1 only,
        which is another way of saying "resume from function 1"
        """
        if func_idx >= 2:
          raise e

      except ExitMasterFn as e:
        currerrtype = ExitMasterFn
        # re-raising the error means exiting any
        # function frame (including) the master function frame
        if func_idx >= 1:
          raise e
          
        self.after_exitmasterfn(func, e)

      except Exception as e:
        print("another error occurred")

      finally:
        if ResumeMasterFn and func_idx == 1:
          pass
        
        elif currerrtype is ExitMasterFn and func_idx == 0:
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


class ResumeMasterFn(Exception):
  def __init__(self, msg=None) -> None:
    if msg is None:
      self._errormsg = "info: go to master func"
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


class BackOffset(Exception):
  def __init__(self, msg=None) -> None:
    if msg is None:
      self._errormsg = "info: back offset"
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




"""
Why not just return the decorated function?
Well, you may not want to return a function when 
in a decorator. But what if you want to force 
the decorated function to exit?
This is what listen.exit_master() for example 
helps you with.

@cool_decorator
@listen.on
def dosomething3():
  print("start do something 3")
  # listen.resume_master()
  # listen.exit_master()
  # a simple return won't stop the decorator
  # from continuing
  # return
  print("end do something 3")


"""
