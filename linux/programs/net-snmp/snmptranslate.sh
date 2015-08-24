[root@fedrapg ~]# snmptranslate -On IF-MIB::ifMIB
.1.3.6.1.2.1.31

[root@fedrapg ~]# snmptranslate -Td IF-MIB::ifMIB
IF-MIB::ifMIB
ifMIB MODULE-IDENTITY
  -- FROM       IF-MIB
  DESCRIPTION   "The MIB module to describe generic objects for network
            interface sub-layers.  This MIB is an updated version of
            MIB-II's ifTable, and incorporates the extensions defined in
            RFC 1229."
::= { iso(1) org(3) dod(6) internet(1) mgmt(2) mib-2(1) 31 }

[root@fedrapg ~]# snmptranslate -Of IF-MIB::ifMIB
.iso.org.dod.internet.mgmt.mib-2.ifMIB

[root@fedrapg ~]# snmptranslate -Tp IF-MIB::ifXTable
+--ifXTable(1)
   |
   +--ifXEntry(1)
      |
      +-- -R-- String    ifName(1)
      |        Textual Convention: DisplayString
      |        Size: 0..255
      +-- -R-- Counter   ifInMulticastPkts(2)
      +-- -R-- Counter   ifInBroadcastPkts(3)
      +-- -R-- Counter   ifOutMulticastPkts(4)
      +-- -R-- Counter   ifOutBroadcastPkts(5)
      +-- -R-- Counter64 ifHCInOctets(6)
      +-- -R-- Counter64 ifHCInUcastPkts(7)
      +-- -R-- Counter64 ifHCInMulticastPkts(8)
      +-- -R-- Counter64 ifHCInBroadcastPkts(9)
      +-- -R-- Counter64 ifHCOutOctets(10)
      +-- -R-- Counter64 ifHCOutUcastPkts(11)
      +-- -R-- Counter64 ifHCOutMulticastPkts(12)
      +-- -R-- Counter64 ifHCOutBroadcastPkts(13)
      +-- -RW- EnumVal   ifLinkUpDownTrapEnable(14)
      |        Values: enabled(1), disabled(2)
      +-- -R-- Gauge     ifHighSpeed(15)
      +-- -RW- EnumVal   ifPromiscuousMode(16)
      |        Textual Convention: TruthValue
      |        Values: true(1), false(2)
      +-- -R-- EnumVal   ifConnectorPresent(17)
      |        Textual Convention: TruthValue
      |        Values: true(1), false(2)
      +-- -RW- String    ifAlias(18)
      |        Textual Convention: DisplayString
      |        Size: 0..64
      +-- -R-- TimeTicks ifCounterDiscontinuityTime(19)
               Textual Convention: TimeStamp



[root@fedrapg ~]# snmptranslate -To | head
.1.3
.1.3.6
.1.3.6.1
.1.3.6.1.1
.1.3.6.1.2
.1.3.6.1.2.1
.1.3.6.1.2.1.10
.1.3.6.1.3
.1.3.6.1.4
.1.3.6.1.4.1

[root@fedrapg ~]# snmptranslate -Ts | head
.iso.org
.iso.org.dod
.iso.org.dod.internet
.iso.org.dod.internet.directory
.iso.org.dod.internet.mgmt
.iso.org.dod.internet.mgmt.mib-2
.iso.org.dod.internet.mgmt.mib-2.transmission
.iso.org.dod.internet.experimental
.iso.org.dod.internet.private
.iso.org.dod.internet.private.enterprises
