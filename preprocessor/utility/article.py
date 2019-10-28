import preprocessor.utility.constants as CONST

class Article:

    CONST_MAP = {}
    CONST_MAP.update(CONST.keyword_map)
    CONST_MAP.update(CONST.symbol_map)
    CONST_MAP.update(CONST.function_map)
    CONST_MAP.update(CONST.censeo_map)

    BLOCK_BEGIN = "__COLON_LITERAL"
    LINE_END = "__STATEMENT_END_LITERAL"
    BLOCK_END = "__BLOCK_END_LITERAL"
    DOT_SYMBOL = "__DOT_SYMBOL_LITERAL"

    def __init__(self, verbis):
        self.verbis = verbis
        self.structure = []
        self.compiled_lines = []

    def create_structure(self):
        # Grand loop for verbis
        curr_level = 0
        curr_struct = []
        for verbum in self.verbis:
            effectus = self.process_verbum(verbum)
            if effectus in [self.LINE_END, self.BLOCK_END]:
                self.structure.append((curr_struct, curr_level))
                curr_struct = list()
                if effectus == self.BLOCK_END:
                    curr_level -= 1
            elif effectus == self.BLOCK_BEGIN:
                curr_struct.append(":")
                self.structure.append((curr_struct, curr_level))
                curr_level += 1
                curr_struct = list()
            else:
                curr_struct.append(effectus)

    def process_verbum(self, verbum):
        verbum_lower = verbum.lower()
        if verbum_lower in self.CONST_MAP:
            effectus = self.CONST_MAP[verbum_lower]
        else:
            effectus = verbum
        return effectus

    def process_struct_dot_symbol(self, struct):
        processed_struct = []
        struct_len = len(struct)
        pointer = 0
        while pointer < struct_len:
            if struct[pointer] == self.DOT_SYMBOL:
                processed_struct[-1] = processed_struct[-1] + "." + struct[pointer+1]
                pointer += 2
            else:
                processed_struct.append(struct[pointer])
                pointer += 1
        return processed_struct

    def create_output(self):
        for struct, level in self.structure:
            processed_struct = self.process_struct_dot_symbol(struct)
            statement = " " * level * 4 + " ".join(processed_struct)
            self.compiled_lines.append(statement)

    def run(self):
        self.create_structure()
        self.create_output()
        return self.compiled_lines

