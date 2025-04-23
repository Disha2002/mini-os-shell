import psutil
import time

def get_cpu_usage():
    """Returns the current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Returns the current memory usage in percentage."""
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    """Returns the current disk usage percentage."""
    disk = psutil.disk_usage('/')
    return disk.percent

def get_system_uptime():
    """Returns the system uptime in seconds."""
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    return uptime_seconds

def list_active_processes():
    """Lists all active processes and their CPU and memory usage."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append({
                'pid': proc.info['pid'],
                'name': proc.info['name'],
                'cpu_percent': proc.info['cpu_percent'],
                'memory_percent': proc.info['memory_percent']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  # Some processes may not be accessible or have terminated
    return processes

def display_system_info():
    """Displays the system's resource usage."""
    print("System Monitor:")
    print(f"CPU Usage: {get_cpu_usage()}%")
    print(f"Memory Usage: {get_memory_usage()}%")
    print(f"Disk Usage: {get_disk_usage()}%")
    print(f"System Uptime: {get_system_uptime():.2f} seconds")
    
    print("\nActive Processes:")
    processes = list_active_processes()
    for proc in processes[:10]:  # Limiting to top 10 processes for readability
        print(f"PID: {proc['pid']}, Name: {proc['name']}, CPU: {proc['cpu_percent']}%, Memory: {proc['memory_percent']}%")

if __name__ == "__main__":
    while True:
        display_system_info()
        print("-" * 40)
        time.sleep(5)  # Update every 5 seconds
