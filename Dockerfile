# Step 1: Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Step 2: Set the working directory in the container
WORKDIR /app
# COPY . /app

# Step 3: Install any required dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    git \
    # Add any additional dependencies your application requires
    && rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/WandererGuy/Ethnic-Minority-Machine-Translation.git
WORKDIR /app/Ethnic-Minority-Machine-Translation
RUN apt-get update
RUN apt-get install -y cmake build-essential pkg-config libgoogle-perftools-dev
RUN git clone https://github.com/google/sentencepiece.git
WORKDIR /app/Ethnic-Minority-Machine-Translation/sentencepiece
RUN mkdir build
WORKDIR /app/Ethnic-Minority-Machine-Translation/sentencepiece/build
RUN cmake ..
RUN make -j $(nproc)
RUN make install
RUN ldconfig -v
WORKDIR /app/Ethnic-Minority-Machine-Translation
RUN tar -zxvf 2.3.0.tar.gz
RUN mv OpenNMT-py-2.3.0 OpenNMT-py
WORKDIR /app/Ethnic-Minority-Machine-Translation/OpenNMT-py
RUN pip install -e .
WORKDIR /app/Ethnic-Minority-Machine-Translation
RUN pip install nltk
RUN pip install fastapi uvicorn pydantic python-multipart
RUN mkdir data
RUN cp target_source/target_source_ede.txt data
RUN mv data/target_source_ede.txt data/target_source.txt
RUN pip install OpenNMT-tf
RUN pip install tensorflow
RUN pip install 'keras<3.0.0' mediapipe-model-maker

# Make the script executable
# RUN chmod +x /app/script.sh
RUN ln -s /usr/bin/python3 /usr/bin/python
CMD ["python", "START.py"]

 

# # Update the package list and install dependencies
# RUN apt-get update && apt-get install -y \
#     software-properties-common \
#     curl \
#     && add-apt-repository ppa:deadsnakes/ppa \
#     && apt-get update \
#     && apt-get install -y python3.10 python3.10-venv python3.10-dev

# # Set the default python version to 3.10
# RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
