from colorama import Fore, init


class Position:

    def __init__(self, trade, order_id):
        self.state = 'open'
        self.enter = trade
        self.exit = None
        self.order_id = order_id

    def close(self, trade):
        self.state = 'closed'
        self.exit = trade

    def print_trade(self):
        init(autoreset=True)  # for auto resetting the color back to default after using colorama

        enter = "Enter: $" + str(self.enter.price) + " | " + str(self.enter.time)
        exit_trade = ("Exit: $" + str(self.exit.price) + " | " + str(self.exit.time)) if self.exit else ""

        if self.state == 'closed':
            prof = self.profit()
            if prof > 0:
                profit = "Profit: " + (Fore.GREEN + '$' + str(prof))
                print(f"{enter} - {exit_trade} - {profit}")
            else:
                loss = "Loss: " + (Fore.RED + "$" + str(prof))
                print(f"{enter} - {exit_trade} - {loss}")
        else:
            print(f"{enter} - {exit_trade}")

    def profit(self):
        fee = 0.0025
        entrance = self.enter.price * (1 + fee)
        if self.exit:
            exit_price = self.exit.price * (1 - fee)
            return exit_price - entrance
        else:
            return 0
