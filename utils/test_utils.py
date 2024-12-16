import json
import csv
import os

def read_json(file_path):
    """Read a JSON file and return the data."""
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json(file_path, data):
    """Write data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_csv(file_path):
    """Read a CSV file and return the data as a list of dictionaries."""
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_csv(file_path, data, fieldnames):
    """Write data to a CSV file."""
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def file_exists(file_path):
    """Check if a file exists."""
    return os.path.isfile(file_path)

def create_directory(directory_path):
    """Create a directory if it does not exist."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def delete_file(file_path):
    """Delete a file."""
    if file_exists(file_path):
        os.remove(file_path)
                  
def delete_directory(directory_path):
    """Delete a directory."""
    if os.path.exists(directory_path):
        os.remove(directory_path)

def get_files(directory_path):
    """Get a list of files in a directory."""
    return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

def get_directories(directory_path):
    """Get a list of directories in a directory."""
    return [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]

def get_file_name(file_path):
    """Get the name of a file."""
    return os.path.basename(file_path)

def get_file_extension(file_path):
    """Get the extension of a file."""
    return os.path.splitext(file_path)[1]

def get_file_size(file_path):
    """Get the size of a file in bytes."""
    return os.path.getsize(file_path)

def get_file_modified_time(file_path):
    """Get the last modified time of a file."""
    return os.path.getmtime(file_path)

def get_file_created_time(file_path):
    """Get the creation time of a file."""
    return os.path.getctime(file_path)

def get_file_accessed_time(file_path):
    """Get the last accessed time of a file."""
    return os.path.getatime(file_path)

def get_file_content(file_path):
    """Get the content of a file."""
    with open(file_path, 'r') as file:
        return file.read()
    
def write_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

def append_file(file_path, content):
    """Append content to a file."""
    with open(file_path, 'a') as file:
        file.write(content)

def copy_file(source_file, destination_file):
    """Copy a file from source to destination."""
    with open(source_file, 'rb') as source:
        with open(destination_file, 'wb') as destination:
            destination.write(source.read())

def move_file(source_file, destination_file):
    """Move a file from source to destination."""
    copy_file(source_file, destination_file)
    delete_file(source_file)

def copy_directory(source_directory, destination_directory):
    """Copy a directory from source to destination.
    Note: This function does not copy subdirectories."""
    create_directory(destination_directory)
    for file in get_files(source_directory):
        copy_file(os.path.join(source_directory, file), os.path.join(destination_directory, file))

def move_directory(source_directory, destination_directory):
    """Move a directory from source to destination.
    Note: This function does not move subdirectories."""
    copy_directory(source_directory, destination_directory)
    delete_directory(source_directory)

def get_environment_variable(variable_name):
    """Get the value of an environment variable."""
    return os.getenv(variable_name)

def set_environment_variable(variable_name, value):
    """Set the value of an environment variable."""
    os.environ[variable_name] = value

def unset_environment_variable(variable_name):
    """Unset an environment variable."""
    del os.environ[variable_name]

def get_current_directory():
    """Get the current working directory."""
    return os.getcwd()

def change_directory(directory_path):
    """Change the current working directory."""
    os.chdir(directory_path)

def get_home_directory():
    """Get the home directory of the current user."""
    return os.path.expanduser('~')

def get_temp_directory():
    """Get the temporary directory."""
    return os.path.gettempdir()

def get_user_name():
    """Get the name of the current user."""
    return os.getlogin()

def get_system_name():
    """Get the name of the operating system."""
    return os.name

def get_system_platform():
    """Get the platform of the operating system."""
    return os.uname().sysname

def get_system_release():

    """Get the release of the operating system."""
    return os.uname().release

def get_system_version():
    """Get the version of the operating system."""
    return os.uname().version

def get_system_architecture():
    """Get the architecture of the operating system."""
    return os.uname().machine

def get_system_info():
    """Get information about the operating system."""
    return {
        'name': get_system_name(),
        'platform': get_system_platform(),
        'release': get_system_release(),
        'version': get_system_version(),
        'architecture': get_system_architecture()
    }

def get_cpu_count():
    """Get the number of CPUs in the system."""
    return os.cpu_count()

def get_memory_info():
    """Get information about memory usage."""
    return {
        'total': os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES'),
        'available': os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_AVPHYS_PAGES')
    }

def get_disk_info():
    """Get information about disk usage."""
    disk_info = os.statvfs('/')
    return {
        'total': disk_info.f_frsize * disk_info.f_blocks,
        'free': disk_info.f_frsize * disk_info.f_bfree,
        'available': disk_info.f_frsize * disk_info.f_bavail
    }

def get_network_info():
    """Get information about network interfaces."""
    return os.popen('ifconfig').read()

def get_process_info():
    """Get information about the current process."""
    return {
        'pid': os.getpid(),
        'ppid': os.getppid(),
        'uid': os.getuid(),
        'gid': os.getgid(),
        'euid': os.geteuid(),
        'egid': os.getegid()
    }

def get_user_info():
    """Get information about the current user."""
    return {
        'name': get_user_name(),
        'home': get_home_directory(),
        'temp': get_temp_directory()
    }

def get_system_info():
    """Get information about the system."""
    return {
        'os': get_system_info(),
        'cpu': get_cpu_count(),
        'memory': get_memory_info(),
        'disk': get_disk_info(),
        'network': get_network_info(),
        'process': get_process_info(),
        'user': get_user_info()
    }

def get_environment_info():
    """Get information about the environment."""
    return {
        'variables': dict(os.environ),
        'current_directory': get_current_directory(),
        'files': get_files(get_current_directory()),
        'directories': get_directories(get_current_directory())
    }

def get_file_info(file_path):
    """Get information about a file."""
    return {
        'name': get_file_name(file_path),
        'extension': get_file_extension(file_path),
        'size': get_file_size(file_path),
        'modified': get_file_modified_time(file_path),
        'created': get_file_created_time(file_path),
        'accessed': get_file_accessed_time(file_path),
        'content': get_file_content(file_path)
    }

def get_directory_info(directory_path):
    """Get information about a directory."""
    return {
        'name': get_file_name(directory_path),
        'files': get_files(directory_path),
        'directories': get_directories(directory_path)
    }
