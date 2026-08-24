# 🌾 AgriTrade — Development Log

> **Project:** AgriTrade — Agricultural Price Forecasting and Market Recommendation System  
> **Team Size:** 4 Members  
> **Developer:** Member 1 — Prakhar  
> **Purpose:** Master development record of the project  
> **Last Updated:** 24 August 2026

---

## 📌 Purpose of This Log

This document is the **master development log** for the AgriTrade project.

It records the actual work completed during development, including:

- Project planning
- Dataset research
- Technical setup
- Database development
- Backend development
- Machine learning development
- Optimization
- Frontend development
- Problems encountered
- Solutions implemented
- Important technical decisions

This log will be maintained continuously throughout the project.

The formal weekly report and final project documentation will be prepared from this development history.

---

# 📊 Overall Project Status

| Component | Status |
|---|---|
| Project Planning | 🟢 Completed |
| Data Source Investigation | 🟢 Completed |
| Historical Dataset Investigation | 🟡 In Progress |
| Git/GitHub Setup | 🟢 Completed |
| Project Structure | 🟢 Completed |
| PostgreSQL Setup | 🟢 Completed |
| Database Schema | 🟢 Completed |
| Seed Data | 🟢 Completed |
| Python Environment | 🟢 Completed |
| Backend Setup | 🟡 In Progress |
| Data Ingestion Pipeline | ⚪ Pending |
| Data Cleaning & EDA | ⚪ Pending |
| ML Forecasting | ⚪ Pending |
| Optimization | ⚪ Pending |
| Frontend | ⚪ Pending |
| System Integration | ⚪ Pending |
| UML/ER Diagrams | ⚪ Pending |
| MVP | ⚪ Pending |

### Status Legend

- 🟢 Completed
- 🟡 In Progress
- ⚪ Pending
- 🔴 Blocked

---

# 🗓️ Development Timeline

## Phase 1 — Project Initiation

### Objectives

The initial objective of AgriTrade was defined as developing a decision-support system that can help farmers make better selling decisions using agricultural market-price data.

### Initial Concept

The proposed system combines:

```text
Agricultural Market Data
        ↓
Historical Price Analysis
        ↓
Price Forecasting
        ↓
Market Comparison
        ↓
Transportation & Storage Cost
        ↓
Profit Calculation
        ↓
Market Recommendation
```

### Team Structure

The project team consists of four members.

Initial responsibilities were divided among:

- Data & Backend
- Machine Learning / Forecasting
- Optimization
- Frontend

Member 1 (Prakhar) is responsible for the core project setup, data investigation, database, backend foundation and integration.

---

# 📅 Development Log — Week 1

## 1. Project Planning

### Work Completed

- AgriTrade was finalized as the final-year project topic.
- The overall problem domain was studied.
- The initial MVP concept was defined.
- The major components of the system were identified.
- The four-member team structure was established.
- Initial responsibilities were divided among team members.
- The following project diagrams were identified as required documentation:
  - Use Case Diagram
  - Activity Diagram
  - ER Diagram
  - Class Diagram
  - System Architecture Diagram

### Initial System Components

```text
Data Collection
      ↓
Data Processing
      ↓
Database
      ↓
Price Forecasting
      ↓
Optimization
      ↓
Recommendation
      ↓
Frontend
```

### Outcome

The initial scope and architecture of the AgriTrade project were established.

---

# 📅 Development Log — Week 2

## 2. Government Agricultural Data Investigation

### Work Completed

Government agricultural market-price data sources were investigated.

A government open-data resource for current daily mandi prices was identified:

> **Current Daily Price of Various Commodities from Various Markets (Mandi)**

### Important Fields Identified

The dataset preview contained fields such as:

| Field | Purpose |
|---|---|
| State | State containing the market |
| District | District containing the market |
| Market | Mandi/market name |
| Commodity | Agricultural commodity |
| Variety | Commodity variety |
| Grade | Commodity grade |
| Arrival Date | Date of market arrival |
| Min Price | Minimum observed price |
| Max Price | Maximum observed price |
| Modal Price | Modal market price |

### Initial Data Observation

The dataset was identified as useful for obtaining agricultural market-price information.

However, the initial dataset was primarily a current/daily price resource and was not sufficient by itself for historical price forecasting.

---

## 3. Government API Investigation

The API interface of the government data resource was investigated.

The API parameters were examined, including:

```text
api-key
format
offset
filters[commodity]
filters[variety]
filters[grade]
```

The API documentation indicated support for formats such as:

```text
JSON
XML
CSV
```

### Problem Encountered

Authentication/API access was required for unrestricted data retrieval.

The JanParichay login/sign-in process was attempted but was not functioning successfully.

### Decision

Instead of blocking development on the API authentication issue, alternative historical downloadable resources were investigated.

---

## 4. Historical Dataset Investigation

A second resource was identified:

> **Variety-wise Daily Market Prices Data of Commodity**

This resource provided filters for:

- State
- District
- Commodity
- Arrival Date

### Test Configuration

```text
State      → Rajasthan
District   → Ajmer
Commodity  → Wheat
```

The filtered preview showed approximately:

> **3,031 records**

---

## 5. Historical Data Validation

The filtered historical dataset was inspected.

Important fields identified included:

```text
Arrival Date
Commodity
Commodity Code
District
Grade
Market
Max Price
Min Price
Modal Price
State
Variety
```

Historical dates observed in the preview included:

```text
23/11/2021
10/12/2021
13/12/2021
29/01/2024
04/03/2024
07/03/2024
11/03/2024
```

This confirmed that the resource contains historical market-price observations.

### Current Limitation

The portal requires successful authentication for downloading the complete filtered dataset.

Therefore:

```text
Historical CSV Download → ⏳ Pending
```

The historical dataset will be obtained when authentication/download access becomes available.

---

# 6. Initial Database Planning

Based on the project requirements and the identified mandi dataset, the initial relational database structure was designed.

The planned entities were:

```text
Crop
Market
Market Price
Weather Record
Transport Cost
Storage Cost
Farmer Request
Price Prediction
Recommendation
```

The database design preserves important mandi fields including:

```text
Variety
Grade
Arrival Date
Minimum Price
Maximum Price
Modal Price
```

---

# 7. Development Environment Setup

## Git and GitHub

A GitHub repository was created for AgriTrade.

The local project was initialized as a Git repository and connected to GitHub.

### Project structure created

```text
agritrade/
├── backend/
├── data/
├── ml/
├── optimization/
├── frontend/
├── database/
├── scripts/
├── tests/
└── docs/
```

### `.gitignore`

A project-specific `.gitignore` was created to prevent sensitive and generated files from being committed.

Ignored categories include:

```text
.env
.venv/
__pycache__/
node_modules/
raw datasets
processed datasets
ML model files
logs
temporary files
database dumps
```

`.gitkeep` files were added where necessary to preserve required empty directories.

---

# 8. GitHub Synchronization

During the initial GitHub push, a repository history conflict occurred because the GitHub repository already contained initial commits.

### Problem

The local and remote repositories had separate histories.

The initial push resulted in a:

```text
non-fast-forward
```

error.

### Solution

The remote history was merged into the local repository using:

```bash
git pull origin main --allow-unrelated-histories
```

A merge conflict occurred in:

```text
.gitignore
```

The conflict was resolved by retaining the project-specific local `.gitignore`.

The merge was committed and successfully pushed.

### Result

```text
Local Repository
       ↕
GitHub Repository
```

GitHub synchronization is now working correctly.

---

# 9. PostgreSQL Setup

PostgreSQL was installed on the Windows 11 development environment.

### Installed Components

- PostgreSQL 18
- pgAdmin 4

The PostgreSQL server was successfully registered in pgAdmin.

---

# 10. AgriTrade Database

A PostgreSQL database named:

```text
agritrade
```

was created.

Database structure:

```text
PostgreSQL 18
└── agritrade
```

---

# 11. Database Schema Implementation

The database schema was implemented in:

```text
database/schema.sql
```

The following nine tables were successfully created:

| # | Table |
|---|---|
| 1 | `crops` |
| 2 | `markets` |
| 3 | `market_prices` |
| 4 | `weather_records` |
| 5 | `transport_costs` |
| 6 | `storage_costs` |
| 7 | `farmer_requests` |
| 8 | `price_predictions` |
| 9 | `recommendations` |

Indexes were also added for frequently queried fields such as:

- Arrival date
- Market
- Crop
- Crop + market + date
- Weather market + date
- Prediction crop + market + date

---

# 12. Database Seed Data

Initial crop data was added using:

```text
database/seed.sql
```

Seeded crops:

```text
Wheat
Mustard
Onion
Potato
Tomato
```

The seed script was successfully executed and verified in PostgreSQL.

---

# 13. Python Environment Setup

Python was installed on the development machine.

A project-specific virtual environment was created:

```text
.venv/
```

PowerShell initially prevented activation because of its execution policy.

The issue was resolved by enabling locally created scripts for the current user.

The virtual environment was successfully activated:

```text
(.venv)
```

---

# 14. Backend Dependencies

The following Python packages were installed:

```text
FastAPI
Uvicorn
SQLAlchemy
psycopg2-binary
python-dotenv
Pydantic
```

### Purpose

| Package | Purpose |
|---|---|
| FastAPI | Backend REST API |
| Uvicorn | Application server |
| SQLAlchemy | Database ORM |
| psycopg2-binary | PostgreSQL driver |
| python-dotenv | Environment configuration |
| Pydantic | API data validation |

The installed dependencies were saved into:

```text
requirements.txt
```

---

# 15. Current Development Checkpoint

At this point the following components have been successfully established:

```text
┌──────────────────────────────────────────┐
│              AGRITRADE                   │
├──────────────────────────────────────────┤
│ Project Planning                  ✅     │
│ Data Source Investigation         ✅     │
│ Historical Data Investigation     ✅     │
│ Git/GitHub                        ✅     │
│ Project Structure                 ✅     │
│ PostgreSQL                        ✅     │
│ Database Schema                   ✅     │
│ Seed Data                         ✅     │
│ Python Environment                ✅     │
│ Backend Dependencies              ✅     │
├──────────────────────────────────────────┤
│ FastAPI Implementation             ⏳    │
│ PostgreSQL Connection              ⏳    │
│ Data Ingestion                     ⏳    │
│ ML Forecasting                     ⏳    │
│ Optimization                       ⏳    │
│ Frontend                           ⏳    │
│ Integration                        ⏳    │
└──────────────────────────────────────────┘
```

---

# 🎯 Next Development Task

The next implementation step is:

```text
Python
   ↓
FastAPI
   ↓
SQLAlchemy
   ↓
PostgreSQL
   ↓
agritrade
```

### Immediate tasks

1. Configure environment variables.
2. Create `config.py`.
3. Create `database.py`.
4. Configure SQLAlchemy.
5. Connect FastAPI to PostgreSQL.
6. Test the database connection.
7. Create the first API endpoint.

---

# 📐 Documentation To Be Maintained

The following diagrams will be developed and updated as the implementation progresses:

- [ ] Use Case Diagram
- [ ] Activity Diagram
- [ ] ER Diagram
- [ ] Class Diagram
- [ ] System Architecture Diagram

These diagrams will be synchronized with the actual implemented system rather than being created independently from the code.

---
📝 Future Log Entry Format

Every significant development session will follow this structure:

## [Date] — [Task/Feature]

### Objective

What we planned to accomplish.

### Work Completed

- ...
- ...
- ...

### Files Changed

```text
path/to/file
path/to/file
```

### Technical Decisions

- ...
- ...

### Problems Encountered

- ...

### Solution

- ...

### Result

🟢 Completed / 🟡 In Progress / 🔴 Blocked

### Next Step

- ...
