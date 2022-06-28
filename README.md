# install_jenkins
sudo apt update

java -version
#if not install
sudo apt install default-jdk -y

#add key repo
sudo wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -

#add address repo
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update

#install jenkins
sudo apt install jenkins -y

#start jenkins
sudo systemctl start jenkins

#check 
sudo service jenkins status

#Setting jenkins

#Start the firewall
sudo ufw enable -y

#open port 8080
sudo ufw allow 8080

#firewall status
sudo ufw status

http://ip_addr_host:8080

#Show password
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
