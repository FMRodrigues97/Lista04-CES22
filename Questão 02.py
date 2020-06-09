class PizzaComponent:
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class Dish(PizzaComponent):
    cost = 0.0


class Decorator(PizzaComponent):
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + " " + PizzaComponent.getDescription(self)


class Massa(Decorator):
    cost = 9.90

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Queijo(Decorator):
    cost = 6.90

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Calabresa(Decorator):
    cost = 7.90

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Oregano(Decorator):
    cost = 1.20

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Tomate(Decorator):
    cost = 4.90

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Cebola(Decorator):
    cost = 5.90

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Molho(Decorator):
    cost = 3.90

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Rucula(Decorator):
    cost = 3.90

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Chocolate(Decorator):
    cost = 15.90

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


calabresa = Calabresa(Cebola(Queijo(Oregano(Molho(Massa(Dish()))))))
print("Calabresa:" + calabresa.getDescription() + ": R$" + str(calabresa.getTotalCost()))

doce = Chocolate(Massa(Dish()))
print("Doce: " + doce.getDescription() + ": R$" + str(doce.getTotalCost()))

vegana = Rucula(Cebola(Oregano(Tomate(Molho(Massa(Dish()))))))
print("Vegana:" + vegana.getDescription() + ": R$" + str(vegana.getTotalCost()))
