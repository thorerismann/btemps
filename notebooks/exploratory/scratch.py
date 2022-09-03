# copy this code into the 1.2 measurement classes jupyter notebook to use the archival data.
class OpenSensors(Sensors):    
    def get_day(self):
        x = self.data
        x['day'] = x.md.dt.to_period("d")
        return x
    def get_mean(self,time):
        x = self.data
        data = x.groupby([time]).agg('mean')
        a = [x for x in data.columns if x[:3] == "val"]
        data[self.name] = data[a]
        return data[[self.name]]
    def get_max(self,time):
        x = self.data
        data = x.groupby([time]).agg('max')
        a = [x for x in data.columns if x[:3] == "val"]
        data[self.name] = data[a]
        return data[[self.name]]
    def get_min(self,time):
        x = self.data
        data = x.groupby([time]).agg('min')
        a = [x for x in data.columns if x[:3] == "val"]
        data[self.name] = data[a]
        return data[[self.name]]
    def get_var(self,time):
        x = self.data
        data = x.groupby([time]).agg('var')
        a = [x for x in data.columns if x[:3] == "val"]
        data[self.name] = data[a]
        return data[[self.name]]

# this corresponds to the archive 1983 data
class archive_Sensors(Sensors):
    
    ## basic stats functions
    def get_mean(self):
        data = self.data
        a = [x for x in data.columns if x[:3] == "mea"]
        data.set_index('month',inplace=True,drop=False)
        return data[a]
    def get_max(self):
        data = self.data
        a = [x for x in data.columns if x[:3] == "max"]
        data.set_index('month',inplace=True,drop=False)
        return data[a]
    def get_min(self):
        data = self.data
        a = [x for x in data.columns if x[:3] == "min"]
        data.set_index('month',inplace=True,drop=False)
        return data[a]

# read in archive_ sensors
#elevation = {'mai':720, 'vog':544, 'boz':441}
#coord = {'mai':(47.145999,7.242621), 'vog': (47.12456,7.242723), 'boz': (47.15189,7.272195)}
#city = {'mai':'evilard', 'vog':'biel', 'boz':'biel'}

#lgm = [ x for x in archive_.columns if "mai" in x]
#lgv = [ x for x in archive_.columns if "vog" in x]
#lgb = [ x for x in archive_.columns if "boz" in x]
#lgm.append('md')
#lgv.append('md')
#lgb.append('md')

#cols = [lgm,lgv,lgb]

#mylist = []
#for i in cols:
#    data = archive_[i].copy()
#    if 'mai' in i[0]:
#        key = 'mai'
#        mylist.append(archive_Sensors('archive_',1983,key,city[key],'lcd',data,'Temperature',elevation[key],coord[key]))
#    elif 'boz' in i[0]:
#        key = 'boz'
#        mylist.append(archive_Sensors('archive_',1983,key,city[key],'lcd',data,'Temperature',elevation[key],coord[key]))
#    elif 'vog' in i[0]:
#        key = 'vog'
#       mylist.append(archive_Sensors('archive_',1983,key,city[key],'lcd',data,'Temperature',elevation[key],coord[key]))
#archival = mylist


# checking dict keys
#a = data_be.columns
#b = data_be_meta.index
#mylist = []
#for x in a:
#    if x not in b:
#        mylist.append(x)
#    else:
#        mylist.append("OK")

# read in Biel Sensors
elevation= {"Log_202":430, "Log_201":432,"Log_203":433,"Log_204":430,"Log_205":439,"Log_206":437,"Log_207":430}
coord= {"Log_202":(47.130669,7.236258), "Log_201":(47.130792,7.241046),"Log_203": (47.136637, 7.246960),"Log_204":(47.141086,7.253485),"Log_205":(47.144746,7.265149),"Log_206":(47.138338,7.295326),"Log_207":(47.179081,7.415102)}
city= {"Log_202":'Biel', "Log_201":'Biel',"Log_203":'Biel',"Log_204":'Biel',"Log_205":'Biel',"Log_206":'Orpund',"Log_207":'Grenchen'}

log_cols = [ x for x in data_lcd.columns if x[:3] == "Log" ]

mylist = []
for i in log_cols:
    data = data_lcd[['md',i]].copy()
    mylist.append(LowCostSensors('biel-temps',2022,i,city[i],'lcd',data,'Temperature',elevation[i],coord[i]))
biel_sensors = mylist

# read in opensensor
#os_1 = OpenSensors('OpenSense',2022,'Gumme Brügg','Brügg','custom',data_os,'Temperature',469,(47.126465,7.285249))

# Data from Biel July 2022
#data_lcd = pd.read_csv(F'{writedir}/alldata.csv')

# data from closesent OpenSenseMap sensor (Brügg) here: https://familie-hoffmann.me/ 
# data_os = pd.read_csv(F'{extdir}/opensense-temp.csv')

# archival mean data 1983
#archive_ = pd.read_csv(F"{writedir}/archive_1983.csv")
#archive_.drop(['Unnamed: 0'],axis=1,inplace=True)



# key names that describe the choice
# load dictionary

#data_os['time_int'] = data_os.createdAt.apply(lambda x: fix_date_string(x))
#data_os['md'] = pd.to_datetime(data_os.time_int,format = '%Y/%m/%d %H:%M:%S')
#data_lcd["md"] = pd.to_datetime(data_lcd.time,format = '%Y/%m/%d %H:%M:%S')
#archive_['md'] = pd.to_datetime(archive_['index'], infer_datetime_format=True)
