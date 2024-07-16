# fullstack-test-nina

Template repository for fullstack web developers at Super NINA.

# Challenge

**Remember to create a new repository with this one as the template. This can be achieved with the button "Use this template", at the top right corner of this repo's github page!**

**Don't clone or fork this repository, as this method could expose your submission to other candidates and allow your hard work to be copied.**

As part of the selection process, we would like you to:

1. [Backend] Implement a missing feature that returns all the complaints from a given user. This will measure your ability in developing new features in an on-going project. This won't be used in the frontend, the route just needs to exist.
2. [Backend] Implement a filtering functionality to the get_complaints route (```/complaints```) allowing it to return only the complaints where the field ```date``` is in between the fields ```from_date``` and ```to_date```, passed through query parameters. This will be necessary for integration with the complaints table in the frontend and will measure your ability to develop and maintain FastAPI routes with parameters.
3. [Backend] Refactor the get_complaint route (```/complaint/{complaint_id}```) so that the returned complaint includes information about the user who registered it. This will be necessary for frontend integration and will measure your ability to develop and maintain python functions and FastAPI routes.

4. [Frontend] Build a small Angular application based on the provided template (there may be some errors that we left on purpose and you should fix), following the [design](https://www.figma.com/design/oosvhfSMv6OsCDCW27NWQ0/Processo-seletivo---2024?node-id=0-1&t=qbuEQHZKt86TTp7j-1) provided by our designer. This will allow us to evaluate your understanding of Angular and measure how well you work with a designer on the team.
5. [Frontend] The application should be able to make a REST API call to the provided backend endpoints and integrate the data with the UI. This will allow us to evaluate your understanding of HTTP requests, and working with external APIs.
6. [Frontend] Implement routing for the 2 pages needed for the Angular Application.

**Helpful tip! After starting the backend server, be sure to check the API's documentation at `http://127.0.0.1:8000/docs`**

Your submission will be tested using:

- Python 3.11
- Node 18.19
- Angular CLI 18.1

<!-- - Connect to a web socket and display real time notifications as pop-ups. This will allow us to evaluate your understandings of websockets and data streaming. -->

Anything more than that such as useful documentation, automated tests or the creation of docker containers will be counted as bonus features and **will** highlight your submission. Remember to explicitly point how to run your additions if you introduced them!

**Not being able to complete all the assignments does not mean failing the challenge! Try to do as much as possible and send us your submission before the deadline even if it's incomplete!**

After the test, even if you aren't selected, the devs at Super NINA will do their best to give you honest feedback and guide you to future improvements.

When you have completed the test, please submit to us (as a response to the email informing you were selected for the tech challenge):

- A link to the code repository (e.g. GitHub, GitLab, etc.) where we can view your code.

- A brief explanation of your decisions, any challenges you encountered, and how you overcame them (in regard to the challenge).

We look forward to seeing your work!

# Backend

## Requirements

- Python 3.11+

## Installing dependencies

From the root of the project, run:

```sh
pip install -r back/requirements.txt
```

## Running server

From the root of the project, run:

```sh
fastapi dev back/app.py
```

# Frontend

## Requirements

- Node 18.19+

## Installing dependencies

From the root of the project, run:

```sh
cd front
npm install
```

## Running frontend

From the root of the project, run:

```sh
cd front
npm start
```
