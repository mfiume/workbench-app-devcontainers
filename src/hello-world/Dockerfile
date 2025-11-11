FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        git \
        curl \
        vim \
        sudo \
        wget \
        ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create jovyan user (standard for Jupyter-based workbench apps)
ARG USERNAME=jovyan
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Install Python packages
RUN pip install --no-cache-dir \
    flask==3.0.0 \
    werkzeug==3.0.1

# Set up workspace directory
WORKDIR /workspace

# Create home directory structure
RUN mkdir -p /home/jovyan/work && chown -R jovyan:jovyan /home/jovyan

# Switch to jovyan user
USER jovyan

# Default command - will be overridden by docker-compose
CMD ["python", "app.py"]
