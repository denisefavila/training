import pytest

from interview.interview.highlight_chemicals import highlight_chemicals


@pytest.mark.parametrize(
    "chemicals, symbols, expected",
    [
        (
            ["Amazon", "Microsoft", "Google"],
            ["I", "Am", "cro", "Na", "le", "abc"],
            ["[Am]azon", "Mi[cro]soft", "Goog[le]"],
        ),
        (["Chemistry", "Physics"], ["Ch", "Phy", "ics"], ["[Ch]emistry", "[Phy]sics"]),
        (
            ["Hydrogen", "Oxygen", "Nitrogen"],
            ["gen", "Oxy", "Hydro"],
            ["Hydro[gen]", "[Oxy]gen", "Nitro[gen]"],
        ),
        (["Amazon"], ["NoMatch"], ["Amazon"]),  # No matches
        (["Amazon"], [], ["Amazon"]),  # No symbols
        ([], ["Am", "azon"], []),  # No chemicals
        (
            ["Amazon", "Google"],
            ["Am", "Go"],
            ["[Am]azon", "[Go]ogle"],
        ),  # Match at the start
        (["Microsoft"], ["soft"], ["Micro[soft]"]),  # Match at the end
        (["Repeat", "Repeat"], ["Re"], ["[Re]peat", "[Re]peat"]),  # Duplicate chemicals
    ],
)
def test_highlight_chemicals(chemicals, symbols, expected):
    result = highlight_chemicals(chemicals, symbols)
    assert result == expected
