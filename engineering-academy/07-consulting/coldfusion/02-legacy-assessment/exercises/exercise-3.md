# Exercise 3: Architecture Mapping

> Create an architecture diagram for a legacy ColdFusion application.

## Objective

Learn to map application architecture from code analysis.

## Scenario

**Application:** Healthcare scheduling system
- 200 CFM files
- Plain CFM with includes
- MSSQL database
- External APIs (Lab system, Insurance verification)
- File storage for documents

## Instructions

### Part 1: Identify Application Structure

From the codebase, identify:

**Directory Structure:**
```
/scheduling
  /admin          # ___ files
  /appointments   # ___ files
  /patients       # ___ files
  /reports        # ___ files
  /includes       # ___ files
  /cfc            # ___ files
  /udf            # ___ files
  /js             # ___ files
  /css            # ___ files
  /images         # ___ files
  /documents      # ___ files (uploaded PDFs)
  Application.cfc
  index.cfm
  dsp_sidebar.cfm
  dsp_header.cfm
```

### Part 2: Database Analysis

Map the database schema:

**Core Tables:**

| Table | Purpose | Foreign Keys | Est. Rows |
|-------|---------|--------------|-----------|
| patients | | | |
| providers | | | |
| appointments | | | |
| locations | | | |
| insurance | | | |
| billing | | | |

**Relationships:**
```
patients ───< appointments >─── providers
patients ───< insurance
patients ───< billing
appointments >─── locations
```

### Part 3: Identify Integration Points

Document external integrations:

| Integration | Type | Authentication | Data Flow |
|-------------|------|----------------|-----------|
| Lab System | REST API | OAuth | Lab results → patients |
| Insurance | SOAP | API Key | Verification → appointments |
| | | | |

### Part 4: Application Flow

Map the main user flows:

**Flow 1: Patient Schedules Appointment**
```
1. Patient logs in
2. → _______________
3. → _______________
4. → _______________
5. → _______________
6. Confirmation displayed
```

**Flow 2: Provider Views Schedule**
```
1. Provider logs in
2. → _______________
3. → _______________
4. → _______________
```

### Part 5: Architecture Diagram

Create a diagram showing:

1. **Presentation Layer** (CFM files)
2. **Business Logic Layer** (CFCs, UDFs)
3. **Data Layer** (Database, queries)
4. **Integration Layer** (External APIs)
5. **Infrastructure** (Server, storage)

Use ASCII or describe:

```
┌─────────────────────────────────────────┐
│           Presentation Layer           │
│  ┌──────────┐  ┌──────────┐           │
│  │ Patients │  │ Appts    │  ...      │
│  └──────────┘  └──────────┘           │
└──────────────────┬────────────────────┘
                   │
┌──────────────────▼────────────────────┐
│         Business Logic Layer           │
│  ┌──────────┐  ┌──────────┐           │
│  │ Services │  │   UDFs  │  ...      │
│  └──────────┘  └──────────┘           │
└──────────────────┬────────────────────┘
                   │
┌──────────────────▼────────────────────┐
│              Data Layer               │
│  ┌──────────┐  ┌──────────┐           │
│  │  MSSQL   │  │  Files   │  ...      │
│  └──────────┘  └──────────┘           │
└──────────────────┬────────────────────┘
                   │
┌──────────────────▼────────────────────┐
│          Integration Layer            │
│  ┌──────────┐  ┌──────────┐           │
│  │Lab API   │  │Insurance │  ...      │
│  └──────────┘  └──────────┘           │
└─────────────────────────────────────────┘
```

### Part 6: Technology Inventory

Create an inventory:

| Component | Technology | Version | Age | Risk |
|-----------|------------|---------|-----|------|
| Application | ColdFusion | 10 | 14 yrs | High |
| Database | | | | |
| Frontend | | | | |
| Web Server | | | | |
| OS | | | | |
| Lab Integration | | | | |
| Insurance Integration | | | | |

### Part 7: Identify Architectural Problems

| Problem | Location | Impact | Recommendation |
|---------|----------|--------|----------------|
| | | | |
| | | | |
| | | | |

## Expected Outcome

1. Complete architecture diagram
2. Technology inventory
3. Integration mapping
4. Identified problems with recommendations

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Structure analysis complete | 20 |
| Database mapping accurate | 20 |
| Integration points documented | 20 |
| Diagram clear and accurate | 20 |
| Problems identified appropriately | 15 |
| Professional presentation | 5 |
| **Total** | **100** |

**Passing Score:** 70/100
