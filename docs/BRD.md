# Business Requirements Document (BRD)
## E-Commerce Sales Intelligence Project

**Document Version:** 1.0  
**Prepared By:** Lincy DCosta  
**Date:** May 2026  
**Status:** Final

---

## 1. Project Overview
This project analyzes 1M+ transactions from a UK-based online retail business (2009–2011) to uncover revenue patterns, customer behavior, and product performance. The goal is to enable data-driven decision-making across sales, marketing, and operations teams.

---

## 2. Business Objectives
- Identify top-performing countries, products, and customer segments
- Understand seasonal revenue trends to optimize promotions
- Segment customers using RFM analysis for targeted marketing
- Provide an interactive dashboard for real-time business monitoring

---

## 3. Stakeholders
| Stakeholder | Role | Interest |
|-------------|------|----------|
| Sales Manager | Primary User | Revenue trends, top products |
| Marketing Team | Primary User | Customer segmentation, retention |
| Operations Team | Secondary User | Order volumes, peak periods |
| Finance Team | Secondary User | Revenue KPIs, AOV tracking |

---

## 4. Scope
**In Scope:**
- Data cleaning and preparation of raw transactional data
- SQL-based business queries for KPI extraction
- Python-based exploratory data analysis (EDA)
- RFM customer segmentation
- Interactive Streamlit dashboard

**Out of Scope:**
- Real-time data integration
- Predictive modeling or forecasting
- CRM system integration

---

## 5. Functional Requirements
| ID | Requirement |
|----|-------------|
| FR1 | System shall display total revenue, orders, customers, and AOV as KPIs |
| FR2 | System shall show monthly revenue trend over the full date range |
| FR3 | System shall rank top 10 countries by revenue excluding UK |
| FR4 | System shall identify top 10 products by revenue |
| FR5 | System shall segment customers into Champions, Loyal, Potential, At Risk, Lost |
| FR6 | System shall allow filtering by country and year |

---

## 6. Non-Functional Requirements
| ID | Requirement |
|----|-------------|
| NFR1 | Dashboard shall load within 10 seconds |
| NFR2 | All visualizations shall be interactive and filterable |
| NFR3 | Data shall be reproducible from raw source |
| NFR4 | Code shall be documented and version controlled on GitHub |

---

## 7. Data Requirements
| Field | Type | Description |
|-------|------|-------------|
| Invoice | String | Unique transaction ID |
| StockCode | String | Product code |
| Description | String | Product name |
| Quantity | Integer | Units purchased |
| InvoiceDate | DateTime | Transaction timestamp |
| Price | Float | Unit price in GBP |
| Customer ID | Float | Unique customer identifier |
| Country | String | Customer's country |

---

## 8. Assumptions & Constraints
- Data covers UK retail transactions only (2009–2011)
- Cancelled orders (Invoice starting with 'C') are excluded from analysis
- Guest orders (null Customer ID) are flagged but retained for revenue analysis
- Analysis is retrospective; no live data feed is included