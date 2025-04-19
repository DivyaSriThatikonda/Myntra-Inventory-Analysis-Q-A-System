import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import pyodbc
from app_direct_db import generate_sql_query, get_db_connection
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(page_title="Myntra Inventory Analysis", layout="wide")

# Custom CSS for white background and black text with Myntra branding
st.markdown("""
    <style>
    /* Single white background for app and sidebar */
    .stApp, [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    /* Plotly chart backgrounds */
    .js-plotly-plot, .plotly, .plot-container, .plotly-graph-div {
        background-color: #FFFFFF !important;
    }
    /* Button styling */
    .stButton>button {
        background-color: #FF4040; /* Rich coral */
        color: #FFFFFF;
        border-radius: 10px;
        border: none;
        padding: 12px 24px;
        font-weight: bold;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #E63939; /* Darker coral */
    }
    /* Text input styling */
    .stTextInput>div>input {
        border-radius: 5px;
        border: 2px solid #FF4040;
        font-size: 18px;
        padding: 10px;
        color: #000000;
        background-color: #F0F0F0; /* Light gray for contrast */
        text-align: center;
    }
    /* Selectbox styling */
    .stSelectbox>div {
        border-radius: 5px;
        border: 1px solid #FF4040;
        font-size: 16px;
        color: #000000;
        background-color: #F0F0F0;
    }
    /* Container styling */
    .st-container {
        background-color: #FFFFFF !important;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: #000000;
    }
    /* Text styling */
    h1, h2, h3, .stMarkdown, .stTable, [data-testid="stTable"], .query-history, .inventory-heading {
        color: #000000 !important;
        font-weight: bold;
    }
    /* Enhanced title with prominent Myntra logo */
    .css-1d391kg { /* Target main title */
        font-size: 40px !important;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px 0;
    }
    .css-1d391kg:before {
        content: url('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Myntra_Logo.svg/1200px-Myntra_Logo.svg.png');
        width: 50px;
        height: 50px;
        margin-right: 10px;
    }
    .css-1d391kg:after {
        content: url('https://img.icons8.com/ios-filled/50/000000/t-shirt.png') url('https://img.icons8.com/ios-filled/50/000000/pants.png');
        width: 100px;
        height: 50px;
        margin-left: 10px;
    }
    /* Inventory heading */
    .inventory-heading {
        font-size: 28px !important;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .inventory-heading:before {
        content: url('https://img.icons8.com/ios-filled/30/000000/t-shirt.png');
    }
    .inventory-heading:after {
        content: url('https://img.icons8.com/ios-filled/30/000000/pants.png');
    }
    /* Query history without red background */
    .query-history {
        font-size: 14px;
        margin-top: 5px;
        padding: 5px;
        border-radius: 5px;
        color: #000000;
        background-color: transparent; /* Removed red background */
    }
    /* Table styling */
    [data-testid="stTable"] td {
        background-color: #F0F0F0; /* Light gray table cells */
        color: #000000 !important;
        font-weight: bold;
    }
    /* SQL code block with box */
    pre {
        background-color: transparent !important; /* Removed red background */
        color: #000000 !important;
        font-size: 14px !important;
        padding: 10px;
        border: 2px solid #000000; /* Added box */
        border-radius: 10px; /* Rounded corners */
    }
    </style>
""", unsafe_allow_html=True)

# Custom Plotly theme for white background
custom_template = {
    "layout": {
        "paper_bgcolor": "#FFFFFF",  # White
        "plot_bgcolor": "#FFFFFF",   # White
        "font": {"color": "#000000"},  # Black text
    }
}
px.defaults.template = custom_template

# Title
st.title("Myntra Inventory Analysis Chatbot")

# Initialize session state
if 'query_history' not in st.session_state:
    st.session_state.query_history = []
if 'alerts_run' not in st.session_state:
    st.session_state.alerts_run = False

# Database connection
@st.cache_resource
def init_connection():
    return get_db_connection()

# Cache query results
@st.cache_data(ttl=300)  # Cache for 5 minutes
def run_query(query, _conn, _cache_key, user_query):
    try:
        df = pd.read_sql(query, _conn)
        # Check for revenue-related queries
        is_revenue = ('revenue' in user_query.lower() or
                      'revenue' in query.lower() or
                      any('revenue' in col.lower() or 'RevenueInRs' in col for col in df.columns))
        if df.shape == (1, 1) and is_revenue:
            value = df.iloc[0, 0]
            # Convert to rupees if in crores
            if 'Revenue_in_Crores' in df.columns or 'crores' in query.lower():
                value *= 10000000
            return pd.DataFrame({'Revenue': [value]})
        return df
    except Exception as e:
        st.error(f"Query Error: {str(e)}")
        return pd.DataFrame()

# Sidebar for natural language query
with st.sidebar:
    st.markdown('<div class="inventory-heading">Ask About Inventory</div>', unsafe_allow_html=True)
    user_query = st.text_input("Enter your query (e.g., 'stock of jeans from sangria')", key="user_query",
                               placeholder="Type your inventory question here...")
    if st.button("Run Query"):
        if user_query:
            conn = init_connection()
            sql_query = generate_sql_query(user_query)
            # Maintain only 5 queries in history
            st.session_state.query_history.append((user_query, sql_query))
            if len(st.session_state.query_history) > 5:
                st.session_state.query_history = st.session_state.query_history[-5:]
            df = run_query(sql_query, conn, _cache_key=user_query, user_query=user_query)
            if not df.empty:
                st.write("**Query Result:**")
                # Display single value if applicable
                if df.shape == (1, 1):
                    value = df.iloc[0, 0]
                    # Format revenue in rupees
                    if df.columns[0] == 'Revenue':
                        st.write(f"₹{value:,.2f}")
                    else:
                        st.write(f"{value}")
                else:
                    # Format revenue columns in tables
                    format_dict = {
                        col: "₹{:.2f}" for col in df.columns if 'revenue' in col.lower() or 'RevenueInRs' in col
                    }
                    format_dict.update({
                        "Predicted_Stockout_Date": "{:%Y-%m-%d}",
                        "Predicted_Restock_Date": "{:%Y-%m-%d}",
                        "DiscountPriceInRs": "₹{:.2f}"
                    })
                    st.dataframe(df.style.format(format_dict), use_container_width=True)
                # Show generated SQL query
                st.write("**Generated SQL Query:**")
                st.code(sql_query, language="sql")
                # Export to CSV
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download Result as CSV",
                    data=csv,
                    file_name=f"query_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
            else:
                st.warning("No results found for the query.")

    # Display query history (max 5)
    if st.session_state.query_history:
        st.write("**Query History (Last 5):**")
        for i, (q, sql) in enumerate(st.session_state.query_history, 1):
            st.markdown(f'<div class="query-history">{i}. {q}</div>', unsafe_allow_html=True)

    # Reset button
    st.header("Reset State")
    if st.button("Reset App State"):
        st.session_state.alerts_run = False
        st.session_state.query_history = []
        st.success("App state reset.")

# Main dashboard
with st.container():
    st.header("Inventory Dashboard")

    # Time filter for charts
    time_filter = st.selectbox("Select Time Period", ["Last 7 Days", "Last 30 Days", "Last 90 Days", "All Time"], key="time_filter")
    time_delta = {"Last 7 Days": 7, "Last 30 Days": 30, "Last 90 Days": 90, "All Time": None}
    days = time_delta[time_filter]

    # Category performance
    st.subheader("Category Performance")
    conn = init_connection()
    query = "SELECT Category, SUM(RevenueInRs) as RevenueInRs FROM sales_and_stock_info"
    if days:
        query += f" WHERE Predicted_Stockout_Date >= DATEADD(day, -{days}, GETDATE())"
    query += " GROUP BY Category"
    cat_df = run_query(query, conn, _cache_key=f"category_{time_filter}", user_query="category revenue")
    if not cat_df.empty:
        # Revenue by Category pie chart with percentage on hover
        fig = px.pie(cat_df, values="RevenueInRs", names="Category", title="Revenue by Category",
                     color_discrete_sequence=px.colors.sequential.Peach[::-1])
        fig.update_traces(textinfo='none')  # Remove text on chart
        fig.update_traces(hovertemplate='%{percent:.1%}')  # Show percentage on hover
        st.plotly_chart(fig, use_container_width=True)
        # Category revenue table with revenue in crores
        cat_df['RevenueInCrores'] = cat_df['RevenueInRs'] / 10000000  # Convert to crores
        st.write("**Revenue by Category:**")
        st.dataframe(cat_df[["Category", "RevenueInCrores"]].style.format({"RevenueInCrores": "{:.2f} Cr"}),
                     use_container_width=True)

    # Dropdown for additional visuals
    st.subheader("Additional Insights")
    visual_option = st.selectbox("Select Visualization", [
        "Top 5 Brands by Revenue",
        "Top 5 Individual Categories by Revenue",
        "Revenue Distribution by Gender"
    ], key="visual_select")

    # Top 5 Brands by Revenue
    if visual_option == "Top 5 Brands by Revenue":
        query = "SELECT TOP 5 BrandName, SUM(RevenueInRs) as RevenueInRs FROM sales_and_stock_info"
        if days:
            query += f" WHERE Predicted_Stockout_Date >= DATEADD(day, -{days}, GETDATE())"
        query += " GROUP BY BrandName ORDER BY RevenueInRs DESC"
        brand_df = run_query(query, conn, _cache_key=f"top_brands_{time_filter}", user_query="brand revenue")
        if not brand_df.empty:
            fig = px.bar(brand_df, x="RevenueInRs", y="BrandName", title="Top 5 Brands by Revenue",
                         color="BrandName", color_discrete_sequence=px.colors.sequential.Peach[::-1],
                         text_auto=".2f")
            fig.update_traces(texttemplate='₹%{text}', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

    # Top 5 Individual Categories by Revenue
    elif visual_option == "Top 5 Individual Categories by Revenue":
        query = "SELECT TOP 5 Individual_category, SUM(RevenueInRs) as RevenueInRs FROM sales_and_stock_info"
        if days:
            query += f" WHERE Predicted_Stockout_Date >= DATEADD(day, -{days}, GETDATE())"
        query += " GROUP BY Individual_category ORDER BY RevenueInRs DESC"
        cat_ind_df = run_query(query, conn, _cache_key=f"top_categories_{time_filter}", user_query="category revenue")
        if not cat_ind_df.empty:
            fig = px.bar(cat_ind_df, x="RevenueInRs", y="Individual_category",
                         title="Top 5 Individual Categories by Revenue",
                         color="Individual_category", color_discrete_sequence=px.colors.sequential.Peach[::-1],
                         text_auto=".2f")
            fig.update_traces(texttemplate='₹%{text}', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

    # Revenue Distribution by Gender
    elif visual_option == "Revenue Distribution by Gender":
        query = "SELECT category_by_Gender, SUM(RevenueInRs) as RevenueInRs FROM sales_and_stock_info"
        if days:
            query += f" WHERE Predicted_Stockout_Date >= DATEADD(day, -{days}, GETDATE())"
        query += " GROUP BY category_by_Gender"
        gender_df = run_query(query, conn, _cache_key=f"gender_{time_filter}", user_query="gender revenue")
        if not gender_df.empty:
            fig = px.pie(gender_df, values="RevenueInRs", names="category_by_Gender",
                         title="Revenue Distribution by Gender",
                         color_discrete_sequence=px.colors.sequential.Peach[::-1])
            fig.update_traces(textinfo='none')  # Remove text on chart
            fig.update_traces(hovertemplate='%{percent:.1%}')  # Show percentage on hover
            st.plotly_chart(fig, use_container_width=True)

# Alerts section
with st.container():
    st.subheader("Alerts")
    if st.button("View Alerts") and not st.session_state.alerts_run:
        st.session_state.alerts_run = True
        query = """
        SELECT TOP 10 BrandName, Individual_category, size, Current_Stock, DiscountPriceInRs, Predicted_Stockout_Date
        FROM sales_and_stock_info
        WHERE Current_Stock <= Reorder_Level OR Predicted_Stockout_Date <= DATEADD(day, 30, GETDATE())
        ORDER BY Current_Stock/NULLIF(Reorder_Level, 0) ASC
        """
        alert_df = run_query(query, conn, _cache_key="alerts", user_query="alerts")
        if not alert_df.empty:
            # Display table
            st.write("**Top 10 Low Stock or Stock-Out Alerts:**")
            st.dataframe(alert_df.style.format({
                "DiscountPriceInRs": "₹{:.2f}",
                "Predicted_Stockout_Date": "{:%Y-%m-%d}"
            }), use_container_width=True)
        else:
            st.info("No alerts at this time.")
        st.session_state.alerts_run = False