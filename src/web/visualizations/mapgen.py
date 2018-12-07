# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import folium
from folium.plugins import MarkerCluster
import os

class MapGenerator(object):
	"""MapGenerator"""
	def __init__(self):
		super(MapGenerator, self).__init__()
	
	def generate_map_html(self, data):
		#df = pd.read_csv('data/speciesLink.csv', sep=',', dtype={'GEOID' : object}, usecols=["latitude", "longitude"])

		df = pd.DataFrame(data=data, columns=["scientificName", "municipality", "state", "country", "latitude", "longitude", "date"])
		columns=["scientificName", "municipality", "state", "country", "date"]
		df.drop(columns, axis=1, inplace=True)

		print 'DROPPED COLUMNS'

		print 'ORIGINAL DF'
		print df

		print 'REPLACE AS NAN'
		df.replace('', np.nan, inplace=True)

		# Drop NaN values from dataframe
		df = df.dropna(subset=['longitude'])
		df = df.dropna(subset=['latitude'])

		# Remove extra padding from column names
		df.columns = df.columns.str.strip()
		df.head()

		print df

		print type(df.latitude[0])
		print type(df.longitude[0])

		map_html = folium.Map(location=[df['latitude'].mean(), 
		 df['longitude'].mean()], 
		 zoom_start=4)

		# Cluster markers interactively
		mc = MarkerCluster()

		# Creating a Marker for each point in df_sample.
		for row in df.itertuples():
		    if(row.latitude != None and row.longitude != None):
		        mc.add_child(folium.Marker(location=[row.latitude,  row.longitude]))
		 
		map_html.add_child(mc)

		outPath = os.path.dirname(__file__).strip('visualizations') + 'templates/visualizations/map.html'
		
		map_html.save(outPath)

		return map_html