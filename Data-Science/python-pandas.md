# Merge vs Join
pd.df.merge() and pd.df.join() are both implementations of the underlying pd.merge() function. df.merge() is the more general
of the two functions. There are three main differences between df.merge() and df.join():
1. Lookup on the right table:

    df1.join(df2) always uses the index of df2 to join. In contrast df1.merge(df2) can join on columns or using right_index=True on the index.
  
2. Lookup on the left table:
  
    df1.join(df2) joins on the index of df1 by default. This can be overwritten by df1.join(df2, on=key_or_keys).
    In contrast, df1.merge(df2) joins on one or multiple columns by default. This can be overwritten using df1.merge(df2, left_index=True).

3. Join:

    df1.join(df2) by default implements a left join, df1.merge(df2) by default implements an inner join. 
