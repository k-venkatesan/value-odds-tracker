from behave import given, when, then
from system.components.model.model import Model


@given(u'the model component')
def step_impl(context):
    context.component = Model()

@when(u'the component starts up')
def step_impl(context):
    pass

@then(u'the initialisation message is displayed')
def step_impl(context):
    if (context.component.get_initialisation_string == "Oddspedia Analyser initialising"):
        print(u'Correct initialisation string')
        pass
    else :
        raise Exception ("Invalid initialisation string")
