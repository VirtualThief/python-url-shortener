# The URL shortener in Python

## How to build

To create development build

    docker-compose -f .\docker-compose.common.yaml -f .\docker-compose.dev.yaml build

To run development build

    docker-compose -f .\docker-compose.common.yaml -f .\docker-compose.dev.yaml up

To stop development build

    docker-compose -f .\docker-compose.common.yaml -f .\docker-compose.dev.yaml down

Build container for testing

    docker-compose -f .\docker-compose.test.yaml build

Run tests

    docker-compose -f .\docker-compose.test.yaml up