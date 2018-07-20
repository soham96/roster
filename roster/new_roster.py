import redis
import argparse
import subprocess
import os

#Starts a Redis Server and initialises a set of new tasks to run
class Perform_Task:

    def __init__(self, roster='tasks_list', url='localhost', port='6379'):
        self.db = redis.StrictRedis(url, port, decode_responses=True)
        self.roster=roster

    def perform_all_tasks(self):
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        
        while self.db.llen(self.roster)>0:
            task=self.db.lpop(self.roster)
            #import ipdb; ipdb.set_trace()
            task=task.split()
            out=subprocess.run(task, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            print(HEADER+out.stdout.decode('utf-8'))
            print(OKBLUE+out.stderr.decode('utf-8'))



class NewRoster:

    def __init__(self, tasks, roster='tasks_list', url='localhost', port='6379'):
        self.db = redis.StrictRedis(url, port, decode_responses=True)
        self.roster=roster
        for task in tasks:
            print(f'Pushing {task}')
            self.db.lpush(self.roster, task)

    def add_task(self, tasks, position=0):
        
        try:
            if position<1:
                raise ValueError
            else:
                pass
        except:
            pass

        for task in tasks:
            print(f'Pushing {task}')
            self.db.lpush(self.roster, task)
    
    def del_task(self):
        raise NotImplementedError
    
    


def main():
    pass

if __name__ == '__main__':
    
    main()