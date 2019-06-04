library(dplyr)
library(lubridate)
library(geojsonio)
library(sp)


path = '/home/mayijun/UBER/'
path = 'C:/Users/Yijun Ma/Desktop/D/DOCUMENT/DCP2019/SPEED/UBER/'


osmseg = read.csv(paste0(path, 'movement-segments-to-osm-ways-new-york-2018.csv'), stringsAsFactors = F, colClasses = 'character')
osmnode = read.csv(paste0(path, 'movement-junctions-to-osm-nodes-new-york-2018.csv'), stringsAsFactors = F, colClasses = 'character')


october = read.csv(paste0(path, 'movement-speeds-hourly-new-york-2018-10.csv'),
                   stringsAsFactors = F, colClasses = 'character')
october = filter(october, hour == '8')
october$date = ymd(paste(october$year, october$month, october$day, sep = '-'))
october$weekday = as.character(wday(october$date, label = T))
october = filter(october, weekday %in% c('Tue', 'Wed', 'Thu'))
october = select(october, segment_id, start_junction_id, end_junction_id, speed_mph_mean, speed_mph_stddev)
october$speed_mph_mean = as.numeric(october$speed_mph_mean)
october$speed_mph_stddev = as.numeric(october$speed_mph_stddev)
october = as.data.frame(october %>% group_by(segment_id, start_junction_id, end_junction_id) %>%
                          summarise(speed_mph_mean = mean(speed_mph_mean), speed_mph_stddev = sqrt(mean(speed_mph_stddev ^ 2))))
october = merge(october, osmseg, by = 'segment_id', all.x = T)
october = merge(october, osmnode, by.x = 'start_junction_id', by.y = 'junction_id', all.x = T)
october = merge(october, osmnode, by.x = 'end_junction_id', by.y = 'junction_id', all.x = T)
october = select(october, osm_way_id, osm_node_id.x, osm_node_id.y, speed_mph_mean, speed_mph_stddev)
colnames(october) = c('osmwayid', 'osmstartnode', 'osmendnode', 'speedmean', 'speedstddev')
october$osmwayid = as.integer(october$osmwayid)


quarter = read.csv(paste0(path, 'movement-speeds-quarterly-by-hod-new-york-2018-Q4.csv'),
                   stringsAsFactors = F, colClasses = 'character')
quarter = filter(quarter, hour_of_day == '8')
quarter = select(quarter, segment_id, start_junction_id, end_junction_id, speed_mph_mean, speed_mph_stddev)
quarter$speed_mph_mean = as.numeric(quarter$speed_mph_mean)
quarter$speed_mph_stddev = as.numeric(quarter$speed_mph_stddev)
quarter = as.data.frame(quarter %>% group_by(segment_id, start_junction_id, end_junction_id) %>%
                          summarise(speed_mph_mean = mean(speed_mph_mean), speed_mph_stddev = sqrt(mean(speed_mph_stddev ^ 2))))
quarter = merge(quarter, osmseg, by = 'segment_id', all.x = T)
quarter = merge(quarter, osmnode, by.x = 'start_junction_id', by.y = 'junction_id', all.x = T)
quarter = merge(quarter, osmnode, by.x = 'end_junction_id', by.y = 'junction_id', all.x = T)
quarter = select(quarter, osm_way_id, osm_node_id.x, osm_node_id.y, speed_mph_mean, speed_mph_stddev)
colnames(quarter) = c('osmwayid', 'osmstartnode', 'osmendnode', 'speedmean', 'speedstddev')
quarter$osmwayid = as.integer(quarter$osmwayid)


osm = geojson_read(paste0(path, 'osm.geojson'), method = 'local', what = 'sp', stringsAsFactors = F)
uber = merge(osm, october, by = c('osmwayid', 'osmstartnode', 'osmendnode'), all.x=T)
uber = merge(uber, quarter, by = c('osmwayid', 'osmstartnode', 'osmendnode'), all.x=T)
uber$speedmean = ifelse(is.na(uber$speedmean.x),uber$speedmean.y,uber$speedmean.x)
uber$speedstddev = ifelse(is.na(uber$speedstddev.x),uber$speedstddev.y,uber$speedstddev.x)
uber = uber[,c(1:6,11,12)]
geojson_write(uber,file = paste0(path, 'uber.geojson'))

