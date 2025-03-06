import subprocess

def shell_out(command_string):
    """
    Executes the given command string as a subprocess and returns a triple
    containing [exit_status, stdout, stderr].
    
    Args:
        command_string (str): The command to execute
        
    Returns:
        list: A list containing [exit_status, stdout, stderr]
    """
    try:
        # Run the command, capturing stdout and stderr
        process = subprocess.Popen(
            command_string,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # This returns stdout and stderr as strings instead of bytes
        )
        
        # Get the output and error (if any)
        stdout, stderr = process.communicate()
        
        # Get the exit status
        status = process.returncode
        
        return [status, stdout, stderr]
    
    except Exception as e:
        # If the subprocess creation itself fails
        return [-1, "", str(e)]


# # Example usage
# result = shell_out("ls -la")
# status, stdout, stderr = result

# print(f"Exit status: {status}")
# print(f"Standard output:\n{stdout}")
# print(f"Standard error:\n{stderr}")

# Another example with a command that might generate an error
result = shell_out("grep missing_pattern nonexistent_file")
status, stdout, stderr = result
print(f"Exit status: {status}")
print(f"Standard output:\n{stdout}")
print(f"Standard error:\n{stderr}")

