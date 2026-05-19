import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ── PAGE CONFIG ──────────────────────────────────────────────
st.set_page_config(
    page_title="E-Commerce Sales Intelligence",
    page_icon="🛒",
    layout="wide"
)

# ── LOAD DATA ────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv(r'C:\Users\Lincy\OneDrive\Desktop\ecommerce-sales-intelligence\data\cleaned\online_retail_clean.csv')
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['YearMonth'] = df['InvoiceDate'].dt.strftime('%Y-%m')
    df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
    df['Hour'] = df['InvoiceDate'].dt.hour
    return df

df = load_data()

# ── SIDEBAR FILTERS ──────────────────────────────────────────
st.sidebar.image("https://img.icons8.com/color/96/shopping-cart.png", width=80)
st.sidebar.title("Filters")

countries = ['All'] + sorted(df['Country'].unique().tolist())
selected_country = st.sidebar.selectbox("Select Country", countries)

years = ['All'] + sorted(df['InvoiceDate'].dt.year.unique().tolist())
selected_year = st.sidebar.selectbox("Select Year", years)

# Apply filters
filtered = df.copy()
if selected_country != 'All':
    filtered = filtered[filtered['Country'] == selected_country]
if selected_year != 'All':
    filtered = filtered[filtered['InvoiceDate'].dt.year == int(selected_year)]

# ── HEADER ───────────────────────────────────────────────────
st.title("🛒 E-Commerce Sales Intelligence Dashboard")
st.markdown("**UK Online Retail Dataset (2009–2011) · 1M+ transactions**")
st.markdown("---")

# ── KPI CARDS ────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Revenue", f"£{filtered['Revenue'].sum():,.0f}")
col2.metric("📦 Total Orders", f"{filtered['Invoice'].nunique():,}")
col3.metric("👥 Unique Customers", f"{filtered['Customer ID'].nunique():,}")
col4.metric("🧾 Avg Order Value", f"£{filtered['Revenue'].sum() / filtered['Invoice'].nunique():,.2f}")

st.markdown("---")

# ── ROW 1: MONTHLY TREND + TOP COUNTRIES ─────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Monthly Revenue Trend")
    monthly = filtered.groupby('YearMonth')['Revenue'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(monthly['YearMonth'], monthly['Revenue'], marker='o', color='#2196F3', linewidth=2)
    ax.fill_between(monthly['YearMonth'], monthly['Revenue'], alpha=0.1, color='#2196F3')
    ax.set_xticklabels(monthly['YearMonth'], rotation=45, ha='right', fontsize=7)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'£{x:,.0f}'))
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.subheader("🌍 Top 10 Countries by Revenue")
    top_countries = filtered[filtered['Country'] != 'United Kingdom'].groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=top_countries.values, y=top_countries.index, palette='Blues_r', ax=ax)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'£{x:,.0f}'))
    plt.tight_layout()
    st.pyplot(fig)

# ── ROW 2: TOP PRODUCTS + DAY OF WEEK ────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top 10 Products by Revenue")
    top_products = filtered.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=top_products.values, y=top_products.index, palette='Greens_r', ax=ax)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'£{x:,.0f}'))
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.subheader("📅 Revenue by Day of Week")
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Sunday']
    day_revenue = filtered.groupby('DayOfWeek')['Revenue'].sum().reindex(day_order)
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=day_revenue.index, y=day_revenue.values, palette='Oranges_r', ax=ax)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'£{x:,.0f}'))
    plt.tight_layout()
    st.pyplot(fig)

# ── ROW 3: RFM SEGMENTATION ───────────────────────────────────
st.markdown("---")
st.subheader("👥 Customer Segmentation (RFM Analysis)")

snapshot_date = df['InvoiceDate'].max()
rfm = filtered[filtered['Customer ID'].notna()].groupby('Customer ID').agg(
    Recency=('InvoiceDate', lambda x: (snapshot_date - x.max()).days),
    Frequency=('Invoice', 'nunique'),
    Monetary=('Revenue', 'sum')
).reset_index()

rfm['R_Score'] = pd.qcut(rfm['Recency'], 4, labels=[4, 3, 2, 1], duplicates='drop')
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 4, labels=[1, 2, 3, 4], duplicates='drop')

def segment(row):
    score = int(row['R_Score']) + int(row['F_Score']) + int(row['M_Score'])
    if score >= 10: return 'Champions'
    elif score >= 8: return 'Loyal Customers'
    elif score >= 6: return 'Potential Loyalists'
    elif score >= 4: return 'At Risk'
    else: return 'Lost'

rfm['Segment'] = rfm.apply(segment, axis=1)
segment_counts = rfm['Segment'].value_counts()

col1, col2 = st.columns(2)
with col1:
    colors = ['#2196F3', '#4CAF50', '#FF9800', '#F44336', '#9E9E9E']
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(segment_counts.values, labels=segment_counts.index, colors=colors,
           autopct='%1.1f%%', startangle=140)
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.dataframe(rfm[['Customer ID', 'Recency', 'Frequency', 'Monetary', 'Segment']].sort_values('Monetary', ascending=False).head(20).reset_index(drop=True))

st.markdown("---")
st.caption("Built by Lincy DCosta · BE AI & Data Science · Fr. CRCE Mumbai")