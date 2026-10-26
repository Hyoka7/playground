import ast
import operator
import random
import pyccolo as pyc


class QuestionOP(pyc.BaseTracer):
    global_guards_enabled = False

    op = pyc.AugmentationSpec(
        aug_type=pyc.AugmentationType.binop, token="?", replacement="|"
    )

    def should_instrument_file(self, filename: str):
        return filename.endswith(".py")

    @pyc.before_binop(when=lambda node: isinstance(node.op, ast.BitOr))
    def apply(
        self,
        ret,
        node: ast.BinOp,
        *_,
        **__,
    ):
        if self.op in self.get_augmentations(id(node)):

            def calc(a, b):
                ops = [operator.add, operator.sub, operator.mul, operator.floordiv]
                if b == 0:
                    ops.remove(operator.floordiv)
                selected = random.choice(ops)
                result = selected(a, b)
                symbols = {
                    operator.add: "+",
                    operator.sub: "-",
                    operator.mul: "*",
                    operator.floordiv: "//",
                }
                print(f"{a} {symbols[selected]} {b} = {result}")
                return result

            return calc
        return ret


class DollarOP(pyc.BaseTracer):
    global_guards_enabled = False

    op = pyc.AugmentationSpec(
        aug_type=pyc.AugmentationType.binop,
        token="$",
        replacement="|",
    )

    def should_instrument_file(self, filename):
        return filename.endswith(".py")

    @pyc.before_binop(when=lambda node: isinstance(node.op, ast.BitOr))
    def apply(
        self,
        ret,
        node: ast.BinOp,
        *_,
        **__,
    ):
        if self.op in self.get_augmentations(id(node)):

            def calc(a, b):
                ops = [
                    operator.xor,
                    operator.lshift,
                    operator.rshift,
                ]
                selected = random.choice(ops)
                result = selected(a, b)
                symbols = {
                    operator.xor: "^",
                    operator.lshift: "<<",
                    operator.rshift: ">>",
                }
                print(f"{a} {symbols[selected]} {b} = {result}")
                return result

            return calc
        return ret
