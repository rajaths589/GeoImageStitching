from osgeo import gdal
import numpy as np
import sys
import time

from ImageGDALInterface import *

def translateImage(name, translate_x, translate_y):
	print "Translating the image to correct the merging ..."
	start = time.time()

	image = ImageAbstraction(name)
	if not image.isValid():
		return

	image.printDetails()

	transLonLatUL = image.getLonLatFromOffSet(translate_x,translate_y)	
	transLonLatLR = image.getLonLatFromOffSet(image.XSize+translate_x,image.YSize+translate_y)	
	newImage = ImageAbstraction.create( 'temp.tif', transLonLatUL, transLonLatLR, image.pixWidth, image.pixHeight, image.projection, image.dtype, image.nBands )	
	
	data = image.readFromImage( 1, (image.ulx,image.uly,image.getLRLonLat()[0],image.getLRLonLat()[1]) )
	newImage.writeIntoImage( 1, (transLonLatUL[0],transLonLatUL[1],transLonLatLR[0],transLonLatLR[1]), data )
	image.deallocate()
	newImage.deallocate()

	end = time.time()
	return end-start
	print "Time taken for translation:\t", (end-start), 'seconds.'



