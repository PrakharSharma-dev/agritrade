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

# 16. Exploratory Data Analysis (EDA)

## Objective

After obtaining the historical Wheat mandi-price dataset, Exploratory Data Analysis was performed before beginning data cleaning, preprocessing, and database ingestion.

The purpose of EDA was to understand:

- Dataset structure and quality
- Price distribution
- Market-level price differences
- Historical price trends
- Observation frequency and data gaps
- Possible seasonal patterns
- Suitability of the dataset for time-series forecasting

The EDA was implemented as a reusable Python script:

```text
scripts/eda.py
```

Python libraries used:

```text
pandas
matplotlib
```

---

## 16.1 Market-wise Price Analysis

A market-wise comparison of average Wheat modal prices was performed.

The dataset contains seven market names:

| Market | Records |
|---|---:|
| Madanganj Kishangarh | 1,048 |
| Kekri | 683 |
| Vijaynagar | 612 |
| Gulabpura | 553 |
| Madanganj Kishangarh APMC | 180 |
| Beawar | 140 |
| Kekri APMC | 102 |

The analysis showed noticeable differences in average modal prices between markets.

### Observation

- Beawar showed the highest average modal price.
- Madanganj Kishangarh APMC was also among the higher-priced markets.
- The remaining markets had somewhat lower average modal prices.
- Market price differences indicate that market selection can influence the potential selling outcome.

### Important Decision

Average price alone will **not** be used to determine the best market.

The eventual recommendation system must also consider:

```text
Expected Selling Price
        -
Transportation Cost
        -
Storage Cost
        =
Estimated Net Profit
```

---

## 16.2 Market-wise Price Trends

A time-series plot was generated with a separate price trend for each market.

### Observations

- The markets show broadly similar long-term price movements.
- Individual markets have different levels of volatility.
- Beawar has relatively high prices but limited historical coverage.
- Madanganj Kishangarh has substantially more historical observations.
- The `APMC` market names appear during different periods and were therefore not automatically merged with similarly named markets.

### Decision

Each market will remain a separate market entity during preprocessing and forecasting.

No automatic merging of:

```text
Madanganj Kishangarh
Madanganj Kishangarh APMC
```

or:

```text
Kekri
Kekri APMC
```

will be performed without further validation of the source data.

---

## 16.3 Observation Frequency and Data Gaps

The number of Wheat price records per month was analyzed.

The analysis showed that the total number of observations changes significantly over time.

### Observation

The number of records decreases substantially after 2024.

This does not necessarily indicate a reduction in actual mandi activity. It is also influenced by changes in market coverage within the downloaded dataset.

### Market Coverage

| Market | Records | Start | End | Maximum Gap |
|---|---:|---|---|---:|
| Madanganj Kishangarh | 1,048 | Aug 2021 | Nov 2025 | 10 days |
| Kekri | 683 | Aug 2021 | Jul 2024 | 17 days |
| Vijaynagar | 612 | Aug 2021 | Jul 2024 | 39 days |
| Gulabpura | 553 | Aug 2021 | Jul 2024 | 45 days |
| Beawar | 140 | Aug 2021 | Jul 2024 | 98 days |
| Madanganj Kishangarh APMC | 180 | Nov 2025 | Aug 2026 | 36 days |
| Kekri APMC | 102 | Feb 2026 | Aug 2026 | 22 days |

### Important Finding

Madanganj Kishangarh has:

- The largest number of observations
- More than four years of historical coverage
- A median observation gap of approximately one day
- A maximum observed gap of only 10 days

Therefore, it provides the strongest initial time-series for the MVP forecasting model.

---

## 16.4 Price Distribution Analysis

A histogram of `Modal_Price` was generated.

### Observation

Most modal-price observations are concentrated approximately between:

```text
₹1,900 – ₹2,600
```

The distribution also contains a right-side tail extending to approximately:

```text
₹3,900
```

### Interpretation

The dataset contains substantial price variation and a small number of high-price observations.

These high values will **not** be automatically removed as outliers. They must first be investigated to determine whether they represent legitimate market observations.

---

## 16.5 Overall Price Trend

A time-series scatter plot of Wheat modal prices was generated.

### Observations

The overall dataset shows:

- An upward movement from 2021 into later years
- Significant short-term fluctuations
- A strong price increase around late 2024 and early 2025
- A decline following the early-2025 peak
- Relative stabilization around the ₹2,200–₹2,500 range during much of 2026

### Interpretation

The historical series contains both:

```text
Trend
+
Short-term fluctuations
```

This indicates that time-series forecasting is a reasonable direction for the project.

---

## 16.6 Monthly Price Analysis

Average Wheat modal price was calculated for each month of the year.

The analysis showed visible month-to-month variation.

Approximate pattern observed:

```text
January     → Higher average
February    → Lower
March       → Lower
April       → Higher
May         → Higher
June        → Moderate
July        → Moderate
August      → Moderate
September   → Lowest average
October     → Recovery
November    → Higher
December    → Higher
```

### Important Limitation

This calculation combines multiple markets with different historical coverage.

Therefore, the observed monthly variation **cannot yet be treated as confirmed seasonal behavior**.

A market-specific seasonality analysis will be performed for the selected forecasting market.

---

## 16.7 Rolling Average Analysis

A 30-day rolling average was calculated for:

```text
Market: Madanganj Kishangarh
Commodity: Wheat
Target: Modal Price
```

### Observation

The rolling average reduced daily noise and made the underlying price movement easier to observe.

The broad pattern was:

```text
2021
  ↓
Gradual increase
  ↓
2022
  ↓
Relatively stable / rising
  ↓
2023
  ↓
Increase followed by correction
  ↓
2024
  ↓
Gradual increase
  ↓
Early 2025
  ↓
Strong peak
  ↓
2025
  ↓
Correction
  ↓
2026
  ↓
Relative stabilization / recovery
```

### Interpretation

The rolling-average analysis supports the presence of meaningful temporal structure in the data and strengthens the case for investigating forecasting models.

---

## 16.8 Duplicate Observation Investigation

Earlier data-quality analysis found:

- **0 exact duplicate rows**
- **6 duplicate date/market/commodity/variety/grade groups**
- These groups correspond to **12 rows**

The duplicate groups contain different price values.

Example structure:

```text
Date + Market + Commodity + Variety + Grade
                ↓
        Multiple price observations
```

### Decision

These records will **not be deleted automatically**.

They may represent legitimate multiple observations from the source.

For the forecasting dataset, we eventually need to determine an appropriate method for obtaining one daily target value per market.

The aggregation strategy will be decided during preprocessing after further source validation.

---

# 17. EDA Conclusions

The EDA established the following important conclusions:

### 1. Dataset quality

The raw dataset passed the initial structural quality checks:

```text
Missing values       → 0
Exact duplicates     → 0
Invalid dates        → 0
Negative prices      → 0
Zero prices         → 0
Invalid price order  → 0
```

### 2. Market selection

For the initial MVP forecasting model:

> **Wheat at Madanganj Kishangarh** is selected as the primary forecasting series.

### Reason

It provides the strongest combination of:

- Number of observations
- Historical coverage
- Temporal consistency
- Relatively small observation gaps

### 3. Market separation

Markets will remain separate during preprocessing.

APMC and non-APMC market names will not be merged without source validation.

### 4. Forecasting suitability

The data contains:

- Long-term trend
- Short-term fluctuations
- Market-specific behavior
- Possible seasonal effects

Therefore, the dataset is suitable for further time-series forecasting investigation.

### 5. Data preprocessing is required

Before ML training, the following steps are required:

```text
Raw CSV
   ↓
Date parsing
   ↓
Price validation
   ↓
Market validation
   ↓
Duplicate-day investigation
   ↓
Missing-date analysis
   ↓
Daily target preparation
   ↓
Feature engineering
   ↓
Forecasting dataset
```

---

# 18. Files Created / Updated During EDA

```text
scripts/
└── eda.py

data/
└── raw/
    └── wheat_daily_prices.csv
```

The raw CSV remains **unchanged** and must not be manually edited.

The EDA script is reusable and can later be adapted for additional commodities or markets.

---

# 19. Current Development Checkpoint — After EDA

```text
┌──────────────────────────────────────────┐
│              AGRITRADE                   │
├──────────────────────────────────────────┤
│ Project Planning                  ✅     │
│ Data Source Investigation         ✅     │
│ Historical Dataset Download       ✅     │
│ Initial Data Quality Analysis     ✅     │
│ Exploratory Data Analysis         ✅     │
│ Git/GitHub                        ✅     │
│ Project Structure                 ✅     │
│ PostgreSQL                        ✅     │
│ Database Schema                   ✅     │
│ Seed Data                         ✅     │
│ Python Environment                ✅     │
│ EDA Script                        ✅     │
├──────────────────────────────────────────┤
│ Data Preprocessing                 ⏳    │
│ PostgreSQL Data Ingestion          ⏳    │
│ FastAPI Implementation             ⏳    │
│ PostgreSQL Connection              ⏳    │
│ ML Forecasting                     ⏳    │
│ Optimization                       ⏳    │
│ Frontend                           ⏳    │
│ Integration                        ⏳    │
│ Final Diagrams                     ⏳    │
│ MVP                                ⏳    │
└──────────────────────────────────────────┘
```

---

# 🎯 Next Development Task

The next technical phase is **Data Preprocessing**.

Planned steps:

1. Validate market names.
2. Investigate multiple observations on the same date.
3. Determine the daily target-price aggregation rule.
4. Analyze missing dates for Madanganj Kishangarh.
5. Create the cleaned dataset.
6. Save the processed dataset separately from the raw CSV.
7. Prepare the cleaned data for PostgreSQL ingestion.

> **Important:** The original file in `data/raw/` will remain untouched.

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

## Week 3 — Data Preprocessing & PostgreSQL Integration

**Date:** 27 August 2026  
**Member:** Prakhar Sharma (Member 1)  
**Phase:** Backend/Data Pipeline Development

---

## 1. Preprocessing Pipeline

After completing the initial Exploratory Data Analysis (EDA), the raw mandi dataset was processed to prepare it for forecasting and database integration.

### Dataset Used

- Commodity: **Wheat**
- Market: **Madanganj Kishangarh**
- District: **Ajmer**
- State: **Rajasthan**

### Raw Dataset

- Total raw records: **3,318**
- Records for Madanganj Kishangarh: **1,048**

### Preprocessing Operations

The preprocessing script was created at:

```text
scripts/preprocess.py
```

The following operations were performed:

1. Converted `Arrival_Date` into a proper date format.
2. Filtered the dataset for the selected market.
3. Validated required columns.
4. Removed records with invalid or missing dates.
5. Removed records with missing price values.
6. Validated minimum, maximum and modal prices.
7. Identified multiple observations occurring on the same date.
8. Aggregated multiple observations for the same date.
9. Sorted the resulting dataset chronologically.
10. Performed final validation.
11. Saved the cleaned dataset separately from the raw dataset.

### Duplicate-Date Handling

Five dates contained multiple observations.

Since the forecasting dataset requires one observation per date, multiple observations were aggregated.

The modal price was calculated using the arithmetic mean.

The raw dataset was kept unchanged.

### Missing-Date Handling

The dataset does not contain observations for every calendar day.

Most gaps were short and were treated as part of the market reporting pattern.

Artificial prices were **not** created for missing dates.

No forward-filling was performed.

### Final Processed Dataset

```text
Records:          1,043
Unique dates:     1,043
Missing values:       0
Duplicate dates:      0

Start date:       2021-08-18
End date:         2025-11-04
```

The processed dataset was saved as:

```text
data/processed/wheat_madanganj_kishangarh.csv
```

---

## 2. PostgreSQL Database Integration

The processed dataset was integrated with the project's PostgreSQL database.

```text
Database: agritrade
Host: localhost
Port: 5432
```

The PostgreSQL database contains the following major tables:

```text
crops
farmer_requests
market_prices
markets
price_predictions
recommendations
storage_costs
transport_costs
weather_records
```

### Crop and Market Setup

The existing `crops` table contained:

```text
crop_id:   1
crop_name: Wheat
```

The following market was added to the `markets` table:

```text
market_name: Madanganj Kishangarh
district:    Ajmer
state:       Rajasthan
```

The corresponding `market_id` was obtained from PostgreSQL and used for price-data insertion.

---

## 3. Data Loading Script

A reusable PostgreSQL ingestion script was created:

```text
scripts/load_data.py
```

The script performs the following operations:

1. Loads the processed CSV.
2. Converts arrival dates into database-compatible dates.
3. Connects to PostgreSQL.
4. Retrieves the appropriate `crop_id`.
5. Retrieves the appropriate `market_id`.
6. Inserts market-price records into `market_prices`.
7. Uses a database transaction.
8. Rolls back the transaction if an error occurs.
9. Reports inserted and skipped records.

---

## 4. Initial Database Import

The first successful import inserted:

```text
1,043 records
```

The database was then verified using SQL queries.

### Verification Results

```text
Total records: 1,043

First date:    2021-08-18
Last date:     2025-11-04
```

The inserted records were also verified through joins between:

```text
market_prices
crops
markets
```

The records correctly corresponded to:

```text
Commodity: Wheat
Market:    Madanganj Kishangarh
District:  Ajmer
State:     Rajasthan
```

---

## 5. Database-Level Duplicate Protection

A unique constraint was added to the `market_prices` table:

```sql
UNIQUE (
    market_id,
    crop_id,
    variety,
    grade,
    arrival_date
)
```

Constraint name:

```text
market_prices_unique_observation
```

This ensures that the same market, crop, variety and grade cannot have multiple price observations for the same arrival date.

The ingestion script was updated with:

```sql
ON CONFLICT (
    market_id,
    crop_id,
    variety,
    grade,
    arrival_date
)
DO NOTHING
```

The loader was then tested again.

### Re-import Test

```text
Records inserted: 0
Records skipped:  1043
```

This confirmed that the loader is safely re-runnable and does not create duplicate records.

---

## 6. Database Credential Security

Database credentials were moved from the Python source code into:

```text
.env
```

The Python package:

```text
python-dotenv
```

was installed to load the environment variables.

The `.env` file contains the database configuration locally and is excluded from GitHub.

A connection test confirmed:

```text
PostgreSQL connection successful
```

The actual database password is not stored in the source code.

---

## 7. Git and GitHub Security Verification

The project's `.gitignore` was checked and verified.

The following are ignored:

```text
.env
.venv/
data/
ml/models/
```

Therefore:

- Database credentials are not pushed.
- Raw datasets are not pushed.
- Processed datasets are not pushed.
- Python virtual-environment files are not pushed.
- Local ML model files are not pushed.

The `.gitignore` itself is tracked by Git.

---

## 8. GitHub Checkpoint

The following development files were committed and pushed to GitHub:

```text
database/schema.sql
requirements.txt
scripts/preprocess.py
scripts/load_data.py
```

Commit message:

```text
Add data preprocessing and PostgreSQL ingestion
```

The repository is synchronized with the local development environment.

---

## 9. Current System State

The data pipeline is now functional:

```text
Government Mandi Dataset
        ↓
Raw CSV
        ↓
EDA
        ↓
Preprocessing
        ↓
Clean Processed CSV
        ↓
Python Data Loader
        ↓
PostgreSQL
        ↓
market_prices
        ↓
1,043 verified records
```

---

## 10. Current Checkpoint

### Completed

- [x] Government mandi dataset obtained
- [x] EDA completed
- [x] Market selected for initial forecasting
- [x] Preprocessing script created
- [x] Processed dataset generated
- [x] PostgreSQL database configured
- [x] Crop and market records configured
- [x] 1,043 price records imported
- [x] Database records verified
- [x] Unique constraint added
- [x] Duplicate-safe ingestion implemented
- [x] `.env` credential management implemented
- [x] `.gitignore` verified
- [x] Changes committed and pushed to GitHub

---

## 11. Next Development Task

The next major development phase is the **FastAPI backend**.

Planned sequence:

PostgreSQL Database
        ↓
FastAPI Backend
        ↓
Database connection layer
        ↓
API routes
        ↓
Market-price endpoints
        ↓
Forecast endpoints
        ↓
Recommendation endpoints
        ↓
Frontend integration
```

Initial API endpoints will focus on retrieving:

- Available crops
- Available markets
- Historical market prices
- Latest market prices

Forecasting and farmer recommendations will be integrated after the basic API layer is operational.

---

## Checkpoint Status

**🟢 DATA PIPELINE COMPLETE**

**Next Phase: 🚀 FASTAPI BACKEND**
### 1. FastAPI Backend Foundation

After completing PostgreSQL integration and data validation, development was continued on the FastAPI backend.

A reusable SQLAlchemy database connection layer was implemented in:

```text
backend/app/database.py
```

The connection uses environment variables loaded from `.env`.

Database connection test:

```text
PostgreSQL connection successful
```

### 2. SQLAlchemy Models

Models were created to represent the existing PostgreSQL tables:

```text
backend/app/models/
├── crop.py
├── market.py
└── market_price.py
```

### 3. FastAPI Routers

API routers were created:

```text
backend/app/routers/
├── crops.py
├── markets.py
└── prices.py
```

Implemented endpoints:

| Endpoint | Purpose | Status |
|---|---|---|
| `GET /api/crops/` | Retrieve available crops | ✅ |
| `GET /api/markets/` | Retrieve available markets | ✅ |
| `GET /api/prices/` | Retrieve historical market prices | ✅ |

The endpoints were verified through FastAPI Swagger UI:

```text
http://127.0.0.1:8000/docs
```

### 4. Historical Prices API

The prices endpoint supports filtering by:

```text
crop_id
market_id
start_date
end_date
```

Example:

```text
/api/prices/?crop_id=1&market_id=1
```

Date filtering:

```text
/api/prices/?crop_id=1&market_id=1&start_date=2024-01-01&end_date=2024-12-31
```

A successful `200` response was verified with actual PostgreSQL market-price records.

Example verified record:

```text
price_id:      2
market_id:     1
crop_id:       1
arrival_date:  2021-08-19
min_price:     1740
max_price:     1981
modal_price:   1861
variety:       Other
grade:         FAQ
price_unit:    ₹/quintal
```

### 5. Pydantic Response Schemas

Response schemas were added:

```text
backend/app/schemas/
├── crop.py
├── market.py
└── market_price.py
```

Response models:

```text
CropResponse
MarketResponse
MarketPriceResponse
```

These provide structured API responses and automatic Swagger documentation.

### 6. Backend Architecture

```text
PostgreSQL
    ↓
SQLAlchemy Models
    ↓
FastAPI Routers
    ↓
Pydantic Response Schemas
    ↓
JSON API Response
    ↓
Frontend
```

## Current Checkpoint

### Completed

- [x] PostgreSQL connection through SQLAlchemy
- [x] SQLAlchemy models for crops, markets and market prices
- [x] Crops API
- [x] Markets API
- [x] Historical prices API
- [x] Crop filtering
- [x] Market filtering
- [x] Date-range filtering
- [x] Pydantic response schemas
- [x] Swagger API documentation
- [x] Successful API response verification

**🟢 FASTAPI + POSTGRESQL API FOUNDATION COMPLETE**

## Next Development Task

The next backend improvement is **pagination for the prices endpoint**.

Planned request:

```text
/api/prices/?skip=0&limit=50
```

This will prevent the frontend from loading all 1,043 historical records in a single request.

Planned sequence:

```text
Pagination
    ↓
API validation
    ↓
Forecasting service
    ↓
Prediction endpoint
    ↓
Recommendation logic
    ↓
Frontend integration


### 1. Backend/Data Layer Completion

The core backend and database-access layer for the AgriTrade MVP has been implemented and verified.

Completed components:

- [x] PostgreSQL database configured
- [x] Historical mandi dataset processed
- [x] Processed data loaded into PostgreSQL
- [x] Duplicate protection implemented
- [x] Database credentials secured using `.env`
- [x] `.gitignore` verified
- [x] SQLAlchemy database connection implemented
- [x] SQLAlchemy models implemented
- [x] Pydantic response schemas implemented
- [x] FastAPI application configured
- [x] Swagger documentation verified

---

## 2. Implemented API Endpoints

| Endpoint | Purpose | Status |
|---|---|---|
| `GET /api/crops/` | Retrieve available crops | ✅ |
| `GET /api/markets/` | Retrieve available markets | ✅ |
| `GET /api/prices/` | Retrieve historical market prices | ✅ |

The APIs were tested using FastAPI Swagger UI.

---

## 3. Prices API Features

The historical prices endpoint supports:

### Crop Filtering

```text
/api/prices/?crop_id=1
```

### Market Filtering

```text
/api/prices/?market_id=1
```

### Date-Range Filtering

```text
/api/prices/?start_date=2024-01-01&end_date=2024-12-31
```

### Pagination

```text
/api/prices/?skip=0&limit=10
```

Pagination was tested successfully, including pagination combined with crop, market and date filters.

The endpoint supports:

```text
crop_id        ✅
market_id      ✅
start_date     ✅
end_date       ✅
skip           ✅
limit          ✅
response model ✅
```

---

## 4. Current Backend Architecture

```text
PostgreSQL
     ↓
SQLAlchemy
     ↓
FastAPI Routers
     ↓
Pydantic Response Schemas
     ↓
JSON API
     ↓
Frontend
```

The backend provides the frontend with access to crop, market and historical price data.

---

## 5. ML Development Handoff

With the core backend/data-access layer completed, the next development phase is the **Machine Learning / Forecasting module**.

Planned ML workflow:

```text
Historical price data
        ↓
Feature preparation
        ↓
Feature engineering
        ↓
Time-aware train/validation/test split
        ↓
Baseline model
        ↓
Model experiments
        ↓
Model evaluation
        ↓
Best-performing model
        ↓
Saved model artifact
        ↓
FastAPI forecast integration
```

### ML Responsibilities

The ML development work will focus on:

- Preparing forecasting features.
- Creating a time-aware training and validation strategy.
- Establishing a baseline forecast.
- Training candidate forecasting models.
- Comparing model performance.
- Evaluating predictions using appropriate metrics.
- Selecting the best-performing model.
- Saving the trained model for backend integration.

### Important Development Principle

The forecasting workflow should use chronologically ordered data so that future observations do not influence training on earlier observations.

---

## 6. Backend–ML Integration Plan

After the ML member completes and validates the forecasting model, it will be integrated with the existing FastAPI backend.

```text
Historical PostgreSQL Data
          ↓
     ML Forecasting
          ↓
    Saved Model
          ↓
   Forecast Service
          ↓
FastAPI /api/forecast/
          ↓
      Frontend
```

The backend will expose predictions through an API, while the ML component will handle feature engineering, model training and evaluation.

---

## 7. Current Project Checkpoint

### Completed

```text
Data acquisition             ✅
EDA                          ✅
Preprocessing                ✅
PostgreSQL ingestion         ✅
Database verification        ✅
Credential security          ✅
Duplicate protection         ✅
SQLAlchemy                   ✅
FastAPI foundation           ✅
API routes                   ✅
Pydantic schemas             ✅
Filtering                    ✅
Pagination                   ✅
Swagger verification         ✅
```

### Current Status

**🟢 CORE BACKEND + DATA ACCESS LAYER COMPLETE**

### Next Phase

**🤖 MACHINE LEARNING / PRICE FORECASTING**

The next implementation task is to prepare the historical price data for time-series forecasting and establish a baseline model.
```

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
