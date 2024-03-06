# Pokémon Squads API

## Overview
The Pokémon Teams API enables users to create, manage, and retrieve Pokémon teams. Each team is associated with a user and can consist of multiple Pokémon, each with their specific stats including name, weight, and height. This API is perfect for Pokémon enthusiasts who wish to organize their ideal Pokémon teams and share them with others.

## Features
- **Create a Team**: Users can create a new Pokémon team by specifying a user name and a list of Pokémon.
- **List All Teams**: Retrieves a list of all created Pokémon teams with detailed information about each Pokémon in the team.
- **Retrieve a Team by User**: Users can fetch a specific team by providing the user's name.

## Technologies Used
- **Django Rest Framework**: For building the RESTful API.
- **PostgreSQL**: As the relational database to store team and Pokémon data.
- **Docker**: For containerization, ensuring the application is easy to setup and run across different environments.

## Getting Started

### Prerequisites
- Docker
- docker-compose

### Setup Instructions
1. Clone the repository to your local machine:
```
git clone git@github.com:joaoleahy/PokeSquadAPI.git
```

2. Use docker-compose to build and start the service:
```
docker-compose up --build
```
The API will now be running locally on the port specified in the `docker-compose.yml` file, typically accessible via `http://localhost:8000`.

## API Endpoints

### Create a Team
- **Endpoint**: `POST /api/teams/create/`
- **Body**:
```json
{
  "user": "Ash",
  "team": ["pikachu", "charizard", "bulbasaur"]
}
```
- **Description**: Creates a new Pokémon team associated with the provided user name.

### List All Teams
- **Endpoint**: `GET /api/teams/`
- **Description**: Fetches a list of all Pokémon teams, including detailed information about the Pokémon in each team.

### Retrieve a Team by User
- **Endpoint**: `GET /api/teams/{user}`
- **Description**: Retrieves a specific Pokémon team by user name.


## Author
- [João Leahy](https://github.com/joaoleahy)
