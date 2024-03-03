# Game of Skate backend

## Installation
Requirements:
(please enure these are on your machine, or if not, install them)
 - [python 3.10](https://www.python.org/psf/)
 - [Docker](https://docs.docker.com/get-docker/)

### Set Up Your Local Development Environment
 - clone this repo
 - `cd` into `gos-be`
 - `make start-app`

navigate to [http://localhost:8000/admin/login/?next=/admin/](http://localhost:8000/admin/login/?next=/admin/) in your broser and log in with the `DJANGO_SUPERUSER_USERNAME` and `DJANGO_SUPERUSER_PASSWORD` in 
`src/gos/gos/.env.local`

## Test App
*While the app is running* from main directory (same directory as `Makefile`) run:
`make test-app`


## Troubleshooting

### Docker

Q: I am getting `[48720] Failed to execute script docker-compose`
A: Try running Docker and trying again.

Q: I add things to requirements.txt but they're not getting added! why?
A: Try clearing the cache: `docker system prune -a`