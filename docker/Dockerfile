# REE Experiment Runner -- GPU variant (NVIDIA CUDA 12.1)
# Requires: nvidia-container-toolkit on Linux, Docker Desktop + WSL2 on Windows
#
# Build:
#   docker build -t ree-runner:gpu -f Dockerfile .
#
# Run (quick test):
#   docker run --gpus all -p 8000:8000 -v ~/.ssh:/root/.ssh:ro ree-runner:gpu
#
# Run via docker-compose (recommended):
#   docker compose -f docker-compose.yml up

FROM nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu22.04

# Prevent interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3.11 \
        python3.11-venv \
        python3-pip \
        git \
        openssh-client \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Make python3.11 the default python3
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 \
    && update-alternatives --install /usr/bin/python python3 /usr/bin/python3.11 1

# Python deps -- PyTorch with CUDA 12.1
RUN pip3 install --no-cache-dir \
        torch==2.1.0+cu121 \
        torchvision==0.16.0+cu121 \
        --extra-index-url https://download.pytorch.org/whl/cu121

RUN pip3 install --no-cache-dir \
        numpy>=1.24.0 \
        "dataclasses-json>=0.6.0"

# Force UTF-8 output (ASCII-safe print statements still used throughout REE)
ENV PYTHONIOENCODING=utf-8
ENV PYTHONUNBUFFERED=1

# Workspace directory where repos are cloned at startup
RUN mkdir -p /workspace
WORKDIR /workspace

# Entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# serve.py binds to 0.0.0.0:8000 already
EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
