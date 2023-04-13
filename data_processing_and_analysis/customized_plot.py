from decimal import Decimal
from scipy.stats import mannwhitneyu
from scipy.stats import ttest_ind
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def customise_plot(ax, args):
    ax.set_xlabel(args.xlab) 
    ax.set_ylabel(args.ylab)
    ax.xaxis.grid(args.xaxis_grid, linewidth=0.5) if args.xaxis_grid else ax.xaxis.grid(args.xaxis_grid)
    ax.yaxis.grid(args.yaxis_grid, linewidth=0.5) if args.yaxis_grid else ax.yaxis.grid(args.yaxis_grid)
    

def draw_swarmBoxPlot(dataframe, study, ax, args, order, test='Mann-Whitney', additional_height =  0.075):
    dataframe = dataframe[['ValidationStatus', study]].dropna()
    sns.boxplot(x="ValidationStatus", y=study, data=dataframe, ax=ax,
                whis=np.inf, order=order, palette=args.palette)
    sns.swarmplot(x="ValidationStatus", y=study, data=dataframe, ax=ax, color=".2", order=order)
    
    box_pairs = [('Use with Caution', 'Valid')]
    
    p_value = get_pvalue_to_annotate(dataframe[dataframe['ValidationStatus'] == 'Valid'][study].dropna(), 
                                     dataframe[dataframe['ValidationStatus'] == 'Use with Caution'][study].dropna(), test)
    
    x1, x2 = 0, 1   # columns 'Sat' and 'Sun' (first column: 0, see plt.xticks())
    y, h, colour = dataframe[study].max() + additional_height, additional_height/3, 'k'
    ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=colour)
    ax.text((x1+x2)*.5, y+h+(additional_height/5), p_value, ha='center', va='bottom', color=colour)
   
    ax.set_title(args.title, weight='bold', y=1.05, size=14)    
    ax.set(ylim=args.ylim)
    
    customise_plot(ax, args)
    
def draw_dotplot(ax, x, y, data, order, hue, args, hue_order=None, jitter=0.1, xlim=(0.49, 0.75)):
    sns.stripplot(x=x, y=y, data=data, hue=hue, ax=ax, order=order, palette=args.palette, s=7, hue_order=hue_order,
                  jitter=jitter, alpha=0.85)
#     if(args.show_legend):
#         ax.legend(title=args.legend_title, title_fontsize='medium', facecolor='white', framealpha=1,
#                   bbox_to_anchor = args.anchor_legend_at)._legend_box.align = "left"
#     else: 
#         ax.legend().remove()
    if(args.ylab =='False'): 
        ax.set(yticklabels=[])
    ax.set_title(args.title, fontsize=12)
    ax.set(xlim=xlim)
    customise_plot(ax, args)
    
def get_pvalue_to_annotate(boxdata1, boxdata2, test='Mann-Whitney'):
    if(test == 'Mann-Whitney'):
        stat, P_val = mannwhitneyu(boxdata1, boxdata2, alternative='two-sided')
        test_str = "Mann-Whitney-Wilcoxon test two-sided"
    else:
        stat, P_val = ttest_ind(boxdata1, boxdata2, alternative='two-sided', equal_var=True)
        test_str = " t-test-individual two-sided with equal variance"
    
    print("Use with Caution v.s. Valid:" + test_str + ", P_val=" + str("{:.2E}".format(Decimal(P_val))) + " stat=", str("{:.2E}".format(Decimal(stat))))
    if(P_val <= 0.00001):
        P_val = "p <= 1e-05"
    elif(P_val > 0.001):
        P_val = "p = " + str(round(P_val, 3))
    elif(P_val > 0.0001):
        P_val = "p = " + str(round(P_val, 4))
    elif(P_val > 0.00001):
        P_val = "p = " + str(round(P_val, 5))
    return P_val
    
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
        ax.text(_x, _y, value,  {'fontsize': args.fontsize}, ha="left")
        i=i-1
    args.yaxis_grid = False
    customise_plot(ax, args)