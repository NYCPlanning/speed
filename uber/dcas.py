import geopandas as gpd
import pandas as pd
import numpy as np
import shapely


#path='C:/Users/Yijun Ma/Desktop/D/DOCUMENT/DCP2020/DCAS/'
path='/home/mayijun/DCAS/'



## Combine OSM geometry and various boundaries
#osm=gpd.read_file(path+'UBER/osm.geojson')
#osm.crs={'init':'epsg:4326'}
#osm=osm.to_crs({'init':'epsg:6539'})
#osm=osm[['osmwayid','osmstartnodeid','osmendnodeid','osmhighway','geometry']].reset_index(drop=True)
#osm.columns=['wayid','startnode','endnode','highway','geometry']
#osm['length']=[x.length for x in osm['geometry']]
#osm=osm.to_crs({'init':'epsg:4326'})
#nycct=gpd.read_file(path+'SHP/nycct.shp')
#nycct.crs={'init':'epsg:4326'}
#nycct.columns=['tract','geometry']
#osm=gpd.sjoin(osm,nycct,how='inner',op='intersects')
#osm=osm[['wayid','startnode','endnode','highway','length','tract','geometry']].reset_index(drop=True)
#print('tract')
#nta=pd.read_csv(path+'SHP/tracttonta.csv',dtype=str)
#osm=pd.merge(osm,nta,how='left',on='tract')
#osm=osm[['wayid','startnode','endnode','highway','length','tract','nta','geometry']].reset_index(drop=True)
#print('nta')
#community=gpd.read_file(path+'SHP/community.shp')
#community.crs={'init':'epsg:4326'}
#community.columns=['community','geometry']
#osm=gpd.sjoin(osm,community,how='inner',op='intersects')
#osm=osm[['wayid','startnode','endnode','highway','length','tract','nta','community','geometry']].reset_index(drop=True)
#print('community')
#council=gpd.read_file(path+'SHP/council.shp')
#council.crs={'init':'epsg:4326'}
#council.columns=['council','geometry']
#osm=gpd.sjoin(osm,council,how='inner',op='intersects')
#osm=osm[['wayid','startnode','endnode','highway','length','tract','nta','community','council','geometry']].reset_index(drop=True)
#print('council')
#osm.to_file(path+'SHP/osm.shp')
#
#
#
## Annual Average
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
#dcasosm=dcasosm.groupby(['wayid','startnode','endnode'],as_index=False).agg({'avgspeed':'mean'}).reset_index(drop=True)
#osm=gpd.read_file(path+'SHP/osm.shp')
#osm.crs={'init':'epsg:4326'}
#osm=osm[(osm['highway']!='motorway')&(osm['highway']!='motorway_link')].reset_index(drop=True)
#dcasosm=pd.merge(osm,dcasosm,how='inner',on=['wayid','startnode','endnode'])
#dcasosm.to_file(path+'OUTPUT/dcasosm.shp')
#
#dcasosm=gpd.read_file(path+'OUTPUT/dcasosm.shp')
#dcasct=dcasosm[['wayid','startnode','endnode','length','tract','avgspeed']].drop_duplicates(keep='first').reset_index(drop=True)
#dcasct['avgspeedlength']=dcasct['avgspeed']*dcasct['length']
#dcasct=dcasct.groupby('tract',as_index=False).agg({'avgspeedlength':'sum','length':'sum'}).reset_index(drop=True)
#dcasct['avgspeed']=dcasct['avgspeedlength']/dcasct['length']
#nycctclipped=gpd.read_file(path+'SHP/nycctclipped.shp')
#dcasct=pd.merge(nycctclipped,dcasct,how='left',left_on='tractid',right_on='tract')
#dcasct.to_file(path+'OUTPUT/dcasct.shp')
#
#dcasosm=gpd.read_file(path+'OUTPUT/dcasosm.shp')
#dcasnta=dcasosm[['wayid','startnode','endnode','length','nta','avgspeed']].drop_duplicates(keep='first').reset_index(drop=True)
#dcasnta['avgspeedlength']=dcasnta['avgspeed']*dcasnta['length']
#dcasnta=dcasnta.groupby('nta',as_index=False).agg({'avgspeedlength':'sum','length':'sum'}).reset_index(drop=True)
#dcasnta['avgspeed']=dcasnta['avgspeedlength']/dcasnta['length']
#ntaclipped=gpd.read_file(path+'SHP/ntaclipped.shp')
#dcasnta=pd.merge(ntaclipped,dcasnta,how='left',left_on='NTACode',right_on='nta')
#dcasnta.to_file(path+'OUTPUT/dcasnta.shp')
#
#dcasosm=gpd.read_file(path+'OUTPUT/dcasosm.shp')
#dcascommunity=dcasosm[['wayid','startnode','endnode','length','community','avgspeed']].drop_duplicates(keep='first').reset_index(drop=True)
#dcascommunity['avgspeedlength']=dcascommunity['avgspeed']*dcascommunity['length']
#dcascommunity=dcascommunity.groupby('community',as_index=False).agg({'avgspeedlength':'sum','length':'sum'}).reset_index(drop=True)
#dcascommunity['avgspeed']=dcascommunity['avgspeedlength']/dcascommunity['length']
#communityclipped=gpd.read_file(path+'SHP/communityclipped.shp')
#dcascommunity=pd.merge(communityclipped,dcascommunity,how='left',left_on='BoroCD',right_on='community')
#dcascommunity.to_file(path+'OUTPUT/dcascommunity.shp')
#
#dcasosm=gpd.read_file(path+'OUTPUT/dcasosm.shp')
#dcascouncil=dcasosm[['wayid','startnode','endnode','length','council','avgspeed']].drop_duplicates(keep='first').reset_index(drop=True)
#dcascouncil['avgspeedlength']=dcascouncil['avgspeed']*dcascouncil['length']
#dcascouncil=dcascouncil.groupby('council',as_index=False).agg({'avgspeedlength':'sum','length':'sum'}).reset_index(drop=True)
#dcascouncil['avgspeed']=dcascouncil['avgspeedlength']/dcascouncil['length']
#councilclipped=gpd.read_file(path+'SHP/councilclipped.shp')
#dcascouncil=pd.merge(councilclipped,dcascouncil,how='left',left_on='CounDist',right_on='council')
#dcascouncil.to_file(path+'OUTPUT/dcascouncil.shp')
#
#
#
## 8-9 AM Average
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
#dcasosm8=pd.merge(q1,q2,how='inner',on=['wayid','startnode','endnode','hod'])
#dcasosm8=pd.merge(dcasosm8,q3,how='inner',on=['wayid','startnode','endnode','hod'])
#dcasosm8=pd.merge(dcasosm8,q4,how='inner',on=['wayid','startnode','endnode','hod'])
#dcasosm8['avgspeed']=np.nanmean(dcasosm8[['meanq1','meanq2','meanq3','meanq4']],axis=1)
#dcasosm8=dcasosm8[dcasosm8['hod']==8].reset_index(drop=True)
#osm=gpd.read_file(path+'SHP/osm.shp')
#osm.crs={'init':'epsg:4326'}
#osm=osm[(osm['highway']!='motorway')&(osm['highway']!='motorway_link')].reset_index(drop=True)
#dcasosm8=pd.merge(osm,dcasosm8,how='inner',on=['wayid','startnode','endnode'])
#dcasosm8.to_file(path+'OUTPUT/dcasosm8.shp')
#
#dcasosm8=gpd.read_file(path+'OUTPUT/dcasosm8.shp')
#dcasct8=dcasosm8[['wayid','startnode','endnode','length','tract','avgspeed']].drop_duplicates(keep='first').reset_index(drop=True)
#dcasct8['avgspeedlength']=dcasct8['avgspeed']*dcasct8['length']
#dcasct8=dcasct8.groupby('tract',as_index=False).agg({'avgspeedlength':'sum','length':'sum'}).reset_index(drop=True)
#dcasct8['avgspeed']=dcasct8['avgspeedlength']/dcasct8['length']
#nycctclipped=gpd.read_file(path+'SHP/nycctclipped.shp')
#dcasct8=pd.merge(nycctclipped,dcasct8,how='left',left_on='tractid',right_on='tract')
#dcasct8.to_file(path+'OUTPUT/dcasct8.shp')
#
#dcasosm8=gpd.read_file(path+'OUTPUT/dcasosm8.shp')
#dcasnta8=dcasosm8[['wayid','startnode','endnode','length','nta','avgspeed']].drop_duplicates(keep='first').reset_index(drop=True)
#dcasnta8['avgspeedlength']=dcasnta8['avgspeed']*dcasnta8['length']
#dcasnta8=dcasnta8.groupby('nta',as_index=False).agg({'avgspeedlength':'sum','length':'sum'}).reset_index(drop=True)
#dcasnta8['avgspeed']=dcasnta8['avgspeedlength']/dcasnta8['length']
#ntaclipped=gpd.read_file(path+'SHP/ntaclipped.shp')
#dcasnta8=pd.merge(ntaclipped,dcasnta8,how='left',left_on='NTACode',right_on='nta')
#dcasnta8.to_file(path+'OUTPUT/dcasnta8.shp')
#
#dcasosm8=gpd.read_file(path+'OUTPUT/dcasosm8.shp')
#dcascommunity8=dcasosm8[['wayid','startnode','endnode','length','community','avgspeed']].drop_duplicates(keep='first').reset_index(drop=True)
#dcascommunity8['avgspeedlength']=dcascommunity8['avgspeed']*dcascommunity8['length']
#dcascommunity8=dcascommunity8.groupby('community',as_index=False).agg({'avgspeedlength':'sum','length':'sum'}).reset_index(drop=True)
#dcascommunity8['avgspeed']=dcascommunity8['avgspeedlength']/dcascommunity8['length']
#communityclipped=gpd.read_file(path+'SHP/communityclipped.shp')
#dcascommunity8=pd.merge(communityclipped,dcascommunity8,how='left',left_on='BoroCD',right_on='community')
#dcascommunity8.to_file(path+'OUTPUT/dcascommunity8.shp')
#
#dcasosm8=gpd.read_file(path+'OUTPUT/dcasosm8.shp')
#dcascouncil8=dcasosm8[['wayid','startnode','endnode','length','council','avgspeed']].drop_duplicates(keep='first').reset_index(drop=True)
#dcascouncil8['avgspeedlength']=dcascouncil8['avgspeed']*dcascouncil8['length']
#dcascouncil8=dcascouncil8.groupby('council',as_index=False).agg({'avgspeedlength':'sum','length':'sum'}).reset_index(drop=True)
#dcascouncil8['avgspeed']=dcascouncil8['avgspeedlength']/dcascouncil8['length']
#councilclipped=gpd.read_file(path+'SHP/councilclipped.shp')
#dcascouncil8=pd.merge(councilclipped,dcascouncil8,how='left',left_on='CounDist',right_on='council')
#dcascouncil8.to_file(path+'OUTPUT/dcascouncil8.shp')
#
#
#
## 17-18 PM Average
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
#dcasosm17=pd.merge(q1,q2,how='inner',on=['wayid','startnode','endnode','hod'])
#dcasosm17=pd.merge(dcasosm17,q3,how='inner',on=['wayid','startnode','endnode','hod'])
#dcasosm17=pd.merge(dcasosm17,q4,how='inner',on=['wayid','startnode','endnode','hod'])
#dcasosm17['avgspeed']=np.nanmean(dcasosm17[['meanq1','meanq2','meanq3','meanq4']],axis=1)
#dcasosm17=dcasosm17[dcasosm17['hod']==17].reset_index(drop=True)
#osm=gpd.read_file(path+'SHP/osm.shp')
#osm.crs={'init':'epsg:4326'}
#osm=osm[(osm['highway']!='motorway')&(osm['highway']!='motorway_link')].reset_index(drop=True)
#dcasosm17=pd.merge(osm,dcasosm17,how='inner',on=['wayid','startnode','endnode'])
#dcasosm17.to_file(path+'OUTPUT/dcasosm17.shp')
#
#dcasosm17=gpd.read_file(path+'OUTPUT/dcasosm17.shp')
#dcasct17=dcasosm17[['wayid','startnode','endnode','length','tract','avgspeed']].drop_duplicates(keep='first').reset_index(drop=True)
#dcasct17['avgspeedlength']=dcasct17['avgspeed']*dcasct17['length']
#dcasct17=dcasct17.groupby('tract',as_index=False).agg({'avgspeedlength':'sum','length':'sum'}).reset_index(drop=True)
#dcasct17['avgspeed']=dcasct17['avgspeedlength']/dcasct17['length']
#nycctclipped=gpd.read_file(path+'SHP/nycctclipped.shp')
#dcasct17=pd.merge(nycctclipped,dcasct17,how='left',left_on='tractid',right_on='tract')
#dcasct17.to_file(path+'OUTPUT/dcasct17.shp')
#
#dcasosm17=gpd.read_file(path+'OUTPUT/dcasosm17.shp')
#dcasnta17=dcasosm17[['wayid','startnode','endnode','length','nta','avgspeed']].drop_duplicates(keep='first').reset_index(drop=True)
#dcasnta17['avgspeedlength']=dcasnta17['avgspeed']*dcasnta17['length']
#dcasnta17=dcasnta17.groupby('nta',as_index=False).agg({'avgspeedlength':'sum','length':'sum'}).reset_index(drop=True)
#dcasnta17['avgspeed']=dcasnta17['avgspeedlength']/dcasnta17['length']
#ntaclipped=gpd.read_file(path+'SHP/ntaclipped.shp')
#dcasnta17=pd.merge(ntaclipped,dcasnta17,how='left',left_on='NTACode',right_on='nta')
#dcasnta17.to_file(path+'OUTPUT/dcasnta17.shp')
#
#dcasosm17=gpd.read_file(path+'OUTPUT/dcasosm17.shp')
#dcascommunity17=dcasosm17[['wayid','startnode','endnode','length','community','avgspeed']].drop_duplicates(keep='first').reset_index(drop=True)
#dcascommunity17['avgspeedlength']=dcascommunity17['avgspeed']*dcascommunity17['length']
#dcascommunity17=dcascommunity17.groupby('community',as_index=False).agg({'avgspeedlength':'sum','length':'sum'}).reset_index(drop=True)
#dcascommunity17['avgspeed']=dcascommunity17['avgspeedlength']/dcascommunity17['length']
#communityclipped=gpd.read_file(path+'SHP/communityclipped.shp')
#dcascommunity17=pd.merge(communityclipped,dcascommunity17,how='left',left_on='BoroCD',right_on='community')
#dcascommunity17.to_file(path+'OUTPUT/dcascommunity17.shp')
#
#dcasosm17=gpd.read_file(path+'OUTPUT/dcasosm17.shp')
#dcascouncil17=dcasosm17[['wayid','startnode','endnode','length','council','avgspeed']].drop_duplicates(keep='first').reset_index(drop=True)
#dcascouncil17['avgspeedlength']=dcascouncil17['avgspeed']*dcascouncil17['length']
#dcascouncil17=dcascouncil17.groupby('council',as_index=False).agg({'avgspeedlength':'sum','length':'sum'}).reset_index(drop=True)
#dcascouncil17['avgspeed']=dcascouncil17['avgspeedlength']/dcascouncil17['length']
#councilclipped=gpd.read_file(path+'SHP/councilclipped.shp')
#dcascouncil17=pd.merge(councilclipped,dcascouncil17,how='left',left_on='CounDist',right_on='council')
#dcascouncil17.to_file(path+'OUTPUT/dcascouncil17.shp')



## Facilities
## Clean MapPLUTO 2020 and create Borough-Block shapefile
#mappluto2020=gpd.read_file(path+'FACILITY/nyc_mappluto_20v1_shp/MapPLUTO.shp')
#mappluto2020=mappluto2020.to_crs({'init':'epsg:4326'})
#mappluto2020=mappluto2020[['BBL','Latitude','Longitude','geometry']].reset_index(drop=True)
#mappluto2020.to_file(path+'FACILITY/mappluto2020.shp')
#
#mappluto2020BB=gpd.read_file(path+'FACILITY/mappluto2020.shp')
#mappluto2020BB['BB']=[str(x)[0:6] for x in mappluto2020BB['BBL']]
#mappluto2020BB=mappluto2020BB.dissolve(by='BB')
#mappluto2020BB['Latitude']=mappluto2020BB.geometry.centroid.y
#mappluto2020BB['Longitude']=mappluto2020BB.geometry.centroid.x
#mappluto2020BB.to_file(path+'FACILITY/mappluto2020BB.shp')
#
## Clean MapPLUTO 2015
#mappluto2015bx=gpd.read_file(path+'FACILITY/mappluto_15v1/Bronx/BXMapPLUTO.shp')
#mappluto2015bx=mappluto2015bx[['BBL','XCoord','YCoord','geometry']].reset_index(drop=True)
#mappluto2015bxpt=gpd.GeoDataFrame(mappluto2015bx,geometry=[shapely.geometry.Point(x, y) for x, y in zip(mappluto2015bx['XCoord'],mappluto2015bx['YCoord'])],crs=mappluto2015bx.crs)
#mappluto2015bxpt=mappluto2015bxpt.to_crs({'init':'epsg:4326'})
#mappluto2015bxpt['Latitude']=mappluto2015bxpt.geometry.y
#mappluto2015bxpt['Longitude']=mappluto2015bxpt.geometry.x
#mappluto2015bxpt=mappluto2015bxpt[['BBL','Latitude','Longitude']].reset_index(drop=True)
#mappluto2015bx=pd.merge(mappluto2015bx,mappluto2015bxpt,how='left',on='BBL')
#mappluto2015bx=mappluto2015bx[['BBL','Latitude','Longitude','geometry']].reset_index(drop=True)
#mappluto2015bx=mappluto2015bx.to_crs({'init':'epsg:4326'})
#
#mappluto2015bk=gpd.read_file(path+'FACILITY/mappluto_15v1/Brooklyn/BKMapPLUTO.shp')
#mappluto2015bk=mappluto2015bk[['BBL','XCoord','YCoord','geometry']].reset_index(drop=True)
#mappluto2015bkpt=gpd.GeoDataFrame(mappluto2015bk,geometry=[shapely.geometry.Point(x, y) for x, y in zip(mappluto2015bk['XCoord'],mappluto2015bk['YCoord'])],crs=mappluto2015bk.crs)
#mappluto2015bkpt=mappluto2015bkpt.to_crs({'init':'epsg:4326'})
#mappluto2015bkpt['Latitude']=mappluto2015bkpt.geometry.y
#mappluto2015bkpt['Longitude']=mappluto2015bkpt.geometry.x
#mappluto2015bkpt=mappluto2015bkpt[['BBL','Latitude','Longitude']].reset_index(drop=True)
#mappluto2015bk=pd.merge(mappluto2015bk,mappluto2015bkpt,how='left',on='BBL')
#mappluto2015bk=mappluto2015bk[['BBL','Latitude','Longitude','geometry']].reset_index(drop=True)
#mappluto2015bk=mappluto2015bk.to_crs({'init':'epsg:4326'})
#
#mappluto2015mn=gpd.read_file(path+'FACILITY/mappluto_15v1/Manhattan/MNMapPLUTO.shp')
#mappluto2015mn=mappluto2015mn[['BBL','XCoord','YCoord','geometry']].reset_index(drop=True)
#mappluto2015mnpt=gpd.GeoDataFrame(mappluto2015mn,geometry=[shapely.geometry.Point(x, y) for x, y in zip(mappluto2015mn['XCoord'],mappluto2015mn['YCoord'])],crs=mappluto2015mn.crs)
#mappluto2015mnpt=mappluto2015mnpt.to_crs({'init':'epsg:4326'})
#mappluto2015mnpt['Latitude']=mappluto2015mnpt.geometry.y
#mappluto2015mnpt['Longitude']=mappluto2015mnpt.geometry.x
#mappluto2015mnpt=mappluto2015mnpt[['BBL','Latitude','Longitude']].reset_index(drop=True)
#mappluto2015mn=pd.merge(mappluto2015mn,mappluto2015mnpt,how='left',on='BBL')
#mappluto2015mn=mappluto2015mn[['BBL','Latitude','Longitude','geometry']].reset_index(drop=True)
#mappluto2015mn=mappluto2015mn.to_crs({'init':'epsg:4326'})
#
#mappluto2015qn=gpd.read_file(path+'FACILITY/mappluto_15v1/Queens/QNMapPLUTO.shp')
#mappluto2015qn=mappluto2015qn[['BBL','XCoord','YCoord','geometry']].reset_index(drop=True)
#mappluto2015qnpt=gpd.GeoDataFrame(mappluto2015qn,geometry=[shapely.geometry.Point(x, y) for x, y in zip(mappluto2015qn['XCoord'],mappluto2015qn['YCoord'])],crs=mappluto2015qn.crs)
#mappluto2015qnpt=mappluto2015qnpt.to_crs({'init':'epsg:4326'})
#mappluto2015qnpt['Latitude']=mappluto2015qnpt.geometry.y
#mappluto2015qnpt['Longitude']=mappluto2015qnpt.geometry.x
#mappluto2015qnpt=mappluto2015qnpt[['BBL','Latitude','Longitude']].reset_index(drop=True)
#mappluto2015qn=pd.merge(mappluto2015qn,mappluto2015qnpt,how='left',on='BBL')
#mappluto2015qn=mappluto2015qn[['BBL','Latitude','Longitude','geometry']].reset_index(drop=True)
#mappluto2015qn=mappluto2015qn.to_crs({'init':'epsg:4326'})
#
#mappluto2015si=gpd.read_file(path+'FACILITY/mappluto_15v1/Staten_Island/SIMapPLUTO.shp')
#mappluto2015si=mappluto2015si[['BBL','XCoord','YCoord','geometry']].reset_index(drop=True)
#mappluto2015sipt=gpd.GeoDataFrame(mappluto2015si,geometry=[shapely.geometry.Point(x, y) for x, y in zip(mappluto2015si['XCoord'],mappluto2015si['YCoord'])],crs=mappluto2015si.crs)
#mappluto2015sipt=mappluto2015sipt.to_crs({'init':'epsg:4326'})
#mappluto2015sipt['Latitude']=mappluto2015sipt.geometry.y
#mappluto2015sipt['Longitude']=mappluto2015sipt.geometry.x
#mappluto2015sipt=mappluto2015sipt[['BBL','Latitude','Longitude']].reset_index(drop=True)
#mappluto2015si=pd.merge(mappluto2015si,mappluto2015sipt,how='left',on='BBL')
#mappluto2015si=mappluto2015si[['BBL','Latitude','Longitude','geometry']].reset_index(drop=True)
#mappluto2015si=mappluto2015si.to_crs({'init':'epsg:4326'})
#
#mappluto2015=pd.concat([mappluto2015bx,mappluto2015bk,mappluto2015mn,mappluto2015qn,mappluto2015si],axis=0,ignore_index=True)
#mappluto2015.to_file(path+'FACILITY/mappluto2015.shp')

# Join to facilitybbl
facilitybbl=pd.read_csv(path+'FACILITY/FacilityBBL.csv',dtype=str,converters={'BBL':float})
mappluto2020=gpd.read_file(path+'FACILITY/mappluto2020.shp')
mappluto2020.crs={'init':'epsg:4326'}


facilitybbl=pd.merge(mappluto2020,facilitybbl,how='right',on='BBL')


k=facilitybbl[pd.isna(facilitybbl['geometry'])]
mappluto2015=gpd.read_file(path+'FACILITY/mapplut02015.shp')
mappluto2015.crs={'init':'epsg:4326'}
k=pd.merge(mappluto2015,k,how='right',on='BBL')
k['BBL']=[str(x) for x in k['BBL']]

