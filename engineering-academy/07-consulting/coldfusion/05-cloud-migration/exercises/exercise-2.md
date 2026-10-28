# Exercise 2: Docker Containerization

> Containerize a ColdFusion application.

## Objective

Learn to create Docker containers for ColdFusion/Lucee applications.

## Scenario

**Application:** API service built in Lucee
**Requirements:** Auto-scaling, zero-downtime deployment

## Instructions

### Part 1: Dockerfile

Create a production Dockerfile:

```dockerfile
# Multi-stage build
FROM ortussolutions/commandbox:latest AS builder

WORKDIR /app
COPY . /app

# Install dependencies
RUN box install

# Production image
FROM ortussolutions/commandbox:alpine

# What should you add for security?

_______________________________________________________________

# Copy application
COPY --from=builder /app /app
WORKDIR /app

# Configuration - what's the best approach?

_______________________________________________________________

EXPOSE 8080
CMD ["server", "start"]
```

### Part 2: Docker Compose

Create docker-compose.yml:

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8080:8080"
    environment:
      - JAVA_OPTS=-Xmx2g
      - APP_ENV=production
    depends_on:
      - redis
      - database
    volumes:
      - uploads:/app/uploads

  redis:
    image: redis:alpine
    volumes:
      - redis-data:/data

  database:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
    volumes:
      - db-data:/var/lib/mysql

# What's missing for production?

_______________________________________________________________

volumes:
  redis-data:
  db-data:
  uploads:
```

### Part 3: Session Management

Configure Redis for session sharing:

```dockerfile
# In your Dockerfile or Lucee config
ENV LUCEE_SESSION_STORE=redis
ENV LUCEE_REDIS_HOST=redis
ENV LUCEE_REDIS_PORT=6379
```

**Application.cfc configuration:**

```cfml
component {
    this.name = "MyAPI";
    
    function onApplicationStart() {
        // Session storage configuration
        application.sessionStorage = {
            type: "redis",
            host: serverSystem.ENV.LUCEE_REDIS_HOST ?: "redis",
            port: serverSystem.ENV.LUCEE_REDIS_PORT ?: 6379,
            timeout: 3600
        };
    }
}
```

**Why use Redis for sessions?**

1. ___________________________________________________
2. ___________________________________________________

### Part 4: CI/CD Pipeline

Create GitHub Actions workflow:

```yaml
name: Docker CI/CD

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Build Docker image
        run: |
          docker build -t api:${{ github.sha }} .
          
      # What else?

      - name: Push to ECR
        run: |
          aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_REGISTRY
          docker tag api:${{ github.sha }} $ECR_REGISTRY/api:latest
          docker push $ECR_REGISTRY/api:latest

      - name: Deploy to ECS
        run: |
          aws ecs update-service --cluster production --service api --force-new-deployment
```

## Expected Outcome

1. Production Dockerfile
2. Docker Compose
3. Session configuration
4. CI/CD pipeline

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Dockerfile production-ready | 25 |
| Docker Compose complete | 25 |
| Session config appropriate | 20 |
| CI/CD workflow logical | 20 |
| Security considerations | 10 |
| **Total** | **100** |

**Passing Score:** 70/100
