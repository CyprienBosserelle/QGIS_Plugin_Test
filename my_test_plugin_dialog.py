# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MyTestPlGiDialog
                                 A QGIS plugin
 somthing that does things
                             -------------------
        begin                : 2016-06-27
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Cyprien Bosserelle
        email                : cyprienb@spc.int
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.core import QgsMapLayer

from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'my_test_plugin_dialog_base.ui'))


class MyTestPlGiDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, iface, parent=None):
        """Constructor."""
        super(MyTestPlGiDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.iface = iface
        list1 = [
            self.tr('Ikonos'),
            self.tr('Quickbird'),
            self.tr('World View 2'),
        ]

        self.comboBox_sattype.clear()
        self.comboBox_sattype.addItems(list1)

        #self.Combo_LayerItem.clear()
        #self.Combo_LayerItem.addItems(list1)

        self.combo_survey.currentIndexChanged.connect(self.loadlayerattributes)

    def loadlayerattributes(self, number):
        #layerlist = self.iface.mapCanvas().layers()
        self.Combo_LayerItem.clear()
        layerlist = []
        for layer in self.iface.mapCanvas().layers():
            if layer.type() == QgsMapLayer.VectorLayer:
                layerlist.append(layer)

        layer = layerlist[number]

        for field in layer.pendingFields():
            self.Combo_LayerItem.addItem(str(field.name()))



