import threading
import time
from datetime import datetime

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_function, interval, task_name="Task"):
        """Add a task to the scheduler.

        task_function: The function to run periodically.
        interval: Time in seconds between task runs.
        task_name: Name for the task (optional).
        """
        task = {
            'task_function': task_function,
            'interval': interval,
            'task_name': task_name
        }
        self.tasks.append(task)

    def _run_task(self, task_function, interval, task_name):
        """Run a task at the specified interval."""
        while True:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{task_name} is running at {current_time}")
            task_function()
            time.sleep(interval)

    def start(self):
        """Start all scheduled tasks in separate threads."""
        for task in self.tasks:
            task_thread = threading.Thread(target=self._run_task,
                                          args=(task['task_function'], task['interval'], task['task_name']))
            task_thread.daemon = True  # Daemon threads exit when the main program ends
            task_thread.start()

def sample_task():
    """A sample task that simply prints a message."""
    print("🌟 Sample task executed.")

def monitor_system_task():
    """A task to monitor system stats (can be modified to suit your needs)."""
    import psutil
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    print(f"CPU Usage: {cpu}%, Memory Usage: {memory}%")

if __name__ == "__main__":
    # Initialize TaskScheduler
    scheduler = TaskScheduler()

    # Add sample tasks with intervals
    scheduler.add_task(sample_task, interval=5, task_name="Sample Task")  # Runs every 5 seconds
    scheduler.add_task(monitor_system_task, interval=10, task_name="System Monitor Task")  # Runs every 10 seconds

    # Start the task scheduler
    print("🕹️ Task scheduler is running...\n")
    scheduler.start()

    # Keep the main thread running
    while True:
        time.sleep(1)  # Main thread is idle but required to keep daemon threads alive
