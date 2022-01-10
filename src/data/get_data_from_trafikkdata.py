import requests
import json

import numpy as np
import pandas as pd
import geopandas as gpd

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

from pathlib import Path

url = 'https://www.vegvesen.no/trafikkdata/api/'

transport = RequestsHTTPTransport(
    url=url, verify=True, retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

filedir = '../../data'
filename = filedir + '/' + 'trafikkdata_hourly_TRAFFICSTATION.csv'

filepath = Path(filedir)
filepath.mkdir(parents=True, exist_ok=True)

queryByHour = """
{
  trafficData(trafficRegistrationPointId: "TRAFFICSTATION") {
    volume {
      byHour(from: "2019-01-01T00:00:01.000Z", to: "2019-12-31T23:59:59.999Z", after:"PAGINATION") {
        edges {
          node {
            to
            byLengthRange {
              total {
                volumeNumbers {
                  volume
                }
              }
              lengthRange {
                representation
              }
            }
          }
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
}
"""

def get_data_from_trafikkdata(trafficstation):
    hasNextPage = True
    endCursor = ""
    count = 0

    tdf = pd.DataFrame()

    while hasNextPage:
        
        # Make query
        queryS = queryByHour.replace("TRAFFICSTATION", trafficstation)
        queryS = queryS.replace("PAGINATION", endCursor)
    
        # Send request
        query = gql(queryS)
        try:
            r = client.execute(query)
        except: 
            continue

        # Extract data from result
        hasNextPage = r['trafficData']['volume']['byHour']['pageInfo']['hasNextPage']
        endCursor = r['trafficData']['volume']['byHour']['pageInfo']['endCursor']
        df_data = r['trafficData']['volume']['byHour']['edges']

        # Convert JSON to dataframe
        df = pd.json_normalize(df_data)
        if df.empty:
            continue
        df['trafikk_id'] = trafficstation
        
        # Extract data and convert JSON to dataframe
        df_bylength = pd.json_normalize(df['node.byLengthRange'])
        if not df_bylength.empty:
            for column in df_bylength:
                df_long = pd.json_normalize(df_bylength[column])
                df = df.join(df_long['total.volumeNumbers.volume'],
                             rsuffix=df_long['lengthRange.representation'].iloc[0])

        # add data to global dataframe
        tdf = tdf.append(df, ignore_index=True)
        
    # drop column no longer used
    tdf.drop(columns=['node.byLengthRange'], inplace=True)
    
    print("Saving last")
    tdf.to_csv(filename.replace("TRAFFICSTATION", trafficstation), index=False)

    print(endCursor)
    print(tdf.memory_usage(deep=True))
