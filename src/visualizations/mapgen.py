# -*- coding: utf-8 -*-

import pandas as pd
import folium
from folium.plugins import MarkerCluster

class MapGenerator(object):
	"""MapGenerator"""
	def __init__(self, data):
		super(MapGenerator, self).__init__()
		self.data = data

	def generate_map_html(data):
		df = pd.read_csv('data/speciesLink.csv', sep=',', dtype={'GEOID' : object}, usecols=["latitude", "longitude"])

		# Drop NaN values from dataframe
		df = df.dropna(subset=['longitude'])
		df = df.dropna(subset=['latitude'])

		# Remove extra padding from column names
		df.columns = df.columns.str.strip()
		df.head()

		#grab a random sample from df
		subset_of_df = df.sample(n=500)

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

		map_html.save("map.html")