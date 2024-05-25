import subprocess

def get_machine_identifier():
    command = "wmic csproduct get UUID"
    result = subprocess.check_output(command, shell=True).decode().split('\n')[1].strip()
    return result
