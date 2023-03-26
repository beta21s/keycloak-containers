### Cấu hình

#### Cấu hình Docker

```
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

#### Cấu hình Docker-compose

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

#### Cấu hình Portainer để quản lý Docker

```
docker volume create portainerData
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainerData:/data portainer/portainer-ce:latest
```
