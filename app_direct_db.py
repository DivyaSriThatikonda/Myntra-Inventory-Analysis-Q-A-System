import pyodbc
import os
from dotenv import load_dotenv
from prompt_config import PROMPT_TEMPLATE, BRAND_NAMES, CATEGORIES, INDIVIDUAL_CATEGORIES, SAMPLE_QUESTIONS
import google.generativeai as genai
import logging

# Configure logging to ERROR only
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


# Database connection
def get_db_connection():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DESKTOP-HJKD3T7;"
            "DATABASE=Inventory_Management;"
            "Trusted_Connection=yes;"
        )
        return conn
    except Exception as e:
        logger.error(f"Database connection error: {str(e)}")
        raise


# Preprocess query
def preprocess_query(query):
    query = query.lower().strip()
    for brand in BRAND_NAMES:
        if brand in query:
            query = query.replace(brand.lower(), brand)  # Preserve exact brand case
    for cat in CATEGORIES + INDIVIDUAL_CATEGORIES:
        if cat in query:
            query = query.replace(cat.lower(), cat)  # Preserve exact category case
    return query


# Generate SQL query
def generate_sql_query(natural_query):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        brand_samples = ", ".join(BRAND_NAMES[:5])
        category_samples = ", ".join(CATEGORIES[:5])
        individual_category_samples = ", ".join(INDIVIDUAL_CATEGORIES[:5])
        sample_questions = "\n".join([f"- '{k}': {v}" for k, v in SAMPLE_QUESTIONS.items()])

        prompt = PROMPT_TEMPLATE.format(
            query=natural_query,
            table_name="sales_and_stock_info",
            columns="Product_id, BrandName, Category, Individual_category, category_by_Gender, Description, DiscountPriceInRs, Current_Stock, Reorder_Level, Quantity_Sold, RevenueInRs, Turnover_Flag, Predicted_Restock_Quantity, Predicted_Stockout_Date, Predicted_Restock_Date, size",
            brand_count=len(BRAND_NAMES),
            brand_samples=brand_samples,
            category_count=len(CATEGORIES),
            category_samples=category_samples,
            individual_category_count=len(INDIVIDUAL_CATEGORIES),
            individual_category_samples=individual_category_samples,
            sample_questions=sample_questions
        )

        processed_query = preprocess_query(natural_query)
        response = model.generate_content(prompt)
        sql_query = response.text.strip()

        # Validate query
        if not sql_query.upper().startswith("SELECT"):
            logger.error(f"Invalid SQL query generated: {sql_query}")
            return "SELECT 'Invalid query generated' AS Error"

        return sql_query
    except Exception as e:
        logger.error(f"Error generating SQL query: {str(e)}")
        return f"SELECT 'Error: {str(e)}' AS Error"