def highlight_chemicals(chemicals, symbols):
    """
    Given an api which returns an array of chemical names and
    an array of chemical symbols, display the chemical names
    with their symbol surrounded by square brackets:

     Ex:
     Chemicals array: ['Amazon', 'Microsoft', 'Google']
     Symbols: ['I', 'Am', 'cro', 'Na', 'le', 'abc']

     Output:
     [Am]azon, Mi[cro]soft, Goog[le]
    """
    set_symbols = set(symbols)

    result = []
    for chemical in chemicals:
        formatted_chemical = []
        start_index = 0
        while start_index < len(chemical):
            match_found = False

        result.append("".join(formatted_chemical))

    return result
