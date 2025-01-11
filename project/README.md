# Domestic Residence and Permissions Data Analysis

## Overview
This project analyzes Domestic Residence & Permissions applications and decisions in Ireland from 2017 to 2024. It explores trends, nationality variations, and application outcomes using data visualizations.

## Objectives
- Analyze application trends over time.
- Identify patterns in nationality-based applications.
- Visualize data with various charts and graphs.
- Predict future application trends using linear regression.

## Data
The dataset includes:
- Applications received, granted, and refused.
- Data categorized by year and nationality.
- Values between 1 and 3 suppressed for statistical reasons.

## Tools Used
- **Pandas**: Data manipulation.
- **Plotly**: Interactive visualizations.
- **Pycountry Convert**: Country to continent mapping.
- **NumPy**: Numerical calculations.
- **Scikit-Learn**: Linear regression modeling for predictive analysis.

## Key Insights
- Application volumes fluctuated over the years.
- Certain nationalities frequently appear among the top applicants.
- Interactive visualizations reveal complex decision patterns.

## Predictive Analysis
A **linear regression model** was implemented using **Scikit-Learn** to forecast the number of **Received** applications for the next 10 years (2025-2034). The top 10 nationalities with the highest total received applications were analyzed individually, ensuring more accurate and specific predictions. This analysis predicts a steady growth in application volumes for these nationalities, emphasizing the importance of proactive policy adjustments and resource planning.

## How to Run
1. Install required libraries:
   ```bash
   pip install pandas plotly pycountry_convert numpy scikit-learn
   ```
2. Open `bigproject.ipynb` and run all cells.

## References
- [Data.gov.ie](https://data.gov.ie/dataset/domestic-residence-permissions-applications-and-decisions-year-and-nationality)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Plotly Documentation](https://plotly.com/)
- [NumPy Documentation](https://numpy.org/)
- [Scikit-Learn Documentation](https://scikit-learn.org/)
- [Pycountry-Convert](https://pypi.org/project/pycountry-convert/)

## License
Licensed under the Creative Commons Attribution 4.0 International License.
