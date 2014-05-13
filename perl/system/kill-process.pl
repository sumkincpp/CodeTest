#!/usr/bin/env sh
# $$ -- The process number of the Perl running this script. 

{
  local $SIG{TERM} = "IGNORE";
  kill TERM, $$;
}
