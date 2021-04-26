# To-Do-List

# Description
Planning is one thing, but when we need to knuckle down and put our plans into action, we tend to push our tasks back further and further until the last minute, or worse — past the established deadline. It happens to the best of us!

In this stage, let's implement the ability to see missed tasks and delete them.

To delete a row from a table, you need to use the ```delete()``` method that accepts an object to delete. As you remember, each row is represented by a Python object:

```python
from datetime import datetime

# delete all rows where date column equals today's date
session.query(Table).filter(Table.date == datetime.today().date()).delete()

# delete a specific row
rows = session.query(Table).filter(Table.date < datetime.today().date()).all()
specific_row = rows[0] # in case rows is not empty
session.delete(specific_row)

# don't forget to commit changes
session.commit()
```

# Objectives
Add the following items into your menu:

* **Missed tasks**: prints all tasks whose deadline was missed, that is, tasks whose deadline date is earlier than today's date.
* **Delete task**: deletes the chosen task. Print 'Nothing to delete' if the tasks list is empty.
**Missed tasks** should print the tasks ordered by the deadline date.

**Delete task** should print all the tasks sorted by the deadline date and ask to enter the number of the task to delete.

See in the example what your program should look like.

# Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

**Output:**

```
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 4

Missed tasks:
1. Learn the for-loop. 19 Apr

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 6

Choose the number of the task you want to delete:
1. Learn the for-loop. 19 Apr
2. Learn the basics of SQL. 29 Apr
> 1
The task has been deleted!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 4

Missed tasks:
Nothing is missed!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 0

Bye!
```
