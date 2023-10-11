from mycroft import MycroftSkill, intent_handler


class PizzaTypes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('types.pizza.intent')
    def handle_types_pizza(self, message):
        response = ''

        self.speak_dialog('types.pizza', data={
            'response': response
        })


def create_skill():
    return PizzaTypes()

