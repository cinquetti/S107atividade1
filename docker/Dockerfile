# Use a imagem oficial do Python 3.8
FROM python:3.8-slim

# Atualiza e instala dependências
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libffi-dev \
        liblzma-dev \
        python-openssl \
        git \
    && rm -rf /var/lib/apt/lists/*

# Instala pipenv globalmente
RUN pip install --upgrade pip setuptools wheel

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o requirements.txt para o contêiner e instala as dependências
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Define um entrypoint padrão
CMD ["python3", "--version"]
