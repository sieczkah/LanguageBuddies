
# Language Buddies

Web app that offers a platform for language enthusiasts to interact with each other in various languages in user-created chat rooms.




## Features

- CRUD operations for users, profiles, rooms, and messages along with authentication and authorization.
- Search functionality for filtering rooms by language, topic, or host.
- Activity feed to showcase recent activity on the web app.
- Random avatars upon User creation using [Multiavatar](https://multiavatar.com/) module.
- Responsive, user-friendly interface created with customized Bootstrap.


## Demo

https://siehy.pythonanywhere.com/


## Run Locally

### If you are using docker:

Pull the docker image with example database setup see the users in table below:

    $ docker pull siehy/language-buddies-sieczkah:latest

Run the docker image on port 8000

    $ docker run -p 8000:8000 siehy/language-buddies-sieczkah:latest

- Go to you localhost on your browser http://127.0.0.1:8000/ and try it!

### Github clone

Clone the project

```bash
  $ git clone https://github.com/sieczkah/LanguageBuddies.git
```
Cd to project directory
    
    $ cd {{ project_name }}
    
Create/Activate the virtualenv for your project.
    
    $ python -m venv .venv
    $ .venv/scripts/activate
    

    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
- Create the .env file.

- You can use .env.dist file that have example data in just rename it to .env

 
Prepare migrations:

    $ python manage.py makemigrations
    
Then simply apply the migrations:

    $ python manage.py migrate
    
You are ready to run the server:

    $ python manage.py runserver
    
- Go to you localhost on your browser http://127.0.0.1:8000/ and try it!   
 
#### Optional:

The repo contains JSON fixture file to populate the databse - to fast start the app.

To populate databes use

    $ python manage.py loaddata example_db.json
    
Example database contains of few rooms, basic languages, some messages.

It also contains users:
| Username | Password        | Type of user |
| :-------- | :---------     | :----------- |
| **admin** | **admin**      | Superuser    |
| **buddy1** | **testuser**  | normal       |
| **buddy2** | **testuser**  |  normal      |
| **buddy3** | **testuser**  |  normal      |
| **buddy4** | **testuser**  |  normal      |



#### RUN the development server:


    $ python manage.py runserver

#### It's up and running!

### If u decide to start the project from blank database you will have to create the superuser and follow the note below:

    $ python manage.py createsuperuser

To enable language support in the project, you need to create languages through the admin panel. Languages are creating by providing language name and Alpha_2 code for the flag.

For example English - GB, Polish - PL, Spanish - ES

. Once created, these languages can be applied to rooms.
It is important to note that when creating the superuser or users through the admin panel, you will need to manually create profiles for them.
Profiles are automatically created with a random avatar when a user registers through the registration form. This is the preferred method for user creation.
    
## Authors

- [@sieczkah](https://www.github.com/sieczkah)

