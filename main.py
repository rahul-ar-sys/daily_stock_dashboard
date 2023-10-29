from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf

# Get the last 365 days of Microsoft stock at a 1 day frequency
msft = yf.Ticker("MSFT")
end_date = pd.Timestamp.today(tz='America/New_York').ceil('D')
start_date = end_date - pd.Timedelta(365,'D')
data = msft.history(start=start_date,end=end_date, interval='1d').reset_index()

# Plot as a line chart
fig = go.Figure(data=go.Scatter(
        x=data.Date,
        y=data.Close,
        mode='lines'
))
fig.update_layout(
    title='Microsoft (MSFT)',
    title_x=0.5,
    autosize=False,
    width=800,
    height=500,
    xaxis= dict(rangeselector=dict(
        buttons=list([
            dict(count=30,
                    label="30D",
                    step="day",
                    stepmode="backward"),
            dict(count=6,
                    label="6M",
                    step="month",
                    stepmode="backward"),
            dict(count=1,
                    label="YTD",
                    step="year",
                    stepmode="todate"),
            dict(count=1,
                    label="1Y",
                    step="year",
                    stepmode="backward")
        ])
    )),
)
fig.show()

print("candlastick chart")

end_date = pd.Timestamp.today(tz='America/New_York').ceil('D')
start_date = end_date - pd.Timedelta(7,'D') # Get the last 4 days, in case of holidays/weekend
crm = yf.Ticker("CRM")
data = crm.history(start=start_date,end=end_date, interval='1m').reset_index()
data = data.rename(columns=dict(Datetime='Date'))
data = data.loc[data.Date.dt.date == data.Date.dt.date.max()] # Get only the last day's data


fig = go.Figure(data=go.Candlestick(
     x = data.Date,
     open = data.Open,
     high = data.High,
     low = data.Low,
     close = data.Close
))

fig.update_layout(
     title='Salesforce (CRM)',
     title_x=0.5,
     autosize=False,
     width=800,
     height=600,
     xaxis= dict(rangeselector=dict(
          buttons=list([
               dict(count=1,
                    label="1H",
                    step="hour",
                    stepmode="backward"),
               dict(label='1D',step="all"),
          ])
     )),
)


fig.update_layout(

)
fig.show()
now = datetime.now()
now = now.strftime("%B %d, %Y at %H:%M")
print(f'Last run on {now} UTC')
