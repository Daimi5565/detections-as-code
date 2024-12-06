import json

# Load logs from JSON file
def load_logs(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Detect failed logins
def detect_failed_logins(logs):
    failed_logins = [log for log in logs if log["status"] == "failed"]
    return failed_logins

# Print the failed login attempts
def print_failed_logins(failed_logins):
    if failed_logins:
        print("Failed Login Attempts Detected:")
        for login in failed_logins:
            print(f"User: {login['user']}, IP: {login['ip']}, Time: {login['timestamp']}")
    else:
        print("No failed login attempts detected.")

# Main function to execute detection
if __name__ == "__main__":
    logs = load_logs("logs.json")
    failed_logins = detect_failed_logins(logs)
    print_failed_logins(failed_logins)
