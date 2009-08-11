'''Adding support to termcolor.
Failures and errors are red and sucessful is green.


>>> SupportToTermcolor.run()
...
>>> colored_output2 = """Story: Support to termcolor
... As a pyhistorian commiter
... I want to have support to colored output
... So that the output becomes more readable
... 
... Scenario 1: Green color
... """+green_output+"""
... Scenario 2: Red color
... """+red_output+"""
... Scenario 3: Green and red colors
... """+green_and_red_output+"""
... Ran 3 scenarios with 3 failures, 0 errors and 0 steps pending
... """
>>> colored_output2 in output.getvalue()
True
'''

from pyhistorian import *
from should_dsl import *
from cStringIO import StringIO
from termcolor import colored

class GreenColor(Scenario):
    @Given('I want my output colored and it pass')
    def nothing(self):
        pass

    @Then('I have green messages')
    def nothing2(self):
        pass

class RedColor(Scenario):
    @Given('I want my output colored and it fails')
    def fail1(self):
         'this scenario' |should_be| 'red colored'

    @Then('I have red messages')
    def fail2(self):
        'this fail color' |should_be| 'red'


class GreenAndRedColors(Scenario):
   @Given('I want my output colored (green and red)')
   def nothing(self):
       pass

   @Then('I have green message')
   def green_message(self):
       pass

   @Then('I have red message')
   def red_message(self):
       'this step' |should_be| 'red'


def red_colored(text):
    return colored(text, color='red')

def green_colored(text):
    return colored(text, color='green')

output = StringIO()

class SupportToTermcolor(Story):
    """As a pyhistorian commiter
       I want to have support to colored output
       So that the output becomes more readable"""
    output = output
    colored = True
    scenarios = (GreenColor, RedColor, GreenAndRedColors)

green_output = green_colored('\
  Given I want my output colored and it pass   ... OK\n')+ \
  green_colored('\
  Then I have green messages   ... OK\n')

red_output = red_colored('\
  Given I want my output colored and it fails   ... FAIL\n')+ \
  red_colored('\
  Then I have red messages   ... FAIL\n') +\
  red_colored('\nFailures:\n')+\
  red_colored("""  File "/home/hugo/pyhistorian/src/tests/colors.py", line 41, in fail1
    'this scenario' |should_be| 'red colored'
  File "/home/hugo/virtualenv2_5/lib/python2.5/site-packages/should_dsl-1.0-py2.5.egg/should_dsl/should_dsl.py", line 25, in __or__
    return self._check_expectation()
  File "/home/hugo/virtualenv2_5/lib/python2.5/site-packages/should_dsl-1.0-py2.5.egg/should_dsl/should_dsl.py", line 111, in _check_expectation
    self._rvalue))
  ShouldNotSatisfied: this scenario is not red colored

""")+\
  red_colored("""  File "/home/hugo/pyhistorian/src/tests/colors.py", line 45, in fail2
    'this fail color' |should_be| 'red'
  File "/home/hugo/virtualenv2_5/lib/python2.5/site-packages/should_dsl-1.0-py2.5.egg/should_dsl/should_dsl.py", line 25, in __or__
    return self._check_expectation()
  File "/home/hugo/virtualenv2_5/lib/python2.5/site-packages/should_dsl-1.0-py2.5.egg/should_dsl/should_dsl.py", line 111, in _check_expectation
    self._rvalue))
  ShouldNotSatisfied: this fail color is not red

""")
green_and_red_output = green_colored('\
  Given I want my output colored (green and red)   ... OK\n')+\
  green_colored('\
  Then I have green message   ... OK\n') + \
  red_colored('\
  And I have red message   ... FAIL\n') +\
  red_colored('\nFailures:\n') + \
  red_colored("""  File "/home/hugo/pyhistorian/src/tests/colors.py", line 59, in red_message
    'this step' |should_be| 'red'
  File "/home/hugo/virtualenv2_5/lib/python2.5/site-packages/should_dsl-1.0-py2.5.egg/should_dsl/should_dsl.py", line 25, in __or__
    return self._check_expectation()
  File "/home/hugo/virtualenv2_5/lib/python2.5/site-packages/should_dsl-1.0-py2.5.egg/should_dsl/should_dsl.py", line 111, in _check_expectation
    self._rvalue))
  ShouldNotSatisfied: this step is not red

""")
