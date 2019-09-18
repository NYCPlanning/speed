import geopandas as gpd
import pandas as pd
import numpy as np

path='D:/BOSTON RD/TRANSPORTATION/MAP/UBER/'

osm=gpd.read_file(path+'osm.geojson')

osmseg=pd.read_csv(path+'movement-segments-to-osm-ways-new-york-2018.csv',dtype=str,converters={'osm_way_id':float})
osmseg['segment_id']=[' '.join(x.split()) for x in osmseg['segment_id']]

osmnode=pd.read_csv(path+'movement-junctions-to-osm-nodes-new-york-2018.csv',dtype=str,converters={'osm_node_id':float})
osmnode['junction_id']=[' '.join(x.split()) for x in osmnode['junction_id']]

q1=pd.read_csv(path+'movement-speeds-quarterly-by-hod-new-york-2018-Q1.csv',dtype=float,converters={'segment_id':str,
                                                                                                    'start_junction_id':str,
                                                                                                    'end_junction_id':str})
q1['segment_id']=[' '.join(x.split()) for x in q1['segment_id']]
q1['start_junction_id']=[' '.join(x.split()) for x in q1['start_junction_id']]
q1['end_junction_id']=[' '.join(x.split()) for x in q1['end_junction_id']]
q1=q1.loc[q1['hour_of_day']==17,['segment_id','start_junction_id','end_junction_id','speed_mph_mean','speed_mph_p50']].reset_index(drop=True)
q1=pd.merge(q1,osmseg,how='left',left_on='segment_id',right_on='segment_id')
q1=pd.merge(q1,osmnode,how='left',left_on='start_junction_id',right_on='junction_id')
q1=pd.merge(q1,osmnode,how='left',left_on='end_junction_id',right_on='junction_id')
q1=q1[['osm_way_id','osm_node_id_x','osm_node_id_y','speed_mph_mean','speed_mph_p50']].reset_index(drop=True)
q1.columns=['osmwayid','osmstartnode','osmendnode','speedmeanq1','speedmedianq1']

q2=pd.read_csv(path+'movement-speeds-quarterly-by-hod-new-york-2018-Q2.csv',dtype=float,converters={'segment_id':str,
                                                                                                    'start_junction_id':str,
                                                                                                    'end_junction_id':str})
q2['segment_id']=[' '.join(x.split()) for x in q2['segment_id']]
q2['start_junction_id']=[' '.join(x.split()) for x in q2['start_junction_id']]
q2['end_junction_id']=[' '.join(x.split()) for x in q2['end_junction_id']]
q2=q2.loc[q2['hour_of_day']==17,['segment_id','start_junction_id','end_junction_id','speed_mph_mean','speed_mph_p50']].reset_index(drop=True)
q2=pd.merge(q2,osmseg,how='left',left_on='segment_id',right_on='segment_id')
q2=pd.merge(q2,osmnode,how='left',left_on='start_junction_id',right_on='junction_id')
q2=pd.merge(q2,osmnode,how='left',left_on='end_junction_id',right_on='junction_id')
q2=q2[['osm_way_id','osm_node_id_x','osm_node_id_y','speed_mph_mean','speed_mph_p50']].reset_index(drop=True)
q2.columns=['osmwayid','osmstartnode','osmendnode','speedmeanq2','speedmedianq2']

q3=pd.read_csv(path+'movement-speeds-quarterly-by-hod-new-york-2018-Q3.csv',dtype=float,converters={'segment_id':str,
                                                                                                    'start_junction_id':str,
                                                                                                    'end_junction_id':str})
q3['segment_id']=[' '.join(x.split()) for x in q3['segment_id']]
q3['start_junction_id']=[' '.join(x.split()) for x in q3['start_junction_id']]
q3['end_junction_id']=[' '.join(x.split()) for x in q3['end_junction_id']]
q3=q3.loc[q3['hour_of_day']==17,['segment_id','start_junction_id','end_junction_id','speed_mph_mean','speed_mph_p50']].reset_index(drop=True)
q3=pd.merge(q3,osmseg,how='left',left_on='segment_id',right_on='segment_id')
q3=pd.merge(q3,osmnode,how='left',left_on='start_junction_id',right_on='junction_id')
q3=pd.merge(q3,osmnode,how='left',left_on='end_junction_id',right_on='junction_id')
q3=q3[['osm_way_id','osm_node_id_x','osm_node_id_y','speed_mph_mean','speed_mph_p50']].reset_index(drop=True)
q3.columns=['osmwayid','osmstartnode','osmendnode','speedmeanq3','speedmedianq3']

q4=pd.read_csv(path+'movement-speeds-quarterly-by-hod-new-york-2018-Q4.csv',dtype=float,converters={'segment_id':str,
                                                                                                    'start_junction_id':str,
                                                                                                    'end_junction_id':str})
q4['segment_id']=[' '.join(x.split()) for x in q4['segment_id']]
q4['start_junction_id']=[' '.join(x.split()) for x in q4['start_junction_id']]
q4['end_junction_id']=[' '.join(x.split()) for x in q4['end_junction_id']]
q4=q4.loc[q4['hour_of_day']==17,['segment_id','start_junction_id','end_junction_id','speed_mph_mean','speed_mph_p50']].reset_index(drop=True)
q4=pd.merge(q4,osmseg,how='left',left_on='segment_id',right_on='segment_id')
q4=pd.merge(q4,osmnode,how='left',left_on='start_junction_id',right_on='junction_id')
q4=pd.merge(q4,osmnode,how='left',left_on='end_junction_id',right_on='junction_id')
q4=q4[['osm_way_id','osm_node_id_x','osm_node_id_y','speed_mph_mean','speed_mph_p50']].reset_index(drop=True)
q4.columns=['osmwayid','osmstartnode','osmendnode','speedmeanq4','speedmedianq4']

uber=pd.merge(osm,q1,how='left',on=['osmwayid','osmstartnode','osmendnode'])
uber=pd.merge(uber,q2,how='left',on=['osmwayid','osmstartnode','osmendnode'])
uber=pd.merge(uber,q3,how='left',on=['osmwayid','osmstartnode','osmendnode'])
uber=pd.merge(uber,q4,how='left',on=['osmwayid','osmstartnode','osmendnode'])
uber['speedmean2018']=np.nanmean(uber[['speedmeanq1','speedmeanq2','speedmeanq3','speedmeanq4']],axis=1)
uber['speedmedian2018']=np.nanmedian(uber[['speedmedianq1','speedmedianq2','speedmedianq3','speedmedianq4']],axis=1)
uber=uber[['osmwayid','osmstartnode','osmendnode','osmname','osmhighway','osmoneway','speedmeanq1','speedmeanq2','speedmeanq3',
           'speedmeanq4','speedmean2018','speedmedianq1','speedmedianq2','speedmedianq3','speedmedianq4','speedmedian2018','geometry']]
uber.to_file(path+'boston.shp')

