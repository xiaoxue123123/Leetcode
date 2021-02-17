year = 1
month = 3000
base = 20000
month_increase = 0.04

import pandas as pd
df = pd.DataFrame(columns=('year','total','net_gain','yearly_net_gain'))
for year in range(1,11):
    year = year
    total = (month+base)*(1+month_increase)**(year*12)
    total_last_year = ((year-1)*12*month+base)*(1+month_increase)**((year-1)*12)
    net_gain = total-(year*12*month+base)
    yearly_net_gain = total-total_last_year-(12*3000)
    df.loc[year-1] = [round(x,0) for x in [year,total,net_gain,yearly_net_gain]]
   # print('year #{}'.format(year))
    #print('total is {},\n net_gain is {},\n yearly net gain is {}'.format(r,net_gain,yearly_net_gain))