def func(x):
  d={}
  d['min'] = x['curAmt'].min()
  d['max'] = x['curAmt'].max()
  d['diff'] = d['max'] - d['min'] 
  return pd.Series(d, index=['min', 'max', 'diff'])

minmax = data.groupby('npayCd').apply(func)
minmax = minmax.reset_index()

minmax = pd.merge(minmax, df, how='right', on='npayCd')
minmax = minmax.sort_values(by='diff', ascending=False)

bigdiff = minmax.head(100)['npayCd']
bigdiff = bigdiff.to_list()
bigdiff = data[data['npayCd'].isin(bigdiff)]

def func(x):
  d={}
  # d['max'] = x['maxAmt'].max() sgguCdNm
  d['maxykiho'] = x.sort_values(by='maxAmt', ascending=False).iloc[0]['ykiho']
  d['maxsgguCdNm'] = x.sort_values(by='maxAmt', ascending=False).iloc[0]['sgguCdNm']

  d['maxyadmNm'] = x.sort_values(by='maxAmt', ascending=False).iloc[0]['yadmNm']
  d['maxAmt'] = x.sort_values(by='maxAmt', ascending=False).iloc[0]['maxAmt']

  d['minykiho'] = x.sort_values(by='maxAmt', ascending=True).iloc[0]['ykiho']
  d['minsgguCdNm'] = x.sort_values(by='maxAmt', ascending=True).iloc[0]['sgguCdNm']

  d['minyadmNm'] = x.sort_values(by='minAmt', ascending=True).iloc[0]['yadmNm']
  d['minAmt'] = x.sort_values(by='minAmt', ascending=True).iloc[0]['minAmt']

  return pd.Series(d, index=['maxykiho', 'maxsgguCdNm', 'maxyadmNm', 'maxAmt', 'minykiho','minsgguCdNm', 'minyadmNm', 'minAmt'])

bigdiffNm = bigdiff.groupby('npayCd').apply(func)
bigdiffNm = bigdiffNm.reset_index()

bigdiffNm = pd.merge(bigdiffNm, df, how='inner', on='npayCd')
bigdiffNm['diff'] = bigdiffNm['maxAmt'] - bigdiffNm['minAmt']

bigdiffNm = bigdiffNm[['npayCd', 'npayCdNm', 'diff', 'maxykiho', 'maxsgguCdNm', 'maxyadmNm', 'maxAmt', 'minykiho','minsgguCdNm', 'minyadmNm', 'minAmt']]
bigdiffNm = bigdiffNm.sort_values('diff', ascending=False)

bigdiffNm.to_csv('진료비 차이가 큰 비급여진료항목 상위100개와 해당병원', encoding='UTF-8')
