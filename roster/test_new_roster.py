import new_roster
# from new_roster import NewRoster, Perform_Task

tasks=['python ../tests/tasks/add.py', 'python ../tests/tasks/sub.py', 'python ../tests/tasks/mul.py']
roster=new_roster.NewRoster(tasks=tasks)

perform=new_roster.Perform_Task()

print('performing all tasks')
perform.perform_all_tasks()

roster.add_task(tasks=['python tasks/div.py'])

print('performing all tasks')
perform.perform_all_tasks()

roster.db.flushdb()