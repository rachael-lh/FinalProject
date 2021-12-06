sudo chmod +x /usr/local/bin/docker-compose
sudo usermod -aG docker $(whoami)
sudo usermod -aG docker jenkins
sudo chmod 666 /var/run/docker.sock
docker-compose down --rmi all
docker-compose build