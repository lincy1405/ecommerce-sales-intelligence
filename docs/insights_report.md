# Insights & Recommendations Report
## E-Commerce Sales Intelligence Project

**Prepared By:** Lincy DCosta  
**Date:** May 2026

---

## Executive Summary
Analysis of 1,041,670 transactions from a UK online retail business (2009–2011) revealed significant opportunities in international expansion, customer retention, and promotional timing. Five key insights with actionable recommendations are outlined below.

---

## Insight 1: Netherlands Has the Highest Quality Customers
**Finding:** Despite being 2nd in total revenue (£554K), Netherlands has the highest Average Order Value at £2,430 — nearly 5x higher than Germany (£546) and France (£573).

**Recommendation:** Prioritize Netherlands for premium product launches and loyalty programs. Assign a dedicated account manager for Dutch B2B clients. Explore why AOV is so high — likely wholesale buyers — and replicate that model in other European markets.

---

## Insight 2: 29.6% of Customers Are Champions — But 18.6% Are At Risk
**Finding:** RFM segmentation shows 1,738 Champions (high recency, frequency, and spend) but 1,155 customers are At Risk of churning.

**Recommendation:** Launch a win-back email campaign targeting At Risk customers with personalized offers based on their past purchases. For Champions, introduce a VIP loyalty tier with early access to new products. Retaining existing customers costs 5x less than acquiring new ones.

---

## Insight 3: Revenue Peaks in November — Promotions Are Mistimed
**Finding:** Revenue spikes sharply in October–November every year (Christmas procurement cycle) and drops 30–40% in January–February.

**Recommendation:** Front-load inventory and marketing spend in September–October to capture early Christmas buyers. Run clearance promotions in January to offset the post-holiday slump. Avoid major product launches in February — lowest traffic month.

---

## Insight 4: Thursday Is the Best Day to Run Promotions
**Finding:** Thursday generates the highest revenue of any weekday. Sunday is the lowest by a significant margin.

**Recommendation:** Schedule email campaigns, flash sales, and new product announcements on Thursdays. Avoid Sunday promotions. Peak shopping hours are 10am–3pm — all digital marketing should be timed within this window.

---

## Insight 5: PAPER CRAFT LITTLE BIRDIE Is a Data Anomaly Worth Investigating
**Finding:** This product shows 80,995 units sold but only 1 invoice — meaning one single bulk order accounts for all its revenue (£168K). This distorts product ranking analysis.

**Recommendation:** Flag wholesale/bulk orders (quantity > 1000 in single invoice) as a separate segment in future analysis. Create a B2B vs B2C split in reporting to avoid retail insights being skewed by wholesale transactions. Investigate if this customer is a reseller and build a dedicated B2B pricing strategy.

---

## Summary Table
| # | Insight | Recommended Action | Priority |
|---|---------|-------------------|----------|
| 1 | Netherlands highest AOV | Premium expansion strategy | High |
| 2 | 1,155 At Risk customers | Win-back campaign | High |
| 3 | Nov revenue spike | Retime promotions to Oct | Medium |
| 4 | Thursday peak day | Schedule campaigns on Thu 10am–3pm | Medium |
| 5 | Bulk order anomaly | B2B vs B2C segmentation | Low |

---

*Analysis conducted using Python (Pandas, Matplotlib, Seaborn), SQL (SQLite), and Streamlit.*  
*Dataset: UCI Online Retail II — 1M+ transactions, 2009–2011.*