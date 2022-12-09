from statannot import add_stat_annotation
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def customise_plot(ax, args):
    ax.set_xlabel(args.xlab) 
    ax.set_ylabel(args.ylab)
    ax.xaxis.grid(args.xaxis_grid, linewidth=0.5) if args.xaxis_grid else ax.xaxis.grid(args.xaxis_grid)
    ax.yaxis.grid(args.yaxis_grid, linewidth=0.5) if args.yaxis_grid else ax.yaxis.grid(args.yaxis_grid)
    
def draw_swarmBoxPlot(dataframe, study, ax, args, order, test="Mann-Whitney"):
    dataframe = dataframe[['ValidationStatus', study]].dropna()
    sns.boxplot(x="ValidationStatus", y=study, data=dataframe, ax=ax,
                whis=np.inf, order=order, palette=args.palette)
    sns.swarmplot(x="ValidationStatus", y=study, data=dataframe, ax=ax, color=".2", order=order)

    box_pairs=[("Use with Caution", "Valid")]
    
    ax.set_title(args.title, weight='bold', y=1.05, size=14)
    test_results = add_stat_annotation(ax, data=dataframe, x="ValidationStatus", y=study, order=order,
                                       box_pairs = box_pairs, test=test, text_format='star', loc='inside', verbose=2)
    ax.set(ylim=args.ylim)
    
    customise_plot(ax, args)
    
def draw_countplot(antibody_validation_status, ax, args):
    df = pd.DataFrame(antibody_validation_status['ValidationStatus'].value_counts(sort = True)).reset_index().\
                                                             rename(columns={'ValidationStatus':'Count', 
                                                                             'index': 'ValidationStatus'})
    df['Percentage'] = round((df['Count']/df['Count'].sum())*100, 3)
    df = df.sort_values('ValidationStatus', ascending=False)
    
    df.replace('Use with Caution', 'Use with\nCaution', inplace=True)
    sns.barplot(data=df, y='ValidationStatus', x='Percentage', ax=ax, order=['Use with\nCaution', 'Valid'], palette=args.palette)
    space=.1
    i = 1
    for p in ax.patches:
        _x = p.get_x() + p.get_width() + float(space)
        _y = p.get_y() + p.get_height() - (p.get_height()*0.5)
        value = '({})'.format(df.loc[i, 'Count'])
        ax.text(_x, _y, value, ha="left")
        i=i-1
        customise_plot(ax, args)