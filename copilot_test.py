
import os
import platform
import subprocess

def get_uptime():
    system = platform.system()
    if system == "Windows":
        # Windows does not have 'uptime' command, use 'net stats srv'
        try:
            output = subprocess.check_output("net stats srv", shell=True, encoding="utf-8")
            for line in output.splitlines():
                if "Statistics since" in line:
                    print("System uptime started at:", line.split("Statistics since")[1].strip())
                    break
        except Exception as e:
            print("Could not determine uptime on Windows:", e)
    else:
        # For Unix/Linux/Mac systems
        try:
            output = subprocess.check_output("uptime -p", shell=True, encoding="utf-8")
            print("System uptime:", output.strip())
        except Exception as e:
            print("Could not determine uptime:", e)

if __name__ == "__main__":
    get_uptime()

