# ProjectDevops2

## Trello

Link to Trello Board: [Trello]()

## Breif

To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

this project should include:

- Project Management
- Python
- Python Testing
- Git
- Linux
- Python Web Development
- Continuous Integration
- Cloud Fundamentals
- Databases

## Approach to the project

- service1
  - frontend
    - develop a frontend that the user can interact with
  - database
    - presistant storage

- service2
  - the frontend will make a call to service to, generate a 2 or 3 character long string

- service3
  - the frontend will make a call to service to, generate a number string 6 to 8 characters long

- service4
  - based on the string generated will random choose a small prize or large prize


## Architecture
this project has a lot of moving parts, sometimes hard to keep track of which is why i thought it would be a good idea to draw a diagram of how the architecture of the final product should look like

![Architecture]()

## method

**The method i chose for this project was itterative, I first started with with the python app, then i dockerised the app. I then procceded to test if all the services were interacting thats why you will see on github, my compose file did include nginx but in the final version it does not. I then created a pipeline that pushes docker images to docker hub before pulling them and deploying on the swarm manager**

## Project Management

for this trello was what i used for this. This allowed me to follow a clear plan to streamline the development process in an agile way throught the project, moving tickets 
to the relevent position in the development stage

![Trello]()

## CI

for the CI server i used, Jenkins, this is what the pipline that i have setup looks like. within the process there is a webhook setup so each time i push the code, jenkins will test, build, push, configure the swarm and finally deploy

![CI]()

## Testing

For testing I used pytest to provide me test coverage of the flask application when conducting unit testing,
getting as close to 100% is ideal, showing all functions have been tested before being deployed.
automated testing whenever pushed from github is useful and allows the version to fail if the testing also fails which would stop the next job, deploying the website to also stop.

![Pytest]()

## Risk Assessment

![Risk Assessment]()

## Future Improvements

- UI changes
- css and javascript to improve UX
- improved testing with jenkins plugins.

## Author

**Jack Pendlebury**

## how to install

```sh
$ git clone https://github.com/JackPendlebury1/ProjectDevOps2.git
```

```sh
$ export rootpass=
```

```sh
$ export SECRET_KEY
```

```sh
$ docker-compose pull && docker-compose up -d
```
