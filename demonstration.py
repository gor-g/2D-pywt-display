# Author : Gor G.
# AKA mySpecialUsername
# March 2022
import pywt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image as mpimg

from pywt2DDisplay import adapt_coeffs




def gimshow(I, title = '', limits = None, show=True):
	"""prepares a picture to show with a colorbar, plots if show is True"""
	if limits!=None:
		assert(type(limits)==tuple and len(limits)==2 ), "limits (tird positional arguments) must be a tuple of len 2"
		plt.imshow(I, cmap="gray", vmin =limits[0], vmax=limits[1])
	else:
		plt.imshow(I, cmap="gray")
	plt.colorbar()
	plt.title(title)
	if show:
		plt.show()
	
	return 0


y = mpimg.imread("lena.png")[:,:,0]
w = pywt.Wavelet('db2')
coeffs = pywt.wavedec2(y, w, level=3, mode='periodization')




x = adapt_coeffs(coeffs)
toShow = pywt.coeffs_to_array(x)

plt.figure(figsize=(10,10))
gimshow(toShow[0], 'Coeffs db2, normalised',  )


x = adapt_coeffs(coeffs, True)
toShow = pywt.coeffs_to_array(x)

plt.figure(figsize=(10,10))
gimshow(toShow[0], 'Coeffs db2, equalised 1000 shades',  )


x = adapt_coeffs(coeffs, True, 20)
toShow = pywt.coeffs_to_array(x)

plt.figure(figsize=(10,10))
gimshow(toShow[0], 'Coeffs db2, equalised 20 shades',  )
