from new_roster import NewRoster, Perform_Task

tasks=['python tasks/add.py', 'python tasks/sub.py', 'python tasks/mul.py']
roster=NewRoster(tasks=tasks)

perform=Perform_Task()

print('performing all tasks')
perform.perform_all_tasks()

roster.add_task(tasks=['python tasks/div.py'])

print('performing all tasks')
perform.perform_all_tasks()

roster.db.flushdb()