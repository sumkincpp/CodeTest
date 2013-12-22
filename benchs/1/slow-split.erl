text() ->
    <<"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.">>.

times(0, _) ->
    ok;
times(N, F) ->
    F(),
    times(N - 1, F).

measure(N) ->
    {ok, Pattern} = re:compile("\\s+"),
    B = text(),
    F = fun() -> re:split(B, Pattern) end,
    {T, ok} = timer:tc(?MODULE, times, [N, F]),
    T / 1000000.
