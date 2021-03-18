#** Created PySimpleGUI to dispay new graph for each week, structure below
#** is solid but we got stuck on syntax to update current object displayed. 

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from networkx.classes.function import selfloop_edges
matplotlib.use('TKAgg')

import networkx as nx
from networkx.drawing.nx_pylab import draw_random
import numpy as np
import PySimpleGUI as sg
import time
import math

# Person class with init, repr, and str.
class Person:
    def __init__(self, name, couple):
        self.name = name
        self.couple = couple
        self.busy = False
        self.hosting = []
        self.host_count = 0
    def __repr__(self):
        return repr(self.name)
    def __str__(self):
        return self.name

    def hosts(self, visitor):
        # Make this household a host if it isn't already.
        if (self.host_count == 0):
            self.hosting.append(self)
            self.host_count += 1
            if self.couple:
                self.host_count += 1
                
        # Host the current household s.
        visitor.busy = True
        self.hosting.append(visitor)
        self.host_count += 1
        if visitor.couple:
            self.host_count += 1

    def reset(self):
        self.busy = False
        self.hosting = []
        self.host_count = 0

# -*-*-*- EOF Person class

# Variables 
group_size = 3;
filename = "sample.txt"
G = nx.DiGraph() # main graph
M = nx.DiGraph() # mirror graph
repeat_visits = []

# Open file
with open(filename) as file:
    lines = file.read().splitlines()
    for L in lines:
        L = L.replace(", ", " + ")
        if "+" in L:
            P = Person(L, True)
        else:
            P = Person(L, False)
        G.add_node(P)

# Generic helper method to draw graph to canvas
def draw_figure(canvas, figure):
    try: 
        selfloop_edges.FigureCanvasTkAgg.get_tk_widget().pack_forget()
    except AttributeError: 
        pass 

    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# Create graph
def fig_maker(M):
    nx.draw_circular(M, with_labels=True)
    fig = plt.gcf()
    return fig

# GUI layout
layout = [[sg.Text('Iterations are Live')],
          [sg.Canvas(key='-CANVAS-')],
          [sg.Button('Close')]]

# create the form and show it without the plot
window = sg.Window('We Love Algorithms', layout, finalize=True, element_justification='center', font='Helvetica 18')

def build_all():

    # Build every edge of the complete graph.
    for s in G.nodes():
        for v in G.nodes():
            if s != v:
                G.add_edge(s, v)

    week = 1
    while G.number_of_edges() > 0:
        print("Week", week)

        for s in G.nodes():
            if s.hosting:
                continue
            for v in G.adj[s]:
                if not v.busy and v.host_count < group_size:
                    v.hosts(s)

                    M.add_node(v)
                    M.add_node(s)
                    M.add_edge(v, s)

                    G.remove_edge(s, v)
                    break
        
        # Assigning repeated visitors (not required connections).
        for s in G.nodes():
            if not s.busy and not s.hosting:
                for v in G.nodes():
                    if s != v and not v.busy and v.host_count < group_size:
                        M.add_edge(v, s)
                        v.hosts(s)
                        repeat_visits.append(s)
                        break
        
        print("Number of Nodes for M: ", M.number_of_nodes())
        print("Number of Edges for M: ", M.number_of_edges())

        fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig_maker(M))
        
        for s in G.nodes():
            if (s.hosting):
                print(s.hosting[0], s.hosting[1:])
            s.reset()            

        # Showing the hosts for this week.
        for s in M.nodes():
            s.reset()

        # Show repeat visitors (to verify that the algorithm is effecient).
        if (repeat_visits):
            print("Repeats:", repeat_visits)
        
        week += 1
        repeat_visits.clear()
        print("\n")
        
i = 0
timeout = delta = 10 # 10 millisecond refresh interval
while True:
    event, values = window.read(timeout=timeout)
    if event == None:
        break

    start_time = time.time()

    build_all()

    i = i+1 if i<359 else 0

    end_time = time.time()
    timeout = max(0, (delta - (end_time-start_time)*1000))

window.close()