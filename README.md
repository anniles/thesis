# thesis
Tour guide for Kavala City

## installation

1. Install vagrant and virtualbox.

2. clone the repostitory and run:

    `$ vagrant up` at the root dir of the repo.

    It may take a while the first time.

3. When it is up you can run:

    `$ vagrant ssh`  to connect to the vm.

    the projects woking direcotry is

    `/home/vagrant/kavala`

4. We need now to set the db connection's password  
    connect as postgres user:

    ` $ sudo su postgres`

    ` $ psql`

    ` postgres# \password kavala` e.g: 123456

5. We now need to run the migrations:

    ` $ python3 manage.py migrate`

6. If we need sample data:

    ` $ python3 manage.py hotels rentals sights`

7. To access the admin we need a superuser

    ` $ python3 manage.py createsuperuser`

8. build the assets

    ` $ npm install`

    ` $ bower install`

    ` $ gulp sass`

9. Run the server

    ` $ python3 manage.py 0.0.0.0:8000`

Access the application at [localhost:5000](http://localhost:5000)
