from PyQt4.QtGui import *
from PyQt4.QtCore import *
from mergeui import Ui_Dialog
from ImageGDALInterface import *
from mergeImages import *
from translateImage import *
import sys, os

class UIResponse():
	def __init__(self):
		self.app = QApplication(sys.argv)
		self.window = QDialog()

		self.ui = Ui_Dialog()
		self.ui.setupUi(self.window)
		self.status = self.ui.status
		self.status.setText('Status:'+'\t Select Input Images to Proceed.')

		self.app.connect( self.ui.imgbtn1, SIGNAL("clicked()"), lambda: self.selectFile(1) )
		self.app.connect( self.ui.imgbtn2, SIGNAL("clicked()"), lambda: self.selectFile(2) )
		self.app.connect( self.ui.btnoutput, SIGNAL("clicked()"), lambda: self.selectFile(3) )
		self.app.connect( self.ui.merge, SIGNAL("clicked()"), self.merge )
		self.app.connect( self.ui.remerge, SIGNAL("clicked()"), self.remerge )
		self.app.connect( self.ui.translate, SIGNAL("clicked()"), self.translate )
		self.app.connect( self.ui.cancel, SIGNAL("clicked()"), sys.exit )

		self.merged 		= False
		self.translated 	= False
		self.remerged 		= False
		self.translateOne 	= False
		
	def selectFile(self, n):		
		if n==1 or n==2:
			path = QFileDialog.getOpenFileName(self.window, 'Select Image', '/home/', selectedFilter='*.tif')
		else:
			path = QFileDialog.getSaveFileName(self.window, 'Select Image', '/home/', selectedFilter='*.tif')

		if path is not None:
			if n==1:
				self.ui.img1.setText(path)				
				self.image1 = str(path)
				self.status.setText('Status:'+'\t Image1 Selected.')
			elif n==2:
				self.ui.img2.setText(path)
				self.image2 = str(path)
				self.status.setText('Status:'+'\t Image2 Selected.')
			else:
				self.ui.output.setText(path)
				self.output = str(path)
				self.status.setText('Status:'+'\t Output Image Selected.')

	def merge(self):
		t = mergeImages( self.image1, self.image2, self.output )
		self.status.setText('Status:'+'\t Merging Completed in '+str(t)+' seconds.')
		self.merged = True

	def remerge(self):		
		if self.merged is not True:
			self.status.setText('Status:'+'\t Merge and translate before remerging the image.')

		if self.translateOne is True:
			t = mergeImages( 'temp.tif', self.image2, self.output )
		else:
			t = mergeImages( self.image1, 'temp.tif' , self.output )

		self.status.setText('Status:'+'\t Re-Merging Completed in '+str(t)+' seconds.')
		os.remove('temp.tif')

	def translate(self):
		if self.merged is not True:
			self.status.setText('Status:'+'\t Merge before translating the image.')
		
		os.remove(self.output)
		option = self.selectImage.isChecked()
		t_X = self.translateX.value()
		t_Y = self.translateY.value()
		if option is True:
			t = translateImage( self.image1, t_X, t_Y )
			self.translateOne = True
		else:
			t = translateImage( self.image2, t_X, t_Y )

		self.status.setText('Status:'+'\t Translation Completed in '+str(t)+' seconds.')
		self.translated = True

	def display(self):
		self.window.show()		
		sys.exit(self.app.exec_())

def main():
	show = UIResponse()	
	show.display()


if __name__ == '__main__':
	main()


