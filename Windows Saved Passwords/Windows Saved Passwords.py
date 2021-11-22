#Creator Szymon "Imeldushiii" Kubiak
import re
import subprocess as p
def passwords(output):
    for x in output:
        command_2 = p.run(['netsh', 'wlan', 'show', 'profile', x],capture_output=True ).stdout.decode()
        if re.search("Security key           : Absent", command_2):
            print(f'[+] Name: {x} Password: None')
        else:
            command_3 = p.run(['netsh', 'wlan', 'show','profile', x, 'key=clear'], capture_output=True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", command_3)
            print(f'[+] Name: {x} Password: {password[1]}')
def main():
        command = p.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True).stdout.decode()
        search_output = (re.findall("All User Profile     : (.*)\r", command))
        if len(search_output) > 0:
            passwords(search_output)
        else:
            print('Found 0 wifi')
            pass
if __name__ == '__main__':
    main()