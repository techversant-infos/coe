# BlogCFC5 Technical Reference

> Detailed technical documentation for the BlogCFC5 application.

---

## Architecture Overview

BlogCFC5 follows a **two-tier architecture**:

```
┌─────────────────────────────────────────────────────────┐
│                     CLIENT LAYER                         │
│  (CFM files in /client/)                                │
│                                                          │
│  index.cfm  → Lists blog entries                         │
│  entry.cfm  → Displays single entry + comments           │
│  page.cfm   → Static pages                              │
│  search.cfm → Search functionality                      │
│  admin/     → Administration panel                      │
└────────────────────────┬────────────────────────────────┘
                         │ cfinclude / CFC calls
┌────────────────────────▼────────────────────────────────┐
│                    SERVICE LAYER                        │
│  (CFCs in /blogCFC6/org/camden/blog/)                  │
│                                                          │
│  entry.cfc   → Blog entry CRUD operations               │
│  factory.cfc → Object creation and management            │
│  user.cfc    → User authentication and management        │
│  page.cfc    → Static page management                   │
│  theme.cfc   → Theme and template handling              │
│  utils.cfc   → Helper functions (formerly UDFs)         │
└─────────────────────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│                    DATA LAYER                          │
│  (SQL Server)                                           │
│                                                          │
│  tblblog                        → Blog entries           │
│  tblblogcomments                → Comments               │
│  tblblogusers                   → Users                  │
│  tblblogcategories              → Categories             │
│  tblblogentriesincategories     → Entry-Category links   │
│  tblblogsubscriptions           → RSS subscriptions      │
│  tblblogenclosures              → File enclosures        │
│  tblblogenclosuredownloads      → Download tracking      │
└─────────────────────────────────────────────────────────┘
```

---

## Core Components

### entry.cfc

**Purpose:** Manages blog entries (posts)

**Key Methods:**

| Method | Description | Parameters |
|--------|-------------|------------|
| `getEntries()` | Retrieve blog entries | `maxRows`, `offset`, `category`, `search` |
| `getEntry()` | Get single entry by alias or ID | `alias` or `id` |
| `addEntry()` | Create new entry | `title`, `body`, `alias`, `author` |
| `updateEntry()` | Update existing entry | `id`, `title`, `body` |
| `deleteEntry()` | Remove entry | `id` |
| `entryExists()` | Check if entry exists | `alias` or `id` |

**Sample Usage:**

```cfml
<!--- Get recent entries --->
<cfset blog = createObject("component", "blogCFC6.org.camden.blog.entry").init()>
<cfset entries = blog.getEntries(maxRows=10)>

<!--- Display entries --->
<cfloop array="#entries#" index="entry">
    <h2>#entry.title#</h2>
    <p>#entry.body#</p>
    <small>Posted on #dateFormat(entry.posted, "mmm dd, yyyy")#</small>
</cfloop>
```

---

### user.cfc

**Purpose:** User authentication and management

**Key Methods:**

| Method | Description |
|--------|-------------|
| `authenticate()` | Verify username/password |
| `getUser()` | Retrieve user by username |
| `addUser()` | Create new user |
| `updateUser()` | Update user details |
| `isLoggedIn()` | Check session state |
| `logout()` | End session |

---

### utils.cfc

**Purpose:** Shared utility functions

**Formerly:** Individual UDF files (migrated to component in v5.9.x)

| Method | Description |
|--------|-------------|
| `blogRoute()` | URL routing helper |
| `isBlogUser()` | Check if current user is admin |
| `getProperty()` | Read configuration property |
| `renderContent()` | Process content (HTML, shortcodes) |

---

## Database Schema

### Core Tables

**tblblog** (Blog Entries)

| Column | Type | Description |
|--------|------|-------------|
| id | INT | Primary key |
| title | NVARCHAR(500) | Entry title |
| alias | NVARCHAR(500) | URL-friendly slug |
| body | NTEXT | Entry content |
| excerpt | NTEXT | Short summary |
| posted | DATETIME | Publish date |
| released | BIT | Is released/published |
| allowcomments | BIT | Comments enabled |
| views | INT | View counter |
| author | NVARCHAR(255) | Author username |
| created | DATETIME | Record creation |
| modified | DATETIME | Last modification |

**tblblogcomments** (Comments)

| Column | Type | Description |
|--------|------|-------------|
| id | INT | Primary key |
| entryidfk | INT | FK to tblblog |
| name | NVARCHAR(255) | Commenter name |
| email | NVARCHAR(255) | Commenter email |
| website | NVARCHAR(500) | Commenter website |
| comment | NTEXT | Comment text |
| created | DATETIME | Submission date |
| moderator | BIT | Approved by moderator |

**tblblogusers** (Users)

| Column | Type | Description |
|--------|------|-------------|
| username | NVARCHAR(255) | Login username |
| password | NVARCHAR(255) | Hashed password |
| email | NVARCHAR(255) | Email address |
| isactive | BIT | Account active |
| isadmin | BIT | Admin privileges |
| created | DATETIME | Account created |

---

## Request Flow Examples

### Homepage Request

```
1. Browser → GET /client/index.cfm
2. index.cfm → Reads blog settings (settings.xml.cfm)
3. index.cfm → Creates entry.cfc instance
4. entry.cfc → getEntries() query on tblblog
5. index.cfm → Loops through entries
6. Browser ← HTML response
```

### Comment Submission

```
1. Browser → POST /client/addcomment.cfm
   (form fields: entryidfk, name, email, website, comment)

2. addcomment.cfm → Validates input
3. addcomment.cfm → INSERT into tblblogcomments
4. addcomment.cfm → Redirect to entry page
```

---

## Configuration

### blog.ini.cfm

```cfml
<cfset blog.title = "My Blog">
<cfset blog.description = "A ColdFusion blog">
<cfset blog.siteurl = "http://localhost">
<cfset blog.dsn = "blogCFC5">
<cfset blog.username = "admin">
<cfset blog.password = "encryptedpassword">
<cfset blog.maxentriesadmin = 25>
<cfset blog.tableprefix = "tbl">
```

---

## Known Technical Characteristics

### Architecture Patterns

| Characteristic | Description |
|----------------|-------------|
| **No framework** | Plain CFM with includes |
| **No ORM** | Direct SQL queries via `<cfquery>` |
| **Session-based auth** | Session variables for login |
| **Single DSN** | All data in one database |

### Security Characteristics

| Item | Status |
|------|--------|
| SQL queries | `<cfquery>` with `cfqueryparam` |
| Password storage | MD5 hashed |
| Session management | `session.username` check |
| XSS protection | `HTMLEditFormat()` used in some places |

### Performance Characteristics

| Area | Observation |
|------|-------------|
| Query patterns | N+1 queries in list views |
| Caching | No application-level caching |
| Indexes | Indexes on primary keys and dates |
| Images | No image processing |

---

## Upgrade History

| Version | Date | Key Changes |
|---------|------|-------------|
| 5.9.2.002 | 2012 | Initial tracked version |
| 5.9.5.xxx | 2016 | Modernization pass |
| 5.9.8.001 | 2019 | Latest stable |

---

## Exercise Opportunities

| Phase | Exercise Focus | BlogCFC5 Aspect |
|-------|---------------|-----------------|
| 01 CF Expertise | Request lifecycle | index.cfm → entry.cfc → SQL |
| 02 Legacy Assessment | Code review | 6 CFCs, plain CFM, legacy patterns |
| 03 Modernization | Strategy | MD5 passwords, no ORM, framework? |
| 04 Lucee Migration | Compatibility | SQL Server, cfquery patterns |
| 05 Cloud | Deployment | Single-server, single-DSN |
| 06 AI | Use cases | Content moderation, search |
| 07 UI | Modernization | Bootstrap? jQuery? |
| 08 Performance | Optimization | N+1 queries, no caching |
| 09 Consulting | Discovery | Real app to assess |
