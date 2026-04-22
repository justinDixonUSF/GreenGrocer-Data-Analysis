# TODO 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# TODO 1: Descriptive Analytics - Overview of Current Performance

def analyze_sales_performance():
    ## Calculate total sales and profit
    total_sales = sales_df["Sales"].sum()
    total_profit = sales_df["Profit"].sum()
    
    ## Calculate average profit margin
    avg_profit_margin = sales_df["ProfitMargin"].mean()
    
    ## Group sales by store and department
    sales_by_store = sales_df.groupby("Store")["Sales"].sum()
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum()
    
    ## Print results so output is visible
    print("\nSales Summary:")
    print("Total Sales:", total_sales)
    print("Total Profit:", total_profit)
    print("Average Profit Margin:", avg_profit_margin)
    
    return {
        'total_sales': total_sales,
        'total_profit': total_profit,
        'avg_profit_margin': avg_profit_margin,
        'sales_by_store': sales_by_store,
        'sales_by_dept': sales_by_dept
    }


def visualize_sales_distribution():
    ## Sales by store
    store_fig = plt.figure()
    sales_df.groupby("Store")["Sales"].sum().plot(kind="bar")
    plt.title("Sales by Store")
    
    ## Sales by department
    dept_fig = plt.figure()
    sales_df.groupby("Department")["Sales"].sum().plot(kind="bar")
    plt.title("Sales by Department")
    
    ## Sales over time
    time_fig = plt.figure()
    sales_df.groupby("Date")["Sales"].sum().plot()
    plt.title("Sales Over Time")
    
    return (store_fig, dept_fig, time_fig)


def analyze_customer_segments():
    ## Segment counts
    segment_counts = customer_df["Segment"].value_counts()
    
    ## Average spend
    segment_avg_spend = customer_df.groupby("Segment")["MonthlySpend"].mean()
    
    ## Loyalty breakdown
    segment_loyalty = pd.crosstab(customer_df["Segment"], customer_df["LoyaltyTier"])
    
    ## Print key insights
    print("\nCustomer Segment Summary:")
    print(segment_counts)
    
    return {
        'segment_counts': segment_counts,
        'segment_avg_spend': segment_avg_spend,
        'segment_loyalty': segment_loyalty
    }


# TODO 2: Diagnostic Analytics

def analyze_sales_correlations():
    ## Merge datasets
    merged = pd.merge(store_df, operational_df, on="Store")
    
    ## Correlation matrix
    store_correlations = merged.corr(numeric_only=True)
    
    ## Top correlations with AnnualSales
    corr_series = store_correlations["AnnualSales"].drop("AnnualSales")
    top_correlations = list(corr_series.sort_values(ascending=False).head(5).items())
    
    ## Visualization
    correlation_fig = plt.figure()
    plt.imshow(store_correlations)
    plt.colorbar()
    plt.title("Correlation Matrix")
    
    return {
        'store_correlations': store_correlations,
        'top_correlations': top_correlations,
        'correlation_fig': correlation_fig
    }


def compare_store_performance():
    ## Efficiency metrics
    efficiency_metrics = operational_df[["Store", "SalesPerSqFt", "SalesPerStaff"]]
    
    ## Rank by profit
    performance_ranking = operational_df.set_index("Store")["AnnualProfit"].rank(ascending=False)
    
    ## Plot
    comparison_fig = plt.figure()
    operational_df.set_index("Store")["AnnualProfit"].plot(kind="bar")
    plt.title("Store Profit Comparison")
    
    return {
        'efficiency_metrics': efficiency_metrics,
        'performance_ranking': performance_ranking,
        'comparison_fig': comparison_fig
    }


def analyze_seasonal_patterns():
    ## Create time features
    sales_df["Month"] = sales_df["Date"].dt.month
    sales_df["DayOfWeek"] = sales_df["Date"].dt.dayofweek
    
    ## Aggregate
    monthly_sales = sales_df.groupby("Month")["Sales"].sum()
    dow_sales = sales_df.groupby("DayOfWeek")["Sales"].sum()
    
    ## Plot
    seasonal_fig = plt.figure()
    monthly_sales.plot(label="Monthly")
    dow_sales.plot(label="Day of Week")
    plt.legend()
    plt.title("Seasonal Patterns")
    
    return {
        'monthly_sales': monthly_sales,
        'dow_sales': dow_sales,
        'seasonal_fig': seasonal_fig
    }


# TODO 3: Predictive Analytics

def predict_store_sales():
    ## Features and target
    X = store_df[["SquareFootage", "StaffCount", "YearsOpen", "WeeklyMarketingSpend"]].values
    y = operational_df["AnnualSales"].values
    
    ## Add intercept
    X = np.c_[np.ones(X.shape[0]), X]
    
    ## Regression using numpy
    coeffs = np.linalg.lstsq(X, y, rcond=None)[0]
    
    ## Predictions
    predictions = X.dot(coeffs)
    
    ## R-squared
    ss_total = np.sum((y - y.mean())**2)
    ss_res = np.sum((y - predictions)**2)
    r_squared = 1 - (ss_res / ss_total)
    
    ## Plot
    model_fig = plt.figure()
    plt.scatter(y, predictions)
    plt.title("Actual vs Predicted Sales")
    
    ## Coefficients dictionary
    names = ["Intercept", "SquareFootage", "StaffCount", "YearsOpen", "MarketingSpend"]
    coefficients = dict(zip(names, coeffs))
    
    return {
        'coefficients': coefficients,
        'r_squared': r_squared,
        'predictions': pd.Series(predictions),
        'model_fig': model_fig
    }


def forecast_department_sales():
    ## Aggregate
    dept_trends = sales_df.groupby(["Date", "Department"])["Sales"].sum().unstack()
    
    ## Growth rate
    growth_rates = dept_trends.pct_change().mean()
    
    ## Moving average
    forecast = dept_trends.rolling(7).mean()
    
    ## Plot
    forecast_fig = plt.figure()
    forecast.plot()
    plt.title("Department Forecast")
    
    return {
        'dept_trends': dept_trends,
        'growth_rates': growth_rates,
        'forecast_fig': forecast_fig
    }


# TODO 4: Integrated Analysis

def identify_profit_opportunities():
    ## Profit by store and department
    combo = sales_df.groupby(["Store", "Department"])["Profit"].sum().reset_index()
    
    ## Top and bottom
    top_combinations = combo.sort_values(by="Profit", ascending=False).head(10)
    underperforming = combo.sort_values(by="Profit").head(10)
    
    ## Opportunity score
    opportunity_score = combo.groupby("Store")["Profit"].mean()
    
    return {
        'top_combinations': top_combinations,
        'underperforming': underperforming,
        'opportunity_score': opportunity_score
    }


def develop_recommendations():
    return [
        "Increase marketing in high-performing stores",
        "Focus on high-margin departments",
        "Target high-spending customer segments",
        "Improve efficiency in low-performing stores",
        "Adjust inventory based on seasonal demand"
    ]


# TODO 5: Executive Summary

def generate_executive_summary():
    print("\nOverview:")
    print("GreenGrocer shows strong seasonal trends and variation across stores.")
    
    print("\nKey Findings:")
    print("- Miami leads in performance")
    print("- Prepared Foods has highest margins")
    print("- Family Shopper drives revenue")
    print("- Sales peak on weekends and summer")
    
    print("\nRecommendations:")
    print("- Invest in top stores")
    print("- Expand high-margin categories")
    print("- Target valuable customers")
    print("- Improve efficiency")
    print("- Plan for seasonality")
    
    print("\nExpected Impact:")
    print("Improved profit, better resource use, and stronger growth.")