sudo apt-get update
sudo apt-get install -y software-properties-common
sudo add-apt-repository universe
sudo apt-get update

sudo apt-get install -y certbot python3-certbot-nginx

sudo certbot --nginx -n --domain ishankhare.dev --redirect --agree-tos -m me@ishankhare.dev
