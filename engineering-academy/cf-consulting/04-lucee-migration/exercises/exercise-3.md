# Exercise 3: Docker Containerization

> Containerize a ColdFusion application for Lucee.

## Objective

Learn to create Docker containers for Lucee applications.

## Instructions

### Part 1: Dockerfile Creation

Create a Dockerfile for a Lucee application:

```dockerfile
# Base image
FROM ortussolutions/commandbox:latest

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN box install

# Expose port
EXPOSE 8080

# Start CommandBox server
CMD ["server", "start"]
```

**Your Task:** Improve the Dockerfile for production:

```dockerfile
# Base image
FROM ortussolutions/commandbox:latest AS build

# Variables
ARG APP_NAME=myapp
ARG ENV=production

# Build stage
WORKDIR /app

# What goes here?
_______________________________________________________________

# Production stage
FROM ortussolutions/commandbox:alpine

# What security considerations?

_______________________________________________________________

# Copy application
COPY --from=build /app /app
WORKDIR /app

# What about configuration secrets?

_______________________________________________________________

EXPOSE 8080
CMD ["server", "start"]
```

### Part 2: Docker Compose

Create docker-compose.yml for a multi-container setup:

```yaml
version: '3.8'

services:
  lucee:
    build: .
    ports:
      - "8080:8080"
    environment:
      - JAVA_OPTS=-Xmx2g
    volumes:
      - ./app:/app
    depends_on:
      - redis
      - database
    networks:
      - app-network

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data

  database:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}
    volumes:
      - db-data:/var/lib/mysql
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

# What else is needed?

_______________________________________________________________

volumes:
  redis-data:
  db-data:

networks:
  app-network:
    driver: bridge
```

### Part 3: Health Check

Add a health check to the Lucee container:

```dockerfile
# Add health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1
```

**Your Task:** Create the /health endpoint in CFML:

```cfml
<!--- /health.cfm --->

_______________________________________________________________

_______________________________________________________________
```

### Part 4: CI/CD Integration

Create a GitHub Actions workflow for Docker deployment:

```yaml
name: Deploy to Docker

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      # What steps are needed?

      - name: Build Docker image
        run: |

_______________________________________________________________

      - name: Push to registry
        run: |

_______________________________________________________________

      - name: Deploy to production
        run: |

_______________________________________________________________
```

## Expected Outcome

1. Production-ready Dockerfile
2. Docker Compose with all services
3. Health check endpoint
4. CI/CD pipeline

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Dockerfile production-ready | 25 |
| Docker Compose complete | 25 |
| Health check implemented | 20 |
| CI/CD workflow logical | 20 |
| Security considerations | 10 |
| **Total** | **100** |

**Passing Score:** 70/100
