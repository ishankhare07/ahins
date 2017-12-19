mkdir blog1
mv deployment.tar.gz blog1
cd blog1
echo "inflating deployment"
tar -zxvf deployment.tar.gz

cd $HOME/blog
echo "bringing down django instance"
docker-compose stop django
cd $HOME

sudo rm -rf blog
mv blog1 blog
cd blog

echo "pulling latest docker images"
docker-compose pull
echo "bringing up django"
docker-compose up -d django
echo "Trying to run django migrate"
docker exec -it ahins-prod /bin/bash -c "python3 manage.py migrate"
