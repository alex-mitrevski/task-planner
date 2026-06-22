import uuid

class Action(object):
    def __init__(self):
        self.id = ''
        self.type = ''
        self.goal = ''

class ActionModelLibrary(object):
    @staticmethod
    def get_action_model(action_name: str, action_params: list) -> Action:
        action = Action()
        action.id = str(uuid.uuid4())
        action.type = action_name
        action = getattr(ActionModelLibrary, action_name)(action, action_params)
        return action

    @staticmethod
    def GOTO(action: Action, params: list) -> Action:
        action.goal = params[2]
        return action

    @staticmethod
    def DOCK(action: Action, params: list) -> Action:
        action.goal = params[2]
        return action

    @staticmethod
    def UNDOCK(action: Action, params: list) -> Action:
        return action

    @staticmethod
    def REQUEST_ELEVATOR(action: Action, params: list) -> Action:
        return action

    @staticmethod
    def WAIT_FOR_ELEVATOR(action: Action, params: list) -> Action:
        return action

    @staticmethod
    def ENTER_ELEVATOR(action: Action, params: list) -> Action:
        return action

    @staticmethod
    def RIDE_ELEVATOR(action: Action, params: list) -> Action:
        return action

    @staticmethod
    def EXIT_ELEVATOR(action: Action, params: list) -> Action:
        action.goal = params[2]
        return action
