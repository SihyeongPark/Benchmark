# The Computer Language Benchmarks Game
# $Id: planC.py,v 1.1 2012-12-29 19:19:31 igouy-guest Exp $
# 2016-10-31 Sihyeong Park Modify

"""
measure without libgtop2
"""
__author__ =  'Isaac Gouy'
__author__ = 'Sihyeong Park'


from domain import Record

import os, sys, cPickle, time, threading, signal, psutil
from errno import ENOENT
from subprocess import Popen


def measure(arg,commandline,delay,maxtime,
      outFile=None,errFile=None,inFile=None,logger=None,affinitymask=None):
   r,w = os.pipe()
   forkedPid = os.fork()

   if forkedPid: # read pickled measurements from the pipe
      os.close(w); rPipe = os.fdopen(r); r = cPickle.Unpickler(rPipe)
      measurements = r.load()
      rPipe.close()
      os.waitpid(forkedPid,0)
      return measurements

   else: 
      # Sample thread will be destroyed when the forked process _exits
      class Sample(threading.Thread):

         def __init__(self,program):
            threading.Thread.__init__(self)
            self.setDaemon(1)
            self.timedout = False 
            self.p = program
            self.maxMem = 0
            self.childpids = None   
            self.start() 
 
         def run(self):
            try:              
               remaining = maxtime               
               while remaining > 0: 
                  # memory get from Process
                  mem = psutil.Process(self.p).memory_info().rss                                  
                  time.sleep(delay)                    
                  remaining -= delay
                  self.maxMem = max((mem + self.childmem())/1024, self.maxMem)
               else:
                  self.timedout = True
                  os.kill(self.p, signal.SIGKILL) 
            except OSError, (e,err):
               if logger: logger.error('%s %s',e,err)

         def childmem(self):
	    if self.childpids == None:
	       self.childpids = set()

            mem = 0
            for child in psutil.Process(self.p).children(recursive=True):
               mem += child.memory_info().rss
            return mem

      try:

         m = Record(arg)

         # only write pickles to the pipe
         os.close(r); wPipe = os.fdopen(w, 'w'); w = cPickle.Pickler(wPipe)

         # psutil cpu_percent get cpu percentage 
         cpus0 = psutil.cpu_percent(interval = 1)
         start = time.time()

         # spawn the program in a separate process
         p = Popen(commandline,stdout=outFile,stderr=errFile,stdin=inFile)
         
         # start a thread to sample the program's resident memory use
         t = Sample( program = p.pid )

         # wait for program exit status and resource usage
         rusage = os.wait3(0)

         elapsed = time.time() - start
         cpus1 = psutil.cpu_percent(interval = 0)

         # summarize measurements 
         if t.timedout:
            m.setTimedout()
         elif rusage[1] == os.EX_OK:
            m.setOkay()
         else:
            m.setError()

         m.userSysTime = rusage[2][0] + rusage[2][1]
         m.maxMem = t.maxMem
         m.cpuLoad = (cpus1 - cpus0)
	 m.elapsed = elapsed


      except KeyboardInterrupt:
         os.kill(p.pid, signal.SIGKILL)

      except ZeroDivisionError, (e,err): 
         if logger: logger.warn('%s %s',err,'too fast to measure?')

      except (OSError,ValueError), (e,err):
         if e == ENOENT: # No such file or directory
            if logger: logger.warn('%s %s',err,commandline)
            m.setMissing() 
         else:
            if logger: logger.error('%s %s',e,err)
            m.setError()       
   
      finally:
         w.dump(m)
         wPipe.close()

         # Sample thread will be destroyed when the forked process _exits
         os._exit(0)



