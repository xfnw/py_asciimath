import sys


def get_symbols_for(symbol_group, lang_to):  # pragma: no cover
    return {
        k: (
            None
            if lang_to is None
            else (
                v[lang_to]
                if not isinstance(v[lang_to], list)
                else v[lang_to][0]
            )
        )
        for k, v in getattr(sys.modules[__name__], symbol_group).items()
    }


binary_functions = {
    "frac": {"latex": "\\frac", "mathml": "<mfrac>{}{}</mfrac>"},
    "binom": {"latex": "\\binom", "mathml": "<mo>(</mo><mfrac linethickness='0'>{}{}</mfrac><mo>)</mo>"},
    "root": {"latex": "\\sqrt", "mathml": "<mroot>{}{}</mroot>"},
    "stackrel": {"latex": "\\stackrel", "mathml": "<mover>{}{}</mover>"},
    "overset": {"latex": "\\overset", "mathml": "<mover>{}{}</mover>"},
    "underset": {"latex": "\\underset", "mathml": "<munder>{}{}</munder>"},
    "color": {
        "latex": "\\textcolor",
        "mathml": "<mstyle mathcolor='{}'>{}</mstyle>",
    },
}

unary_functions = {
    "sqrt": {"latex": "\\sqrt", "mathml": "<msqrt>{}</msqrt>"},
    "text": {"latex": "\\textrm", "mathml": "<mtext>{}</mtext>"},
    "abs": {"latex": "abs", "mathml": "<mo>|</mo>{}<mo>|</mo>"},
    "floor": {
        "latex": "floor",
        "mathml": "<mo>&lfloor;</mo>{}<mo>&rfloor;</mo>",
    },
    "ceil": {"latex": "ceil", "mathml": "<mo>&lceil;</mo>{}<mo>&rceil;</mo>"},
    "norm": {
        "latex": "norm",
        "mathml": "<mo>&DoubleVerticalBar;</mo>{}<mo>&DoubleVerticalBar;</mo>",
    },
    "ubrace": {
        "latex": "\\underbrace",
        "mathml": "<munder>{}<mo>&#x23DF;</mo></munder>",
    },
    "underbrace": {
        "latex": "\\underbrace",
        "mathml": "<munder>{}<mo>&#x23DF;</mo></munder>",
    },
    "obrace": {
        "latex": "\\overbrace",
        "mathml": "<mover>{}<mo>&#x23DF;</mo></mover>",
    },
    "overbrace": {
        "latex": "\\overbrace",
        "mathml": "<mover>{}<mo>&#x23DF;</mo></mover>",
    },
    "cancel": {
        "latex": "\\cancel",
        "mathml": "<menclose notation='updiagonalstrike'>{}</menclose>",
    },
    "bb": {
        "latex": "\\boldsymbol",
        "mathml": "<mstyle mathvariant='bold'>{}</mstyle>",
    },
    "bbb": {
        "latex": "\\mathbb",
        "mathml": "<mstyle mathvariant='double-struck'>{}</mstyle>",
    },
    "cc": {
        "latex": "\\mathcal",
        "mathml": "<mstyle mathvariant='script'>{}</mstyle>",
    },
    "tt": {
        "latex": "\\texttt",
        "mathml": "<mstyle mathvariant='monospace'>{}</mstyle>",
    },
    "fr": {
        "latex": "\\mathfrak",
        "mathml": "<mstyle mathvariant='fraktur'>{}</mstyle>",
    },
    "sf": {
        "latex": "\\textsf",
        "mathml": "<mstyle mathvariant='sanf-serif'>{}</mstyle>",
    },
    "ul": {
        "latex": "\\underline",
        "mathml": "<munder>{}<mo>&#x332;</mo></munder>",
    },
    "underline": {
        "latex": "\\underline",
        "mathml": "<munder>{}<mo>&#x332;</mo></munder>",
    },
    "bar": {
        "latex": "\\overline",
        "mathml": "<mover>{}<mo>&#x332;</mo></mover>",
    },
    "overline": {
        "latex": "\\overline",
        "mathml": "<mover>{}<mo>&#x332;</mo></mover>",
    },
    "hat": {"latex": "\\hat", "mathml": "<mover>{}<mo>^</mo></mover>"},
    "vec": {
        "latex": "\\vec",
        "mathml": "<mover>{}<mo stretchy='false'>&#x2192;</mo></mover>",
    },
    "dot": {
        "latex": "\\dot",
        "mathml": "<mover>{}<mo stretchy='false'>.</mo></mover>",
    },
    "ddot": {
        "latex": "\\ddot",
        "mathml": "<mover>{}<mo stretchy='false'>..</mo></mover>",
    },
    "dstyle": {
        "latex": "\\displaystyle",
        "mathml": "<mstyle displaystyle='true'>{}</mstyle>",
    },
}

operation_symbols = {
    "+": {"latex": "+", "mathml": "+"},
    "*": {"latex": "\\cdot", "mathml": "&sdot;"},
    "-": {"latex": "-", "mathml": "-"},
    "cdot": {"latex": "\\cdot", "mathml": "&sdot;"},
    "**": {"latex": "\\ast", "mathml": "&ast;"},
    "ast": {"latex": "\\ast", "mathml": "&ast;"},
    "***": {"latex": "\\star", "mathml": "&Star;"},
    "star": {"latex": "\\star", "mathml": "&Star;"},
    "//": {"latex": "/", "mathml": "/"},
    r"\\": {"latex": "\\setminus", "mathml": "&setminus;"},
    "setminus": {"latex": "\\setminus", "mathml": "&setminus;"},
    "xx": {"latex": "\\times", "mathml": "&times;"},
    "times": {"latex": "\\times", "mathml": "&times;"},
    "-:": {"latex": "\\div", "mathml": "&div;"},
    "div": {"latex": "\\div", "mathml": "&div;"},
    "|><": {"latex": "\\ltimes", "mathml": "&ltimes;"},
    "ltimes": {"latex": "\\ltimes", "mathml": "&ltimes;"},
    "><|": {"latex": "\\rtimes", "mathml": "&rtimes;"},
    "rtimes": {"latex": "\\rtimes", "mathml": "&rtimes;"},
    "|><|": {"latex": "\\bowtie", "mathml": "&bowtie;"},
    "bowtie": {"latex": "\\bowtie", "mathml": "&bowtie;"},
    "@": {"latex": "\\circ", "mathml": "&SmallCircle;"},
    "circ": {"latex": "\\circ", "mathml": "&SmallCircle;"},
    "o+": {"latex": "\\oplus", "mathml": "&oplus;"},
    "oplus": {"latex": "\\oplus", "mathml": "&oplus;"},
    "ox": {"latex": "\\otimes", "mathml": "&times;"},
    "otimes": {"latex": "\\otimes", "mathml": "&times;"},
    "o.": {"latex": "\\odot", "mathml": "&odot;"},
    "odot": {"latex": "\\odot", "mathml": "&odot;"},
    "sum": {"latex": "\\sum", "mathml": "&sum;"},
    "prod": {"latex": "\\prod", "mathml": "&prod;"},
    "^^": {"latex": "\\wedge", "mathml": "&wedge;"},
    "wedge": {"latex": "\\wedge", "mathml": "&wedge;"},
    "^^^": {"latex": "\\bigwedge", "mathml": "&bigwedge;"},
    "bigwedge": {"latex": "\\bigwedge", "mathml": "&bigwedge;"},
    "vv": {"latex": "\\vee", "mathml": "&vee;"},
    "vee": {"latex": "\\vee", "mathml": "&vee;"},
    "vvv": {"latex": "\\bigvee", "mathml": "&bigvee;"},
    "bigvee": {"latex": "\\bigvee", "mathml": "&bigvee;"},
    "nn": {"latex": "\\cap", "mathml": "&cap;"},
    "cap": {"latex": "\\cap", "mathml": "&cap;"},
    "nnn": {"latex": "\\bigcap", "mathml": "&bigcap;"},
    "bigcap": {"latex": "\\bigcap", "mathml": "&bigcap;"},
    "uu": {"latex": "\\cup", "mathml": "&cup;"},
    "cup": {"latex": "\\cup", "mathml": "&cup;"},
    "uuu": {"latex": "\\bigcup", "mathml": "&bigcup;"},
    "bigcup": {"latex": "\\bigcup", "mathml": "&bigcup;"},
}

logical_symbols = {
    "and": {"latex": "\\mathmr{and}", "mathml": "and"},
    "or": {"latex": "\\mathmr{and}", "mathml": "or"},
    "not": {"latex": "\\neg", "mathml": "&not;"},
    "neg": {"latex": "\\neg", "mathml": "&not;"},
    "=>": {"latex": "\\implies", "mathml": "&Implies;"},
    "implies": {"latex": "\\implies", "mathml": "&Implies;"},
    "if": {"latex": "\\mathmr{if}", "mathml": "if"},
    "<=>": {"latex": "\\iff", "mathml": "&iff;"},
    "iff": {"latex": "\\iff", "mathml": "&iff;"},
    "AA": {"latex": "\\forall", "mathml": "&ForAll;"},
    "forall": {"latex": "\\forall", "mathml": "&ForAll;"},
    "EE": {"latex": "\\exists", "mathml": "&Exists;"},
    "exists": {"latex": "\\exists", "mathml": "&Exists;"},
    "_|_": {"latex": "\\bot", "mathml": "&bot;"},
    "bot": {"latex": "\\bot", "mathml": "&bot;"},
    "TT": {"latex": "\\top", "mathml": "&top;"},
    "top": {"latex": "\\top", "mathml": "&top;"},
    "|--": {"latex": "\\vdash", "mathml": "&RightTee;"},
    "vdash": {"latex": "\\vdash", "mathml": "&RightTee;"},
    "|==": {"latex": "\\models", "mathml": "&DoubleRightTee;"},
    "models": {"latex": "\\models", "mathml": "&DoubleRightTee;"},
}

relation_symbols = {
    "=": {"latex": "=", "mathml": "="},
    "!=": {"latex": "\\ne", "mathml": "&NotEqual;"},
    "ne": {"latex": "\\ne", "mathml": "&NotEqual;"},
    "<": {"latex": "<", "mathml": "&lt;"},
    "lt": {"latex": "<", "mathml": "&lt;"},
    ">": {"latex": ">", "mathml": "&gt;"},
    "gt": {"latex": ">", "mathml": "&gt;"},
    "<=": {"latex": "\\le", "mathml": "&leq;"},
    "le": {"latex": "\\le", "mathml": "&leq;"},
    ">=": {"latex": "\\ge", "mathml": "&geq;"},
    "ge": {"latex": "\\ge", "mathml": "&geq;"},
    "-<": {"latex": "\\prec", "mathml": "&Precedes;"},
    "prec": {"latex": "\\prec", "mathml": "&Precedes;"},
    "-<=": {"latex": "\\preceq", "mathml": "&PrecedesEqual;"},
    "preceq": {"latex": "\\preceq", "mathml": "&PrecedesEqual;"},
    ">-": {"latex": "\\succ", "mathml": "&Succeeds;"},
    "succ": {"latex": "\\succ", "mathml": "&Succeeds;"},
    ">-=": {"latex": "\\succeq", "mathml": "&SucceedsEqual;"},
    "succeq": {"latex": "\\succeq", "mathml": "&SucceedsEqual;"},
    "in": {"latex": "\\in", "mathml": "&in;"},
    "!in": {"latex": "\\notin", "mathml": "&notin;"},
    "notin": {"latex": "\\notin", "mathml": "&notin;"},
    "sub": {"latex": "\\subset", "mathml": "&subset;"},
    "subset": {"latex": "\\subset", "mathml": "&subset;"},
    "sup": {"latex": "\\supset", "mathml": "&supset;"},
    "supset": {"latex": "\\supset", "mathml": "&supset;"},
    "sube": {"latex": "\\subseteq", "mathml": "&SubsetEqual;"},
    "subseteq": {"latex": "\\subseteq", "mathml": "&SubsetEqual;"},
    "supe": {"latex": "\\supseteq", "mathml": "&SupersetEqual;"},
    "supseteq": {"latex": "\\supseteq", "mathml": "&SupersetEqual;"},
    "-=": {"latex": "\\equiv", "mathml": "&equiv;"},
    "equiv": {"latex": "\\equiv", "mathml": "&equiv;"},
    "~=": {"latex": "\\cong", "mathml": "&cong;"},
    "cong": {"latex": "\\cong", "mathml": "&cong;"},
    "~~": {"latex": "\\approx", "mathml": "&approx;"},
    "approx": {"latex": "\\approx", "mathml": "&approx;"},
    "prop": {"latex": "\\propto", "mathml": "&prop;"},
    "propto": {"latex": "\\propto", "mathml": "&prop;"},
}

function_symbols = {
    "sin": {"latex": "\\sin", "mathml": "sin"},
    "cos": {"latex": "\\cos", "mathml": "cos"},
    "tan": {"latex": "\\tan", "mathml": "tan"},
    "sec": {"latex": "\\sec", "mathml": "sec"},
    "csc": {"latex": "\\csc", "mathml": "csc"},
    "cot": {"latex": "\\cot", "mathml": "cot"},
    "arcsin": {"latex": "\\arcsin", "mathml": "arcsin"},
    "arccos": {"latex": "\\arccos", "mathml": "arccos"},
    "arctan": {"latex": "\\arctan", "mathml": "arctan"},
    "sinh": {"latex": "\\sinh", "mathml": "sinh"},
    "cosh": {"latex": "\\cosh", "mathml": "cosh"},
    "tanh": {"latex": "\\tanh", "mathml": "tanh"},
    "sech": {"latex": "\\sech", "mathml": "sech"},
    "csch": {"latex": "\\csch", "mathml": "csch"},
    "coth": {"latex": "\\coth", "mathml": "coth"},
    "exp": {"latex": "\\exp", "mathml": "exp"},
    "log": {"latex": "\\log", "mathml": "log"},
    "ln": {"latex": "\\ln", "mathml": "ln"},
    "det": {"latex": "\\det", "mathml": "det"},
    "dim": {"latex": "\\dim", "mathml": "dim"},
    "mod": {"latex": "\\mod", "mathml": "mod"},
    "gcd": {"latex": "\\gcd", "mathml": "gcd"},
    "lcm": {"latex": "\\lcm", "mathml": "lcm"},
    "lub": {"latex": "\\lub", "mathml": "lub"},
    "glb": {"latex": "\\glb", "mathml": "glb"},
    "min": {"latex": "\\min", "mathml": "min"},
    "max": {"latex": "\\max", "mathml": "max"},
    "lim": {"latex": "\\lim", "mathml": "lim"},
    "f": {"latex": "f", "mathml": "f"},
    "g": {"latex": "g", "mathml": "g"},
}

greek_letters = {
    "alpha": {"latex": "\\alpha", "mathml": "&alpha;"},
    "beta": {"latex": "\\beta", "mathml": "&beta;"},
    "gamma": {"latex": "\\gamma", "mathml": "&gamma;"},
    "Gamma": {"latex": "\\Gamma", "mathml": "&Gamma;"},
    "delta": {"latex": "\\delta", "mathml": "&delta;"},
    "Delta": {"latex": "\\Delta", "mathml": "&Delta;"},
    "epsilon": {"latex": "\\epsilon", "mathml": "&epsiv;"},
    "varepsilon": {"latex": "\\varepsilon", "mathml": "&varepsilon;"},
    "zeta": {"latex": "\\zeta", "mathml": "&zeta;"},
    "eta": {"latex": "\\eta", "mathml": "&eta;"},
    "theta": {"latex": "\\theta", "mathml": "&theta;"},
    "Theta": {"latex": "\\Theta", "mathml": "&Theta;"},
    "vartheta": {"latex": "\\vartheta", "mathml": "&vartheta;"},
    "iota": {"latex": "\\iota", "mathml": "&iota;"},
    "kappa": {"latex": "\\kappa", "mathml": "&kappa;"},
    "lambda": {"latex": "\\lambda", "mathml": "&lambda;"},
    "Lambda": {"latex": "\\Lambda", "mathml": "&Lambda;"},
    "mu": {"latex": "\\mu", "mathml": "&mu;"},
    "nu": {"latex": "\\nu", "mathml": "&nu;"},
    "xi": {"latex": "\\xi", "mathml": "&xi;"},
    "Xi": {"latex": "\\Xi", "mathml": "&Xi;"},
    "pi": {"latex": "\\pi", "mathml": "&pi;"},
    "Pi": {"latex": "\\Pi", "mathml": "&Pi;"},
    "rho": {"latex": "\\rho", "mathml": "&rho;"},
    "sigma": {"latex": "\\sigma", "mathml": "&sigma;"},
    "Sigma": {"latex": "\\Sigma", "mathml": "&Sigma;"},
    "tau": {"latex": "\\tau", "mathml": "&tau;"},
    "upsilon": {"latex": "\\upsilon", "mathml": "&upsilon;"},
    "phi": {"latex": "\\phi", "mathml": "&phi;"},
    "Phi": {"latex": "\\Phi", "mathml": "&Phi;"},
    "varphi": {"latex": "\\varphi", "mathml": "&varphi;"},
    "chi": {"latex": "\\chi", "mathml": "&chi;"},
    "psi": {"latex": "\\psi", "mathml": "&psi;"},
    "Psi": {"latex": "\\Psi", "mathml": "&Psi;"},
    "omega": {"latex": "\\omega", "mathml": "&omega;"},
    "Omega": {"latex": "\\Omega", "mathml": "&Omega;"},
}

left_parenthesis = {
    "(:": {"latex": "\\langle", "mathml": "&langle;"},
    "(": {"latex": "(", "mathml": "("},
    "[": {"latex": "[", "mathml": "["},
    "{:": {"latex": ".", "mathml": ""},
    "{": {"latex": "\\{", "mathml": "{"},
    "|:": {"latex": "\\vert", "mathml": "&VerticalBar;"},
    "||:": {"latex": "\\lVert", "mathml": "&DoubleVerticalBar;"},
    "langle": {"latex": "\\langle", "mathml": "&langle;"},
    "<<": {"latex": "\\langle", "mathml": "&langle;"},
}

right_parenthesis = {
    ":)": {"latex": "\\rangle", "mathml": "&rangle;"},
    ")": {"latex": ")", "mathml": ")"},
    "]": {"latex": "]", "mathml": "]"},
    ":}": {"latex": ".", "mathml": ""},
    "}": {"latex": "\\}", "mathml": "}"},
    ":|": {"latex": "\\vert", "mathml": "&VerticalBar;"},
    ":||": {"latex": "\\rVert", "mathml": "&DoubleVerticalBar;"},
    "rangle": {"latex": "\\rangle", "mathml": "&rangle;"},
    ">>": {"latex": "\\rangle", "mathml": "&rangle;"},
}

arrows = {
    "uarr": {"latex": "\\uparrow", "mathml": "&uarr;"},
    "uparrow": {"latex": "\\uparrow", "mathml": "&uparrow;"},
    "darr": {"latex": "\\downarrow", "mathml": "&darr;"},
    "downarrow": {"latex": "\\downarrow", "mathml": "&downarrow;"},
    "rarr": {"latex": "\\rightarrow", "mathml": "&rarr;"},
    "rArr": {"latex": "\\Rightarrow", "mathml": "&rArr;"},
    "rightarrow": {"latex": "\\rightarrow", "mathml": "&rightarrow;"},
    "->": {"latex": "\\to", "mathml": "&rightarrow;"},
    "to": {"latex": "\\to", "mathml": "&rightarrow;"},
    ">->": {"latex": "\\rightarrowtail", "mathml": "&rightarrowtail;"},
    "rightarrowtail": {
        "latex": "\\rightarrowtail",
        "mathml": "&rightarrowtail;",
    },
    "->>": {"latex": "\\twoheadrightarrow", "mathml": "&twoheadrightarrow;"},
    "twoheadrightarrow": {
        "latex": "\\twoheadrightarrow",
        "mathml": "&twoheadrightarrow;",
    },
    ">->>": {"latex": "\\twoheadrightarrowtail", "mathml": "&Rarrtl;"},
    "twoheadrightarrowtail": {
        "latex": "\\twoheadrightarrowtail",
        "mathml": "&Rarrtl;",
    },
    "|->": {"latex": "\\mapsto", "mathml": "&mapsto;"},
    "mapsto": {"latex": "\\mapsto", "mathml": "&mapsto;"},
    "larr": {"latex": "\\leftarrow", "mathml": "&larr;"},
    "leftarrow": {"latex": "\\leftarrow", "mathml": "&leftarrow;"},
    "harr": {"latex": "\\leftrightarrow", "mathml": "&harr;"},
    "leftrightarrow": {
        "latex": "\\leftrightarrow",
        "mathml": "&leftrightarrow;",
    },
    "lArr": {"latex": "\\Leftarrow", "mathml": "&lArr;"},
    "Leftarrow": {"latex": "\\Leftarrow", "mathml": "&Leftarrow;"},
    "hArr": {"latex": "\\Leftrightarrow", "mathml": "&hArr;"},
    "Leftrightarrow": {
        "latex": "\\Leftrightarrow",
        "mathml": "&Leftrightarrow;",
    },
}

colors = {
    "red": {"latex": "red", "mathml": "red"},
}

misc_symbols = {
    "^": {"latex": "^", "mathml": "&#x5E;"},
    ",": {"latex": ",", "mathml": ","},
    ".": {"latex": ".", "mathml": "."},
    "_": {"latex": "_", "mathml": "_"},
    "'": {"latex": "'", "mathml": "'"},
    "/": {"latex": "/", "mathml": "/"},
    "|": {"latex": ["|", "\\vert", "\\mid"], "mathml": "|"},
    ":": {"latex": ":", "mathml": ":"},
    "int": {"latex": "\\int", "mathml": "&int;"},
    "integral": {"latex": "\\int", "mathml": "&int;"},
    "oint": {"latex": "\\oint", "mathml": "&conint;"},
    "del": {"latex": "\\partial", "mathml": "&part;"},
    "partial": {"latex": "\\partial", "mathml": "&part;"},
    "grad": {"latex": "\\nabla", "mathml": "&Del;"},
    "nabla": {"latex": "\\nabla", "mathml": "&Del;"},
    "+-": {"latex": "\\pm", "mathml": "&PlusMinus;"},
    "pm": {"latex": "\\pm", "mathml": "&PlusMinus;"},
    "O/": {"latex": "\\emptyset", "mathml": "&emptyset;"},
    "emptyset": {"latex": "\\emptyset", "mathml": "&emptyset;"},
    "oo": {"latex": "\\infty", "mathml": "&infin;"},
    "infty": {"latex": "\\infty", "mathml": "&infin;"},
    "aleph": {"latex": "\\aleph", "mathml": "&aleph;"},
    ":.": {"latex": "\\therefore", "mathml": "&therefore;"},
    "therefore": {"latex": "\\therefore", "mathml": "&therefore;"},
    ":'": {"latex": "\\because", "mathml": "&because;"},
    "because": {"latex": "\\because", "mathml": "&because;"},
    "...": {"latex": "\\ldots", "mathml": "..."},
    "ldots": {"latex": "\\ldots", "mathml": "..."},
    "cdots": {"latex": "\\cdots", "mathml": "&ctdot;"},
    "vdots": {"latex": "\\vdots", "mathml": "&vellip;"},
    "ddots": {"latex": "\\ddots", "mathml": "&dtdot;"},
    "quad": {"latex": "\\quad", "mathml": "&nbsp;"},
    "/_": {"latex": "\\angle", "mathml": "&angle;"},
    "angle": {"latex": "\\angle", "mathml": "&angle;"},
    "frown": {"latex": "\\frown", "mathml": "&frown;"},
    r"/_\\": {"latex": "\\triangle", "mathml": "&bigtriangleup;"},
    "triangle": {"latex": "\\triangle", "mathml": "&bigtriangleup;"},
    "diamond": {"latex": "\\diamond", "mathml": "&diamond;"},
    "square": {"latex": "\\square", "mathml": "&square;"},
    "|__": {"latex": "\\lfloor", "mathml": "&lfloor;"},
    "lfloor": {"latex": "\\lfloor", "mathml": "&lfloor;"},
    "__|": {"latex": "\\rfloor", "mathml": "&rfloor;"},
    "rfloor": {"latex": "\\rfloor", "mathml": "&rfloor;"},
    "|~": {"latex": "\\lceiling", "mathml": "&lceil;"},
    "lceiling": {"latex": "\\lceiling", "mathml": "&lceil;"},
    "~|": {"latex": "\\rceiling", "mathml": "&rceil;"},
    "rceiling": {"latex": "\\rceiling", "mathml": "&rceil;"},
    "CC": {"latex": "\\mathbb{C}", "mathml": "&Copf;"},
    "NN": {"latex": "\\mathbb{N}", "mathml": "&Nopf;"},
    "QQ": {"latex": "\\mathbb{Q}", "mathml": "&Qopf;"},
    "RR": {"latex": "\\mathbb{R}", "mathml": "&Ropf;"},
    "ZZ": {"latex": "\\mathbb{Z}", "mathml": "&Zopf;"},
    "!": {"latex": "!", "mathml": "!"},
}

# matrix2par = {
#     "pmatrix": ["(", ")"],
#     "bmatrix": ["[", "]"],
#     "Bmatrix": ["\{", "\}"],
#     "vmatrix": ["|", "|"],
#     "Vmatrix": ["||", "||"],
# }
