# Note: Function names are chosen here to match with Python's unittest library
# and may therefore deviate from PEP-8 standards


def assertEqual(expected, actual):
    if expected != actual:
        raise Exception(
            "Expected and actual results do not match \n"
            "Expected: {} \n"
            "Actual:   {}".format(expected, actual)
        )
