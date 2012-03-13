from Globals import InitializeClass
# from AccessControl import ClassSecurityInfo

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenUtils.Utils import convToUnits

from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS, ZEN_CHANGE_DEVICE

_kw = dict(mode='w')

class BladeChassisPsu(DeviceComponent, ManagedEntity):
    "Blade Chassis PSU Information"
    
    portal_type = meta_type = 'BladeChassisPsu'

    bcpNumber = -1
    bcpProductName = ""
    bcpStatus = ""
    bcpCapacity = ""
    bcpSerialNum = ""
    bcpPartNumber = ""
    bcpSparePartNumber = ""
    bcpProductVersion = ""

    _properties = (
	dict(id='bcpNumber', type='int',  **_kw),
	dict(id='bcpProductName', type='string',  **_kw),
    dict(id='bcpStatus', type='string', **_kw),
	dict(id='bcpCapacity', type='string',  **_kw),
	dict(id='bcpSerialNum', type='string',  **_kw),
	dict(id='bcpPartNumber', type='string',  **_kw),
	dict(id='bcpSparePartNumber', type='string',  **_kw),
	dict(id='bcpProductVersion', type='string',  **_kw)
    )

    _relations = (
	('bladechassis', ToOne(ToManyCont, 'ZenPacks.community.HPBladeChassis.BladeChassis', 'bladechassispsus')),
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
    

InitializeClass(BladeChassisPsu)
