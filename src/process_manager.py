import subprocess
import psutil # type: ignore
import time
import os

class ProcessManager:
    def __init__(self):
        """Initializes the Process Manager."""
        self.processes = {}

    def start_process(self, command):
        """Start a new process."""
        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.processes[process.pid] = process
            print(f"Process started with PID: {process.pid}")
            return process.pid
        except Exception as e:
            print(f"Error starting process: {e}")
            return None

    def list_processes(self):
        """List all currently running processes."""
        print("Running processes:")
        for pid, process in self.processes.items():
            try:
                process_info = psutil.Process(pid)
                print(f"PID: {pid}, Name: {process_info.name()}, Status: {process_info.status()}")
            except psutil.NoSuchProcess:
                print(f"PID: {pid} no longer exists.")
                del self.processes[pid]

    def terminate_process(self, pid):
        """Terminate a process by its PID."""
        try:
            if pid in self.processes:
                process = psutil.Process(pid)
                process.terminate()
                print(f"Terminated process with PID: {pid}")
                del self.processes[pid]
            else:
                print(f"No process with PID {pid} found.")
        except psutil.NoSuchProcess:
            print(f"Process with PID {pid} does not exist.")
        except Exception as e:
            print(f"Error terminating process {pid}: {e}")

    def monitor_process(self, pid):
        """Monitor a process and print its status."""
        try:
            if pid in self.processes:
                process = psutil.Process(pid)
                while process.is_running():
                    print(f"Monitoring process {pid}: {process.status()}")
                    time.sleep(2)  # Check status every 2 seconds
                print(f"Process {pid} has finished running.")
            else:
                print(f"No process with PID {pid} found.")
        except psutil.NoSuchProcess:
            print(f"Process with PID {pid} does not exist.")
        except Exception as e:
            print(f"Error monitoring process {pid}: {e}")

# Example Usage:
if __name__ == "__main__":
    process_manager = ProcessManager()

    # Start a new process
    pid = process_manager.start_process("ping google.com")

    # List all running processes
    process_manager.list_processes()

    # Monitor the process
    if pid:
        process_manager.monitor_process(pid)

    # Terminate the process
    if pid:
        process_manager.terminate_process(pid)

    # List all running processes after termination
    process_manager.list_processes()
