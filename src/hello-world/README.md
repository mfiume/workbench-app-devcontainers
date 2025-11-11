# Hello World Flask App for Verily Workbench

A simple Flask web application demonstrating custom app deployment in Verily Workbench.

## Features

- 🌶️ **Flask Web Framework** - Python-based web application
- 🎨 **Beautiful UI** - Animated, gradient-styled interface
- 🏥 **Health Checks** - Built-in health and info endpoints
- 🐳 **Docker-based** - Containerized for easy deployment
- ☁️ **Workbench-ready** - Configured for Verily Workbench

## Endpoints

- `/` - Main hello world page with animated UI
- `/health` - Health check endpoint (JSON)
- `/api/info` - Application information endpoint (JSON)

## Deployment in Verily Workbench

### Repository Configuration

```
Repository URL:     git@github.com:mfiume/workbench-app-devcontainers.git
Repository branch:  hello-world-app
Folder path:        src/hello-world
```

### Compute Configuration

- **Machine Type:** n1-highmem-2 (2 CPU, 13 GB)
- **Disk Size:** 100 GB
- **Port:** 8888

## Files

- `app.py` - Flask application with routes
- `Dockerfile` - Container image definition
- `docker-compose.yaml` - Service orchestration
- `requirements.txt` - Python dependencies
- `.devcontainer.json` - Workbench configuration
