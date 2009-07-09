import sys

class Step(object):
    '''Step is a baseclass for step directives'''

    name = 'step'

    def __init__(self, message, *args):
        self._message = message
        self._args = args
        self._context = sys._getframe(1)
        self._set_step_attrs(self._context.f_locals)
        step = self.__class__.name
        self._steps = self._context.f_locals['_%ss' % step]
        self._steps.append((None, self._message, self._args))

    def _set_step_attrs(self, local_attrs):
        for private_step in ['_givens', '_whens', '_thens']:
            if not private_step in local_attrs:
                local_attrs[private_step] = []

    def __call__(self, method=None):
        del self._steps[-1]
        self._steps.append((method, self._message, self._args))
        return method


# english steps
class Given(Step):
    name = 'given'

class When(Step):
    name = 'when'

class Then(Step):
    name = 'then'


# portuguese steps
class DadoQue(Given):
    '''given in portuguese'''

class Quando(When):
    '''when in portuguese'''

class Entao(Then):
    '''then in portuguese'''


