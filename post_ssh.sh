mkdir blog1
mv deployment.tar.gz blog1
cd blog1
echo "inflating deployment"
tar -zxvf deployment.tar.gz

cd $HOME/blog
echo "bringing down cluster"
docker-compose stop
cd $HOME

sudo rm -rf blog
mv blog1 blog
cd blog

echo "pulling latest docker images"
docker-compose pull
echo "bringing up cluster"
docker-compose up -d nginx-prod
echo "Trying to run django migrate"
docker exec -it ahins-prod /bin/bash -c "python3 manage.py migrate"
