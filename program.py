import tkinter as tk
from tkinter import ttk


class polyFrame(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        tk.Canvas.__init__(self, master=parent, *args, **kwargs)


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

class Triangulation(tk.Tk):
    algorithms = ['diagonal', 'monotone', 'ear']

    def algoIter(self):
        if not self.diagonals:
            self.triangulate()
        else:
            self.polygon.create_line(self.diagonals.pop(0))
            self.polygon.pack()

    def __init__(self, algo='diagonal', *args, **kwargs):
        self.algorithm = algo
        self.vertices = [[100, 0, 200, 100],
                         [200, 100, 150, 150],
                         [150, 150, 150, 250],
                         [150, 250, 100, 150],
                         [100, 150, 50, 250],
                         [50, 250, 0, 100],
                         [0, 100, 100, 0]
                         ]

        self.diagonals = []
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)
        self.graph = tk.Frame(self.container)
        self.header = tk.Frame(self.container)
        self.footer = tk.Frame(self.container)
        self.polygon = polyFrame(self.graph)

        self.container.grid(row=0, column=0, sticky=tk.NSEW)
        self.header.grid(row=0, column=0, sticky=tk.NSEW)
        self.graph.grid(row=1, column=0, sticky=tk.NSEW)
        self.footer.grid(row=2, column=0, sticky=tk.NSEW)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.buildGraph()
        self.triangulate()

        self.nameLabel = tk.Label(self.header, text=self.algorithm, font='bold')
        self.nameLabel.pack()

        btnEar = ttk.Button(self.footer, text='Iterate Through Algorithm', command=self.algoIter)
        btnEar.pack(padx=5, pady=5)

    def buildGraph(self):
        try:
            for vertex in self.vertices:
                # polygon.create_polygon(vertex, outline='black', fill='White')
                self.polygon.create_line(vertex)
                self.polygon.pack()
        except IndexError:
            return 0

    def triangulate(self):

        if not self.algorithm:
            return

        elif self.algorithm == 'ear':
            self.diagonals = [[0, 100, 200, 100],
                              [0, 100, 100, 150],
                              [100, 150, 150, 150],
                              [100, 150, 200, 100]]
        elif self.algorithm == 'diagonal':
            self.diagonals = [[100, 0, 50, 250],
                              [100, 0, 100, 150],
                              [100, 0, 150, 250],
                              [100, 0, 150, 150]]
        elif self.algorithm == 'monotone':
            self.diagonals = [[0, 100, 100, 150],
                              [100, 150, 100, 0],
                              [100, 0, 150, 250],
                              [100, 0, 150, 150]]

sim1 = Triangulation('ear')
sim2 = Triangulation('diagonal')
sim3= Triangulation('monotone')

sim1.title('Ear Based Triangulation Algorithm')
sim2.title('Diagonal Based Triangulation Algorithm')
sim3.title('Monotone Based Triangulation Algorithm')

sim1.mainloop()
sim2.mainloop()
sim3.mainloop()

