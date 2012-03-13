from Products.ZenReports import Utils


class HPBladeSrvList:

    def run(self, dmd, args):
        report = []
        for device in  reduce(lambda x, y: x+y,map(lambda x: x.bladeservers(), dmd.Devices.BladeChassis.HPBladeChassis.getSubDevicesGen())):
            report.append(Utils.Record(
                bsId=device.titleOrId(),
                bsDisplayName=device.bsDisplayName,
                bsProductId=device.bsProductId,
                bsSerialNum=device.bsSerialNum,
                bsCPUCount=device.bsCPUCount,
                bsInstalledRam=device.bsInstalledRam,
                bsIloIp=device.bsIloIp,
                ))

        return report
