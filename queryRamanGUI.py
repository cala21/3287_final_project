import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from pylab import *
import sqlobject
from sqlobject.sqlbuilder import *
import numpy as np
from createRamanDB import *
import Tkinter as tk
import ttk



class myApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
            
        for F in (StartPage,PageOne):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='RamanShift')
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Compare Distribution', command=lambda: controller.show_frame(PageOne))

        button1.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='RamanShift')
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text='Back',command=lambda: controller.show_frame(StartPage))
        
        button1.pack()

        connection_string = 'mysql://cami:hamira@localhost/sqlobj_test'
        connection = connectionForURI(connection_string)
        sqlhub.processConnection = connection
        f = Figure(figsize = (5,5), dpi=100)
        a = f.add_subplot(111)

        for n in range(1,4):
            x = []
            y = []
            query_count = Select([Data.q.count], where=Data.q.experiment==n)
            count= connection.queryAll(connection.sqlrepr(query_count))
            
            query_ramanShift = Select([Data.q.ramanShift], where=Data.q.experiment==n)
            ramanShift= connection.queryAll(connection.sqlrepr(query_ramanShift))
            
            
            query_label = Select([Molecule.q.molecule_name, Experiment.q.molecule], where= (Molecule.q.id == Experiment.q.molecule) & (Experiment.q.id == n))
            
            ramanlabel = connection.queryAll(connection.sqlrepr(query_label))
            print ramanlabel[0][0]
            for i,j in zip(count,ramanShift):
                x.append(i[0])
                y.append(j[0])

         
            try:
                
                
                a.hist((x,y),100, histtype = 'step', label = ramanlabel[0][0])
                a.legend(loc='upper left')
                a.set_xlabel("Raman Shift (1/m)")
                a.set_ylabel("Count")
                a.set_ylim([0,100])
                a.set_xlim([1000,1200])
            
            
            except ValueError:
                pass
        canvas  =FigureCanvasTkAgg(f,self)
        canvas.show()
        canvas.get_tk_widget().pack(side = tk.TOP, fill=tk.BOTH, expand =True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side = tk.TOP, fill=tk.BOTH, expand =True)


app = myApp()
app.mainloop()

