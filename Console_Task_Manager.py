import psutil
import os


def print_processes():
    print("PID\tName\t\t\tStatus")
    for process in psutil.process_iter(['pid', 'name', 'status']):
        pid, name, status = process.info['pid'], process.info['name'], process.info['status']
        print("{}\t{}\t\t{}".format(pid, name, status))


def kill_process(pid):
    try:
        process = psutil.Process(pid)
        process.kill()
        print("Process with PID {} has been terminated.".format(pid))
    except psutil.NoSuchProcess:
        print("Process with PID {} not found.".format(pid))
    except psutil.AccessDenied:
        print("Access denied to terminate process with PID {}.".format(pid))


def main():
    while True:
        print("\nTask Manager")
        print("1. View running processes")
        print("2. Kill a process by PID")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == '1':
            print_processes()
        elif choice == '2':
            pid = input("Enter PID of process to kill: ")
            kill_process(int(pid))
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
