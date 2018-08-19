def convert_percentage(series):
        return series/series.sum()

def get_p_value(df, predictor, outcome):
    """Input: df, predictor column, outcome column. Returns p-value."""
    pt = pd.crosstab(df[predictor], df[outcome])
    return round(stat.chi2_contingency(pt)[1],4)

def produce_p_table(df, predictor, outcome):
    """Takes a df, the name of the predictor column and the name of the outcome 
       column and produced a table of p-values for pairwise hypothesis testing."""

    categories = df[predictor].dropna().unique()
    eth_outer = []
    for cat1 in categories:
        eth_inner = []  
        for cat2 in categories:
            if cat1 == cat2:
                # you cannot test against yourself
                eth_inner.append(np.nan)
            else:
                df_subset = df[df[predictor].isin([cat1, cat2])].copy()
                df_subset[predictor] = df_subset[predictor].astype(str)
                p = get_p_value(df_subset, predictor, outcome)
                eth_inner.append(p)
        eth_outer.append(eth_inner)
    return pd.DataFrame(eth_outer, columns = categories, index = categories)

def plot_p_table(df, predictor, outcome, p-value=0.05, annot=True):
    """Takes a df, the name of the predictor column and the name of the outcome 
       column, and a p-value and produces a visualization of the pairwise p-values of 
       the outcomes. They appear red if correlated, blue if not. """ 
    import seaborn as sea
    my_cmap = sea.diverging_palette(20, 220, sep=20, as_cmap=True)
    ptab = produce_p_table(df, predictor, outcome)
    sea.heatmap(ptab, center=p-value, annot = annot, linewidth=0.5, vmin=0.0, vmax=0.1, cmap=my_cmap)
    plt.title('Correlation - p-value', fontsize = 16)
    plt.show()
