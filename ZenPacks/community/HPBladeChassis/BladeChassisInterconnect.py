from Globals import InitializeClass
# from AccessControl import ClassSecurityInfo

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenUtils.Utils import convToUnits

from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS, ZEN_CHANGE_DEVICE

_kw = dict(mode='w')

class BladeChassisInterconnect(DeviceComponent, ManagedEntity):
    "Blade Chassis Interconnect Information"
    
    portal_type = meta_type = 'BladeChassisInterconnect'

    bciNumber = -1
    bciType = ""
    bciProductName = ""
    bciStatus = ""
    bciMgmtIp = ""
    bciSerialNum = ""
    bciPartNumber = ""
    bciSparePartNumber = ""

    _properties = (
	dict(id='bciNumber', type='int',  **_kw),
	dict(id='bciType', type='string',  **_kw),
	dict(id='bciProductName', type='string',  **_kw),
	dict(id='bciStatus', type='string',  **_kw),
    dict(id='bciMgmtIp', type='string', **_kw),
	dict(id='bciSerialNum', type='string',  **_kw),
	dict(id='bciPartNumber', type='string',  **_kw),
	dict(id='bciSparePartNumber', type='string',  **_kw)
    )

    _relations = (
	('bladechassis', ToOne(ToManyCont, 'ZenPacks.community.HPBladeChassis.BladeChassis', 'bladechassisinterconnects')),
    )

    # Screen action bindings (and tab definitions)
    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
        },),
    },)

    def device(self):
	return self.bladechassis()

    def managedDeviceLink(self):
	from Products.ZenModel.ZenModelRM import ZenModelRM
	d = self.getDmdRoot("Devices").findDevice(self.bsProductName)
	if d:
	    return ZenModelRM.urlLink(d, 'link')
	return None

    def snmpIgnore(self):
	return ManagedEntity.snmpIgnore(self) or self.snmpindex < 0

    

InitializeClass(BladeChassisInterconnect)
