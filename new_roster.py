import threading
import subprocess

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'


class myThread(threading.Thread):
    def __init__(self, task):
        threading.Thread.__init__(self)
        self.task = task

    def run(self):
        code = self.task.split()
        out=subprocess.run(code, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print(HEADER+out.stdout.decode('utf-8'))
        print(OKBLUE+out.stderr.decode('utf-8'))


def main():
    tasks=['python mul.py', 'python add.py']

    while len(tasks)>0:
        
        thread1 = myThread(tasks.pop())
        thread1.start()
        while thread1.isAlive():
            task=input('Enter new Task')
            tasks.append(task)

if __name__ == '__main__':
    main()