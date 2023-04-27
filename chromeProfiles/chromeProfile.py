# for chrome
# import subprocess

# profile_directory = "/home/user/.config/google-chrome/Profile 1"
# chrome_command = f"google-chrome --new-window --profile-directory='{profile_directory}' --disable-gpu"
# subprocess.Popen(chrome_command, shell=True)


# for firefox
import subprocess

profile_folder_names = ['7ry0jwaa.bing1', 'np9fh78l.bing2', '62kt3mzg.bing3', 'b6u8m62q.bing4']
profile_folder_name = 'cfb61ejg.sipayi' # this is for example

def openChrome(profile_folder_name):
    firefox_command = f"firefox --new-window --profile '/home/sai/snap/firefox/common/.mozilla/firefox/{profile_folder_name}'"
    subprocess.Popen(firefox_command, shell=True)

if __name__ == "__main__":
    openChrome(profile_folder_name)