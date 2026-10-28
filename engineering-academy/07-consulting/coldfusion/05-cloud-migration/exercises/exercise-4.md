# Exercise 4: CI/CD Pipeline

> Build a complete CI/CD pipeline for ColdFusion.

## Objective

Learn to create automated deployment pipelines for ColdFusion applications.

## Scenario

**Application:** Multi-environment CF app
**Environments:** Dev, Staging, Production
**Requirements:** Blue-green deployment, rollback capability

## Instructions

### Part 1: Pipeline Architecture

Design the pipeline:

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│   Dev   │────►│ Staging  │────►│Production│
│ Auto    │     │ Manual   │     │ Blue-    │
│ Deploy  │     │ Approve  │     │ Green    │
└──────────┘     └──────────┘     └──────────┘
```

### Part 2: GitHub Actions Workflow

Create the CI/CD workflow:

```yaml
name: CF CI/CD Pipeline

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      mysql:
        image: mysql:8.0
        env:
          MYSQL_ROOT_PASSWORD: test
        options: >-
          --health-cmd="mysqladmin ping"
          --health-interval=10s
          --health-timeout=5s
          --health-retries=5
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup CommandBox
        run: |
          wget https://downloads.ortusolutions.com/CommandBox/linux/amd64/commandbox.zip
          unzip commandbox.zip
          
      - name: Install dependencies
        run: |
          box install
          
      - name: Run tests
        run: |
          box testbox run reporter=json
          
      - name: Upload test results
        uses: actions/upload-artifact@v3
        with:
          name: test-results
          path: test-results.json

  build:
    needs: test
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      # Build Docker image
      
      _______________________________________________________
      
      - name: Push to registry
        run: |
          docker push $ECR_REGISTRY/cf-app:${{ github.sha }}
          
      - name: Deploy to staging
        run: |
          aws ecs update-service --cluster staging --service cf-app --force-new-deployment

  deploy-production:
    needs: build
    runs-on: ubuntu-latest
    environment: production
    
    steps:
      - name: Deploy to production
        run: |
          # Blue-green deployment
          
          _______________________________________________________
          
      - name: Smoke test
        run: |
          curl -f https://api.example.com/health
```

### Part 3: Blue-Green Deployment

Complete the blue-green deployment:

```bash
#!/bin/bash

# Blue-Green Deployment Script

DEPLOYMENT_GROUP=$(aws deploy get-deployment-group \
    --application-name cf-app \
    --deployment-group-name production)

# Step 1: Deploy to new (green) environment
aws deploy create-deployment \
    --application-name cf-app \
    --deployment-group-name production \
    --deployment-config-name CodeDeployDefault.HalfAtATime \
    --revision "{\"revisionType\":\"Docker\",\"dockerImage\":\"$ECR_REGISTRY/cf-app:$GITHUB_SHA\"}" \
    --description "Deploy version $GITHUB_SHA"

# Step 2: Wait for deployment

# Step 3: What command tests the green environment?


# Step 4: How do you switch traffic to green?


# Step 5: What if something goes wrong?
```

### Part 4: Rollback Strategy

Design the rollback procedure:

| Step | Action | Command |
|------|--------|---------|
| 1 | Identify issue | |
| 2 | | aws deploy stop-deployment |
| 3 | Switch traffic to blue | |
| 4 | Verify | |

## Expected Outcome

1. Complete CI/CD workflow
2. Blue-green deployment script
3. Rollback procedure

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| CI workflow complete | 30 |
| CD pipeline logical | 30 |
| Blue-green script | 20 |
| Rollback procedure | 15 |
| Professional presentation | 5 |
| **Total** | **100** |

**Passing Score:** 70/100
