# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MyTestPlGi
                                 A QGIS plugin
 somthing that does things
                             -------------------
        begin                : 2016-06-27
        copyright            : (C) 2016 by Cyprien Bosserelle
        email                : cyprienb@spc.int
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MyTestPlGi class from file MyTestPlGi.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .my_test_plugin import MyTestPlGi
    return MyTestPlGi(iface)
