import task_01
import task_02
import task_03

tasks = [
    task_01.run,
    task_02.run,
    task_03.run
]

for f in tasks:
    f()
