echo "Apt Update.."
apt-get -qqy update
echo "Apt Install.."
apt-get -qqy install postgresql libpq-dev libyaml-0-2 libyaml-dev
apt-get -qqy install python3 python3-dev python3-pip python3-setuptools
# Pillow requirements
apt-get -qqy install libtiff5-dev libjpeg8 libjpeg8-dev zlib1g zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

echo "Setup Postgres"
su postgres -c 'createuser -d kavala'
su postgres -c 'createdb -O  kavala kavala'

echo "Pip install requirements"
cd /home/vagrant/kavala
pip3 install -r requirements.txt

vagrantTip="The shared directory is located at /home/vagrant/kavala\nTo access your shared files: cd kavala"

echo -e $vagrantTip > /etc/motd

