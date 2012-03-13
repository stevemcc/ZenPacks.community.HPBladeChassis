
from zope.component import adapts
from zope.interface import implements

from Products.ZenUtils.Utils import convToUnits
from Products.Zuul.decorators import info
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from Products.Zuul.infos.component import ComponentInfo

from .BladeChassis import BladeChassis
from .BladeChassisFan import BladeChassisFan
from .BladeChassisPsu import BladeChassisPsu
from .BladeChassisInterconnect import BladeChassisInterconnect
from .BladeServer import BladeServer

from .interfaces import IBladeServerInfo, IBladeChassisInfo, IBladeChassisFanInfo, IBladeChassisPsuInfo, IBladeChassisInterconnectInfo


class BladeChassisComponentInfo(ComponentInfo):
    @property
    def entity(self):
        return {
            'uid': self._object.getPrimaryUrlPath(),
            'name': self._object.titleOrId(),
            }


class BladeChassisInfo(DeviceInfo):
    implements(IBladeChassisInfo)
    adapts(BladeChassis)

    bcEnclosureName = ProxyProperty('bcEnclosureName')
    bcEnclosureType = ProxyProperty("bcEnclosureType")
    bcPartNumber = ProxyProperty("bcPartNumber")
    bcSerialNumber = ProxyProperty("bcSerialNumber")
    bcUUID = ProxyProperty("bcUUID")
    bcAssetTag = ProxyProperty("bcAssetTag")
    bcMidplaneSparePartNumber = ProxyProperty("bcMidplaneSparePartNumber")
    bcPduType = ProxyProperty("bcPduType")
    bcPduSparePartNumber = ProxyProperty("bcPduSparePartNumber")
    bcOATrayType = ProxyProperty("bcOATrayType")
    bcOATraySparePartNumber = ProxyProperty("bcOATraySparePartNumber")
    bcOATraySerialNumber = ProxyProperty("bcOATraySerialNumber")

class BladeChassisFanInfo(BladeChassisComponentInfo):
    implements(IBladeChassisFanInfo)
    adapts(BladeChassisFan)

    bcfNumber = ProxyProperty("bcfNumber")
    bcfProductName = ProxyProperty("bcfProductName")
    bcfStatus = ProxyProperty("bcfStatus")
    bcfPartNumber = ProxyProperty("bcfPartNumber")
    bcfSparePartNumber = ProxyProperty("bcfSparePartNumber")
    bcfProductVersion = ProxyProperty("bcfProductVersion")

class BladeChassisPsuInfo(BladeChassisComponentInfo):
    implements(IBladeChassisPsuInfo)
    adapts(BladeChassisPsu)

    bcpNumber = ProxyProperty("bcpNumber")
    bcpProductName = ProxyProperty("bcpProductName")
    bcpStatus = ProxyProperty("bcpStatus")
    bcpCapacity = ProxyProperty("bcpCapacity")
    bcpSerialNum = ProxyProperty("bcpSerialNum")
    bcpPartNumber = ProxyProperty("bcpPartNumber")
    bcpSparePartNumber = ProxyProperty("bcpSparePartNumber")
    bcpProductVersion = ProxyProperty("bcpProductVersion")

class BladeChassisInterconnectInfo(BladeChassisComponentInfo):
    implements(IBladeChassisInterconnectInfo)
    adapts(BladeChassisInterconnect)
    bciNumber = ProxyProperty("bciNumber")
    bciType = ProxyProperty("bciType")
    bciProductName = ProxyProperty("bciProductName")
    bciStatus = ProxyProperty("bciStatus")
    bciMgmtIp = ProxyProperty("bciMgmtIp")
    bciSerialNum = ProxyProperty("bciSerialNum")
    bciPartNumber = ProxyProperty("bciPartNumber")
    bciSparePartNumber = ProxyProperty("bciSparePartNumber")

class BladeServerInfo(BladeChassisComponentInfo):
    implements(IBladeServerInfo)
    adapts(BladeServer)

    bsDisplayName = ProxyProperty("bsDisplayName")
    bsId = ProxyProperty("bsId")
    bsPosition = ProxyProperty("bsPosition")
    bsHeight = ProxyProperty("bsHeight")
    bsWidth = ProxyProperty("bsWidth")
    bsDepth = ProxyProperty("bsDepth")
    bsSlotsUsed = ProxyProperty("bsSlotsUsed")
    bsSerialNum = ProxyProperty("bsSerialNum")
    bsProductId = ProxyProperty("bsProductId")
    bsPartNumber = ProxyProperty("bsPartNumber")
    bsSystemBoardPartNum = ProxyProperty("bsSystemBoardPartNum")
    bsCPUType = ProxyProperty("bsCPUType")
    bsCPUCount = ProxyProperty("bsCPUCount")
    bsNic1Mac = ProxyProperty("bsNic1Mac")
    bsNic2Mac = ProxyProperty("bsNic2Mac")
    bsIloIp = ProxyProperty("bsIloIp")
    bsInstalledRam = ProxyProperty("bsInstalledRam")
    bsIloFirmwareVersion = ProxyProperty("bsIloFirmwareVersion")

