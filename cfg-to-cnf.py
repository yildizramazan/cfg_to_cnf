
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
        nullable = set()
        for lhs, rhs in self.productions.items():
            for prod in rhs:
                if prod == '𝛜':
                    rhs.remove('𝛜')
                    nullable.add(lhs)
                    break

        while True:
            new_nullable = set(nullable)
            for lhs, rhs in self.productions.items():
                for prod in rhs:
                    if all(symbol in nullable for symbol in prod):
                        new_nullable.add(lhs)
            if new_nullable == nullable:
                break
            nullable = new_nullable

        new_productions = {}
        for lhs, rhs in self.productions.items():
            new_rhs = []
            for prod in rhs:
                if prod != '':
                    new_rhs.append(prod)
                subsets = self.all_combinations(prod, nullable)
                for subset in subsets:
                    if subset and subset != prod:
                        new_rhs.append(subset)
            new_productions[lhs] = list(set(new_rhs))
        self.productions = new_productions

    def all_combinations(self, prod, nullable):
        if not prod:
            return []
        results = [[]]
        for symbol in prod:
            if symbol in nullable:
                results = [result + [symbol] for result in results] + results
            else:
                results = [result + [symbol] for result in results]
        return [''.join(result) for result in results]





    def get_new_variable(self):
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if letter not in self.variables:
                return letter

    def print_grammar(self):
        all_left_hs = []
        for left_hs, right_hs in self.productions.items():
            all_left_hs.append(left_hs)
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


example_null_removal = {
    'S': ['ABAC'],
    'A': ['aA', '𝛜'],
    'B': ['bB', '𝛜'],
    'C': ['c']
}
cnf_converter = cfg_to_cnf(example_null_removal)

print(cnf_converter.productions)
