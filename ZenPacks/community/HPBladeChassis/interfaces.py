from Products.Zuul.form import schema
from Products.Zuul.interfaces import IFacade
from Products.Zuul.interfaces import IDeviceInfo
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

class IBladeChassisInfo(IDeviceInfo):
    bcEnclosureName = schema.Text(title=_t(u"Enclosure Name"))
    bcEnclosureType = schema.Text(title=_t(u"Enclosure Type"))
    bcPartNumber = schema.Text(title=_t(u"Part Number"))
    bcSerialNumber = schema.Text(title=_t(u"Serial Number"))
    bcUUID = schema.Text(title=_t(u"UUID"))
    bcAssetTag = schema.Text(title=_t(u"Asset Tag"))
    bcMidplaneSparePartNumber = schema.Text(title=_t(u"Midplane Spare Part Number"))
    bcPduType = schema.Text(title=_t(u"PDU Type"))
    bcPduSparePartNumber = schema.Text(title=_t(u"PDU Space Part Number"))
    bcOATrayType = schema.Text(title=_t(u"Tray Type"))
    bcOATraySparePartNumber = schema.Text(title=_t(u"Tray Spare Part Number"))
    bcOATraySerialNumber = schema.Text(title=_t(u"Tray Serial Number"))

class IBladeChassisFanInfo(IComponentInfo):
    bcfNumber = schema.Int(title=_t(u"Number"))
    bcfProductName = schema.Text(title=_t(u"Product Name"))
    bcfStatus = schema.Text(title=_t(u"Status"))
    bcfPartNumber = schema.Text(title=_t(u"Part Number"))
    bcfSparePartNumber = schema.Text(title=_t(u"Spare Part Number"))
    bcfProductVersion = schema.Text(title=_t(u"Product Version"))

class IBladeChassisPsuInfo(IComponentInfo):
    bcpNumber = schema.Int(title=_t(u"Number"))
    bcpProductName = schema.Text(title=_t(u"Product Name"))
    bcpStatus = schema.Text(title=_t(u"Status"))
    bcpCapacity = schema.Text(title=_t(u"Capacity"))
    bcpSerialNumber = schema.Text(title=_t(u"Serial Number"))
    bcpPartNumber = schema.Text(title=_t(u"Part Number"))
    bcpSparePartNumber = schema.Text(title=_t(u"Spare Part Number"))
    bcpProductVersion = schema.Text(title=_t(u"Product Version"))

class IBladeChassisInterconnectInfo(IComponentInfo):
    bciNumber = schema.Int(title=_t(u"Number"))
    bciType = schema.Text(title=_t(u"Type"))
    componentUid = schema.Text(title=_t(u"Id"))
    bciProductName = schema.Text(title=_t(u"Product Name"))
    bciStatus = schema.Text(title=_t(u"Status"))
    bciMgmtIp = schema.Text(title=_t(u"Management IP"))
    bciSerialNumber = schema.Text(title=_t(u"Serial Number"))
    bciPartNumber = schema.Text(title=_t(u"Part Number"))
    bciSparePartNumber = schema.Text(title=_t(u"Spare Part Number"))

class IBladeServerInfo(IComponentInfo):
    bsDisplayName = schema.Text(title=_t(u"Display Name")) 
    bsId = schema.Text(title=_t(u"Id"))
    bsPosition = schema.Int(title=_t(u"Position"))
    bsHeight = schema.Int(title=_t(u"Height"))
    bsWidth = schema.Int(title=_t(u"Width"))
    bsDepth = schema.Int(title=_t(u"Depth"))
    bsSlotsUsed = schema.Int(title=_t(u"Slots Used"))
    bsSerialNum = schema.Text(title=_t(u"Serial Number")) 
    bsProductId = schema.Text(title=_t(u"Product Id"))
    bsPartNumber = schema.Text(title=_t(u"Part Number"))
    bsSystemBoardPartNum = schema.Text(title=_t(u"System Board Part Number"))
    bsCPUType = schema.Text(title=_t(u"CPU Type"))
    bsCPUCount = schema.Int(title=_t(u"CPU Count"))
    bsNic1Mac = schema.Text(title=_t(u"NIC1 MAC"))
    bsNic2Mac = schema.Text(title=_t(u"NIC2 MAC"))
    bsIloIp = schema.Text(title=_t(u"ILO IP"))
    bsInstalledRam = schema.Int(title=_t(u"Installed Ram"))
    bsIloFirmwareVersion = schema.Text(title=_t(u"Firmware Version"))

