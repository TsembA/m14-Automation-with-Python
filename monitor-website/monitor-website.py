import requests
import smtplib
import os
import paramiko
import linode_api4
import time
import schedule
import paramiko.agent
from dotenv import load_dotenv

load_dotenv()


EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASS = os.environ.get('EMAIL_PASS')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')

def restart_server_and_container():
    print('Rebooting the server...')
    client = linode_api4.LinodeClient(LINODE_TOKEN)
    nginx_server = client.load(linode_api4.Instance, 77670794)
    nginx_server.reboot()

    while True:
        nginx_server = client.load(linode_api4.Instance, 77670794)
        print(f"Waiting for server... Status: {nginx_server.status}")
        if nginx_server.status == 'running':
            print("Server is up. Restarting container...")
            restart_container()
            break
        time.sleep(60)

def send_notification(email_msg):
    print('Sending an email...')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
        message = f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)

def restart_container():
    print('Restarting the application...')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('172.236.237.121', username='root', key_filename='/Users/tsemb/.ssh/id_ed25519')
    stdin, stdout, stderr = ssh.exec_command('docker start 4d092c431241')
    print(stdout.readlines())
    print(stderr.read().decode())
    ssh.close()

def monitor_application():
    try:
        response = requests.get('http://172-236-237-121.ip.linodeusercontent.com:80/')
        if response.status_code == 200:
            print('Application is running successfully!')
        else:
            print('Application Down. Fix it!')
            msg = f'Application returned {response.status_code}'
            send_notification(msg)
            restart_container()
    except Exception as ex:
        print(f'Connection error happened: {ex}')
        msg = 'Application not accessible at all'
        send_notification(msg)
        restart_server_and_container()

schedule.every(5).minutes.do(monitor_application)

monitor_application()
while True:
    schedule.run_pending()
