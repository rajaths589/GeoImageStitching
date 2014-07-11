from osgeo import gdal
import time
import numpy as np
from ImageGDALInterface import *

def mergeImages( name1, name2, name3 ):
	print "Merging Images ..."
	start = time.time()

	image1 = ImageAbstraction( name1 )
	image2 = ImageAbstraction( name2 )

	if not (image1.isValid() and image2.isValid()):
		return

	output_ulx = min( image1.ulx, image2.ulx )
	output_uly = max( image1.uly, image2.uly )
	output_lrx = max( image1.lrx, image2.lrx )
	output_lry = min( image1.lry, image2.lry )

	output_pwidth 		= image1.pixWidth
	output_pheight 		= image1.pixHeight
	output_projection 	= image1.projection
	output_bandtype		= image1.dtype
	output_bandcount	= image1.nBands

	newImage = ImageAbstraction.create( name3, ( output_ulx, output_uly ), ( output_lrx, output_lry ), output_pwidth, output_pheight, output_projection, output_bandtype, output_bandcount )
	
	overlap = findOverlapArea( image1, image2 )
	if overlap is None:
		print "No overlap area in Images. Terminating ..."

	if image1.uly>=image2.uly:
		above = image1
		below = image2
	else:
		above = image2
		below = image1

	if above.ulx < below.ulx:
		
		copyarea = ( above.ulx, above.uly, overlap[0], above.lry )		
		copy_into( above, 1, newImage, 1, copyarea )

		copyarea = ( overlap[0], above.uly, above.lrx, overlap[1] )		
		copy_into( above, 1, newImage, 1, copyarea )

		copyarea = ( overlap[0], above.lry, above.lrx, below.lry )		
		copy_into( below, 1, newImage, 1, copyarea )

		copyarea = ( overlap[2], below.uly, below.lrx, below.lry )		
		copy_into( below, 1, newImage, 1, copyarea )

		copyarea = overlap
		data1 = above.readFromImageNP( 1, copyarea, np.float )
		data2 = below.readFromImageNP( 1, copyarea, np.float )
		zeroCheck = np.equal( 0, data2 )
		data = np.choose( zeroCheck,( data2, data1 ) )
		dataNpy = np.array( data )
		newImage.writeIntoImageNP( 1, copyarea, dataNpy )

	else:

		copyarea = ( below.ulx, below.uly, overlap[0], below.lry )		
		copy_into( below, 1, newImage, 1, copyarea )

		copyarea = ( overlap[0], above.lry, below.lrx, below.lry )		
		copy_into( below, 1, newImage, 1, copyarea )

		copyarea = ( above.ulx, above.uly, overlap[2], overlap[1] )		
		copy_into( above, 1, newImage, 1, copyarea )

		copyarea = ( overlap[2], above.uly, above.lrx, above.lry )		
		copy_into( above, 1, newImage, 1, copyarea )		

		copyarea = overlap
		data1 = above.readFromImageNP( 1, copyarea, np.float )
		data1 = below.readFromImageNP( 1, copyarea, np.float )
		zeroCheck = np.equal( 0, data2 )
		data = np.choose( zeroCheck,( data2, data1 ) )
		dataNpy = np.array( data )
		newImage.writeIntoImageNP( 1, copyarea, dataNpy )

	above.deallocate()
	below.deallocate()
	image1.deallocate()
	image2.deallocate()
	newImage.deallocate()

	end = time.time()
	return end-start
	print "Time taken for Merging:\t", (end-start), "seconds."
