#!/usr/bin/python

#pip install watchdog

#import watchdog
import sys
import time
import datetime

taskagent_dir = "/Users/rhuber/Dropbox/Apps/TaskAgent/"
config_dir    = "TaskAutomator/"
today_file    = "Today.txt"
done_file     = config_dir + "Done.txt"

class Tasks:

  def __init__(self):
    pass

  def update(self):
    self.run_time      = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.current_tasks = file(taskagent_dir + today_file, 'r').readlines()
    if [x.startswith('x ') for x in self.current_tasks].count(True) > 0:
      #print "found completed tasks"
      self.done_tasks    = file(taskagent_dir + done_file, 'a')
      self.today_tasks   = file(taskagent_dir + today_file, 'w')
      return True
    else:
      #print "no completed tasks"
      return False

  def process(self):
    for task in self.current_tasks:
      task = task.strip()
      #print task
      if task.startswith('x '):
        self.done_tasks.write(task + " " + self.run_time + "\n")
      #elif task.startswith('- '):
      #  pass
      else:
        self.today_tasks.write(task + "\n")
    self.today_tasks.close()
    self.done_tasks.close()

T = Tasks()
print "Watching.."
while True:
  if T.update():
    T.process()
  time.sleep(5)


