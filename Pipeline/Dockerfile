FROM openjdk:17-slim

# Create app folder and set as working directory
WORKDIR /booknlp

# Install dependencies
RUN apt-get update && apt-get install -y git wget unzip && apt-get clean

# Clone BookNLP
RUN git clone https://github.com/booknlp/booknlp.git .

# Set entrypoint to run BookNLP
ENTRYPOINT ["java", "-Xmx4g", "-jar", "/booknlp/booknlp.jar"]
