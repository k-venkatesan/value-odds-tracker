from behave import given, then
from system.component_tests.utilities.assertion_helpers import assertEqual

from system.components.model.units.oddspedia_analyser import OddspediaAnalyser


@given("the Oddspedia Analyser")
def step_impl(context):
    context.oddspedia_analyser = OddspediaAnalyser()


@then('the initialisation string is "{expected_initialisation_string}"')
def step_impl(context, expected_initialisation_string):
    expected_initialisation_string = str(expected_initialisation_string)
    actual_initialisation_string = (
        context.oddspedia_analyser.get_initialisation_string()
    )

    assertEqual(expected_initialisation_string, actual_initialisation_string)
