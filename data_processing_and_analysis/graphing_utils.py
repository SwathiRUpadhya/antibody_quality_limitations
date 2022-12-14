import matplotlib as mpl

mpl.rcParams.update({
    'font.family':'Arial',
    'text.usetex': False,
    'axes.spines.top': False,
    'axes.spines.right': False, 
    'axes.spines.left': False, 
    'axes.axisbelow': True,
    'axes.labelpad': 6.0,
    'axes.linewidth':0.8,
    'font.size':9,
    'axes.labelsize':9,
    'legend.fontsize':9,
    'xtick.labelsize':9,
    'ytick.labelsize':9,
    'lines.linewidth':1,
    'figure.dpi': 100,
    'lines.linewidth':1,
    'legend.edgecolor': 'white',
    'legend.loc': 'best',
    'legend.frameon':True,
    'legend.framealpha': 0.9,
    'svg.fonttype': "none",
    'mathtext.bf': 'Arial:bold'
})

    
from dataclasses import dataclass, field
@dataclass
class additional_plot_parameters:   
    title: str = field(default=None)
    xlab: str = field(default=None)
    ylab: str = field(default=None)
    ylim: tuple = field(default=(-0.45, 1.15))
    palette: list = field(default=None)
    fontsize: str = field(default=None)
    xaxis_grid: bool = field(default=False)    
    yaxis_grid: bool = field(default=True)
    show_legend: bool = field(default=True)      
    anchor_legend_at: tuple = field(default=None)
    r2 : float = field(default=None)
        
# Getting palette colors 
def get_color(name='grey'):
    return {
        'orange':'#E69F00',
        'green':'#009E73',
        'denim-blue': '#1864aa',
        'dark-sky-blue': '#5ba3cf',
        'light-blue': '#86bcdc'
    }[name]