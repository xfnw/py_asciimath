# py_asciimath [![Build Status](https://travis-ci.com/belerico/py_asciimath.svg?branch=mathml)](https://travis-ci.com/belerico/py_asciimath) [![PyPI version](https://badge.fury.io/py/py-asciimath.svg)](https://badge.fury.io/py/py-asciimath)

py_asciimath is a simple yet powerful Python module that can:

* convert an ASCIIMath string to LaTeX or MathML
* convert a MathML string to LaTeX (the conversion is done thank to the [XSLT MathML Library](https://sourceforge.net/projects/xsltml/). Please report any unexpected behavior)

ASCIIMath is an easy-to-write markup language for mathematics: for more information check out the main website at http://asciimath.org/. MathML is a markup language for describing mathematical notation and capturing both its structure and content: for more information check out the main website at https://www.w3.org/TR/MathML3/Overview.html. LaTeX is a high-quality typesetting system: for more information check out the main website at https://www.latex-project.org/.

## Install

To install the package run `pip install -U --user py-asciimath` or `pip3 install -U --user py-asciimath`

## Usage

### As python module
```python
from py_asciimath.parser.parser import (
        ASCIIMath2MathML,
        ASCIIMath2Tex,
        MathML2Tex,
    )


if __name__ == "__main__":
    print("ASCIIMath to MathML")
    asciimath2mathml = ASCIIMath2MathML(log=False, inplace=True)
    parsed = asciimath2mathml.translate(
        r"langle [bigcup Theta CC NN QQ RR ZZ 1,twoheadrightarrowtail cdot 2],"
        r"[rarr 2,int[3(x+1)]dx]:}",
        dtd="mathml2",
        dtd_validation=True,
        network=True,
        displaystyle=True,
        pprint=False,
        xml_pprint=False,
        from_file=False,
    )
    
    print(parsed, "\n\nMathML to LaTeX")
    mathml2tex = MathML2Tex()
    parsed = mathml2tex.translate(parsed, network=False, from_file=False,)

    print(parsed, "\n\nASCIIMath to LaTeX")
    asciimath2tex = ASCIIMath2Tex(log=False, inplace=True)
    parsed = asciimath2tex.translate(
        r"langle [bigcup Theta CC NN QQ RR ZZ 1,twoheadrightarrowtail cdot 2],"
        r"[rarr 2,int[3(x+1)]dx]:}",
        displaystyle=True,
        pprint=False,
        from_file=False,
    )
    print(parsed)
```

results in:

```
ASCIIMath to MathML
INFO:Translating...
INFO:Validating against remote dtd...
INFO:Loading dtd and validating...
<!DOCTYPE math PUBLIC "-//W3C//DTD MathML 2.0//EN" "http://www.w3.org/Math/DTD/mathml2/mathml2.dtd">
<math xmlns="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink"><mstyle displaystyle="true"><mrow><mo>&langle;</mo><mtable><mtr><mtd><mo>&bigcup;</mo><mo>&Theta;</mo><mo>&Copf;</mo><mo>&Nopf;</mo><mo>&Qopf;</mo><mo>&Ropf;</mo><mo>&Zopf;</mo><mn>1</mn></mtd><mtd><mo>&Rarrtl;</mo><mo>&sdot;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>&rarr;</mo><mn>2</mn></mtd><mtd><mo>&Integral;</mo><mrow><mo>[</mo><mrow><mn>3</mn><mrow><mo>(</mo><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mo>)</mo></mrow></mrow><mo>]</mo></mrow><mi>dx</mi></mtd></mtr></mtable><mo/></mrow></mstyle></math> 

MathML to LaTeX
INFO:Translating...
WARNING:Remote DTD found and network is False: replacing with local DTD
INFO:Validating against local dtd...
INFO:Loading dtd and validating...
INFO:Translating...
$ {\displaystyle \langle \begin{array}{cc}\bigcup \Theta \mathbb{C} \mathbb{N}\mathbb{Q}\mathbb{R} \mathbb{Z}1& \twoheadrightarrowtail \cdot 2\\ \to 2& \int \left[3\left(x+1\right)\right]\mathrm{dx}\end{array}}$ 

ASCIIMath to LaTeX
INFO:Translating...
\[\left\langle \begin{matrix}\bigcup \Theta \mathbb{C} \mathbb{N} \mathbb{Q} \mathbb{R} \mathbb{Z} 1  &  \twoheadrightarrowtail \cdot 2  \\  \rightarrow 2  &  \int \left[3 \left(x + 1\right)\right] \mathrm{dx}\end{matrix}\right.\]
```

### From the command line
```
py_asciimath: a simple ASCIIMath/MathML/LaTeX converter

Usage:
  py_asciimath.py <EXP> from <ILANG> to <OLANG> [options]
  py_asciimath.py <EXP> (-i <ILANG> | --input=ILANG)
                        (-o <OLANG> | --output=OLANG)
                        [options]
  py_asciimath.py from-file <PATH> from <ILANG> to <OLANG> [options]
  py_asciimath.py from-file <PATH> (-i <ILANG> | --input=ILANG)
                                   (-o <OLANG> | --output=OLANG) [options]
  py_asciimath.py (-h | --help)
  py_asciimath.py --version

Options:
  --dstyle                      Add display style
  -i <ILANG> --input=ILANG      Input language
                                Supported input language: asciimath, mathml
  --log                         Log the transformation process
  --network                     Works only with ILANG=mathnml or OLANG=mathml
                                Use network to validate XML against DTD
  -o <OLANG> --output=OLANG     Output language
                                Supported output language: latex, mathml
  --pprint                      Works only with OLANG=mathml. Pretty print
  --to-file=OPATH               Save translation to OPATH file
  --validate-xml=MathMLDTD      Works only with OLANG=mathml
                                Validate against a MathML DTD
                                MathMLDTD can be: mathml1, mathml2 or mathml3
  --version                     Show version
```

For example, `py_asciimath "sum_(i=1)^n i^3=((n(n+1))/2)^2" from asciimath to latex` prints:

```
INFO:Translating...
$\sum_{i = 1}^{n} i^{3} = \left(\frac{n \left(n + 1\right)}{2}\right)^{2}$
```
If the option `--log` is present, then it prints also every transformation of the input, so `py_asciimath "e^x > 0 forall x in RR" from asciimath to latex --log` prints:

```
INFO:Translating...
INFO:Calling const with args:
INFO:   items = [Token(LETTER, 'e')]
INFO:Calling const with args:
INFO:   items = [Token(LETTER, 'x')]
INFO:Calling exp_super with args:
INFO:   items = ['e', 'x']
INFO:Calling remove_parenthesis with args:
INFO:   s = 'x'
INFO:Calling symbol with args:
INFO:   items = [Token(MORETHAN, '>')]
INFO:Calling exp_interm with args:
INFO:   items = ['>']
INFO:Calling const with args:
INFO:   items = [Token(NUMBER, '0')]
INFO:Calling exp_interm with args:
INFO:   items = ['0']
INFO:Calling symbol with args:
INFO:   items = [Token(FORALL, 'forall')]
INFO:Calling exp_interm with args:
INFO:   items = ['\\forall']
INFO:Calling const with args:
INFO:   items = [Token(LETTER, 'x')]
INFO:Calling exp_interm with args:
INFO:   items = ['x']
INFO:Calling symbol with args:
INFO:   items = [Token(IN, 'in')]
INFO:Calling exp_interm with args:
INFO:   items = ['\\in']
INFO:Calling symbol with args:
INFO:   items = [Token(RR, 'RR')]
INFO:Calling exp_interm with args:
INFO:   items = ['\\mathbb{R}']
INFO:Calling exp with args:
INFO:   items = ['\\mathbb{R}']
INFO:Calling exp with args:
INFO:   items = ['\\in', '\\mathbb{R}']
INFO:Calling exp with args:
INFO:   items = ['x', '\\in \\mathbb{R}']
INFO:Calling exp with args:
INFO:   items = ['\\forall', 'x \\in \\mathbb{R}']
INFO:Calling exp with args:
INFO:   items = ['0', '\\forall x \\in \\mathbb{R}']
INFO:Calling exp with args:
INFO:   items = ['>', '0 \\forall x \\in \\mathbb{R}']
INFO:Calling exp with args:
INFO:   items = ['e^{x}', '> 0 \\forall x \\in \\mathbb{R}']
$e^{x} > 0 \forall x \in \mathbb{R}$
```

## Grammar

The grammar used to parse the input is:
```
start: i start* -> exp
i: s -> exp_interm
    | s "/" s -> exp_frac
    | s "_" s -> exp_under
    | s "^" s -> exp_super
    | s "_" s "^" s -> exp_under_super
s: l start? r -> exp_par
    | u s -> exp_unary
    | b s s -> exp_binary
    | asciimath -> symbol
    | c -> const
    | QS -> q_str
c: /d[A-Za-z]/ // derivatives
  | NUMBER
  | LETTER
l: "(" | "(:" | "[" | "{" | "{:" | "|:" | "||:" | "langle" | "<<" // left parenthesis
r: ")" | ":)" | "]" | "}" | ":}" | ":|" | ":||" | "rangle" | ">>" // right parenthesis
b: {} // asciimath binary functions symbols
u: {} // asciimath unary functions symbols
asciimath: {} // asciimath symbols
QS: "\"" /(?<=").+(?=")/ "\"" // Quoted String
```
For the complete list of symbols, please refer to http://asciimath.org/#syntax. The only symbol that I've added is `dstyle`, that stands for `displaystyle` as a unary function.

## Rendering (matrices and systems of equations)

For a text to be rendered as a matrix must have a structure like 

<div align="center">
    <code>L '[' ... (, ...)* ']', '[' ... (, ...)* ']' (, '[' ... (, ...)* ']' )* R</code> 
    <br>
    or
    <br>
    <code>L '(' ... (, ...)* ')', '(' ... (, ...)* ')' (, '(' ... (, ...)* ')' )* R</code>
</div>

that is:

* It must be delimited by a left (`L`) and right (`R`) parenthesis
* Every row can be separated by `[]` XOR `()` (if one starts with `[]`, every row will be recognized with the same parenthesis, same for `()`), followed by `,` and possibly another row
* Every matrix must contain at least two rows
* Every rows contains zero or more columns, where `...` can be any ASCIIMath expression
* Every row must contain the same number of columns

Since `L` and `R` can be any left or right parenthesis, and every matrices must have the same number of columns, to render a system of equation one can write something like `{[(root n x)/(x) <= 4], [x^2=e^x]:}`.  
On the other hand a matrix can be somenthing like `[[(root n x)/(x) <= 4, int x dx], [x^2=e^x, lim_(x to infty) 1 / (x^2)]]`.

## Rendering (LaTeX semantics)

A parsed ASCIIMath string is rendered as follows:

* `latex`, `u` and `c` symbols are converted to their LaTeX equivalent
* `text` and `ul` correspond to the `\textrm` and `\underline` functions
* `bb`, `bbb`, `cc`, `tt`, `fr` and `sf` correspond to the `\boldsymbol`, `\mathbb`, `\mathcal`, `\texttt`, `\mathfrak` and `\textsf` functions
* `frac` is rendered as a fraction, `root n x` as the n-th root of x and `stackrel x y` displays x upon y
* Any text placed between a pair of `"` is rendered in the same font as normal text.
* `/` stands for a fraction. The `_` and `^` tokens have the same behaviour as in LaTeX but the subscript must be placed before the superscript if they are both present

### Delimiters

Left and right delimiters are preceded by the `\left` and `\right` commands to be well-sized. `(:` and `:)` are chevrons (angle parenthesis). `{:` and `:}` are invisible delimiters like LaTeX's {. `|:` is converted to `\lvert` , while `||:` is converted to `\lVert`. The other delimiters are rendered as expected.  
Useless delimiters are automatically removed in expressions like: 

* `(...)/(...)`
* `(...)_(...)`, `(...)^(...)` and the combination of sub and superscript
* `u (...)`, `b (...) (...)` where u and b are unary and binary operators
  
If you want them to be rendered, you have to double them, for example: `((x+y))/2` or `{: (x+y) :}/2`.

## Rendering (MathML semantics)

The translation follows the MathML specification at https://www.w3.org/TR/MathML3/.

# Known issues
The MathML1 DTD validation will fail when one wish to apply a font style
