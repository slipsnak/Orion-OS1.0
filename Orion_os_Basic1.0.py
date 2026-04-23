import os
import threading
import time
import socket

# System configuration
system_config = {'processes': [], 'memory': {}}
root_dir = "./orion_filesystem"
users = {"admin": "admin123"}
current_user = None

# Initialize file system
def initialize_file_system():
    os.makedirs(root_dir, exist_ok=True)
    print("File system initialized.")

# File system functions
def create_file(filename):
    filepath = os.path.join(root_dir, filename)
    with open(filepath, 'w') as f:
        f.write('')
    print(f"File '{filename}' created.")

def read_file(filename):
    filepath = os.path.join(root_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
            print(content)
    else:
        print(f"File '{filename}' does not exist.")

def delete_file(filename):
    filepath = os.path.join(root_dir, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"File '{filename}' deleted.")
    else:
        print(f"File '{filename}' does not exist.")

def list_files():
    print("Files:", os.listdir(root_dir))

# Process handling functions
def list_processes():
    print("Running processes:", system_config['processes'])

def start_process(process_name):
    system_config['processes'].append(process_name)
    print(f"Process '{process_name}' started.")

def stop_process(process_name):
    if process_name in system_config['processes']:
        system_config['processes'].remove(process_name)
        print(f"Process '{process_name}' stopped.")
    else:
        print(f"Process '{process_name}' is not running.")

# Task scheduler functions
def add_task(task, delay):
    threading.Thread(target=execute_task, args=(task, delay)).start()
    print(f"Task '{task}' added to run after {delay} seconds.")

def execute_task(task, delay):
    time.sleep(delay)
    print(f"Executing task: {task}")

# User management functions
def login(username, password):
    global current_user
    if users.get(username) == password:
        current_user = username
        print(f"User '{username}' logged in.")
    else:
        print("Invalid username or password.")

def logout():
    global current_user
    if current_user:
        print(f"User '{current_user}' logged out.")
        current_user = None

def register(username, password):
    if username in users:
        print(f"User '{username}' already exists.")
    else:
        users[username] = password
        print(f"User '{username}' registered.")

def delete_user(username):
    if username in users:
        del users[username]
        print(f"User '{username}' deleted.")
    else:
        print(f"User '{username}' does not exist.")

# Network utility functions
def ping(host):
    try:
        ip = socket.gethostbyname(host)
        print(f"Pinging {host} [{ip}]...")
        s = socket.create_connection((ip, 80), 2)
        print(f"Ping to {host} successful!")
        s.close()
    except socket.error as e:
        print(f"Ping to {host} failed: {e}")

def get_ip_address(url):
    try:
        ip = socket.gethostbyname(url)
        print(f"IP address of {url} is {ip}")
    except socket.error as e:
        print(f"Failed to get IP address: {e}")

# System information
def system_info():
    print(f"OS: Orion OS")
    print(f"Processes: {len(system_config['processes'])}")
    print(f"Files: {len(os.listdir(root_dir))}")
    print(f"Logged in as: {current_user if current_user else 'No user'}")

# Package management
def install_package(package_name):
    print(f"Installing package: {package_name}")
    # Simulation of package installation
    time.sleep(2)
    print(f"Package '{package_name}' installed successfully.")

def remove_package(package_name):
    print(f"Removing package: {package_name}")
    # Simulation of package removal
    time.sleep(2)
    print(f"Package '{package_name}' removed successfully.")

def list_packages():
    print("Installed packages:")
    # Simulation of listing packages
    print("Package1")
    print("Package2")
    print("Package3")

# Shell script execution
def execute_script(script_path):
    if os.path.exists(script_path):
        with open(script_path, 'r') as script_file:
            for line in script_file:
                handle_command(line.strip())
    else:
        print(f"Script '{script_path}' does not exist.")

# Help function
def show_help():
    help_text = """
    Available commands:
    - help: Show this help message
    - list_processes: List running processes
    - start_process <process_name>: Start a process
    - stop_process <process_name>: Stop a process
    - create_file <filename>: Create a file
    - read_file <filename>: Read a file
    - delete_file <filename>: Delete a file
    - list_files: List files in the file system
    - add_task <task> <delay_in_seconds>: Schedule a task to run after a delay
    - login <username> <password>: Log in as a user
    - logout: Log out the current user
    - register <username> <password>: Register a new user
    - delete_user <username>: Delete a user
    - ping <host>: Ping a host to check connectivity
    - get_ip <url>: Get the IP address of a URL
    - system_info: Display system information
    - install_package <package_name>: Install a package
    - remove_package <package_name>: Remove a package
    - list_packages: List installed packages
    - execute_script <script_path>: Execute a shell script
    - exit: Exit the OS
    """
    print(help_text)

# Command handler
def handle_command(command):
    parts = command.split()
    if not parts:
        return

    cmd = parts[0]
    args = parts[1:]

    if cmd == "help":
        show_help()
    elif cmd == "list_processes":
        list_processes()
    elif cmd == "start_process" and args:
        start_process(args[0])
    elif cmd == "stop_process" and args:
        stop_process(args[0])
    elif cmd == "create_file" and args:
        create_file(args[0])
    elif cmd == "read_file" and args:
        read_file(args[0])
    elif cmd == "delete_file" and args:
        delete_file(args[0])
    elif cmd == "list_files":
        list_files()
    elif cmd == "add_task" and len(args) == 2:
        add_task(args[0], int(args[1]))
    elif cmd == "login" and len(args) == 2:
        login(args[0], args[1])
    elif cmd == "logout":
        logout()
    elif cmd == "register" and len(args) == 2:
        register(args[0], args[1])
    elif cmd == "delete_user" and args:
        delete_user(args[0])
    elif cmd == "ping" and args:
        ping(args[0])
    elif cmd == "get_ip" and args:
        get_ip_address(args[0])
    elif cmd == "system_info":
        system_info()
    elif cmd == "install_package" and args:
        install_package(args[0])
    elif cmd == "remove_package" and args:
        remove_package(args[0])
    elif cmd == "list_packages":
        list_packages()
    elif cmd == "execute_script" and args:
        execute_script(args[0])
    else:
        print(f"Unknown command: {command}")

def run_shell():
    print("Orion OS: type 'help' for a list of commands.")
    while True:
        command = input("Orion OS >> ")
        if command.lower() == "exit":
            break
        handle_command(command)

def main():
    initialize_file_system()
    run_shell()

if __name__ == "__main__":
    main()
