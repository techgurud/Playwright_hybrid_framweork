import os

class FileUtils:
    @staticmethod
    def read_file(file_path):
        """Reads the content of a file."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def write_file(file_path, content):
        """Writes content to a file."""
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    @staticmethod
    def append_to_file(file_path, content):
        """Appends content to a file."""
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content)

    @staticmethod
    def delete_file(file_path):
        """Deletes a file."""
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    @staticmethod
    def create_directory(directory_path):
        """Creates a directory if it does not exist."""
        os.makedirs(directory_path, exist_ok=True)

    @staticmethod
    def delete_directory(directory_path):
        """Deletes a directory and its contents."""
        if os.path.exists(directory_path):
            for root, dirs, files in os.walk(directory_path, topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    os.rmdir(os.path.join(root, dir))
            os.rmdir(directory_path)
        else:
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

    @staticmethod
    def list_files(directory_path):
        """Lists all files in a directory."""
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
        return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    @staticmethod
    def file_exists(file_path):
        """Checks if a file exists."""
        return os.path.exists(file_path)