import sublime_plugin
import math


def try_eval(str):
    try:
        return eval(str, {"logit": logit}, {})
    except Exception:
        return None

def logit(x):
    return 1/(1+math.exp(-x))

def eval_expr(orig, i, expr):
    x = try_eval(orig) or 0

    return eval(expr, {"s": orig, "x": x, "i": i, "math": math, "logit": logit}, {})

class ExprInputHandler(sublime_plugin.TextInputHandler):
    def __init__(self, view):
        self.view = view

    def placeholder(self):
        return "Expression"

    def initial_text(self):
        if len(self.view.sel()) == 1:
            return self.view.substr(self.view.sel()[0]).replace("@","").lower()
        elif self.view.sel()[0].size() == 0:
            return "i + 1"
        elif try_eval(self.view.substr(self.view.sel()[0]).replace("@","").lower()) is not None:
            return "x"
        else:
            return "s"

    def preview(self, expr):
        try:
            v = self.view
            s = v.sel()
            count = len(s)
            if count > 5:
                count = 5
            results = [repr(eval_expr(v.substr(s[i]).replace("@","").lower(), i, expr)) for i in range(count)]
            if count != len(s):
                results.append("...")
            return ", ".join(results)
        except Exception:
            return ""

    def validate(self, expr):
        try:
            v = self.view
            s = v.sel()
            for i in range(len(s)):
                dataRaw = v.substr(s[i])
                data = dataRaw.replace("@", "").lower()
                eval_expr(data, i, expr)
            return True
        except Exception:
            return False


class ArithmeticEviewsCommand(sublime_plugin.TextCommand):
    def run(self, edit, expr):
        for i in range(len(self.view.sel())):
            s = self.view.sel()[i]
            dataRaw = self.view.substr(s)
            data = dataRaw.replace("@","").lower()
            self.view.replace(edit, s, str(eval_expr(data, i, expr)))

    def input(self, args):
        return ExprInputHandler(self.view)
