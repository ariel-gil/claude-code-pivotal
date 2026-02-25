"""
DEMO: A small task tracker with several bugs.

Try asking Claude Code to:
  1. "Find and fix the bugs in buggy_app.py"
  2. "Add a feature to mark tasks as done"
  3. "Write tests for this file"
  4. "Refactor this to use a class"
"""


def create_task(title, priority="medium"):
    """Create a new task dictionary."""
    task = {
        "title": title,
        "priority": priority,
        "done": False,
    }
    return task


def add_task(task_list, task):
    """Add a task to the list. Should prevent duplicates by title."""
    # BUG: This always adds — never checks for duplicates
    task_list.append(task)
    return task_list


def get_high_priority(task_list):
    """Return only high-priority tasks."""
    # BUG: Wrong comparison — should check for "high", not "low"
    return [t for t in task_list if t["priority"] == "low"]


def summarize(task_list):
    """Print a summary of all tasks."""
    print(f"You have {len(task_list)} tasks:")
    for i, task in enumerate(task_list):
        status = "done" if task["done"] else "pending"
        # BUG: f-string references wrong variable name
        print(f"  {i+1}. {task['titl']} [{task['priority']}] — {status}")


def remove_task(task_list, title):
    """Remove a task by title. Returns True if removed, False if not found."""
    for i, task in enumerate(task_list):
        if task["title"] == title:
            task_list.pop(i)
            # BUG: Should return True here, but falls through
    return False


# --- Quick manual test ---
if __name__ == "__main__":
    tasks = []
    add_task(tasks, create_task("Write slides", "high"))
    add_task(tasks, create_task("Book room", "low"))
    add_task(tasks, create_task("Send invites", "high"))

    print("High priority:")
    for t in get_high_priority(tasks):
        print(f"  - {t['title']}")

    print()
    summarize(tasks)
