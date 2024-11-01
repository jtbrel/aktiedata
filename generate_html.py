import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


def update_data():

    tickers_dict = {
        'swe': ['EVO.ST', 'INVE-B.ST'],
        'nor': ['DNB.OL', 'YAR.OL', '2020.OL', 'SBO.OL'],
        'us': ['MSFT', 'AMZN', 'GOOG'],
    }

    tickers_list = sorted([item for sublist in tickers_dict.values() for item in sublist])

    tickers = yf.Tickers(tickers_list)

    cols = ['Earnings Date', 'Earnings High', 'Earnings Low', 'Earnings Average', 'Dividend Date', 'Ex-Dividend Date']
    df_calendar = pd.DataFrame((tickers.tickers[i].calendar for i in tickers_list), index=tickers_list)
    html_content = df_calendar.to_html(classes='table table-striped', border=0)

    with open("dataframe.html", "w") as f:
        f.write(f"""
        <html>
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }}
            </style>
        </head>
        <body>
            <h1>My DataFrame</h1>
            {html_content}
        </body>
        </html>
        """)

if __name__ == "__main__":
    update_data()