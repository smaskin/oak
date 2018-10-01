Установить и настроить сервер Ubuntu Server 17

brew install vagrant
vagrant init
поправил Vagrantfile
vagrant up
vagrant ssh
git clone https://github.com/smaskin/oak.gi
cd oak
sudo apt-get install python3-venv
python3 -m venv venv
. venv/bin/activate
pip install wheel
pip install -r requirements.txt
pip install psycopg2
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql
CREATE DATABASE geekshop;
CREATE USER django with NOSUPERUSER PASSWORD 'geekbrains';
GRANT ALL PRIVILEGES ON DATABASE oak TO django;
ALTER ROLE django SET CLIENT_ENCODING TO 'UTF8';
ALTER ROLE django SET default_transaction_isolation TO 'READ COMMITTED';
ALTER ROLE django SET TIME ZONE 'Asia/Yekaterinburg';
\q
python manage.py migrate
sudo systemctl status postgresql
sudo python3 manage.py runserver 192.168.33.10:80
python manage.py loaddata db.json
pip install gunicorn
