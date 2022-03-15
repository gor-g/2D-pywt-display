# Author : Gor G.
# AKA mySpecialUsername
# March 2022


def adapt_coeffs(coeffs, equa=False, Hsize=1000):
  """ EN: normalise, or equalise the histogram each coefficeint matrix of the pywt.wavedec2() output
  FR: normalise ou égalise l'histogramme de chaque coefficeint du résulatat de pywt.wavedec2() """
  def equalise(I, Hsize=Hsize):
    """
    input: 2D np.ndarray
    output: equalise the histogram of the input array
    """
    # EN: remaps the values of I to integers between 0 and Hsize to apply bitcount
    # FR : remène les valeurs de I à des entiers entre 0 et Hsize pour appliquer bitcount
    I = I-np.min(I); I = I/np.max(I)*(Hsize-1); I=I.astype(int) 
    
    # EN: calculates the normalised histogram, than the cumulated histogramm
    # FR: calculer l'histo normalisé, puis le histo cumulé
    H = np.bincount(I.flatten(), minlength=Hsize)
    H = H/np.sum(H)
    
    cumulH = np.cumsum(H)
    # EN: reassigns the equalised values of the pixels
    # FR: assinge les valeurs équalisées
    res = [cumulH[i] for i in I.flatten()]
    return np.reshape(res, I.shape)
  
  def normalise(I):"""linearly normalise the input np.ndarray"""
    I = I-np.min(I); I = I/np.max(I)
    return I
  
  # EN: coose the transformation to apply
  # FR: choisit la transformation qu'il faut appliquer
  tfo = equalise if equa else normalise 
  
  # EN: applys the transformation to each coefficient matrix
  # FR: applique la transformation à chaque coefficient
  res = [tfo(coeffs[0])]
  for i in range (1,len(coeffs)):
    T=tuple([tfo(coeffs[i][j]) for j in range(3)])
    res+=[T]

  return res
