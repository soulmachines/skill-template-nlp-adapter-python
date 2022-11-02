# Skill Template - NLP Adapter <br/>[![GitHub license](https://img.shields.io/badge/license-Apache%202.0-blue)](./LICENSE) [![Python Version](https://img.shields.io/badge/python-v3.11-blue)](https://www.python.org/) [![FastAPI Version](https://img.shields.io/badge/fastAPI-v0.85.1-blue)](https://pypi.org/project/fastapi/)

This Python application is a template for Skill Developers to use as a starting point for writing an NLP Adapter Skill.

Written in [FastAPI](https://fastapi.tiangolo.com/).

See the [Soul Machines Skills Documentation](https://docs.soulmachines.com/skills-api) for more information.

## Pre-requisites:

- [Python 3.11](https://www.python.org/)
- [Pip 22.3](https://pip.pypa.io/en/stable/cli/pip_install/)
- [Docker Desktop and Compose](https://docs.docker.com/compose/install/)

## Env Variables

Create the `.env` file and add env variables as needed.

```
cp .env_example .env
```

## Quick Spin-up using Docker Compose

You may run the following commands to quickly spin up the application.

```
docker-compose up --build
```

### Tear-down via Docker Compose

When you want to stop the application, run:

```
docker-compose down
```

## Local Development

Create and activate Python's virtual env, then install requirements

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Run the following to start your local development server

```
python manage.py run
```

### Debugging with VS Code

1. Set up virtual env and install requirements as per [Local Development](#local-development)
2. Click on **Run and Debug**
3. Select **Python: Local Debugging** as the configuration
4. Add your breakpoints
5. Click the **Play** button

## Common Endpoints

Test the app's endpoints using Postman:

- POST Init: [http://localhost:3000/init]()
- POST Session: [http://localhost:3000/session]()
- POST Execute: [http://localhost:3000/execute]()
- DELETE Delete: [http://localhost:3000/delete]()

### Documentation

- Auto-generated OpenAPI docs of your app: [http://localhost:3000/docs]()

## Serve for use with Studio

Localtunnel may be used to generate a public web address for your locally-running Skill, allowing DDNA Studio to connect to your Skill from a live Digital Person.

Generate a URL with a personalized subdomain using the following command, and then use this URL to configure the endpoints in your Skill Definition.

```
npx localtunnel --port 3000 --subdomain your-unique-id
```

## Licensing
This repository is licensed under the Apache License, Version 2.0. See
[LICENSE](./LICENSE) for the full license text.

## Issues
For any issues, please reach out to one of our Customer Success team members.