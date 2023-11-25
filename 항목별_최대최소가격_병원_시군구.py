def func(x):
  d={}
  d['min'] = x['curAmt'].min()
  d['max'] = x['curAmt'].max()
  return pd.Series(d, index=['min', 'max', 'diff'])

minmax = data.groupby('npayCd').apply(func)
minmax = minmax.reset_index()
minmax = pd.merge(minmax, df, how='right', on='npayCd')
minmax = minmax.sort_values(by='diff', ascending=False)
