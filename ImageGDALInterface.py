from osgeo import gdal
import numpy as np

class ImageAbstraction:
	def __init__(self,name, internal=None):
		if internal is None:
			gdal.AllRegister()		

			self.image = gdal.Open(name)
		else:
			self.image = internal
			
		self.name  = name
		
		gT = self.image.GetGeoTransform()
		
		self.ulx       = gT[0]
		self.uly       = gT[3]
		self.pixWidth  = gT[1]
		self.pixHeight = gT[5]

		self.dtype      = self.image.GetRasterBand(1).DataType
		self.projection = self.image.GetProjection()
		self.nBands     = self.image.RasterCount

		self.XSize = self.image.RasterXSize
		self.YSize = self.image.RasterYSize
		
		lr = self.getLRLonLat()
		self.lrx = lr[0]
		self.lry = lr[1]

	@staticmethod
	def create( name, ul, lr, pWidth, pHeight, projection, bandType, bandCount ):		
		if name is None:
			name = 'image.tif'
			print "Output file name not given. Using Default name : image.tif ."

		create_options = []
		create_options.append("COMPRESS=DEFLATE")
		create_options.append("PREDICTOR=2")
		create_options.append("ZLEVEL=9")

		Driver = gdal.GetDriverByName('GTiff')
		if Driver is None:
			print "Driver for GTiff is not found. Terminating ..."
			return

		gT = [ul[0],pWidth,0,ul[1],0,pHeight]
		XSize = int((lr[0]-ul[0])/pWidth + 0.5)
		YSize = int((ul[1]-lr[1])/pWidth + 0.5)

		gdal.PushErrorHandler( 'CPLQuietErrorHandler' )
		output = gdal.Open( name, gdal.GA_Update )
		gdal.PopErrorHandler()
		if output is not None:
			print "File already exists. Please try with a different name.  Terminating ..."
			return

		output = Driver.Create( name, XSize, YSize, bandCount, bandType, create_options )
		if output is None:
			print "Image Creation failed. Terminating ..."
			return

		output.SetGeoTransform(gT)
		output.SetProjection(projection)

		output_abstraction = ImageAbstraction(name,output)		
		return output_abstraction

	def isValid(self):
		if self.image is not None:
			return True
		else:
			return False
	
	def printDetails( self ):
		print
		print "Path:\t"+self.name		
		print "Extent:\t", (self.XSize,self.YSize)
		print "Origin in LatLong:\t", (self.ulx,self.uly)
		print "Pixel Dimensions:\t", (self.pixWidth,self.pixHeight)
		print "Projection:\t", self.projection
		print "No. of Bands:\t", self.nBands		
		print "Band DataType:\t", self.dtype
		print 

	def isNorthUp( self ):
		gT = self.image.GetGeoTransform()
		if gT[2]==0 and gT[4]==0:
			print "The Image: "+self.name+" is north up."
		else:
			print "The Image: "+self.name+" is not north up."

	def getOffSet( self, lon, lat ):
		xOff = int( (lon - self.ulx)/self.pixWidth  +  0.5)
		yOff = int( (lat - self.uly)/self.pixHeight +  0.5)
		return (xOff,yOff)
	
	def getOffSetFromLatLon( self, fromLon, fromLat, toLon, toLat ):
		xOff = int( (toLon - fromLon)/self.pixWidth  + 0.5)
		yOff = int( (toLat - fromLat)/self.pixHeight + 0.5)
		return (xOff,yOff)

	def deallocate( self ):
		self.image = None

	def getLonLatFromOffSet( self, xOff, yOff ):
		lon = xOff*self.pixWidth  + self.ulx
		lat = yOff*self.pixHeight + self.uly
		return (lon,lat)

	def getLRLonLat( self ):
		return self.getLonLatFromOffSet(self.XSize,self.YSize)

	#area is a tuplet with (ulx,uly,lrx,lry) of copydata
	def readFromImage( self, band, area ):
		bandData = self.image.GetRasterBand(band)
		offset = self.getOffSet(area[0], area[1])
		size = self.getOffSetFromLatLon(area[0], area[1], area[2], area[3])
		data = bandData.ReadRaster( offset[0], offset[1], size[0], size[1], size[0], size[1], self.dtype)
		return data

	#NOTE: No option to choose targetSize. Might cause errors.
	def writeIntoImage( self, band, area, data ):
		bandData = self.image.GetRasterBand(band)
		offset = self.getOffSet(area[0], area[1])
		size = self.getOffSetFromLatLon(area[0], area[1], area[2], area[3])
		bandData.WriteRaster( offset[0], offset[1], size[0], size[1], data, size[0], size[1], self.dtype)

	#dtype - numpy datatype e.g. np.float
	def readFromImageNP( self, band, area, dtype ):
		bandData = self.image.GetRasterBand(band)
		offset = self.getOffSet(area[0], area[1])
		size = self.getOffSetFromLatLon(area[0], area[1], area[2], area[3])
		data = bandData.ReadAsArray(offset[0], offset[1], size[0], size[1], size[0], size[1]).astype(dtype)
		return data

	def writeIntoImageNP( self, band, area, data ):
		bandData = self.image.GetRasterBand(band)
		offset = self.getOffSet(area[0], area[1])
		bandData.WriteArray(data, offset[0], offset[1])

#area is a tuplet with (ulx,uly,lrx,lry) of copydata
def copy_into( source, sourceBand, target, targetBand, datatype, area ):
	data = source.readFromImage(sourceBand, area)
	target.writeIntoImage(targetBand, area, data)

def findOverlapArea( image1, image2 ):
	overlap = None
	image1LR = image1.getLRLonLat()
	image2LR = image2.getLRLonLat()

	overlap_ulx = max( image1.ulx, image2.ulx )
	overlap_uly = min( image1.uly, image2.uly )
	overlap_lrx = min( image1LR[0], image2LR[0])
	overlap_lry = max( image1LR[1], image2LR[1] )

	if (overlap_ulx>overlap_lrx):
		print "The Input Images do not overlap."
		return None
	if (overlap_uly<overlap_lry):
		print "The Input Images do not overlap."
		return None

	return ( overlap_ulx, overlap_uly, overlap_lrx, overlap_lry )
