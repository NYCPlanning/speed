import geopandas as gpd
import pandas as pd
import numpy as np

#path='C:/Users/Yijun Ma/Desktop/D/DOCUMENT/DCP2020/DCAS/'
path='/home/mayijun/DCAS/'

osm=gpd.read_file(path+'UBER/osm.geojson')
osm.crs={'init':'epsg:4326'}
osm=osm.to_crs({'init':'epsg:6539'})
osm=osm[['osmwayid','osmstartnodeid','osmendnodeid','osmhighway','geometry']].reset_index(drop=True)
osm.columns=['wayid','startnode','endnode','highway','geometry']
osm['length']=[x.length for x in osm['geometry']]
osm=osm.to_crs({'init':'epsg:4326'})
ct=gpd.read_file(path+'SHP/nycct.shp')
ct.crs={'init':'epsg:4326'}
ct.columns=['tract','geometry']
nta=gpd.read_file(path+'SHP/nta.shp')
nta.crs={'init':'epsg:4326'}
nta=nta[['NTACode','geometry']].reset_index(drop=True)
nta.columns=['nta','geometry']
community=gpd.read_file(path+'SHP/community.shp')
community.crs={'init':'epsg:4326'}
community.columns=['community','geometry']
council=gpd.read_file(path+'SHP/council.shp')
council.crs={'init':'epsg:4326'}
council.columns=['council','geometry']
#osm=gpd.sjoin(osm,ct,how='inner',op='intersects')
#osm=osm[['wayid','startnode','endnode','highway','length','tract','geometry']].reset_index(drop=True)
#print('tract')
osm=gpd.sjoin(osm,nta,how='inner',op='intersects')
osm=osm[['wayid','startnode','endnode','highway','length','tract','nta','geometry']].reset_index(drop=True)
print('nta')
osm=gpd.sjoin(osm,community,how='inner',op='intersects')
osm=osm[['wayid','startnode','endnode','highway','length','tract','nta','community','geometry']].reset_index(drop=True)
print('community')
osm=gpd.sjoin(osm,council,how='inner',op='intersects')
osm=osm[['wayid','startnode','endnode','highway','length','tract','nta','community','council','geometry']].reset_index(drop=True)
print('council')
osm.to_file(path+'SHP/osm.shp')

#q1=pd.read_csv(path+'UBER/movement-speeds-quarterly-by-hod-new-york-2019-Q1.csv',dtype=float,converters={'segment_id':str,
#                                                                                                         'start_junction_id':str,
#                                                                                                         'end_junction_id':str})
#q1=q1[['osm_way_id','osm_start_node_id','osm_end_node_id','hour_of_day','speed_mph_mean','speed_mph_stddev','speed_mph_p50','speed_mph_p85']].reset_index(drop=True)
#q1.columns=['wayid','startnode','endnode','hod','meanq1','stddevq1','p50q1','p85q1']
#q2=pd.read_csv(path+'UBER/movement-speeds-quarterly-by-hod-new-york-2019-Q2.csv',dtype=float,converters={'segment_id':str,
#                                                                                                         'start_junction_id':str,
#                                                                                                         'end_junction_id':str})
#q2=q2[['osm_way_id','osm_start_node_id','osm_end_node_id','hour_of_day','speed_mph_mean','speed_mph_stddev','speed_mph_p50','speed_mph_p85']].reset_index(drop=True)
#q2.columns=['wayid','startnode','endnode','hod','meanq2','stddevq2','p50q2','p85q2']
#q3=pd.read_csv(path+'UBER/movement-speeds-quarterly-by-hod-new-york-2019-Q3.csv',dtype=float,converters={'segment_id':str,
#                                                                                                         'start_junction_id':str,
#                                                                                                         'end_junction_id':str})
#q3=q3[['osm_way_id','osm_start_node_id','osm_end_node_id','hour_of_day','speed_mph_mean','speed_mph_stddev','speed_mph_p50','speed_mph_p85']].reset_index(drop=True)
#q3.columns=['wayid','startnode','endnode','hod','meanq3','stddevq3','p50q3','p85q3']
#q4=pd.read_csv(path+'UBER/movement-speeds-quarterly-by-hod-new-york-2019-Q4.csv',dtype=float,converters={'segment_id':str,
#                                                                                                         'start_junction_id':str,
#                                                                                                         'end_junction_id':str})
#q4=q4[['osm_way_id','osm_start_node_id','osm_end_node_id','hour_of_day','speed_mph_mean','speed_mph_stddev','speed_mph_p50','speed_mph_p85']].reset_index(drop=True)
#q4.columns=['wayid','startnode','endnode','hod','meanq4','stddevq4','p50q4','p85q4']
#dcasosm=pd.merge(q1,q2,how='inner',on=['wayid','startnode','endnode','hod'])
#dcasosm=pd.merge(dcasosm,q3,how='inner',on=['wayid','startnode','endnode','hod'])
#dcasosm=pd.merge(dcasosm,q4,how='inner',on=['wayid','startnode','endnode','hod'])
#dcasosm['avgspeed']=np.nanmean(dcasosm[['meanq1','meanq2','meanq3','meanq4']],axis=1)
#osm=gpd.read_file(path+'osm.shp')
#osm.crs={'init':'epsg:4326'}
#dcas=pd.merge(osm,dcas,how='inner',on=['wayid','startnode','endnode'])
#dcas=dcas[(dcas['highway']!='motorway')&(dcas['highway']!='motorway_link')].reset_index(drop=True)
#dcas=dcas[dcas['hod']==8].reset_index(drop=True)





#dcas['avgspeedlength']=dcas['avgspeed']*dcas['length']
#dcas=dcas.groupby('tractid',as_index=False).agg({'avgspeedlength':'sum','length':'sum'})
#dcas['avgspeed']=dcas['avgspeedlength']/dcas['length']
#nycct=gpd.read_file(path+'quadstatectclipped.shp')
#nycct.crs={'init':'epsg:4326'}
#nycct=nycct[[str(x)[0:5] in ['36005','36047','36061','36081','36085'] for x in nycct['tractid']]]
#dcas=pd.merge(nycct,dcas,how='left',on='tractid')
#dcas=dcas[['tractid','avgspeed','geometry']].reset_index(drop=True)
#dcas.to_file(path+'dcas.shp')



