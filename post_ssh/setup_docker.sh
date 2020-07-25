sudo apt-get update
sudo apt-get install -y \
    sudo apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent

DEBIAN_FRONTEND=noninteractive sudo apt-get install -y software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"

sudo apt update
sudo apt install -y docker-ce docker-ce-cli 
sudo usermod -aG docker ishankhare
docker run hello-world
