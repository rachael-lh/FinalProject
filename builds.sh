chmod +x /usr/local/bin/docker-compose
usermod -aG docker $(whoami)
usermod -aG docker jenkins
chmod 666 /var/run/docker.sock
docker-compose down --rmi all
docker-compose build