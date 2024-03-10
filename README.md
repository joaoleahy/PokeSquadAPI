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
- **Swagger (drf-yasg)**: To provide a user-friendly interface for documenting and testing the API endpoints. Swagger makes it easy for developers and users to understand the API's capabilities without digging into the source code.

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

### Setup Instructions for Local Testing Without Docker

If you're unable to use Docker or prefer to run the API directly on your local machine, follow these steps:

1. **Clone the repository** to your local machine:
   ```
   git clone git@github.com:joaoleahy/PokeSquadAPI.git
   ```

2. **Navigate into the project directory**:
   ```
   cd PokeSquadAPI
   ```

3. **Install the required Python packages**. It's recommended to use a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. **Set up your PostgreSQL database**:
   - Ensure PostgreSQL is installed on your system.
   - Create a database for the project.
   - Modify the `DATABASES` setting in `settings.py` to reflect your PostgreSQL configuration, specifically the `NAME`, `USER`, and `PASSWORD`.

5. **Run migrations** to set up your database schema:
   ```
   python manage.py migrate
   ```

6. **Collect static files** (if your project uses Django's static files):
   ```
   python manage.py collectstatic
   ```
7. **Run the tests to ensure everything is working as expected:**:
   ```
   python manage.py test
   ```

8. **Start the Django development server**:
   ```
   python manage.py runserver
   ```
   The API will now be running locally on `http://localhost:8000`.

9. **Access the API** via the browser or using a tool like Postman to test the endpoints.

Remember to deactivate your virtual environment when you're done by running `deactivate`.

This setup allows you to run and test the API directly on your machine, bypassing the need for Docker.

## API Endpoints

### Create a Team
- **Endpoint**: `POST /api/teams/create/`
- **Body**:
```json
{
  "user": "Jon",
  "team": ["pikachu", "charizard", "bulbasaur"]
}
```
- **Description**: Creates a new Pokémon team associated with the provided user name.

### List All Teams
- **Endpoint**: `GET /api/teams/`
```json
{
  "1": {
    "owner": "Ash",
    "pokemons": [
      {
        "id": 9,
        "name": "blastoise",
        "weight": 855,
        "height": 16
      },
      {
        "id": 25,
        "name": "pikachu",
        "weight": 60,
        "height": 4
      }
    ]
  },
  "2": {
    "owner": "Dany",
    "pokemons": [
      {
        "id": 9,
        "name": "blastoise",
        "weight": 855,
        "height": 16
      },
      {
        "id": 25,
        "name": "pikachu",
        "weight": 60,
        "height": 4
      },
      {
        "id": 3,
        "name": "venusaur",
        "weight": 1000,
        "height": 20
      },
      {
        "id": 6,
        "name": "charizard",
        "weight": 905,
        "height": 17
      },
      {
        "id": 131,
        "name": "lapras",
        "weight": 2200,
        "height": 25
      },
      {
        "id": 54,
        "name": "psyduck",
        "weight": 196,
        "height": 8
      }
    ]
  }
}
```
- **Description**: Fetches a list of all Pokémon teams, including detailed information about the Pokémon in each team.

### Retrieve a Team by User
- **Endpoint**: `GET /api/teams/{user}`
```json
{
  "owner": "Ash",
  "pokemons": [
    {
      "id": 9,
      "name": "blastoise",
      "weight": 855,
      "height": 16
    },
    {
      "id": 25,
      "name": "pikachu",
      "weight": 60,
      "height": 4
    }
  ]
}
```
- **Description**: Retrieves a specific Pokémon team by user name.


## Author
- [João Leahy](https://github.com/joaoleahy)
