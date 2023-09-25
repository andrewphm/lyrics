# Flask Lyrics Generator Application

This is a Flask web application that generates song lyrics using a Markov chain model.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes using Docker.

### Prerequisites

You need to have Docker installed on your machine. You can download Docker [here](https://www.docker.com/products/docker-desktop).

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/andrewphm/lyrics.git
```

Navigate to the project directory:

```bash
cd lyrics
```

### Building the Docker Image

To build the Docker image, run the following command in your terminal:

```bash
docker build -t my_flask_app .
```

This command builds a Docker image, which we tag (or name) as `my_flask_app`.

### Running the Docker Container

To run the application, execute the following command:

```bash
docker run -p 5000:5000 my_flask_app
```

This command maps the port 5000 inside the Docker container to the port 5000 on your machine, and then runs the Docker image we previously built.

### Accessing the Application

After running the Docker container, you should be able to access the application at:

```
http://localhost:5000
```

Just open this URL in your web browser.
