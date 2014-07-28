#!/usr/bin/python

#pip install watchdog

#import watchdog
import time
import datetime

taskagent_dir = "/Users/rhuber/Dropbox/Apps/TaskAgent/"
config_dir    = "TaskAutomator/"
today_file    = "Today.txt"
daily_file    = config_dir + "Daily.txt"
done_file     = config_dir + "Done.txt"

class List:
  def __init__(self, lines):
    self.items = []
    for item in lines:
      item = item.strip()
      if item.startswith('x ') or item.startswith('- '):
        item = item.split(' ', 1)
      else:
        item = ['-', item]
      self.items.append(item)
  def get_items(self):
    return self.items
  def get_finished_items(self):
    return [x[1] for x in self.items if x[0] == 'x']
  def get_unfinished_items(self):
    return [x[1] for x in self.items if x[0] == '-']
  def print_unfinished_items(self):
    output = ''
    items = self.get_unfinished_items()
    for item in items:
      if item != items[-1]:
        output += "- %s\n" % item
      else:
        output += "- %s" % item
    return output
  def print_finished_items(self):
    output = ''
    items = self.get_finished_items()
    for item in items:
      if item != items[-1]:
        output += "x %s %s\n" % (item, run_time)
      else:
        output += "x %s %s" % (item, run_time)
    return output


def update():
  task_list = List(file(taskagent_dir + today_file, 'r').readlines())
  daily_list = List(file(taskagent_dir + daily_file, 'r').readlines())
  if len(task_list.get_finished_items()) > 0:
    print "found completed tasks"
    print task_list.print_finished_items()
    done_tasks    = file(taskagent_dir + done_file, 'a').write(task_list.print_finished_items() + "\n")
    today_tasks   = file(taskagent_dir + today_file, 'w').write(task_list.print_unfinished_items())
    return True
  else:
    #print "no completed tasks"
    return False

while True:
  run_time      = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  update()
  time.sleep(5)

