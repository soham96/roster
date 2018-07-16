from new_roster import NewRoster

tasks=['add', 'subtract', 'mul']
roster=NewRoster(tasks=tasks)

roster.perform_task()

roster.add_task(tasks=['div'])

roster.perform_task()

print('performing all tasks')
roster.perform_all_tasks()

roster.db.flushdb()