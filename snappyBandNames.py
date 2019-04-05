


from gdal_tif2rgb import read_tif_and_get_bands


""" snappy-based """
import os, time, shutil
from snappy import jpy, ProgressMonitor, ProductIO, HashMap, GPF
# from read_all_folders import read_all_folders_in

FileReader = jpy.get_type('java.io.FileReader')
GraphIO = jpy.get_type('org.esa.snap.core.gpf.graph.GraphIO')
Graph = jpy.get_type('org.esa.snap.core.gpf.graph.Graph')
GraphProcessor = jpy.get_type('org.esa.snap.core.gpf.graph.GraphProcessor')
PrintPM = jpy.get_type('com.bc.ceres.core.PrintWriterProgressMonitor')
System = jpy.get_type('java.lang.System')
pm = PrintPM(System.out)



""" Use GDAL to read tif """
dataPath = "data\\"
dataName = "SAR_20180817_DSC115_snap"

bandList = sorted(['VV', 'VH'])
data, _ = read_tif_and_get_bands(dataPath, dataName, bandList)

print(data.shape)


""" Use snappy to read tif """
product = ProductIO.readProduct(dataPath + dataName + '.tif')
bandNames = product.getBandNames()
print("{}: {}, {}".format(len(bandNames), bandNames[0], bandNames[1]))

""" Set bandName for product band by band"""
for i in range(0, len(bandNames)):
    product.getBandAt(i).setName(bandList[i])

bandNames = product.getBandNames()
print("{}: {}, {}".format(len(bandNames), bandNames[0], bandNames[1]))

# ProductIO.writeProduct(product, dataPath + dataName + "_snap", 'GeoTIFF', pm)







