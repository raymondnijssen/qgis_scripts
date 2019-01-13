# qgis_scripts
Handy scripts for qgis :)


# scratchlayer.py

## ScratchLayer()

Quickly creates a memory layer for displaying geometries. Choose 'Point',
'LineString' or 'Polygon' for Feature type.

Usage:

```python
# load it easily from any location using:
exec(open("/git/qgis_scripts/scripts/scratchlayer.py").read())

# create layer:
lsl = ScratchLayer('lines', 'LineString')

# add geometries:
lsl.addGeometry(QgsGeometry('LINESTRING((0 0, 1 0, 1 1))', 'line1'))
lsl.addGeometry(QgsGeometry('LINESTRING((1 1, 0 2, 2 2))', 'line2'))

# refresh layer:
lsl.refresh()
```
