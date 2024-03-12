import tkinter as tk
import WrappedOnDemand as wod
import pandas as pd
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class WODGUI:

    def __init__(self):
        self.dataFrame = wod.getDataFrame()
        artists = wod.getTopArtists(self.dataFrame)
        songs = wod.getTopSongs(self.dataFrame)
        listeningByDay = wod.getListeningByDay(self.dataFrame)
        listeningByMonth = wod.getListeningByMonth(self.dataFrame)

        self.root = tk.Tk()
        self.root.title("Wrapped On Demand")
        self.root.geometry("1000x800")

        self.initializeFrame()

        label = tk.Label(self.frame, text="Welcome to Your Wrapped On Demand", bg="black", foreground="#1db954", font=("@Yu Gothic Medium", 24))
        label.pack(padx=10, pady=10)

        artistLabel = tk.Label(self.frame, text="Top Artists", bg="#535353", foreground="#1db954", font=("@Yu Gothic Medium", 24))
        artistLabel.pack(fill="x")
        self.displayArtists(artists)

        songLabel = tk.Label(self.frame, text="Top Songs", bg="#535353", foreground="#1db954", font=("@Yu Gothic Medium", 24))
        songLabel.pack(fill="x")
        self.displaySongs(songs)

        dayLabel = tk.Label(self.frame, text="Your Listening By Day", bg="#535353", foreground="#1db954", font=("@Yu Gothic Medium", 24))
        dayLabel.pack(fill="x")
        self.drawPlot(listeningByDay, "Day", "Hours")

        monthLabel = tk.Label(self.frame, text="Your Listening By Month", bg="#535353", foreground="#1db954", font=("@Yu Gothic Medium", 24))
        monthLabel.pack(fill="x")
        self.drawPlot(listeningByMonth, "Month", "Hours")

        self.root.mainloop()

    def initializeFrame(self):
        #Create Main Frame in Root
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=1)

    #Create Canvas: Where all Info will be
        self.my_canvas = tk.Canvas(self.main_frame)
        self.my_canvas.pack(side="left", fill="both", expand=1)

    #Create Scrollbar to control canvas
        self.my_scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.my_canvas.yview)
        self.my_scrollbar.pack(side="right", fill="y")

    #Configure the canvas
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set, bg="#535353")
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

    #Create another frame in the canvas
        self.frame = tk.Frame(self.my_canvas)
        self.frame.configure(bg="#535353")
    
    #Add new frame to a window in the canvas
        self.my_canvas.create_window((0,0), window=self.frame, anchor="nw")
    
    def displayArtists(self, artists):
        for artist, hours in artists.items():
            text = tk.Label(self.frame, text=f"{artist}: {hours:.2f} hours", bg="#535353", foreground="white", font=("@Yu Gothic Medium", 18))
            text.pack(fill="x")
    
    def displaySongs(self, songs):
        for (artist, song), hours in songs.items():
            text = tk.Label(self.frame, text=f"{artist}: {song} - {hours:.2f} hours", bg="#535353", foreground="white", font=("@Yu Gothic Medium", 18))
            text.pack(fill="x")

    def drawPlot(self, data, x, y):

        figure, axis = plt.subplots()
        figure.set_facecolor("#535353")
        axis.set_facecolor("#535353")
        bars = axis.bar(data.index, data, color="#1db954")
        axis.set_xlabel(x)
        axis.set_ylabel(y)
        axis.xaxis.label.set_color("#1db954")  # Set x-axis label color
        axis.yaxis.label.set_color("#1db954")  # Set y-axis label color
        axis.tick_params(axis='x', colors='#b3b3b3')   # Set x-axis tick label color
        axis.tick_params(axis='y', colors='#b3b3b3')
        for spine in axis.spines.values():
            spine.set_edgecolor('#b3b3b3')
        plt.xticks(rotation=30, ha='right')
        canvas = FigureCanvasTkAgg(figure, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack(padx=20, pady=20, fill="both", expand=True)


        

WODGUI()