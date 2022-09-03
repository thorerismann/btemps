c.columns = c.columns.map(''.join)
c.reset_index(inplace=True,drop = False)

cum_cols = [x for x in c.columns if "cum" in x]
dif_cols = [x for x in c.columns if "dif" in x]
cum = cum_cols
cum.append("md")
dif = dif_cols
dif.append("md")
data_cum = c[cum].copy()
data_dif = c[dif].copy()

data_c = data_cum.melt(id_vars=['md'], value_vars=cum_cols,var_name = "aws-lcd station pair",value_name="cumulative difference")

data_c['day'] = data_c.md.dt.to_period('d')

data_dif.set_index('md',inplace=True)
hourly = data_dif.resample(rule='h').agg([np.mean, np.std])
hourly.reset_index(inplace=True,drop =False)
hourly.columns = hourly.columns.map(''.join)
log_cols = [x for x in hourly.columns if "TEMP" in x]
loggers = len(log_cols)
hourly['h'] = hourly.md.dt.strftime('%H')
maxl = ["max"]*loggers
minl = ["min"]*loggers
meanl = ["mean"]*loggers
varl = ["var"]*loggers
max_ = dict(zip(log_cols,maxl))
min_ = dict(zip(log_cols,minl))
mean_ = dict(zip(log_cols,meanl))
var_ = dict(zip(log_cols,varl))
hourly_ = hourly.groupby(['h']).agg(mean_)
means = [x for x in hourly_.columns if 'mean' in x]
stds = [x for x in hourly_.columns if 'std' in x]
hourly_m = hourly_[means]
hourly_m.reset_index(inplace=True, drop = False)
to_graph = hourly_m.melt(id_vars=['h'], value_vars=means,var_name = "aws-lcd station pair",value_name="mean hourly differences")