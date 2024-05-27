#Ramazan Yıldız
#220709024
#Context Free Form to Chomsky Normal Form Converter

class cfg_to_cnf:
    def __init__(self,productions):
        self.productions = productions
        self.variables = []
        self.terminals = []
        self.new_productions = {}
        self.starting_symbol = None
        self.add_new_start()
        self.remove_null_productions()
        self.dict_to_cfg()
        self.print_grammar()


    def dict_to_cfg(self):

        self.starting_symbol = list(self.productions.keys())[0]

        for left_hs, right_hs in self.productions.items():
            if left_hs not in self.variables:
                self.variables.append(left_hs)

            for element in right_hs:
                for symbol in element:
                    if symbol.islower():
                        if symbol not in self.terminals:
                            self.terminals.append(symbol)
                    else:
                        if symbol not in self.variables:
                            self.variables.append(symbol)

        print(f"terminals are: {self.terminals}")
        print(f"variables are: {self.variables}")


    def add_new_start(self):
        new_start = {}
        for left_hs, right_hs in self.productions.items():
            for element in right_hs:
                for letter in element:
                    if letter == "S":
                        new_start = {"Z": ["S"]}
        print("ne")
        self.productions = {**new_start, **self.productions}

    def remove_null_productions(self):
        nullable = []
        for left_hs, right_hs in self.productions.items():
            for element in right_hs:
                if element == '𝛜':
                    if left_hs not in nullable:
                        nullable.append(left_hs)
                    break
        print(f"nullables variables are: {nullable}")

        for null_sym in nullable:
            for left_hs, right_hs in self.productions.items():
                for element in right_hs:
                    for variable in element:
                        if null_sym == variable:
                            print(f"left hs is {left_hs} right hs is: {right_hs}, element is {element}, variable is {variable} and null_sym is {null_sym}")




    def get_new_variable(self):
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if letter not in self.variables:
                return letter

    def print_grammar(self):
        all_left_hs = []
        for left_hs, right_hs in self.productions.items():
            all_left_hs.append(left_hs)
            rhs_at_once = ""
            a_list = []
            for prod in right_hs:
                a_list.append(f"{''.join(prod)}")
            rhs_at_once = "|".join(a_list)
            print(f"{left_hs} -> {''.join(rhs_at_once)}")

epsilon_sym = '𝛜'
example_productions = {
    'S': ['ASA', 'aB'],
    'A': ['B', 'S'],
    'B': ['b', '𝛜'],
    'C': ['c', '𝛜'],
    'D': ['d', 'C']
}

cnf_converter = cfg_to_cnf(example_productions)

print(cnf_converter.productions)
