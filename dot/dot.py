import pandas as pd

path='C:/Users/Yijun Ma/Desktop/D/DOCUMENT/DCP2019/SPEED/'

dot=pd.read_csv(path+'DOT/LinkSpeedQuery.txt',sep='\t')

dot=pd.read_csv(path+'DOT/DOT_Traffic_Speeds_NBE.csv',nrows=1000000)
k=dot.LINK_NAME.drop_duplicates()
