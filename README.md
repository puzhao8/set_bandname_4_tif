# set_bandname_4_tif
This project tries to read and write bandname from/to GeoTiff with GDAL and snappy


The folder .\data\ includes two GeoTiff files, and both of them share the same data with two bands, i.e., VH and VV (two polarization).
The GeoTiff file ends with "gdal.tif" was written by gdal, while that ends with "snappy.tif" was written by snappy. 


It was found that:
1. The bandnames wroten by gdal can be read correctly by gdal, but cannot be read by SNAP software or with snappy.
2. The bandnames wroten by snappy can be read with snappy and displaied in SNAP, but cannot read by gdal.

And I haven't found a solution to write bandname into a tif that can be correctly read by both gdal and snappy (SNAP).
