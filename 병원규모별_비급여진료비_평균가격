data.groupby('clCdNm')['npayCd'].count() 
# 각 병원 종류마다 비급여 진료를 얼마나 하는지? 

병원       83654
상급종합     26252
요양병원     23748
의원      481883
정신병원      3774
종합병원     73236
치과병원      5167
치과의원    159777
한방병원     14224
한의원      92046

# 의원이 압도적으로 많고, 그 다음 치과의원, 한의원, 병원, 종합병원 순
# 일단 상위 5개 항목으로 데이터를 정리해보도록 한다. 추후에 추가할 수 있음

data_uiwon = data[data['clCdNm']=='의원']
data_chigwa = data[data['clCdNm']=='치과의원']
data_hanuiwon = data[data['clCdNm']=='한의원']
data_byeongwon = data[data['clCdNm']=='병원']
data_jonghab = data[data['clCdNm']=='종합병원']

# npayCd(비급여코드)랑 npayCdNm(비급여코드이름)만 추출한 데이터프레임 만들어놓기
df = pd.DataFrame({'npayCd': data['npayCd'].unique() ,
                   'npayCdNm': data['npayCdNm'].unique()})

# groupby(npayCdNm)해서 curAmt의 평균을 구한 다음 새 dataframe으로 만들기 -> 규모별로 따로 진행
def func(x):
  d={}
  d['mean'] = x['curAmt'].mean()
  return pd.Series(d, index=['mean'])

#의원: 473개 항목
uiwon_npayCd = data_uiwon.groupby(['npayCd']).apply(func)
uiwon_npayCd = uiwon_npayCd.reset_index()
uiwon_npayCd.rename(columns= {'mean':'의원'}, inplace=True)
uiwon_npayCd

#치과: 63개 항목
chigwa_npayCd = data_chigwa.groupby(['npayCd']).apply(func)
chigwa_npayCd = chigwa_npayCd.reset_index()
chigwa_npayCd.rename(columns= {'mean':'치과의원'}, inplace=True)
chigwa_npayCd

#한의원: 46개 항목
hanuiwon_npayCd = data_hanuiwon.groupby(['npayCd']).apply(func)
hanuiwon_npayCd = hanuiwon_npayCd.reset_index()
hanuiwon_npayCd.rename(columns= {'mean':'한의원'}, inplace=True)
hanuiwon_npayCd

#병원: 501개 항목
byeongwon_npayCd = data_byeongwon.groupby(['npayCd']).apply(func)
byeongwon_npayCd = byeongwon_npayCd.reset_index()
byeongwon_npayCd.rename(columns= {'mean':'병원'}, inplace=True)
byeongwon_npayCd

#종합병원: 518개 항목
jonghab_npayCd = data_jonghab.groupby(['npayCd']).apply(func)
jonghab_npayCd = jonghab_npayCd.reset_index()
jonghab_npayCd.rename(columns= {'mean':'종합병원'}, inplace=True)
jonghab_npayCd

# 규모별로 만든 데이터프레임을 npayCd를 기준으로 합치기
ckCdNm = pd.merge(uiwon_npayCd, chigwa_npayCd, how='outer', on='npayCd')
ckCdNm = pd.merge(ckCdNm, hanuiwon_npayCd, how='outer', on='npayCd')
ckCdNm = pd.merge(ckCdNm, byeongwon_npayCd , how='outer', on='npayCd')
ckCdNm = pd.merge(ckCdNm, jonghab_npayCd , how='outer', on='npayCd')

# 비급여진료 항목을 알 수 있게 df를 npayCd를 기준으로 합치기
ckCdNm = pd.merge(ckCdNm, df, how='right', on='npayCd')

ckCdNm.to_csv('병원규모별 비급여진료비 평균가격', encoding='UTF-8')
