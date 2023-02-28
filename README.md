# Code_Isekai

## Judge0 Deployment

### With HTTP
1. Install [Docker](https://docs.docker.com) and [Docker Compose](https://docs.docker.com/compose).
2. Download and extract the release archive:
```
wget https://github.com/judge0/judge0/releases/download/v1.13.0/judge0-v1.13.0.zip
unzip judge0-v1.13.0.zip
```

3. Run all services and wait a few seconds until everything is initialized:
```
cd judge0-v1.13.0
docker-compose up -d db redis
docker-compose up -d
```

4. Your instance of Judge0 CE v1.13.0 is now available at `http://<IP ADDRESS OF YOUR SERVER>:2358`.
