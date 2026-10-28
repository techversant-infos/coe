# Capstone Application: BlogCFC5

> A real ColdFusion blogging application used throughout the curriculum.

---

## Two Capstone Layers

This CoE uses two capstone layers:

| Layer | Purpose | Type |
|-------|---------|------|
| **BlogCFC5** | Technical codebase for exercises | Real open-source app |
| **Pinnacle Regional Health** | Consulting context for scenarios | Fictional healthcare org |

**BlogCFC5** is the technical codebase you work with — the actual CF code to analyze, migrate, optimize, and modernize.

**Pinnacle Regional Health** is a fictional client context used to simulate consulting constraints — healthcare regulations, multi-clinic operations, HIPAA requirements. It appears in role-play scripts and scenario exercises.

> **Note:** The Pinnacle scenario provides realistic consulting constraints. It does not exist as a codebase — use BlogCFC5 for all technical exercises.

---

## Application Overview

**Repository:** [teamcfadvance/BlogCFC5](https://github.com/teamcfadvance/BlogCFC5)

| Detail | Value |
|--------|-------|
| License | Apache 2.0 |
| Created | 2012 |
| Last Updated | 2019 |
| Language | ColdFusion (CFML) |
| Database | SQL Server |
| Stars | 30 | Forks | 20 |

---

## What This Is

BlogCFC5 is a complete ColdFusion blogging platform. It was once "The Number One Blogging Software In The ColdFusion Universe!"

Real features include:
- Blog post creation and management
- Comment system with moderation
- Category organization
- User management and authentication
- RSS/Atom feeds with podcast support
- Search functionality
- File enclosures (podcasting)
- Admin dashboard

---

## Local Setup Instructions

### Prerequisites

| Requirement | Version |
|-------------|---------|
| ColdFusion | 10+ (Adobe) or Lucee 5+ |
| SQL Server | 2012+ |
| CommandBox | (optional, for Lucee) |

### Option 1: Adobe ColdFusion

1. **Download the repository**
   ```bash
   git clone https://github.com/teamcfadvance/BlogCFC5.git
   ```

2. **Create SQL Server database**
   ```sql
   -- Create database
   CREATE DATABASE BlogCFC5;
   USE BlogCFC5;
   
   -- Run schema from /install directory
   ```

3. **Configure datasource**
   - Open ColdFusion Administrator
   - Go to Data Sources
   - Add new datasource:
     - Name: `blog`
     - Driver: SQL Server
     - Database: `BlogCFC5`
     - Server: localhost
     - Port: 1433

4. **Update configuration**
   Edit `blogCFC6/settings.xml.cfm`:
   ```cfm
   <cfset setting name="blogname" value="My Blog">
   <cfset setting name="blogurl" value="http://localhost:8500/blogcfc5/client">
   ```

5. **Deploy to ColdFusion**
   ```bash
   # Copy to ColdFusion webroot
   cp -r BlogCFC5 /path/to/coldfusion/webroot/
   ```

6. **Access the application**
   - Frontend: http://localhost:8500/BlogCFC5/client/
   - Admin: http://localhost:8500/BlogCFC5/client/admin/

### Option 2: Lucee (CommandBox)

1. **Install CommandBox**
   ```bash
   # Mac/Linux
   brew install commandbox
   
   # Windows
   # Download from https://www.ortussolutions.com/products/commandbox
   ```

2. **Download and setup**
   ```bash
   git clone https://github.com/teamcfadvance/BlogCFC5.git
   cd BlogCFC5
   ```

3. **Start server with CommandBox**
   ```bash
   box server start port=8500
   ```

4. **Create MySQL alternative (optional)**
   
   BlogCFC5 uses SQL Server by default. For MySQL, you'll need to:
   - Convert SQL scripts (field types differ)
   - Update datasource configuration
   - Modify query syntax where needed

### Troubleshooting

| Issue | Solution |
|-------|----------|
| "Datasource not found" | Verify SQL Server is running and credentials are correct |
| "Table not found" | Run the SQL scripts in `/install` directory |
| Login not working | Check `settings.xml.cfm` and ensure admin credentials match |
| Slow page loads | Enable request debugging in ColdFusion Administrator |

---

## Repository Structure

```
BlogCFC5/
├── blogCFC6/                    # Core blogging engine
│   ├── Application.cfc
│   ├── org/
│   │   └── camden/
│   │       └── blog/
│   │           ├── entry.cfc   # Blog entry operations
│   │           ├── factory.cfc # Object factory
│   │           ├── page.cfc    # Page management
│   │           ├── theme.cfc   # Theme system
│   │           ├── user.cfc    # User management
│   │           └── utils.cfc   # Utility functions
│   ├── pods/                   # Reusable UI components
│   ├── tags/                   # Custom tags
│   └── themes/
│       └── default/
│
├── client/                     # User-facing pages
│   ├── Application.cfc
│   ├── index.cfm              # Homepage / blog list
│   ├── entry.cfm              # Individual blog post
│   ├── page.cfm               # Static pages
│   ├── contact.cfm            # Contact form
│   ├── search.cfm             # Search
│   ├── admin/                  # Admin panel
│   │   ├── index.cfm
│   │   ├── entries.cfm
│   │   ├── comments.cfm
│   │   └── settings.cfm
│   ├── rss.cfm                # RSS feed
│   ├── addcomment.cfm         # Comment submission
│   ├── download.cfm           # File downloads
│   └── ...
│
├── install/                    # Setup files
│   ├── schema.sql             # Database schema
│   ├── upgrade-*.sql          # Upgrade scripts
│   └── blog.ini.cfm           # Configuration
│
├── tests/                      # Test suite
│   └── ...
│
└── README.md
```

---

## Key Components

### Core CFCs

| Component | Purpose | Key Methods |
|-----------|---------|-------------|
| `entry.cfc` | Blog entries | `getEntry()`, `saveEntry()`, `deleteEntry()` |
| `user.cfc` | User management | `authenticate()`, `getUser()`, `saveUser()` |
| `page.cfc` | Static pages | `getPage()`, `savePage()` |
| `factory.cfc` | Object creation | `getEntry()`, `getUser()` |
| `theme.cfc` | Theme handling | `render()`, `getTheme()` |
| `utils.cfc` | Utilities | Former UDFs consolidated |

### Database Tables

| Table | Purpose |
|-------|---------|
| `tblblog` | Blog entries |
| `tblblogcomments` | Comments |
| `tblblogusers` | User accounts |
| `tblblogcategories` | Categories |
| `tblblogsettings` | Configuration |

---

## Curriculum Usage

Each phase uses this application as the consulting context:

| Phase | Focus | Exercise |
|-------|-------|----------|
| 01 | CF Deep Expertise | Request lifecycle analysis |
| 02 | Legacy Assessment | Full assessment report |
| 03 | Modernization | Strategy recommendation |
| 04 | Lucee Migration | Migration plan |
| 05 | Cloud | Architecture design |
| 06 | AI Integration | Use case proposal |
| 07 | UI Modernization | Redesign concept |
| 08 | Performance | Optimization plan |
| 09 | Consulting | Client discovery |

See [exercises/](exercises/) for phase-specific exercises.

---

## For Exercises

Throughout the curriculum, you will:

1. **Read and analyze** the codebase
2. **Identify issues** in architecture, security, performance
3. **Document findings** in assessment reports
4. **Recommend solutions** with effort estimates
5. **Present recommendations** as if to a client
