# Health Check Service 🏥

A lightweight, containerized service that monitors backend server health and reports status to healthchecks.io, perfect for home server monitoring.

## Overview 🔍

This service performs periodic health checks on a specified backend server and reports its status to healthchecks.io. Built with reliability and simplicity in mind, it's ideal for monitoring self-hosted services and personal servers.

## Features ✨

- 🔄 Monitors backend server endpoint every 30 minutes
- 📊 Reports status to healthchecks.io
- 📝 Comprehensive logging with timestamps
- 🐳 Docker support for easy deployment
- 🔄 Automatic restart on failure
- 📁 Persistent log storage
- ⚙️ Environment variable configuration

## Prerequisites 📋

- Python 3.11+ or Docker
- Internet connectivity
- healthchecks.io account (for monitoring)

## Configuration ⚙️

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Update the `.env` file with your configuration:
```env
BACKEND_URL=https://your-backend-url
HEALTHCHECK_UUID=your-healthcheck-uuid
HEALTHCHECK_BASE_URL=https://hc-ping.com  # Optional, defaults to https://hc-ping.com
```

Required environment variables:
- `BACKEND_URL`: The URL of your backend server to monitor
- `HEALTHCHECK_UUID`: Your healthchecks.io UUID

Optional environment variables:
- `HEALTHCHECK_BASE_URL`: Base URL for healthchecks.io (defaults to https://hc-ping.com)

## Setup 🚀

### Running Locally

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the service:
```bash
python healthcheck.py
```

### Running with Docker (Recommended)

1. Build the Docker image:
```bash
docker build -t healthcheck-service .
```

2. Run the container:
```bash
docker run -d \
  --name healthcheck \
  --restart unless-stopped \
  -v $(pwd)/logs:/app/logs \
  --env-file .env \
  healthcheck-service
```

Alternatively, you can provide environment variables directly:
```bash
docker run -d \
  --name healthcheck \
  --restart unless-stopped \
  -v $(pwd)/logs:/app/logs \
  -e BACKEND_URL=https://your-backend-url \
  -e HEALTHCHECK_UUID=your-healthcheck-uuid \
  healthcheck-service
```

## Logs 📊

The service maintains detailed logs in two locations:
- File: `logs/healthcheck.log`
- Docker container logs (when running in Docker)

To view container logs:
```bash
docker logs healthcheck
```

## Project Structure 📁

```
.
├── Dockerfile          # Docker configuration
├── README.md          # Documentation
├── healthcheck.py     # Main service script
├── requirements.txt   # Python dependencies
├── .env.example       # Example environment configuration
├── .env              # Your environment configuration (git-ignored)
└── .gitignore        # Git ignore rules
```
