# Use Jenkins LTS image
FROM jenkins/jenkins:lts

USER root

# Install base dependencies + build tools for Python
RUN apt-get update -y && \
    apt-get install -y \
        ca-certificates \
        curl \
        gnupg \
        wget \
        build-essential \
        zlib1g-dev \
        libssl-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        libffi-dev \
        liblzma-dev \
        xz-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Docker (your original configuration)
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg \
        | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg && \
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
    https://download.docker.com/linux/debian \
    $(. /etc/os-release && echo $VERSION_CODENAME) stable" \
    > /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# -------- Install Python 3.10.16 --------
WORKDIR /usr/src

RUN wget https://www.python.org/ftp/python/3.10.16/Python-3.10.16.tgz && \
    tar -xzf Python-3.10.16.tgz && \
    cd Python-3.10.16 && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall

# Create symlink
RUN ln -s /usr/local/bin/python3.10 /usr/bin/python && \
    ln -s /usr/local/bin/pip3.10 /usr/bin/pip

# Verify
RUN python --version

# Add Jenkins user to docker group
RUN groupadd -f docker && \
    usermod -aG docker jenkins

VOLUME /var/lib/docker

USER jenkins