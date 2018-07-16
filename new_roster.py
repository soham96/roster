import redis

#Starts a Redis Server and initialises a set of new tasks to run
class NewRoster:

    def __init__(self, tasks, roster='tasks_list', url='localhost', port='6379'):
        self.db = redis.StrictRedis(url, port, decode_responses=True)
        self.roster=roster
        for task in tasks:
            print(f'Pushing {task}')
            self.db.lpush(self.roster, task)

    def add_task(self, tasks, position=0):
        
        for task in tasks:
            print(f'Pushing {task}')
            self.db.lpush(self.roster, task)
    
    def del_task(self):
        raise NotImplementedError
    
    def perform_task(self):
        task=self.db.lpop(self.roster)
        print(task)
    
    def perform_all_tasks(self):
        i=0
        while i<=5:
            task=self.db.lpop(self.roster)
            print(task)
            i+=1
