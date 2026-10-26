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
                ops = [operator.add, operator.sub, operator.mul, operator.truediv]
                if b == 0:
                    ops.remove(operator.truediv)
                return random.choice(ops)(a, b)

            return calc
        return ret
