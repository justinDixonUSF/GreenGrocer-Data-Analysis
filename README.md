# Sales Analytics Pipeline

## Overview

This project analyzes retail sales, customer behavior, and store performance using descriptive, diagnostic, predictive, and prescriptive analytics.

The goal is to help you understand performance, identify problems, forecast future trends, and guide business decisions.

## Features

### 1. Descriptive Analytics
Understand what has happened in your business.

- Total sales and profit
- Average profit margin
- Sales by store and department
- Customer segmentation insights
- Visualizations of sales trends

Functions:
- analyze_sales_performance()
- visualize_sales_distribution()
- analyze_customer_segments()

### 2. Diagnostic Analytics
Understand why performance changed.

- Correlation analysis between store and operational data
- Store efficiency comparison
- Seasonal sales pattern analysis

Functions:
- analyze_sales_correlations()
- compare_store_performance()
- analyze_seasonal_patterns()

### 3. Predictive Analytics
Estimate future performance.

- Linear regression model for store sales
- Department level sales forecasting using moving averages

Functions:
- predict_store_sales()
- forecast_department_sales()

### 4. Prescriptive Analytics
Identify actions to improve performance.

- Detect high and low performing store-department combinations
- Generate business recommendations

Functions:
- identify_profit_opportunities()
- develop_recommendations()

### 5. Executive Summary
Quick business overview for stakeholders.

Function:
- generate_executive_summary()

## Data Requirements

You need the following pandas DataFrames loaded before running the functions:

### sales_df
- Sales
- Profit
- ProfitMargin
- Store
- Department
- Date (datetime format required)

### customer_df
- Segment
- MonthlySpend
- LoyaltyTier

### store_df
- Store
- SquareFootage
- StaffCount
- YearsOpen

### operational_df
- Store
- AnnualSales
- AnnualProfit
- SalesPerSqFt
- SalesPerStaff
- WeeklyMarketingSpend

## Installation

pip install pandas numpy matplotlib scipy

## Usage Example

# Run descriptive analysis
summary = analyze_sales_performance()

# Visualize data
figs = visualize_sales_distribution()

# Analyze customer segments
segments = analyze_customer_segments()

# Run predictive model
model_results = predict_store_sales()

# Generate recommendations
recommendations = develop_recommendations()

# Print executive summary
generate_executive_summary()

## Notes

Ensure Date columns are converted to datetime:
sales_df["Date"] = pd.to_datetime(sales_df["Date"])

Missing or incorrect data will affect results.

Visualizations use matplotlib and return figure objects for further customization.
