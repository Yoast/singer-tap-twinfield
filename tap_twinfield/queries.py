"""Twinfield browse queries."""
# -*- coding: utf-8 -*-

from types import MappingProxyType

QUERIES: MappingProxyType = MappingProxyType({
    '410': """
 <columns code="410">
    <column id="1">
        <field>fin.trs.head.yearperiod</field>
        <label>Periode</label>
        <visible>true</visible>
        <ask>true</ask>
        <operator>between</operator>
        <from>:period_lower:</from>
        <to>:period_upper:</to>
        <finderparam/>
    </column>
    <column id="2">
        <field>fin.trs.head.bankcode</field>
        <label>Bank</label>
        <visible>false</visible>
        <ask>true</ask>
        <operator>equal</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="3">
        <field>fin.trs.head.code</field>
        <label>Bank</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="4">
        <field>fin.trs.head.shortname</field>
        <label>Naam</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="5">
        <field>fin.trs.head.number</field>
        <label>Boekst.nr.</label>
        <visible>true</visible>
        <ask>true</ask>
        <operator>between</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="6">
        <field>fin.trs.head.stmnumber</field>
        <label>Afschriftnr.</label>
        <visible>true</visible>
        <ask>true</ask>
        <operator>between</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="7">
        <field>fin.trs.line.dim1</field>
        <label>Grootboek</label>
        <visible>true</visible>
        <ask>true</ask>
        <operator>equal</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="8">
        <field>fin.trs.line.dim1name</field>
        <label>Naam</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="9">
        <field>fin.trs.head.curcode</field>
        <label>Valuta</label>
        <visible>true</visible>
        <ask>true</ask>
        <operator>equal</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="10">
        <field>fin.trs.line.valuesigned</field>
        <label>Bedrag</label>
        <visible>true</visible>
        <ask>true</ask>
        <operator>between</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="11">
        <field>fin.trs.line.basevaluesigned</field>
        <label>Euro</label>
        <visible>true</visible>
        <ask>true</ask>
        <operator>between</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="12">
        <field>fin.trs.line.repvaluesigned</field>
        <label/>
        <visible>false</visible>
        <ask>false</ask>
        <operator>between</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="13">
        <field>fin.trs.head.startvalue</field>
        <label>Vorig saldo</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="14">
        <field>fin.trs.head.closevalue</field>
        <label>Eindsaldo</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="15">
        <field>fin.trs.head.status</field>
        <label>Status</label>
        <visible>true</visible>
        <ask>true</ask>
        <operator>equal</operator>
        <from>normal</from>
        <to/>
        <finderparam/>
    </column>
    <column id="16">
        <field>fin.trs.head.banktype</field>
        <label>Banktype</label>
        <visible>false</visible>
        <ask>false</ask>
        <operator>equal</operator>
        <from>bank</from>
        <to/>
        <finderparam/>
    </column>
</columns>
""",
    '030_3': '',
})
