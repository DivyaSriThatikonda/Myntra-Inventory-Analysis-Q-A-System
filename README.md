# Myntra-Inventory-Analysis-Q-A-System
# Myntra Inventory Analysis Chatbot

Welcome to the **Myntra Inventory Analysis Chatbot**, a Streamlit-based application designed to analyze and manage inventory data for Myntra, a leading Indian fashion e-commerce platform. This project leverages the free Google Gemini API from Google AI Studio to convert natural language queries into SQL, enabling users to explore inventory details (e.g., stock levels, revenue) and visualize performance metrics, all powered by a Microsoft SQL Server backend.

## Features
- **Natural Language Querying**: Powered by Google Gemini, ask questions like "stock of jeans from Sangria" or "sum of revenue of Anouk kurtas" to generate SQL queries dynamically.
- **Interactive Visualizations**: Pie charts for category revenue (with percentage hover) and bar charts for top brands/categories, styled with a Myntra-branded theme.
- **Revenue Insights**: Displays revenue in crores for category performance and rupees for other queries.
- **Alerts System**: Highlights top 10 low-stock or soon-to-stock-out items.
- **Query History**: Tracks the last 5 queries in the sidebar.
- **Downloadable Results**: Export query results as CSV files.
- **User-Friendly UI**: Features a clean design with the Myntra logo and apparel icons (T-shirt, pants).

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python, pyodbc (for SQL Server connectivity), Google Gemini API (free tier from Google AI Studio)
- **Visualization**: Plotly Express
- **Database**: Microsoft SQL Server (assumes `sales_and_stock_info` table)
- **Dependencies**: pandas, python-dotenv

## Dataset Overview
The project uses a `sales_and_stock_info` table in the `Inventory_Management` database, containing approximately 500,000 rows of Myntra inventory data. Key details include:

- **Brands**: Features around 200 unique brands, including popular ones like Anouk, Sangria, Roadster, HRX, and W.
- **Categories**: Includes about 10 unique categories, such as Jeans, Kurtas, Trousers, Shirts, and Jackets.
- **Individual Categories**: Comprises around 50 unique sub-categories, e.g., Slim Fit Jeans, Anarkali Kurtas, Chinos, Casual Shirts, and Bomber Jackets (note: hyphens are retained in names like track-pants and kurta-sets for consistency).
- **Files**:
  - `streamlit_app.py`: Main application file with UI and visualization logic.
  - `app_direct_db.py`: Handles database connections and SQL query generation using Gemini.
  - `prompt_config.py`: Configures the Gemini prompt for natural language to SQL conversion.
  - `requirements.txt`: Lists project dependencies.
  - `.env`: Stores database credentials (not included in repo for security).
- **Columns**:
  - `BrandName`: Brand of the item (e.g., Anouk, Sangria), converted to lowercase for consistency.
  - `Category`: Broad category (e.g., Jeans, Kurtas), lowercase.
  - `Individual_category`: Specific sub-category (e.g., Slim Fit Jeans, track-pants), lowercase with hyphens retained.
  - `category_by_Gender`: Gender association (e.g., Men, Women), lowercase.
  - `size`: Item size (e.g., S, M, L), lowercase.
  - `Current_Stock`: Current stock quantity.
  - `Reorder_Level`: Threshold for reordering.
  - `DiscountPriceInRs`: Price in rupees after discount.
  - `RevenueInRs`: Total revenue in rupees.
  - `Predicted_Stockout_Date`: Estimated date of stock depletion.
  - `Predicted_Restock_Date`: Estimated restock date.

## Prerequisites
- Python 3.8+
- Git (for cloning the repository)
- Microsoft SQL Server (or compatible DB) with the `Inventory_Management` database
- ODBC Driver for SQL Server installed
- Google AI Studio API Key (free tier, sign up at [ai.google.dev](https://ai.google.dev))

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/myntra-inventory-analysis-chatbot.git
   cd myntra-inventory-analysis-chatbot
