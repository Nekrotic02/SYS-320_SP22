from getpass import getpass
import os, sys, argparse, paramiko


parser = argparse.ArgumentParser(

    description='Threat hunting using Karken binary over SSH',
    epilog='Developed by Ciaran Byrne 07/03/2022 (DD/MM/YYYY)'
)

parser.add_argument('-t','--target',required=True,help='Host to connect to via SSH')
parser.add_argument('-u','--username',required=True,help='Username for remote system')
parser.add_argument('-p','--port',required=True,help='port to connect to (Default 22)')

args = parser.parse_args()

host = args.target
username = args.username 
port = args.port

password = getpass(prompt='Enter Password for SSH: ')

try:

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,username,password)
except: 
    print("Authentication Failed")

sftp = ssh.open_sftp()

sftp.put('kraken','/home/ciaran.byrne/kraken')

stdin, stdout, stderr = ssh.exec_command('chmod 777 ./kraken',get_pty=True)

stdin, stdout, stderr = ssh.exec_command('sudo -S ./kraken --folder /usr/bin --folder  --folder /usr/sbin/   --folder /usr/local/bin  --folder /sbin  --folder /usr/local/sbin  --folder /bin ',get_pty=True)
stdin.write(password + "\n")
stdin.flush()
stdin.write("")
if stderr.channel.recv_exit_status() != 0:
    print('The Following Error occured: {}'.format(stderr.readlines()))
    print()


results = stdout.readlines()

results = ''.join(results)

with open('results.txt','w') as f:
    f.write(results)
f.close 
ssh.close()