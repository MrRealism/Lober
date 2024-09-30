import os

def secure_linux_system():
    # Update and upgrade the system (DISABLED FOR NOW)
    # os.system('sudo apt-get update && sudo apt-get upgrade -y')

    # Install security updates
    #os.system('sudo apt-get install unattended-upgrades -y')
    #os.system('sudo dpkg-reconfigure --priority=low unattended-upgrades')

    # Make backups
    os.system("sudo mkdir /dev/bkp")
    os.system("rocky")# change password when on diffrent box
    os.system("sudo cp /var /dev/bkp")
    os.system("sudo cp /etc /dev/bkp")
    os.system("sudo cp /opt /dev/bkp")
    os.system("sudo cp /home /dev/bkp")
    os.system("sudo chattr +a /dev/bkp")

    # Change Passwords
    os.system('sudo passwd rocky')
    os.system('Rocky')
    os.system('Rocky')

    # Configure the firewall
    os.system('sudo dnf install ufw -y')
    os.system('sudo ufw default deny incoming')
    os.system('sudo ufw default allow outgoing')
    os.system('sudo ufw allow ssh')
    os.system('sudo ufw allow ftp')
    os.system('sudo ufw enable')

    # Disable root login
    # os.system('sudo passwd -l root')

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
