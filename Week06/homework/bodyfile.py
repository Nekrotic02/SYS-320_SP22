import os, sys, argparse, paramiko
from getpass import getpass

parser = argparse.ArgumentParser(

    description='Creates body file for everything in the /usr/bin directory, saves the body file in the local system',
    epilog='Developed by Ciaran Byrne 03/02/2022 (DD/MM/YYYY)'
)

parser.add_argument('-t','--target',required=True,help='Host to connect to via SSH')
parser.add_argument('-u','--username',required=True,help='Username for remote system')
parser.add_argument('-p','--port',required=True,help='port to connect to')

args = parser.parse_args()

host = args.target
username = args.username 
port = args.port 

password = getpass(prompt='Enter Password for SSH: ')

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(host,port,username,password)

except paramiko.AuthenticationException():
    print('Authentication Failed')

sftp = ssh.open_sftp()

sftp.chdir('/usr/bin')

file_list = sftp.listdir()

def statFile(toStat):

    # i is going to be the variable used for each of the metadata elements 
    i = os.stat(toStat,follow_symlinks=False)
    
    # inode 
    inode=i[1]
    
    # mode 

    mode=i[0]

    #uid 
    uid = i[4]

    #gid 

    gid = i[5]

    #file size 

    fsize = i[6]

    #access time 

    atime = i[7]

    # modification time 

    mtime = i[8]

    # ctime 

    ctime = i[9]
    crtime = i[9]

    file = "0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(toStat,inode,mode,uid,gid,fsize,atime,mtime,ctime,crtime)
    return file 

results = []
for eachFile in file_list:
    

with open('results.txt','a') as f: 
    f.write(results)
ssh.close()