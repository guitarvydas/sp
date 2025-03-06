import subprocess

def run_command(command_string, string_to_parse):
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
        stdin_param = subprocess.PIPE if string_to_parse is not None else None
        process = subprocess.Popen(
            command_string,
            shell=True,
            stdin=stdin_param,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # This returns stdout and stderr as strings instead of bytes
        )
        
        # Get the output and error (if any)
        stdout, stderr = process.communicate(input=string_to_parse)
        
        # Get the exit status
        status = process.returncode
        
        return [status, stdout, stderr]
    
    except Exception as e:
        # If the subprocess creation itself fails
        return [-1, "", str(e)]

def shell_out (command, string_to_parse):
    [rc, stdout, stderr] = run_command (command, string_to_parse)
    if rc == 0:
        return [rc, stdout, stderr]
    else:
        raise RuntimeError(f"Command failed with exit code {rc}. \n stderr: {stderr} \n stdout: {stdout}")

# # Example usage
# result = shell_out("ls -la")
# status, stdout, stderr = result

# print(f"Exit status: {status}")
# print(f"Standard output:\n{stdout}")
# print(f"Standard error:\n{stderr}")

# # Another example with a command that might generate an error
# result = shell_out("grep missing_pattern nonexistent_file")
# status, stdout, stderr = result
# print(f"Exit status: {status}")
# print(f"Standard output:\n{stdout}")
# print(f"Standard error:\n{stderr}")

