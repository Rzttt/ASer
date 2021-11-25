from app import db_deal_

name = '「Fate/Zero」开播十周年纪念插画介绍PV公开'

n = db_deal_.get_new_by_name(name)
print(n)