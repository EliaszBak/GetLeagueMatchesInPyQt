from functools import partial

class Controller:
    def __init__(self, view):
        self._view = view

        self.connectSignals()

    def connectSignals(self):
        self._view.isLec.stateChanged.connect(partial(self._view.append, 'LEC'))
        self._view.isLck.stateChanged.connect(partial(self._view.append, 'LCK'))
        self._view.isLcs.stateChanged.connect(partial(self._view.append, 'LCS'))
        self._view.isLpl.stateChanged.connect(partial(self._view.append, 'LPL'))
        self._view.isMsi.stateChanged.connect(partial(self._view.append, 'MSI'))
        self._view.isWorlds.stateChanged.connect(partial(self._view.append, 'Worlds'))

        self._view.submitButton.clicked.connect(self._view.setMatches)