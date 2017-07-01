
import os.path
import csv
import os
import subprocess
import pandas as pd
if not os.path.exists('US'):
    os.makedirs('US')

f = open('users.csv', 'rb')
reader = csv.reader(f)
states=set()
statesAndId={}
for row in reader:
    #print row
    states.add(row[3])
f.close()
print states
statesAndId['AL']='01'
statesAndId['AK']='02'
statesAndId['AZ']='04'
statesAndId['AR']='05'
statesAndId['CA']='06'
statesAndId['CO']='08'
statesAndId['CT']='09'
statesAndId['DE']='10'
statesAndId['DC']='11'
statesAndId['FL']='12'
statesAndId['GA']='13'
statesAndId['HI']='15'
statesAndId['ID']='16'
statesAndId['IL']='17'
statesAndId['IN']='18'
statesAndId['IA']='19'
statesAndId['KS']='20'
statesAndId['KY']='21'
statesAndId['LA']='22'
statesAndId['ME']='23'
statesAndId['MD']='24'
statesAndId['MA']='25'
statesAndId['MI']='26'
statesAndId['MN']='27'
statesAndId['MS']='28'
statesAndId['MO']='29'
statesAndId['MT']='30'
statesAndId['NE']='31'
statesAndId['NV']='32'
statesAndId['NH']='33'
statesAndId['NJ']='34'
statesAndId['NM']='35'
statesAndId['NY']='36'
statesAndId['NC']='37'
statesAndId['ND']='38'
statesAndId['OH']='39'
statesAndId['OK']='40'
statesAndId['OR']='41'
statesAndId['PA']='42'
statesAndId['RI']='44'
statesAndId['SC']='45'
statesAndId['SD']='46'
statesAndId['TN']='47'
statesAndId['TX']='48'
statesAndId['UT']='49'
statesAndId['VT']='50'
statesAndId['VA']='51'
statesAndId['WA']='53'
statesAndId['WV']='54'
statesAndId['WI']='55'
statesAndId['WY']='56'
statesAndId['PR']='72'
set(['WA', 'DE', 'DC', 'WI', 'WV', 'HI', 'FL', 'WY', 'NH', 'NJ', 'NM', 'TX', 'LA', 'NC', 'ND', 'NE', 'TN', 'NY', 'PA', 'AK', 'NV', 'VA', 'CO', 'CA', 'AL', 'AR', 'VT', 'IL', 'GA', 'IN', 'IA', 'OK', 'AZ', 'ID', 'CT', 'ME', 'MD', 'MA', 'OH', 'UT', 'MO', 'MN', 'MI', 'RI', 'KS', 'MT', 'MS', 'PR', 'SC', 'KY', 'OR', 'SD'])

for s in states:
    if not os.path.exists('US/'+s):
        os.makedirs('US/'+s)

for i in states:
    if os.path.exists('all_040_in_'+statesAndId[i]+'.P12A.csv'):
        os.remove('all_040_in_'+statesAndId[i]+'.P12A.csv')
    data_url='http://censusdata.ire.org/'+statesAndId[i]+'/all_040_in_'+statesAndId[i]+'.P12A.csv'
    data_white=pd.read_csv(data_url)
    data_white.to_csv('US/'+i+'/all_040_in_'+statesAndId[i]+'.P12A.csv')
    
    'SS/all_LLL_in_SS.TT'

for i in states:
    if os.path.exists('all_040_in_'+statesAndId[i]+'.P12B.csv'):
        os.remove('all_040_in_'+statesAndId[i]+'.P12B.csv')
    data_url='http://censusdata.ire.org/'+statesAndId[i]+'/all_040_in_'+statesAndId[i]+'.P12B.csv'
    data_black=pd.read_csv(data_url)
    data_black.to_csv('US/'+i+'/all_040_in_'+statesAndId[i]+'.P12B.csv')

for i in states:
    if os.path.exists('all_040_in_'+statesAndId[i]+'.P12D.csv'):
        os.remove('all_040_in_'+statesAndId[i]+'.P12D.csv')
    data_url='http://censusdata.ire.org/'+statesAndId[i]+'/all_040_in_'+statesAndId[i]+'.P12D.csv'
    data_asian=pd.read_csv(data_url)
    data_asian.to_csv('US/'+i+'/all_040_in_'+statesAndId[i]+'.P12D.csv')

for i in states:
    if os.path.exists('all_040_in_'+statesAndId[i]+'.P12H.csv'):
        os.remove('all_040_in_'+statesAndId[i]+'.P12H.csv')
    data_url='http://censusdata.ire.org/'+statesAndId[i]+'/all_040_in_'+statesAndId[i]+'.P12H.csv'
    data_latino=pd.read_csv(data_url)
    data_latino.to_csv('US/'+i+'/all_040_in_'+statesAndId[i]+'.P12H.csv')

census_summary_url = "/Dataset-CUBE/census_summary.csv"
census_summary = pd.read_csv(census_summary_url)

for i in states:
    data_url='US/'+i+'/all_040_in_'+statesAndId[i]+'.P12A.csv'
    data_white=pd.read_csv(data_url)
    data_url='US/'+i+'/all_040_in_'+statesAndId[i]+'.P12B.csv'
    data_black=pd.read_csv(data_url)
    data_url='US/'+i+'/all_040_in_'+statesAndId[i]+'.P12D.csv'
    data_asian=pd.read_csv(data_url)
    data_url='US/'+i+'/all_040_in_'+statesAndId[i]+'.P12H.csv'
    data_latino=pd.read_csv(data_url)
    
    census_summary[i][0]=data_white['P012A006']
    census_summary[i][1]=data_white['P012A030']
    census_summary[i][2]=data_white['P012A007']+data_white['P012A008']+data_white['P012A009']
    census_summary[i][3]=data_white['P012A031']+data_white['P012A032']+data_white['P012A033']
    census_summary[i][4]=data_white['P012A010']
    census_summary[i][5]=data_white['P012A034']
    census_summary[i][6]=data_white['P012A011']
    census_summary[i][7]=data_white['P012A035']
    census_summary[i][8]=data_white['P012A012']
    census_summary[i][9]=data_white['P012A036']
    census_summary[i][10]=data_white['P012A013']
    census_summary[i][11]=data_white['P012A037']
    census_summary[i][12]=data_white['P012A014']
    census_summary[i][13]=data_white['P012A038']
    census_summary[i][14]=data_white['P012A015']
    census_summary[i][15]=data_white['P012A039']
    census_summary[i][16]=data_white['P012A016']
    census_summary[i][17]=data_white['P012A040']
    census_summary[i][18]=data_white['P012A017']
    census_summary[i][19]=data_white['P012A041']
    census_summary[i][20]=data_white['P012A018']+data_white['P012A019']
    census_summary[i][21]=data_white['P012A042']+data_white['P012A043']
    census_summary[i][22]=data_white['P012A020']+data_white['P012A021']
    census_summary[i][23]=data_white['P012A044']+data_white['P012A045']
    
    census_summary[i][24]=data_black['P012B006']
    census_summary[i][25]=data_black['P012B030']
    census_summary[i][26]=data_black['P012B007']+data_black['P012B008']+data_black['P012B009']
    census_summary[i][27]=data_black['P012B031']+data_black['P012B032']+data_black['P012B033']
    census_summary[i][28]=data_black['P012B010']
    census_summary[i][29]=data_black['P012B034']
    census_summary[i][30]=data_black['P012B011']
    census_summary[i][31]=data_black['P012B035']
    census_summary[i][32]=data_black['P012B012']
    census_summary[i][33]=data_black['P012B036']
    census_summary[i][34]=data_black['P012B013']
    census_summary[i][35]=data_black['P012B037']
    census_summary[i][36]=data_black['P012B014']
    census_summary[i][37]=data_black['P012B038']
    census_summary[i][38]=data_black['P012B015']
    census_summary[i][39]=data_black['P012B039']
    census_summary[i][40]=data_black['P012B016']
    census_summary[i][41]=data_black['P012B040']
    census_summary[i][42]=data_black['P012B017']
    census_summary[i][43]=data_black['P012B041']
    census_summary[i][44]=data_black['P012B018']+data_black['P012B019']
    census_summary[i][45]=data_black['P012B042']+data_black['P012B043']
    census_summary[i][46]=data_black['P012B020']+data_black['P012B021']
    census_summary[i][47]=data_black['P012B044']+data_black['P012B045']
    
    census_summary[i][48]=data_asian['P012D006']
    census_summary[i][49]=data_asian['P012D030']
    census_summary[i][50]=data_asian['P012D007']+data_asian['P012D008']+data_asian['P012D009']
    census_summary[i][51]=data_asian['P012D031']+data_asian['P012D032']+data_asian['P012D033']
    census_summary[i][52]=data_asian['P012D010']
    census_summary[i][53]=data_asian['P012D034']
    census_summary[i][54]=data_asian['P012D011']
    census_summary[i][55]=data_asian['P012D035']
    census_summary[i][56]=data_asian['P012D012']
    census_summary[i][57]=data_asian['P012D036']
    census_summary[i][58]=data_asian['P012D013']
    census_summary[i][59]=data_asian['P012D037']
    census_summary[i][60]=data_asian['P012D014']
    census_summary[i][61]=data_asian['P012D038']
    census_summary[i][62]=data_asian['P012D015']
    census_summary[i][63]=data_asian['P012D039']
    census_summary[i][64]=data_asian['P012D016']
    census_summary[i][65]=data_asian['P012D040']
    census_summary[i][66]=data_asian['P012D017']
    census_summary[i][67]=data_asian['P012D041']
    census_summary[i][68]=data_asian['P012D018']+data_asian['P012D019']
    census_summary[i][69]=data_asian['P012D042']+data_asian['P012D043']
    census_summary[i][70]=data_asian['P012D020']+data_asian['P012D021']
    census_summary[i][71]=data_asian['P012D044']+data_asian['P012D045']
    
    census_summary[i][72]=data_latino['P012H006']
    census_summary[i][73]=data_latino['P012H030']
    census_summary[i][74]=data_latino['P012H007']+data_latino['P012H008']+data_latino['P012H009']
    census_summary[i][75]=data_latino['P012H031']+data_latino['P012H032']+data_latino['P012H033']
    census_summary[i][76]=data_latino['P012H010']
    census_summary[i][77]=data_latino['P012H034']
    census_summary[i][78]=data_latino['P012H011']
    census_summary[i][79]=data_latino['P012H035']
    census_summary[i][80]=data_latino['P012H012']
    census_summary[i][81]=data_latino['P012H036']
    census_summary[i][82]=data_latino['P012H013']
    census_summary[i][83]=data_latino['P012H037']
    census_summary[i][84]=data_latino['P012H014']
    census_summary[i][85]=data_latino['P012H038']
    census_summary[i][86]=data_latino['P012H015']
    census_summary[i][87]=data_latino['P012H039']
    census_summary[i][88]=data_latino['P012H016']
    census_summary[i][89]=data_latino['P012H040']
    census_summary[i][90]=data_latino['P012H017']
    census_summary[i][91]=data_latino['P012H041']
    census_summary[i][92]=data_latino['P012H018']+data_latino['P012H019']
    census_summary[i][93]=data_latino['P012H042']+data_latino['P012H043']
    census_summary[i][94]=data_latino['P012H020']+data_latino['P012H021']
    census_summary[i][95]=data_latino['P012H044']+data_latino['P012H045']
    

for i in range(0,len(census_summary)):
    census_summary['tot'][i]=0
    for s in states:
        census_summary['tot'][i]+=census_summary[s][i]


census_summary.to_csv('/Dataset-CUBE/census_summary.csv')

 