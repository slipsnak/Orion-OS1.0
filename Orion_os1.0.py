import os
import threading
import time
import socket
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

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
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write('')
        messagebox.showinfo("Create File", f"File '{filename}' created.")
    else:
        messagebox.showerror("Create File", f"File '{filename}' already exists.")

def read_file(filename):
    filepath = os.path.join(root_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
            messagebox.showinfo("Read File", content)
    else:
        messagebox.showerror("Read File", f"File '{filename}' does not exist.")

def delete_file(filename):
    filepath = os.path.join(root_dir, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        messagebox.showinfo("Delete File", f"File '{filename}' deleted.")
    else:
        messagebox.showerror("Delete File", f"File '{filename}' does not exist.")

def list_files():
    files = os.listdir(root_dir)
    if files:
        messagebox.showinfo("List Files", "Files: " + ", ".join(files))
    else:
        messagebox.showinfo("List Files", "No files found.")

# Process handling functions
def list_processes():
    if system_config['processes']:
        messagebox.showinfo("List Processes", "Running processes: " + ", ".join(system_config['processes']))
    else:
        messagebox.showinfo("List Processes", "No running processes.")

def start_process(process_name):
    system_config['processes'].append(process_name)
    messagebox.showinfo("Start Process", f"Process '{process_name}' started.")

def stop_process(process_name):
    if process_name in system_config['processes']:
        system_config['processes'].remove(process_name)
        messagebox.showinfo("Stop Process", f"Process '{process_name}' stopped.")
    else:
        messagebox.showerror("Stop Process", f"Process '{process_name}' is not running.")

# Task scheduler functions
def add_task(task, delay):
    threading.Thread(target=execute_task, args=(task, delay)).start()
    messagebox.showinfo("Add Task", f"Task '{task}' added to run after {delay} seconds.")

def execute_task(task, delay):
    time.sleep(delay)
    messagebox.showinfo("Execute Task", f"Executing task: {task}")

# User management functions
def login(username, password):
    global current_user
    if users.get(username) == password:
        current_user = username
        messagebox.showinfo("Login", f"User '{username}' logged in.")
    else:
        messagebox.showerror("Login", "Invalid username or password.")

def logout():
    global current_user
    if current_user:
        messagebox.showinfo("Logout", f"User '{current_user}' logged out.")
        current_user = None
    else:
        messagebox.showerror("Logout", "No user is currently logged in.")

def register(username, password):
    if username in users:
        messagebox.showerror("Register", f"User '{username}' already exists.")
    else:
        users[username] = password
        messagebox.showinfo("Register", f"User '{username}' registered.")

def delete_user(username):
    if username in users:
        del users[username]
        messagebox.showinfo("Delete User", f"User '{username}' deleted.")
    else:
        messagebox.showerror("Delete User", f"User '{username}' does not exist.")

def change_password(username, old_password, new_password):
    if users.get(username) == old_password:
        users[username] = new_password
        messagebox.showinfo("Change Password", f"Password for user '{username}' changed successfully.")
    else:
        messagebox.showerror("Change Password", "Invalid username or password.")

def list_users():
    if users:
        messagebox.showinfo("List Users", "Registered users: " + ", ".join(users.keys()))
    else:
        messagebox.showinfo("List Users", "No users registered.")

# Network utility functions
def ping(host):
    try:
        ip = socket.gethostbyname(host)
        messagebox.showinfo("Ping", f"Pinging {host} [{ip}]...")
        s = socket.create_connection((ip, 80), 2)
        messagebox.showinfo("Ping", f"Ping to {host} successful!")
        s.close()
    except socket.error as e:
        messagebox.showerror("Ping", f"Ping to {host} failed: {e}")

def get_ip_address(url):
    try:
        ip = socket.gethostbyname(url)
        messagebox.showinfo("Get IP Address", f"IP address of {url} is {ip}")
    except socket.error as e:
        messagebox.showerror("Get IP Address", f"Failed to get IP address: {e}")

# System information
def system_info():
    info = f"""
    OS: Orion OS
    Processes: {len(system_config['processes'])}
    Files: {len(os.listdir(root_dir))}
    Logged in as: {current_user if current_user else 'No user'}
    """
    messagebox.showinfo("System Info", info)

# Package management
def install_package(package_name):
    messagebox.showinfo("Install Package", f"Installing package: {package_name}...")
    # Simulation of package installation
    time.sleep(2)
    messagebox.showinfo("Install Package", f"Package '{package_name}' installed successfully.")

def remove_package(package_name):
    messagebox.showinfo("Remove Package", f"Removing package: {package_name}...")
    # Simulation of package removal
    time.sleep(2)
    messagebox.showinfo("Remove Package", f"Package '{package_name}' removed successfully.")

def list_packages():
    packages = ["Package1", "Package2", "Package3"]
    messagebox.showinfo("List Packages", "Installed packages: " + ", ".join(packages))

# Shell script execution
def execute_script(script_path):
    if os.path.exists(script_path):
        with open(script_path, 'r') as script_file:
            for line in script_file:
                handle_command(line.strip())
    else:
        messagebox.showerror("Execute Script", f"Script '{script_path}' does not exist.")

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
    elif cmd == "change_password" and len(args) == 3:
        change_password(args[0], args[1], args[2])
    elif cmd == "list_users":
        list_users()
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
        messagebox.showerror("Unknown Command", f"Unknown command: {command}")

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
    - change_password <username> <old_password> <new_password>: Change user password
    - list_users: List registered users
    - ping <host>: Ping a host to check connectivity
    - get_ip <url>: Get the IP address of a URL
    - system_info: Display system information
    - install_package <package_name>: Install a package
    - remove_package <package_name>: Remove a package
    - list_packages: List installed packages
    - execute_script <script_path>: Execute a shell script
    - exit: Exit the OS
    """
    messagebox.showinfo("Help", help_text)

# Loading screen
def show_loading_screen():
    loading_screen = tk.Tk()
    loading_screen.title("Orion OS")
    loading_screen.geometry("300x200")

    label = tk.Label(loading_screen, text="Loading Orion OS...", font=("Helvetica", 16))
    label.pack(expand=True)

    loading_screen.after(3000, loading_screen.destroy)  # Show the loading screen for 3 seconds
    loading_screen.mainloop()

# GUI Class
class OrionOSGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Orion OS")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        self.cmd_label = tk.Label(self, text="Enter Command:", bg="#f0f0f0", font=("Helvetica", 14))
        self.cmd_label.pack(pady=10)

        self.cmd_entry = tk.Entry(self, width=70, font=("Helvetica", 12))
        self.cmd_entry.pack(pady=5)

        self.run_btn = tk.Button(self, text="Run", command=self.run_command, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.run_btn.pack(pady=10)

        self.output_text = tk.Text(self, height=20, width=100, font=("Helvetica", 12))
        self.output_text.pack(pady=10)

        self.output_text.config(state=tk.DISABLED)

    def run_command(self):
        cmd = self.cmd_entry.get()
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, f"Command: {cmd}\n")
        self.output_text.config(state=tk.DISABLED)
        self.cmd_entry.delete(0, tk.END)
        handle_command(cmd)

def run_gui():
    show_loading_screen()
    app = OrionOSGUI()
    app.mainloop()

def main():
    initialize_file_system()
    run_gui()

if __name__ == "__main__":
    main()

