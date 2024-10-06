import os

def secure_linux_system():

    # Some basic commands
    os.system('passwd -l root')
    os.system('echo "PermitRootLogin no" >> /etc/ssh/sshd_config')
    os.system('echo "Protocol 2" >> /etc/ssh/sshd_config')
    os.system('echo "AllowUsers Realism ubuntu" >> /etc/ssh/sshd_config')
    os.system('echo "ssl_enable" >> /etc/vsftp/vsftp.conf')
    #os.system('echo "Match User !plinktern, !hkeating" >> /etc/ssh/sshd_config')
    #os.system('echo "PasswordAuthentication no')
    print("Finished basic commands")

    
    

    # Change Passwords
    os.system('sudo passwd plinktern')
    os.system('sudo passwd hkeating')
    print("Finished Passwords")
    
    # Make backups
    os.system("sudo mkdir /lib32")
    os.system("sudo mkdir /lib32/bkp")
    os.system("sudo cp -r /var /lib32/bkp")
    os.system("sudo cp -r /etc /lib32/bkp")
    os.system("sudo cp -r /opt /lib32/bkp")
    os.system("sudo cp -r /home /lib32/bkp")
    os.system("sudo cp /var/ftp/ImaHorse.jpg /lib32/bkp")
    os.system("sudo cp /var/ftp/ImaHorse.jpg ~")
    os.system("sudo cp /var/ftp/ImaHorse.jpg /bin")
    os.system("sudo cp /var/ftp/ImaHorse.jpg /media")
    os.system("sudo cp /var/ftp/ImaHorse.jpg /var")
    os.system("sudo chattr +i /var/ftp/ImaHorse.jpg")
    os.system("sudo chattr +a /lib32")
    print("Finished Backups")

     # update services / install services
    os.system('sudo yum install wireshark-cli -y')
    os.system('sudo yum install nano -y')
    os.system('sudo yum install nmap -y')
    os.system('sudo yum install curl -y')
    os.system('sudo yum install net-tools -y')
    #os.system('sudo yum update')
    print("Finished updates")

     # Configure the firewall
    os.system('yum install -y epel-release')
    os.system('sudo dnf install ufw -y')
    os.system('sudo ufw default deny incoming')
    os.system('sudo ufw default allow outgoing')
    os.system('sudo ufw allow ssh')
    os.system('sudo ufw allow ftp')
    os.system("sudo ufw deny 4444")
    os.system('ufw allow http')
    os.system('ufw allow https')
    os.system('sudo ufw enable')
    print("Finished ufw")


    # Disable root login
    # os.system('sudo passwd -l root')

    # remove password for user (keypair)
          # -> run this id .ssh is not already on server <- os.system('mkdir ~/.ssh && chmod 700 ~/.shh')
    # os.system('ssh-keygen -b 4096')
    # os.system('ssh-copy-id iNSERT_USERNAME@INSERT-IP')


    # DONOT RUN UNLESS ABSOLUTLEY NESSEARY sudo apt reinstall coreutils


    '''
    # Set up SSH key authentication
    os.system('sudo mkdir /home/Tester/.ssh')
    os.system('sudo cp ~/.ssh/authorized_keys /home/Tester/.ssh/')
    os.system('sudo chown -R Tester:Tester /home/Tester/.ssh')
    os.system('sudo chmod 700 /home/Tester/.ssh')
    os.system('sudo chmod 600 /home/Tester/.ssh/authorized_keys')
    '''
    '''
    # Disable password authentication for SSH
    ssh_config_path = '/etc/ssh/sshd_config'
    with open(ssh_config_path, 'r') as file:
        ssh_config = file.readlines()
    
    with open(ssh_config_path, 'w') as file:
        for line in ssh_config:
            if line.strip().startswith('PasswordAuthentication'):
                file.write('PasswordAuthentication no\n')
            else:
                file.write(line)
    
    os.system('sudo systemctl restart sshd')
    '''
# Run the function to secure the Linux system
secure_linux_system()

print("The Linux system has been secured.")



'''
            --CHANGE DEFAULT PASSWORDS--
sudo passwd {username}: Change user's password

                   --SSH COMMANDS--
nano /etc/ssh/sshd_config: Opens the sshd configuration file
    -Set Pubkey Authentication to no
    -Add line: AllowUsers hkeating plinktern
    -Restart ssh service with: sudo systemctl restart sshd

            --KILL MALICIOUS PROCESSES--
sudo ps aux: Display running processes
sudo kill {process_number}: Kills the process with a given process_number
sudo pkill {process_name}: Kills all processes containing process_name

           --REMOVE UNUSED USER ACCOUNTS--
cat /etc/passwd: Shows all user accounts
sudo userdel {username}: Removes the user account called username
    -Can only be removed after all user processes have been killed

            --CLOSE UNUSED OPEN PORTS--
sudo ss -tulnp | grep LISTEN: Shows all open TCP/UDP and listening ports
sudo systemctl stop {name_of_service}: Closes the port running a service called name_of_service
sudo systemctl disable {name_of_service}: Disables this port on any system reboot

                --FIREWALL COMMANDS--
sudo ufw deny from {IP_address}: Denies all traffic from IP_address
     -Use cat /var/log/auth.log | grep sshd
     -Checks for sshd connections to server
sudo ufw deny from {IP_address} to ssh: Denies all ssh connections from IP_address
sudo ufw allow {service}: Allows a certain service (ssh, http)
sudo ufw delete {#}: Deletes the ufw rule located at #
sudo ufw insert {#} {rule}: Inserts the ufw rule at # position

                --MYSQL COMMANDS--
sudo mysql -uroot -p: Log in to mySQL
\s: Check status of server
     -Look for SSL (enabled/disabled)
sudo nano /etc/mysql/my.cnf: View SQL configuration file
     -Add the following lines at the end:
     -[mysqld]
     -bind-address = 0.0.0.0
     -require_secure_transport = ON
sudo service mysql restart: Restart the mySQL service to update config

            --OTHER HELPFUL COMMANDS--
hostname -i: Displays your IP address
man {command}: Displays the manual for command 
service --status-all | grep '\[ + \]': shows all currently runing services
chattr +a /path/to/folder : makes a folder immutable
chattr +i /path/to/file : makes a file immutable 


'''



"""
How to secure SSH on linux

Access ssh config:
    sudo nano /etc/ssh/sshd_config

Things to change:
   
change - #AddressFamily (to) AddressFamily inet (this changes to ipv4)(remove # to change)
change - #PermitRootLogin (to) PermitRootLogin no (remove # to change)
notes:
    
after this will need to put -p after the ssh to specify port-

"""
