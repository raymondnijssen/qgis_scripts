from qgis.core import QgsVectorLayer, QgsField, QgsProject, QgsFeature

print('loading ScratchLayer class')

class ScratchLayer():

    def __init__(self, iface, name=u'ScratchLayer', featureType=u'LineString'):
 
        self.name = name
        self.featureType = featureType
        
        self.removeAllLayersWithSameName() 
        (self.layer, self.provider) = self.createLayer(iface, name, featureType)

        self.nextId = 0

        
    def createLayer(self, iface, name, featureType, addToMap=True):
        featureType += u'?crs=' + iface.mapCanvas().mapSettings().destinationCrs().authid()
        layer = QgsVectorLayer(featureType, name, 'memory')

        provider = layer.dataProvider()
        
        fields = []
        fields.append(QgsField(u'id', QVariant.LongLong, 'int8'))
        fields.append(QgsField(u'code', QVariant.String))
        provider.addAttributes(fields)
        layer.updateFields()

        if addToMap:
            QgsProject.instance().addMapLayer(layer)

        '''
        if qml_file is not None:
            qml = os.path.join(self.plugin.data_path, qml_file)
            layer.loadNamedStyle(qml)

        if refresh:
            self.plugin.iface.mapCanvas().refreshAllLayers()
        '''

        return (layer, provider)


    def addGeometry(self, geometry, code='', refresh=False):
        feat = QgsFeature()

        feat.setGeometry(geometry)
        attributes = [self.nextId, code]
        self.nextId += 1
        feat.setAttributes(attributes)

        self.provider.addFeatures([feat])
        
        if refresh:
            self.refresh()


    def clear(self):
        featureIds = []
        for feature in self.layer.getFeatures():
            featureIds.append(feature.id())
        self.provider.deleteFeatures(featureIds)
        self.refresh()


    def removeAllLayersWithSameName(self):
        layers = QgsProject.instance().mapLayersByName(self.name)
        for layer in layers:
            QgsProject.instance().removeMapLayer(layer.id())
    
    
    def refresh(self):
        iface.mapCanvas().refreshAllLayers()


