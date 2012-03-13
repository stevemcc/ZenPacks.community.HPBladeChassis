(function(){
var ZC = Ext.ns('Zenoss.component');
ZC.registerName('BladeChassisPsu', _t('Blade Chassis PSU'), _t('Blade Chassis PSUs'));
ZC.registerName('BladeServer', _t('Blade Server'), _t('Blade Servers'));

ZC.BladeChassisPsuPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            autoExpandColumn: 'bcpProductName',
            componentType: 'BladeChassisPsu',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'bcpProductName'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'bcpStatus'},
                {name: 'bcpCapacity'},
                {name: 'bcpSerialNum'},
                {name: 'bcpPartNumber'},
                {name: 'bcpSparePartNumber'},
                {name: 'bcpProductVersion'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('#'),
                width: 50
            },{
                id: 'bcpProductName',
                dataIndex: 'bcpProductName',
                header: _t('Product Name'),
                width: 80
            },{
                id: 'bcpStatus',
                dataIndex: 'bcpStatus',
                header: _t('Status'),
                width: 70
            },{
                id: 'bcpSerialNum',
                dataIndex: 'bcpSerialNum',
                header: _t('Serial Number'),
                width: 120
            },{
                id: 'bcpCapacity',
                dataIndex: 'bcpCapacity',
                header: _t('Capacity'),
                width: 120
            },{
                id: 'bcpPartNumber',
                dataIndex: 'bcpPartNumber',
                header: _t('Part #'),
                width: 120
            },{
                id: 'bcpSparePartNumber',
                dataIndex: 'bcpSparePartNumber',
                header: _t('Spare Part #'),
                width: 120
            },{
                id: 'bcpProductVersion',
                dataIndex: 'bcpProductVersion',
                header: _t('Version'),
                width: 50
            }]
        });
        ZC.BladeChassisPsuPanel.superclass.constructor.call(this, config);
    }
});
Ext.reg('BladeChassisPsuPanel', ZC.BladeChassisPsuPanel);

ZC.BladeServerPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            autoExpandColumn: 'name',
            componentType: 'BladeServer',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'bsId'},
                {name: 'bsDisplayName'},
                {name: 'severity'},
                {name: 'name'},
                {name: 'bsIloIp'},
                {name: 'bsCPUCount'},
                {name: 'bsProductId'},
                {name: 'bsInstalledRam'},
                {name: 'bsSerialNum'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Id'),
            },{
                id: 'bsDisplayName',
                dataIndex: 'bsDisplayName',
                header: _t('Name'),
                width: 200
            },{
                id: 'bsSerialNum',
                dataIndex: 'bsSerialNum',
                header: _t('Serial Number'),
                width: 120
            },{
                id: 'bsCPUCount',
                dataIndex: 'bsCPUCount',
                header: _t('CPU Count'),
                width: 100
            },{
                id: 'bsInstalledRam',
                dataIndex: 'bsInstalledRam',
                header: _t('Installed Ram'),
                width: 150
            },{
                id: 'bsIloIp',
                dataIndex: 'bsIloIp',
                header: _t('ILO IP Adress'),
                width: 120
            }]
        });
        ZC.BladeServerPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('BladeServerPanel', ZC.BladeServerPanel);

ZC.BladeChassisFanPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            autoExpandColumn: 'bcfProductName',
            componentType: 'BladeChassisFan',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'bcfNumber'},
                {name: 'bcfProductName'},
                {name: 'severity'},
                {name: 'bcfStatus'},
                {name: 'bcfPartNumber'},
                {name: 'bcfSparePartNumber'},
                {name: 'bcfProductVersion'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('#'),
                width: 70
            },{
                id: 'bcfProductName',
                dataIndex: 'bcfProductName',
                header: _t('Product Name'),
            },{
                id: 'bcfStatus',
                dataIndex: 'bcfStatus',
                header: _t('Status'),
                width: 70
            },{
                id: 'bcfPartNumber',
                dataIndex: 'bcfPartNumber',
                header: _t('Part Number'),
                sortable: true,
                width: 180
            },{
                id: 'bcfSparePartNumber',
                dataIndex: 'bcfSparePartNumber',
                header: _t('Spare Part Number'),
                sortable: true,
                width: 180
            },{
                id: 'bcfProductVersion',
                dataIndex: 'bcfProductVersion',
                header: _t('Version'),
                sortable: true,
                width: 100
            }]
        });
        ZC.BladeChassisFanPanel.superclass.constructor.call(this, config);
    }
});
Ext.reg('BladeChassisFanPanel', ZC.BladeChassisFanPanel);

ZC.BladeChassisInterconnectPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            autoExpandColumn: 'bciProductName',
            componentType: 'BladeChassisInterconnect',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'bciNumber'},
                {name: 'bciProductName'},
                {name: 'severity'},
                {name: 'bciStatus'},
                {name: 'bciType'},
                {name: 'bciMgmtIp'},
                {name: 'bciSerialNum'},
                {name: 'bciPartNumber'},
                {name: 'bciSparePartNumber'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Bay'),
                width: 70
            },{
                id: 'bciProductName',
                dataIndex: 'bciProductName',
                header: _t('Product Name'),
            },{
                id: 'bciMgmtIp',
                dataIndex: 'bciMgmtIp',
                header: _t('Management IP'),
                width: 200
            },{
                id: 'bciSerialNum',
                dataIndex: 'bciSerialNum',
                header: _t('Serial Number'),
                width: 180
            },{
                id: 'bciPartNumber',
                dataIndex: 'bciPartNumber',
                header: _t('Part Number'),
                width: 180
            },{
                id: 'bciSparePartNumber',
                dataIndex: 'bciSparePartNumber',
                header: _t('bciSparePartNumber'),
                width: 180
            }]
        });
        ZC.BladeChassisInterconnectPanel.superclass.constructor.call(this, config);
    }
});
Ext.reg('BladeChassisInterconnectPanel', ZC.BladeChassisInterconnectPanel);

})();
