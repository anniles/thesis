# thesis
Tour guide for Kavala City

## installation

- run `npm i` to install any dependencies

- Install vagrant and virualbox

- run `vagrant up` to bring up the vm (the first time it downloads the box and provisions the vm.

- run `vagrant ssh` after to connect to the vm.

- set database access:

    `sudo -u postgres psql`

    ```sql
    alter user kavala with password '123456'
    ```

- inside the vm run `python3 manage.py migrate`.

 - to run the server inside the vm run:  
    `python3 manage.py runserver 0.0.0.0:8000`

    afterwards you can open your browser and point at `localhost:8000`.

- `vagrant halt` shuts down the vm

## build assets

Using the gulp task runner

Tasks:

- `gulp sass`: compiles sass to css and uses an autoprefixer for the css
- `gulp sass:watch`: watches predefined sources for changes and runs `gulp sass`
- `gulp`: runs the 2 above
