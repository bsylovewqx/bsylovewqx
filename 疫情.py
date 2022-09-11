from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType
import requests
import json
res = json.loads(requests.get('http://www.dzyong.top:3005/yiqing/province/').text)
print(res)
province = [p['provinceName'] for p in res['data']]
val1 = [p['confirmedNum'] for p in res['data']]
val2 = [p['curesNum'] for p in res['data']]
val3 = [p['deathsNum'] for p in res['data']]
geo = Geo()
geo.add_schema(maptype="china")
geo.add(
    "geo",
    [list(z) for z in zip(province, val1)],
    type_=ChartType.EFFECT_SCATTER,
)

geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False, background_color='black', color='green'))
geo.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(is_piecewise=True, min_=0, max_=30000),
    title_opts=opts.TitleOpts(title="全国实时数据"))
geo.render('全国实时数据.html')
