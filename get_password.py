import subprocess

def get_wifi_passwords():
    try:
        # Get all wifi profiles
        profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [line.split(':')[1].strip() for line in profiles_data if 'All User Profile' in line]

        print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
        print("-" * 40)

        for profile in profiles:
            try:
                # Get password for each profile
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
                password = [line.split(':')[1].strip() for line in results if 'Key Content' in line][0]
                print("{:<30}| {:<}".format(profile, password))
            except IndexError:
                print("{:<30}| {:<}".format(profile, "Password not found"))
    except subprocess.CalledProcessError as e:
        print(f"Error executing netsh command: {e}")

if __name__ == "__main__":
    get_wifi_passwords()
    input("Press Enter to exit")
