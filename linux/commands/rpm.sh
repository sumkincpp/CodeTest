[root@meoooww FoundNewDevice]# rpm -qa net-snmp*
net-snmp-libs-5.3.2.2-25.el5_11
net-snmp-libs-5.3.2.2-25.el5_11
net-snmp-utils-5.3.2.2-25.el5_11
net-snmp-5.3.2.2-25.el5_11
[root@meoooww FoundNewDevice]# rpm -qd net-snmp*
package net-snmp* is not installed
[root@meoooww FoundNewDevice]# rpm -qd net-snmp-5.3.2.2-25.el5_11
/usr/share/doc/net-snmp-5.3.2.2/AGENT.txt
/usr/share/doc/net-snmp-5.3.2.2/COPYING
/usr/share/doc/net-snmp-5.3.2.2/ChangeLog.trimmed
/usr/share/doc/net-snmp-5.3.2.2/EXAMPLE.conf
/usr/share/doc/net-snmp-5.3.2.2/FAQ
/usr/share/doc/net-snmp-5.3.2.2/NEWS
/usr/share/doc/net-snmp-5.3.2.2/PORTING
/usr/share/doc/net-snmp-5.3.2.2/README
/usr/share/doc/net-snmp-5.3.2.2/README.agent-mibs
/usr/share/doc/net-snmp-5.3.2.2/README.agentx
/usr/share/doc/net-snmp-5.3.2.2/README.irix
/usr/share/doc/net-snmp-5.3.2.2/README.krb5
/usr/share/doc/net-snmp-5.3.2.2/README.mib2c
/usr/share/doc/net-snmp-5.3.2.2/README.snmpv3
/usr/share/doc/net-snmp-5.3.2.2/README.thread
/usr/share/doc/net-snmp-5.3.2.2/README.tru64
/usr/share/doc/net-snmp-5.3.2.2/TODO
/usr/share/doc/net-snmp-5.3.2.2/ipf-mod.pl
/usr/share/doc/net-snmp-5.3.2.2/passtest
/usr/share/man/man5/mib2c.conf.5.gz
/usr/share/man/man5/snmp.conf.5.gz
/usr/share/man/man5/snmp_config.5.gz
/usr/share/man/man5/snmpd.conf.5.gz
/usr/share/man/man5/snmpd.examples.5.gz
/usr/share/man/man5/snmpd.internal.5.gz
/usr/share/man/man5/snmptrapd.conf.5.gz
/usr/share/man/man5/variables.5.gz
/usr/share/man/man8/snmpd.8.gz
/usr/share/man/man8/snmptrapd.8.gz

[root@meoooww FoundNewDevice]# rpm -q --changelog net-snmp-5.3.2.2-25.el5_11 | head
* Thu Sep 04 2014 Jan Safranek <jsafrane@redhat.com> - 5.3.2.2-25
- another rebuild for 5.11.z

* Sat Aug 30 2014 Jan Safranek <jsafrane@redhat.com> - 5.3.2.2-24
- rebuilt for 5.11.z

* Wed Mar 05 2014 Jan Safranek <jsafrane@redhat.com> - 5.3.2.2-23
- fixed snmptrapd crashing on forwarding SNMPv3 traps (#1133795)

* Wed Mar 05 2014 Jan Safranek <jsafrane@redhat.com> - 5.3.2.2-20.1
