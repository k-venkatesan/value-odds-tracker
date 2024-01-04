import unittest

from system.components.value_odds_aggregator.units.oddspedia_analyser import (
    OddspediaAnalyser,
)


class OddspediaAnalyserTester(unittest.TestCase):
    oddspedia_analyser = OddspediaAnalyser()

    def test_initialisation_string(self):
        self.assertEqual(
            "Oddspedia Analyser initialising",
            self.oddspedia_analyser.get_initialisation_string(),
        )


if __name__ == "__main__":
    unittest.main()
