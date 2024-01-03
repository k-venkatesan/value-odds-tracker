def assertEqual(expected, actual):
    if expected != actual:
        raise Exception(
            "Expected and actual results do not match \n"
            "Expected: {} \n"
            "Actual:   {}".format(expected, actual)
        )
