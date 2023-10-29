# Daily Stock Dashboard
## Introduction
This is a dashboard that displays the daily stock price of a company. The dashboard is built using Python and Dash. The data is pulled from the [Alpha Vantage API](https://www.alphavantage.co/). The dashboard is deployed on Heroku and can be accessed [here](https://daily-stock-dashboard.herokuapp.com/).

This Python project retrieves and visualizes historical stock price data for Microsoft (MSFT) and Salesforce (CRM) using the Yahoo Finance API and Plotly. It generates line charts for Microsoft and candlestick charts for Salesforce. Additionally, it displays the timestamp of the last script run in UTC.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)


## Installation

To run this project, you'll need to have Python and the required libraries installed. You can install the necessary libraries using `pip`:

```bash
pip install pandas yfinance plotly
```
Additionally, you need to have the yfinance library installed, which provides access to Yahoo Finance data.
## Usage
### 1.Clone this repository to your local machine:
```
git clone https://github.com/rahul-ar-sys/daily_stock_dashboard.git
```
### 2.Navigate to the project directory:
```
cd daily_stock_dashboard
```
### 3.Run the Python script:
``` python main.py```
## Dependencies
The project relies on the following Python libraries:

### pandas: 
Used for data manipulation and analysis.
### yfinance: 
Provides access to Yahoo Finance data.
### plotly.graph_objects:
Used for creating interactive charts and visualizations.

### You can install these dependencies using the provided installation instructions.

## Project Structure
The project consists of the following files:
stock_visualization.py: The main Python script for data retrieval and visualization.
README.md: This documentation file.

