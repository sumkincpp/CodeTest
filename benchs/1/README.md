# Is Erlang slow?

 - http://erlang.org/mailman/listinfo/erlang-questions

Ruby outputs

  3.180000   0.000000   3.180000 (  3.182452)

Erlang outputs

Erlang R16B03 (erts-5.10.4) [source] [smp:2:2] [async-threads:10] [hipe] [kernel-poll:false]

Eshell V5.10.4  (abort with ^G)
1> test:measure(50000).
18.261952
