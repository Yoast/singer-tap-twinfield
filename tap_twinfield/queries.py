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
      <to>:period_lower:</to>
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
        <label>Bank Naam</label>
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
        <label>Grootboek Naam</label>
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
    '030_3': """
<columns code="030_3">
    <column id="1">
        <field>fin.trs.head.office</field>
        <label>Administratie</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="2">
        <field>fin.trs.head.officename</field>
        <label>Adm.naam</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="3">
        <field>fin.trs.head.year</field>
        <label>Jaar</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="4">
        <field>fin.trs.head.period</field>
        <label>Periode</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="5">
        <field>fin.trs.head.yearperiod</field>
        <label>Jaar/periode (JJJJ/PP)</label>
        <visible>false</visible>
        <ask>true</ask>
        <operator>between</operator>
        <from>:period_lower:</from>
        <to>:period_upper:</to>
        <finderparam/>
    </column>
    <column id="6">
        <field>fin.trs.head.code</field>
        <label>Dagboek</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="7">
        <field>fin.trs.head.number</field>
        <label>Boekingsnummer</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="8">
        <field>fin.trs.head.status</field>
        <label>Status</label>
        <visible>true</visible>
        <ask>true</ask>
        <operator>equal</operator>
        <from>normal</from>
        <to/>
        <finderparam/>
    </column>
    <column id="9">
        <field>fin.trs.head.date</field>
        <label>Boekdatum</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="10">
        <field>fin.trs.head.curcode</field>
        <label>Valuta</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="11">
        <field>fin.trs.head.relation</field>
        <label>Relatie</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="12">
        <field>fin.trs.head.relationname</field>
        <label>Relatienaam</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="13">
        <field>fin.trs.head.inpdate</field>
        <label>Invoerdatum</label>
        <visible>true</visible>
        <ask>true</ask>
        <operator>between</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="14">
        <field>fin.trs.head.modified</field>
        <label>Wijzigingsdatum</label>
        <visible>false</visible>
        <ask>true</ask>
        <operator>between</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="15">
        <field>fin.trs.head.username</field>
        <label>Gebruikersnaam</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="16">
        <field>fin.trs.line.dim1</field>
        <label>Grootboekrek.</label>
        <visible>true</visible>
        <ask>true</ask>
        <operator>between</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="17">
        <field>fin.trs.line.dim1name</field>
        <label>Grootboekrek.naam</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="18">
        <field>fin.trs.line.dim1type</field>
        <label>Dimensietype 1</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="19">
        <field>fin.trs.line.dim2</field>
        <label>Kpl./rel.</label>
        <visible>true</visible>
        <ask>true</ask>
        <operator>between</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="20">
        <field>fin.trs.line.dim2name</field>
        <label>Kpl.-/rel.naam</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="21">
        <field>fin.trs.line.dim2type</field>
        <label>Dimensietype 2</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="22">
        <field>fin.trs.line.dim3</field>
        <label>Act./proj.</label>
        <visible>true</visible>
        <ask>true</ask>
        <operator>between</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="23">
        <field>fin.trs.line.dim3name</field>
        <label>Act.-/proj.naam</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="24">
        <field>fin.trs.line.dim3type</field>
        <label>Dimensietype 3</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="25">
        <field>fin.trs.line.valuesigned</field>
        <label>Bedrag</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="26">
        <field>fin.trs.line.basevaluesigned</field>
        <label>Basisbedrag</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="27">
        <field>fin.trs.line.repvaluesigned</field>
        <label>Rapportagebedrag</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="28">
        <field>fin.trs.line.debitcredit</field>
        <label>D/C</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="29">
        <field>fin.trs.line.vatcode</field>
        <label>Btw-code</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="30">
        <field>fin.trs.line.vatbasevaluesigned</field>
        <label>Btw-bedrag</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="31">
            <field>fin.trs.line.quantity</field>
            <label>Aantal</label>
            <visible>true</visible>
            <ask>false</ask>
            <operator>none</operator>
            <from/>
            <to/>
            <finderparam/>
    </column>
    <column id="32">
            <field>fin.trs.line.chequenumber</field>
            <label>Cheque</label>
            <visible>true</visible>
            <ask>false</ask>
            <operator>none</operator>
            <from/>
            <to/>
            <finderparam/>
    </column>
    <column id="33">
        <field>fin.trs.line.description</field>
        <label>Omschrijving</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="34">
        <field>fin.trs.line.invnumber</field>
        <label>Factuurnummer</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="35">
        <field>fin.trs.line.dim1group1</field>
        <label>Groep 1</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="36">
        <field>fin.trs.line.dim1group1name</field>
        <label>Groepnaam 1</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="37">
        <field>fin.trs.line.dim1group2</field>
        <label>Groep 2</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="38">
        <field>fin.trs.line.dim1group2name</field>
        <label>Groepnaam 2</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="39">
        <field>fin.trs.line.dim1group3</field>
        <label>Groep 3</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="40">
        <field>fin.trs.line.dim1group3name</field>
        <label>Groepnaam 3</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="41">
        <field>fin.trs.line.dim1group4</field>
        <label>Groep 4</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="42">
        <field>fin.trs.line.dim1group4name</field>
        <label>Groepnaam 4</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="43">
        <field>fin.trs.line.dim1group5</field>
        <label>Groep 5</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="44">
        <field>fin.trs.line.dim1group5name</field>
        <label>Groepnaam 5</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="45">
        <field>fin.trs.line.freetext1</field>
        <label>Vrij tekstveld 1</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="46">
        <field>fin.trs.line.freetext2</field>
        <label>Vrij tekstveld 2</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="47">
        <field>fin.trs.line.freetext3</field>
        <label>Vrij tekstveld 3</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="48">
      <field>fin.trs.head.origin</field>
        <label>Boekingsoorsprong</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="49">
        <field>fin.trs.mng.type</field>
        <label>transactie type groep</label>
        <visible>true</visible>
        <ask>false</ask>
        <operator>none</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
    <column id="51">
        <field>fin.trs.head.reportingstructure</field>
        <label>Rapportagestructuur</label>
        <visible>false</visible>
        <ask>true</ask>
        <operator>equal</operator>
        <from/>
        <to/>
        <finderparam/>
    </column>
</columns>
""",
    '000': """
<columns code="000">
    <column id="1">
      <field>fin.trs.head.yearperiod</field>
      <label>Periode</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from>:period_lower:</from>
      <to>:period_lower:</to>
      <finderparam/>
    </column>
    <column id="2">
      <field>fin.trs.head.code</field>
      <label>Dagboek</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam>hidden=1</finderparam>
    </column>
    <column id="3">
      <field>fin.trs.head.shortname</field>
      <label>Naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="4">
      <field>fin.trs.head.number</field>
      <label>Boekst.nr.</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="5">
      <field>fin.trs.head.status</field>
      <label>Status</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from>normal</from>
      <to/>
      <finderparam/>
    </column>
    <column id="6">
      <field>fin.trs.line.dim1</field>
      <label>Grootboek</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="7">
      <field>fin.trs.line.dim1name</field>
      <label>Naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="8">
      <field>fin.trs.head.curcode</field>
      <label>Valuta</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="9">
      <field>fin.trs.line.valuesigned</field>
      <label>Bedrag</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="10">
      <field>fin.trs.line.basevaluesigned</field>
      <label>Euro</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="11">
      <field>fin.trs.line.repvaluesigned</field>
      <label/>
      <visible>false</visible>
      <ask>false</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="12">
      <field>fin.trs.line.description</field>
      <label>Omschrijving</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="13">
      <field>fin.trs.head.browseregime</field>
      <label>Regime</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
</columns>
""",
    '010': """
<columns code="010">
    <column id="1">
      <field>fin.trs.head.yearperiod</field>
      <label>Periode</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from>:period_lower:</from>
      <to>:period_lower:</to>
      <finderparam/>
    </column>
    <column id="2">
      <field>fin.trs.line.dim1</field>
      <label>Grootboek</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="3">
      <field>fin.trs.line.dim1name</field>
      <label>Naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="4">
      <field>fin.trs.head.code</field>
      <label>Dagboek</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam>hidden=1</finderparam>
    </column>
    <column id="5">
      <field>fin.trs.head.shortname</field>
      <label>Naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="6">
      <field>fin.trs.head.number</field>
      <label>Boekst.nr.</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="7">
      <field>fin.trs.head.curcode</field>
      <label>Valuta</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="8">
      <field>fin.trs.line.valuesigned</field>
      <label>Bedrag</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="9">
      <field>fin.trs.line.basevaluesigned</field>
      <label>Euro</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="10">
      <field>fin.trs.line.openbasevaluesigned</field>
      <label>Openstaand bedrag</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="11">
      <field>fin.trs.line.matchstatus</field>
      <label>Betaalstatus</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from>available</from>
      <to/>
      <finderparam/>
    </column>
    <column id="12">
      <field>fin.trs.head.status</field>
      <label>Status</label>
      <visible>false</visible>
      <ask>false</ask>
      <operator>equal</operator>
      <from>normal</from>
      <to/>
      <finderparam/>
    </column>
    <column id="13">
      <field>fin.trs.head.browseregime</field>
      <label>Regime</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
</columns>
""",
    '020': """
<columns code="020">
    <column id="1">
      <field>fin.trs.head.yearperiod</field>
      <label>Periode</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from>:period_lower:</from>
      <to>:period_lower:</to>
      <finderparam/>
    </column>
    <column id="2">
      <field>fin.trs.head.typecategory</field>
      <label>Dagboekcategorie</label>
      <visible>false</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="3">
      <field>fin.trs.head.code</field>
      <label>Dagboek</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam>hidden=1</finderparam>
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
      <field>fin.trs.head.status</field>
      <label>Status</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from>normal</from>
      <to/>
      <finderparam/>
    </column>
    <column id="7">
      <field>fin.trs.head.date</field>
      <label>Boekdatum</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="8">
      <field>fin.trs.head.inpdate</field>
      <label>Invoerdatum</label>
      <visible>false</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="9">
      <field>fin.trs.head.modified</field>
      <label>Wijzigingsdatum</label>
      <visible>false</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="10">
      <field>fin.trs.line.dim1</field>
      <label>Grootboek</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="11">
      <field>fin.trs.line.dim2</field>
      <label>Relatie</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="12">
      <field>fin.trs.line.dim3</field>
      <label>Project</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="13">
      <field>fin.trs.head.curcode</field>
      <label>Valuta</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="14">
      <field>fin.trs.line.valuesigned</field>
      <label>Bedrag</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="15">
      <field>fin.trs.line.basevaluesigned</field>
      <label>Euro</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="16">
      <field>fin.trs.line.repvaluesigned</field>
      <label/>
      <visible>false</visible>
      <ask>false</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="17">
      <field>fin.trs.line.invnumber</field>
      <label>Factuurnr.</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="18">
      <field>fin.trs.head.user</field>
      <label>Gebruiker</label>
      <visible>false</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="19">
      <field>fin.trs.head.inpdate</field>
      <label>Invoerdatum</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="20">
      <field>fin.trs.line.description</field>
      <label>Omschrijving</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="21">
      <field>fin.trs.head.browseregime</field>
      <label>Regime</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
</columns>
""",
    '040_1': """
<columns code="040_1">
    <column id="1">
      <field>fin.trs.head.office</field>
      <label>Administratie</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="2">
      <field>fin.trs.head.officename</field>
      <label>Adm.naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="3">
      <field>fin.trs.head.year</field>
      <label>Jaar</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="4">
      <field>fin.trs.head.period</field>
      <label>Periode</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="5">
      <field>fin.trs.head.yearperiod</field>
      <label>Jaar/periode (JJJJ/PP)</label>
      <visible>false</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from>:period_lower:</from>
      <to>:period_lower:</to>
      <finderparam/>
    </column>
    <column id="6">
      <field>fin.trs.head.status</field>
      <label>Status</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from>normal</from>
      <to/>
      <finderparam/>
    </column>
    <column id="7">
      <field>fin.trs.line.dim1</field>
      <label>Grootboekrek.</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="8">
      <field>fin.trs.line.dim1name</field>
      <label>Grootboekrek.naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="9">
      <field>fin.trs.line.dim1type</field>
      <label>Dimensietype 1</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="10">
      <field>fin.trs.line.dim2</field>
      <label>Kpl./rel.</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="11">
      <field>fin.trs.line.dim2name</field>
      <label>Kpl.-/rel.naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="12">
      <field>fin.trs.line.dim2type</field>
      <label>Dimensietype 2</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="13">
      <field>fin.trs.line.dim3</field>
      <label>Act./proj.</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="14">
      <field>fin.trs.line.dim3name</field>
      <label>Act.-/proj.naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="15">
      <field>fin.trs.line.dim3type</field>
      <label>Dimensietype 3</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="16">
      <field>fin.trs.line.basevaluesigned</field>
      <label>Basisbedrag</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="17">
      <field>fin.trs.line.repvaluesigned</field>
      <label>Rapportagebedrag</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="18">
      <field>fin.trs.line.debitcredit</field>
      <label>D/C</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="19">
      <field>fin.trs.line.quantity</field>
      <label>Aantal</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="20">
      <field>fin.trs.line.dim1group1</field>
      <label>Groep 1</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="21">
      <field>fin.trs.line.dim1group1name</field>
      <label>Groepnaam 1</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="22">
      <field>fin.trs.line.dim1group2</field>
      <label>Groep 2</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="23">
      <field>fin.trs.line.dim1group2name</field>
      <label>Groepnaam 2</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="24">
      <field>fin.trs.line.dim1group3</field>
      <label>Groep 3</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="25">
      <field>fin.trs.line.dim1group3name</field>
      <label>Groepnaam 3</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="27">
      <field>fin.trs.line.dim1group4</field>
      <label>Groep 4</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="28">
      <field>fin.trs.line.dim1group4name</field>
      <label>Groepnaam 4</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="29">
      <field>fin.trs.line.dim1group5</field>
      <label>Groep 5</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="30">
      <field>fin.trs.line.dim1group5name</field>
      <label>Groepnaam 5</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="31">
      <field>fin.trs.head.reportingstructure</field>
      <label>Rapportagestructuur</label>
      <visible>false</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
</columns>
""",
    '060': """
<columns code="060">
    <column id="1">
      <field>fin.trs.head.office</field>
      <label>Administratie</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="2">
      <field>fin.trs.head.officename</field>
      <label>Adm.naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="3">
      <field>fin.trs.head.yearperiod</field>
      <label>Jaar/periode (JJJJ/PP)</label>
      <visible>false</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from>:period_lower:</from>
      <to>:period_lower:</to>
      <finderparam/>
    </column>
    <column id="4">
      <field>fin.trs.head.year</field>
      <label>Jaar</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="5">
      <field>fin.trs.head.period</field>
      <label>Periode</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="6">
      <field>fin.trs.line.dim1type</field>
      <label>Type</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="7">
      <field>fin.trs.line.dim1</field>
      <label>Grootboekrek.</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="8">
      <field>fin.trs.line.dim1name</field>
      <label>Grootboekrek.naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="10">
      <field>fin.trs.head.curcode</field>
      <label>Valuta</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="11">
      <field>fin.trs.line.valuesigned</field>
      <label>Bedrag</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="12">
      <field>fin.trs.line.basevaluesigned</field>
      <label>Basisbedrag</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="13">
      <field>fin.trs.line.repvaluesigned</field>
      <label>Rapportagebedrag</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="14">
      <field>fin.trs.line.debitcredit</field>
      <label>D/C</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="16">
      <field>fin.trs.head.status</field>
      <label>Status</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from>normal</from>
      <to/>
      <finderparam/>
    </column>
    <column id="17">
      <field>fin.trs.line.dim1group1</field>
      <label>Groep 1</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="18">
      <field>fin.trs.line.dim1group1name</field>
      <label>Groepnaam 1</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="19">
      <field>fin.trs.line.dim1group2</field>
      <label>Groep 2</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="20">
      <field>fin.trs.line.dim1group2name</field>
      <label>Groepnaam 2</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="21">
      <field>fin.trs.line.dim1group3</field>
      <label>Groep 3</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="22">
      <field>fin.trs.line.dim1group3name</field>
      <label>Groepnaam 3</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="24">
      <field>fin.trs.line.dim1group4</field>
      <label>Groep 4</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="25">
      <field>fin.trs.line.dim1group4name</field>
      <label>Groepnaam 4</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="26">
      <field>fin.trs.line.dim1group5</field>
      <label>Groep 5</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="27">
      <field>fin.trs.line.dim1group5name</field>
      <label>Groepnaam 5</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="28">
      <field>fin.trs.head.reportingstructure</field>
      <label>Rapportagestructuur</label>
      <visible>false</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
</columns>
""",
    '230_2': """
<columns code="230_2">
    <column id="1">
      <field>fin.trs.head.office</field>
      <label>Administratie</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="2">
      <field>fin.trs.head.officename</field>
      <label>Adm.naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="3">
      <field>fin.trs.head.year</field>
      <label>Jaar</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="4">
      <field>fin.trs.head.period</field>
      <label>Periode</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="5">
      <field>fin.trs.head.yearperiod</field>
      <label>Jaar/periode (JJJJ/PP)</label>
      <visible>false</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from>:period_lower:</from>
      <to>:period_lower:</to>
      <finderparam/>
    </column>
    <column id="6">
      <field>fin.trs.head.code</field>
      <label>Dagboek</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>like</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="7">
      <field>fin.trs.head.shortname</field>
      <label>Dagboeknaam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="8">
      <field>fin.trs.head.number</field>
      <label>Boekingsnummer</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="9">
      <field>fin.trs.head.status</field>
      <label>Status</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from>normal</from>
      <to/>
      <finderparam/>
    </column>
    <column id="10">
      <field>fin.trs.head.date</field>
      <label>Boekdatum</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="11">
      <field>fin.trs.line.datedue</field>
      <label>Vervaldatum</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="12">
      <field>fin.trs.line.invnumber</field>
      <label>Factuurnummer</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="13">
      <field>fin.trs.head.curcode</field>
      <label>Valuta</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="14">
      <field>fin.trs.head.modified</field>
      <label>Wijzigingsdatum boeking</label>
      <visible>false</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="15">
      <field>fin.trs.line.dim1</field>
      <label>Grootboekrek.</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="16">
      <field>fin.trs.line.dim1name</field>
      <label>Grootboekrek.naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="17">
      <field>fin.trs.line.dim2</field>
      <label>Kpl./rel.</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="18">
      <field>fin.trs.line.dim2name</field>
      <label>Kpl.-/rel.naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="19">
      <field>fin.trs.line.valuesigned</field>
      <label>Bedrag</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="20">
      <field>fin.trs.line.basevaluesigned</field>
      <label>Basisbedrag</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="21">
      <field>fin.trs.line.repvaluesigned</field>
      <label>Rapportagebedrag</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="22">
      <field>fin.trs.line.openvaluesigned</field>
      <label>Open amount transaction value</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="23">
      <field>fin.trs.line.openbasevaluesigned</field>
      <label>Open amount base value</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="24">
      <field>fin.trs.line.matchstatus</field>
      <label>Betaalstatus</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>equal</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="25">
      <field>fin.trs.line.matchdate</field>
      <label>Betaaldatum</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="26">
      <field>fin.trs.line.matchnumber</field>
      <label>Afletternummer</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="27">
      <field>fin.trs.line.payrun</field>
      <label>Betaalnummer</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="28">
      <field>fin.trs.line.modified</field>
      <label>Wijzigingsdatum</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="29">
      <field>fin.trs.line.freetext1</field>
      <label>Vrij tekstveld 1</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="30">
      <field>fin.trs.line.freetext2</field>
      <label>Vrij tekstveld 2</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="31">
      <field>fin.trs.line.freetext3</field>
      <label>Vrij tekstveld 3</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
</columns>
""",
    '670': """
<columns code="670">
    <column id="1">
      <field>fin.trs.head.office</field>
      <label>Administratie</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="2">
      <field>fin.trs.head.officename</field>
      <label>Adm.naam</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="3">
      <field>fin.trs.head.code</field>
      <label>Dagboek</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="4">
      <field>fin.trs.head.yearperiod</field>
      <label>Jaar/periode (JJJJ/PP)</label>
      <visible>true</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from>:period_lower:</from>
      <to>:period_lower:</to>
      <finderparam/>
    </column>
    <column id="5">
      <field>fin.trs.head.count</field>
      <label>Aantal transacties</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="6">
      <field>fin.trs.head.inpdate</field>
      <label>Invoerdatum</label>
      <visible>false</visible>
      <ask>true</ask>
      <operator>between</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
    <column id="7">
      <field>fin.trs.line.count</field>
      <label>Aantal transactie regels</label>
      <visible>true</visible>
      <ask>false</ask>
      <operator>none</operator>
      <from/>
      <to/>
      <finderparam/>
    </column>
</columns>
""",
})
