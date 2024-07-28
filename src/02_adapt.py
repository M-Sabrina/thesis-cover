import numpy as np
import skimage as ski
import skimage.io as io

pattern_cropped = io.imread("images/pattern_cropped.tif")


# play with contrast
pattern_cropped_vs1 = ski.exposure.adjust_gamma(pattern_cropped).astype(np.uint8)
io.imsave("images/pattern_cropped_vs1.png", pattern_cropped_vs1)

pattern_cropped_vs2 = ski.exposure.adjust_log(pattern_cropped).astype(np.uint8)
io.imsave("images/pattern_cropped_vs2.png", pattern_cropped_vs2)

pattern_cropped_vs3 = ski.exposure.adjust_sigmoid(pattern_cropped).astype(np.uint8)
io.imsave("images/pattern_cropped_vs3.png", pattern_cropped_vs3)

pattern_cropped_vs4 = ski.exposure.equalize_hist(pattern_cropped).astype(np.uint8)
io.imsave("images/pattern_cropped_vs4.png", pattern_cropped_vs4)
