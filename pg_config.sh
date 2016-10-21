echo "Apt Update.."
apt-get -qqy update
echo "Apt Install.."
apt-get -qqy update
apt-get -qqy install postgresql libpq-dev 
apt-get -qqy install python3 python3-dev python3-pip python3-setuptools
apt-get -qqy install libtiff5-dev libjpeg libjpeg-dev libjpeg8-dev zliblg-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

echo "Setup Postgres"
su postgres -c 'createuser -d kavala'
su postgres -c 'createdb -O  kavala kavala'

# seems useless
echo "export PYTHONPATH=/usr/lib/python3" >> /home/vagrant/.bashrc

echo "Pip install requirements"
cd /home/vagrant/kavala
pip3 install -r requirements.txt

vagrantTip="[35m[1mThe shared directory is located at /vagrant\nTo access your shared files: cd /vagrant(B[m"

echo -e $vagrantTip > /etc/motd

