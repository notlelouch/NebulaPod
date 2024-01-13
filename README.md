[![progress-banner](https://backend.codecrafters.io/progress/docker/ecc992c6-193d-487b-b151-aa907fd8d6ff)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

# NebulaPod

NebulaPod is a Docker implementation written in Python that allows you to pull Docker images from Docker Hub and execute commands within them. This project is designed to provide a lightweight and efficient alternative for running containerized applications without the need for a full-fledged container runtime.

## Features

- **Docker Image Execution:** Run commands inside Docker images pulled from Docker Hub.
- **STDOUT and STDERR Handling:** Capture and display standard output and error streams.
- **Exit Code Handling:** Properly handle and return exit codes from executed commands.
- **Filesystem Isolation:** Enhance security by isolating the filesystem for each container.
- **Process Isolation:** Isolate processes within the container for improved resource management.
- **Docker Registry Support:** Fetch Docker images from any Docker registry.

## Getting Started

### Prerequisites

Python 3.6 or higher

### Installation

Clone the repository and navigate to the project directory:

```bash
    git clone https://github.com/<your-username>/NebulaPod.git
    cd NebulaPod
   ```

## Usage

You can now execute your program like this:

```sh
mydocker run ubuntu:latest /usr/local/bin/docker-explorer echo hey
```

## Project Structure

**main.py:** The core implementation of NebulaPod

## Contributing

Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, please open an issue or submit a pull request.

