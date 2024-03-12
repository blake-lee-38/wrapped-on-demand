import json
import pandas as pd
from collections import defaultdict
import tkinter as tk
from tkinter import Scrollbar


msToHours = 3600000


def getDataFrame():
    # Load the provided JSON files
    files = [
        "./data_files/StreamingHistory_music_0.json",
        "./data_files/StreamingHistory_music_1.json",
    ]

    data = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            data.extend(json.load(f))

    # Convert data into a pandas DataFrame
    df = pd.DataFrame(data)
    df['endTime'] = pd.to_datetime(df['endTime'])
    return df


# Calculate most listented to Artists
def getTopArtists(df):
    artist_most_listened = df.groupby('artistName')['msPlayed'].sum().sort_values(ascending=False)
    artists = (artist_most_listened.head(5) / msToHours)

    return artists

# Calculate most listened to Songs
def getTopSongs(df):
    songs_most_listened = df.groupby(['artistName', 'trackName'])['msPlayed'].sum().sort_values(ascending=False)
    songs = (songs_most_listened.head(5) / msToHours)

    return songs

def getListeningByDay(df):
    # Calculate Listening By Day of the Week
    df['day'] = df['endTime'].dt.day_name()
    listening_by_day = df.groupby('day')['msPlayed'].sum() / msToHours
    #Order the days of the week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    listening_by_day = listening_by_day.reindex(days)
    #Calculate number of weeks to get average
    weeks = (df['endTime'].max() - df['endTime'].min()).days / 7
    average_listening_by_day = listening_by_day / weeks
    return average_listening_by_day

def getListeningByMonth(df):
    #Calculate Listening by Month
    df['month'] = df['endTime'].dt.month_name()
    listening_by_month = df.groupby('month')['msPlayed'].sum() / msToHours
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    listening_by_month = listening_by_month.reindex(months)

    return listening_by_month
