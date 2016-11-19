import tkinter as tk
from tkinter import ttk


class Graph(tk.Frame):
    DEFAULT_NUM_NODES = 10

    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(tk.Frame(self), parent)
        try:
            self.numNodes = kwargs['vertices']
        except KeyError:
            self.numNodes = Graph.DEFAULT_NUM_NODES

        self.vertices = self.buildVertexList()

    def buildVertexList(self):
        vertexList = []
        return vertexList

class Animation(tk.Tk):
    algorithms = ['DFS', 'BFS']

    def __init__(self, *args, **kwargs):
        self.algorithm = None
        try:
            if kwargs['algo'] in Animation.algorithms:
                self.algorithm = kwargs['algo']
        except KeyError:
            self.algorithms = 'DFS'

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, width=1600, height=900)
        container.grid(row=0, column=0, sticky=tk.NSEW)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.graph = Graph()

ani = Animation()
ani.title("Herb Prices")
ani.mainloop()
