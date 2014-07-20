lists:foldl(
  fun(I, Sm) ->
    I + Sum
  end, 
  0,
  [ X || X < lists:seq(1,999), X rem 3 == 0 orelse X rem 5 == 0 ]
).
