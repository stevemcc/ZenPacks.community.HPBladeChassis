from Globals import InitializeClass
from Products.ZenModel.Device import Device
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import *

import copy

class BladeChassis(Device):
    "HP Blade Chassis Device"

    portal_type = meta_type = 'BladeChassis'

    bcEnclosureName = ""
    bcEnclosureType = ""
    bcPartNumber = ""
    bcSerialNumber = ""
    bcUUID = ""
    bcAssetTag = ""
    bcMidplaneSparePartNumber = ""
    bcPduType = ""
    bcPduSparePartNumber = ""
    bcOATrayType = ""
    bcOATraySparePartNumber = ""
    bcOATraySerialNumber = ""

    _relations = Device._relations + (
	('bladeservers', ToManyCont(ToOne, "ZenPacks.community.HPBladeChassis.BladeServer", "bladechassis")),
    ) + (
	('bladechassisfans', ToManyCont(ToOne, "ZenPacks.community.HPBladeChassis.BladeChassisFan", "bladechassis")),
    ) + (
	('bladechassisinterconnects', ToManyCont(ToOne, "ZenPacks.community.HPBladeChassis.BladeChassisInterconnect", "bladechassis")),
    ) + (
	('bladechassispsus', ToManyCont(ToOne, "ZenPacks.community.HPBladeChassis.BladeChassisPsu", "bladechassis")),
    ) 
    
    factory_type_information = (
        {
            'id'             : 'Device',
            'meta_type'      : 'Device',
            'description'    : """Base class for all devices""",
            'icon'           : 'Device_icon.gif',
            'product'        : 'ZenModel',
            'factory'        : 'manage_addDevice',
            'immediate_view' : 'devicedetail',
            'actions'        :
            (
                {'id'           : 'bladechassisData'
                 , 'name'       : 'Chassis Details'
                 , 'action'     : 'bladechassisData'
                 , 'permissions': (ZEN_VIEW, )
                },
                { 'id'            : 'events'
                , 'name'          : 'Events'
                , 'action'        : 'viewEvents'
                , 'permissions'   : (ZEN_VIEW, )
                },
                { 'id'            : 'perfServer'
                , 'name'          : 'Graphs'
                , 'action'        : 'viewDevicePerformance'
                , 'permissions'   : (ZEN_VIEW, )
                },
                { 'id'            : 'edit'
                , 'name'          : 'Edit'
                , 'action'        : 'editDevice'
                , 'permissions'   : (ZEN_CHANGE_DEVICE,)
                },
            )
         },
        )


InitializeClass(BladeChassis)
