import geopandas as gpd
import pandas as pd
import numpy as np

#path='C:/Users/Yijun Ma/Desktop/D/DOCUMENT/DCP2020/DCAS/'
path='/home/mayijun/DCAS/'

osm=gpd.read_file(path+'osm.geojson')
osm.crs={'init':'epsg:4326'}
osm=osm.to_crs({'init':'epsg:6539'})
osm=osm[['osmwayid','osmstartnodeid','osmendnodeid','osmname','osmhighway','geometry']].reset_index(drop=True)
osm['length']=[x.length for x in osm['geometry']]
osm=osm.to_crs({'init':'epsg:4326'})
bk=gpd.read_file(path+'quadstatebk.shp')
bk.crs={'init':'epsg:4326'}
bk=bk[['blockid','geometry']].reset_index(drop=True)
osm=gpd.sjoin(osm,bk,how='inner',op='intersects')
osm=osm[['osmwayid','osmstartnodeid','osmendnodeid','osmname','osmhighway','length','blockid','geometry']].reset_index(drop=True)
osm.to_file(path+'osm.shp')

#q1=pd.read_csv(path+'movement-speeds-quarterly-by-hod-new-york-2019-Q1.csv',dtype=float,converters={'segment_id':str,
#                                                                                                    'start_junction_id':str,
#                                                                                                    'end_junction_id':str})
#q1=q1[['osm_way_id','osm_start_node_id','osm_end_node_id','hour_of_day','speed_mph_mean']].reset_index(drop=True)
#q1.columns=['osmwayid','osmstartnodeid','osmendnodeid','hod','meanq1']
#
#q2=pd.read_csv(path+'movement-speeds-quarterly-by-hod-new-york-2019-Q2.csv',dtype=float,converters={'segment_id':str,
#                                                                                                    'start_junction_id':str,
#                                                                                                    'end_junction_id':str})
#q2=q2[['osm_way_id','osm_start_node_id','osm_end_node_id','hour_of_day','speed_mph_mean']].reset_index(drop=True)
#q2.columns=['osmwayid','osmstartnodeid','osmendnodeid','hod','meanq2']
#
#q3=pd.read_csv(path+'movement-speeds-quarterly-by-hod-new-york-2019-Q3.csv',dtype=float,converters={'segment_id':str,
#                                                                                                    'start_junction_id':str,
#                                                                                                    'end_junction_id':str})
#q3=q3[['osm_way_id','osm_start_node_id','osm_end_node_id','hour_of_day','speed_mph_mean']].reset_index(drop=True)
#q3.columns=['osmwayid','osmstartnodeid','osmendnodeid','hod','meanq3']
#
#
#dcas=pd.merge(q1,q2,how='inner',on=['osmwayid','osmstartnodeid','osmendnodeid','hod'])
#dcas['mean']=np.nanmean(dcas[['meanq1','meanq2']],axis=1)
#dcas=pd.merge(osm,dcas,how='inner',on=['osmwayid','osmstartnodeid','osmendnodeid'])
#dcas=dcas[dcas['hod']==8].reset_index(drop=True)
#
#dcas.to_file(path+'dcas.shp')



#osm=gpd.read_file(path+'osm.shp')
#
#ct=gpd.read_file(path+'quadstatect.shp')
#ct.crs={'init':'epsg:4326'}
#ct=ct[['tractid','geometry']].reset_index(drop=True)
#osm=gpd.sjoin(osm,ct,how='inner',op='intersects')
