

# Hex IP to raw ip address ( FFFFFF00 --> A.B.C.D )
join '.', unpack "C*", pack "H*", $ip;

# Hex STRING to RAW STRING ( two hex bytes ->> 1 raw byte )
$string =~ s/([a-fA-F0-9][a-fA-F0-9])/chr(hex($1))/eg;
