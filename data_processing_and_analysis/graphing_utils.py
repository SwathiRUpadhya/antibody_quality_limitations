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
    legend_title: str = field(default=None)
    r2 : float = field(default=None)
        
# Getting palette colors 
def get_color(name='grey'):
    return {
        'orange':'#E69F00',
        'green':'#009E73',
        'blue': '#0072B2',
        'yellow': '#f0e442',
        'light-blue-ot': '#56b4e9',
        'denim-blue': '#1864aa',
        'dark-sky-blue': '#5ba3cf',
        'light-blue': '#86bcdc'
    }[name]

def set_axis_props(ax, **kwargs):
    
    xlab = kwargs.get('xlabel', None)
    xfontsize = kwargs.get('xlabel_fontsize', mpl.rcParams['axes.labelsize'])
    if xlab != None:
        ax.set_xlabel(xlab, fontsize=xfontsize)
        
    ylab = kwargs.get('ylabel', None)
    yfontsize = kwargs.get('ylabel_fontsize', mpl.rcParams['axes.labelsize'])
    if ylab != None:
        ax.set_ylabel(ylab, fontsize=yfontsize)
    
    show_xticks = kwargs.get('show_xticks', True)
    if show_xticks==False:
        ax.tick_params(axis='x', which='both', length=0)
    
    show_yticks = kwargs.get('show_yticks', True)
    if show_yticks==False:
        ax.tick_params(axis='y', which='both', length=0)
        
    show_yticklabels = kwargs.get('show_yticklabels', True)
    if show_yticklabels==False:
        ax.get_yaxis().set_ticks([])
        
    show_xticklabels = kwargs.get('show_xticklabels', True)
    if show_xticklabels==False:
        ax.get_xaxis().set_ticks([])
        
    xtick_fontsize = kwargs.get('xtick_fontsize', mpl.rcParams['xtick.labelsize'])
    ax.tick_params(axis='x', which='both', labelsize=xtick_fontsize)
    
    ytick_fontsize = kwargs.get('ytick_fontsize', mpl.rcParams['ytick.labelsize'])
    ax.tick_params(axis='y', which='both', labelsize=ytick_fontsize)

    show_xaxis = kwargs.get('show_xaxis', True)
    if show_xaxis==False:
        ax.spines['bottom'].set_visible(False)
        
    show_top_spine = kwargs.get('show_top_spine', False)
    if show_top_spine==True:
        ax.spines['top'].set_visible(True)

    show_right_spine = kwargs.get('show_right_spine', False)
    if show_right_spine==True:
        ax.spines['right'].set_visible(True)