mkdir blog1
mv deployment.tar.gz blog1
cd blog1; tar -zxvf deployment.tar.gz; cd $HOME;
cd blog; docker-compose stop; cd $HOME;
sudo rm -rf blog; mv blog1 blog;
cd blog; docker-compose up -d django
echo "Trying to run django migrate";
docker exec -it ahins-prod /bin/bash -c "python3 manage.py migrate"
