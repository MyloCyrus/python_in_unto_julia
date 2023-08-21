 _       _ _(_)_     |  Documentation: https://docs.julialang.org
  (_)     | (_) (_)    |
   _ _   _| |_  __ _   |  Type "?" for help, "]?" for Pkg help.
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 1.9.2 (2023-07-05)
 _/ |\__'_|_|_|\__'_|  |  Official https://julialang.org/ release
|__/                   |

julia> j?
ERROR: syntax: space required before "?" operator
Stacktrace:
 [1] top-level scope
   @ none:1

julia>  j?
ERROR: syntax: space required before "?" operator
Stacktrace:
 [1] top-level scope
   @ none:1

julia> j ?
       pkg
ERROR: syntax: colon expected in "?" expression
Stacktrace:
 [1] top-level scope
   @ none:1

julia> j ?
       pkg install
ERROR: syntax: colon expected in "?" expression
Stacktrace:
 [1] top-level scope
   @ none:1

julia> j ?
       pkg install
ERROR: syntax: colon expected in "?" expression
Stacktrace:
 [1] top-level scope
   @ none:1

julia> j ?kg install NiceStuff
       pkg install
ERROR: syntax: space required after "?" operator
Stacktrace:
 [1] top-level scope
   @ none:1

julia> pkg.add NiceStuff
ERROR: syntax: extra token "NiceStuff" after end of expression
Stacktrace:
 [1] top-level scope
   @ none:1

julia> pkg.add NiceStuff
ERROR: syntax: extra token "NiceStuff" after end of expression
Stacktrace:
 [1] top-level scope
   @ none:1

julia> pkg.add NiceStuff
ERROR: syntax: extra token "NiceStuff" after end of expression
Stacktrace:
 [1] top-level scope
   @ none:1

julia> pkg.add (NiceStuff)
ERROR: syntax: space before "(" not allowed in "pkg.add (" at REPL[7]:1
Stacktrace:
 [1] top-level scope
   @ none:1

julia> pkg.add(NiceStuff)
ERROR: UndefVarError: `pkg` not defined
Stacktrace:
 [1] top-level scope
   @ REPL[8]:1

julia> pkg.addNiceStuff
ERROR: UndefVarError: `pkg` not defined
Stacktrace:
 [1] top-level scope
   @ REPL[9]:1

julia> using pkg
 │ Attempted to find missing packages in package registries but no registries are installed.
 └ Use package mode to install a registry. `pkg> registry add` will install the default registries.

ERROR: ArgumentError: Package pkg not found in current path.
- Run `import Pkg; Pkg.add("pkg")` to install the pkg package.
Stacktrace:
 [1] macro expansion
   @ .\loading.jl:1630 [inlined]
 [2] macro expansion
   @ .\lock.jl:267 [inlined]
 [3] require(into::Module, mod::Symbol)
   @ Base .\loading.jl:1611

julia> 'pkg> registry add
       NiceStuff
       'import Pkg; Pkg.add(NiceStuff)
ERROR: syntax: character literal contains multiple characters
Stacktrace:
 [1] top-level scope
   @ none:1

julia> 'import Pkg; Pkg.add(NiceStuff)
       nicestuff
       pkjg.add("NiceStuff")
ERROR: syntax: invalid character literal
Stacktrace:
 [1] top-level scope
   @ none:1

julia> julia> ]
ERROR: syntax: unexpected "]"
Stacktrace:
 [1] top-level scope
   @ none:1

julia> (v1.0) pkg> add Calculus
ERROR: syntax: missing comma or ) in argument list
Stacktrace:
 [1] top-level scope
   @ none:1

julia> ... messages
ERROR: syntax: invalid identifier name "..."
Stacktrace:
 [1] top-level scope
   @ none:1

julia> (v1.0) pkg> add julia> ]
ERROR: syntax: missing comma or ) in argument list
Stacktrace:
 [1] top-level scope
   @ none:1

julia> (v1.0) pkg> add Calculus
ERROR: syntax: missing comma or ) in argument list
Stacktrace:
 [1] top-level scope
   @ none:1

julia> ... messages
ERROR: syntax: invalid identifier name "..."
Stacktrace:
 [1] top-level scope
   @ none:1

julia> (v1.0) pkg> add nicestuff
ERROR: syntax: missing comma or ) in argument list
Stacktrace:
 [1] top-level scope
   @ none:1

julia> download(url, [ output = tempname() ];
           [ method = "GET", ]
           [ headers = <none>, ]
ERROR: syntax: space before "[" not allowed in "[method = "GET"] [" at REPL[20]:3
Stacktrace:
 [1] top-level scope
   @ none:1

julia>     [ timeout = <none>, ]
ERROR: syntax: "<" is not a unary operator
Stacktrace:
 [1] top-level scope
   @ none:1

julia>     [ progress = <none>, ]
ERROR: syntax: "<" is not a unary operator
Stacktrace:
 [1] top-level scope
   @ none:1

julia>     [ verbose = false, ]
ERROR: syntax: misplaced assignment statement in "[verbose = false]" around REPL[23]:1
Stacktrace:
 [1] top-level scope
   @ REPL[23]:1

julia>     [ debug = <none>, ]
ERROR: syntax: "<" is not a unary operator
Stacktrace:
 [1] top-level scope
   @ none:1

julia>     [ downloader = <default>, ]
ERROR: syntax: "<" is not a unary operator
Stacktrace:
 [1] top-level scope
   @ none:1

julia> ) -> output
ERROR: syntax: unexpected ")"
Stacktrace:
 [1] top-level scope
   @ none:1

julia> C:\Users\sa-SierotyLab1\Downloads\utils.jl
ERROR: syntax: "\" is not a unary operator
Stacktrace:
 [1] top-level scope
   @ none:1

julia> PKG_BRANCH = master
ERROR: UndefVarError: `master` not defined
Stacktrace:
 [1] top-level scope
   @ REPL[28]:1

julia> pkg> add GLMakie
ERROR: syntax: extra token "GLMakie" after end of expression
Stacktrace:
 [1] top-level scope
   @ none:1

julia> pkg> add glmakie
ERROR: syntax: extra token "glmakie" after end of expression
Stacktrace:
 [1] top-level scope
   @ none:1

julia> C:\Users\sa-SierotyLab1\Downloads\gallery.jl
ERROR: syntax: "\" is not a unary operator
Stacktrace:
 [1] top-level scope
   @ none:1

julia> C:\Users\sa-SierotyLab1\Downloads\utils.jl
ERROR: syntax: "\" is not a unary operator
Stacktrace:
 [1] top-level scope
   @ none:1

julia> data = [([x], 2x-x^3) for x in -2:0.1f0:2]
41-element Vector{Tuple{Vector{Float32}, Float32}}:
 ([-2.0], 4.0)
 ([-1.9], 3.0589998)
 ([-1.8], 2.2319994)
 ([-1.7], 1.513)
 ([-1.6], 0.89600015)
 ([-1.5], 0.375)
 ([-1.4], -0.055999994)
 ([-1.3], -0.40300012)
 ([-1.2], -0.67199993)
 ([-1.1], -0.86899996) 
 ([-1.0], -1.0)
 ([-0.9], -1.0710001)
 ([-0.8], -1.088)
 ⋮
 ([0.9], 1.0710001)
 ([1.0], 1.0)
 ([1.1], 0.86899996)
 ([1.2], 0.67199993)
 ([1.3], 0.40300012)
 ([1.4], 0.055999994)
 ([1.5], -0.375)
 ([1.6], -0.89600015)
 ([1.7], -1.513)
 ([1.8], -2.2319994)
 ([1.9], -3.0589998)
 ([2.0], -4.0)

julia>

julia> model = Chain(Dense(1 => 23, tanh), Dense(23 => 1, bias=false), only)
ERROR: UndefVarError: `Dense` not defined
Stacktrace:
 [1] top-level scope
   @ REPL[34]:1

julia>

julia> optim = Flux.setup(Adam(), model)
ERROR: UndefVarError: `Flux` not defined
Stacktrace:
 [1] top-level scope
   @ REPL[35]:1

julia> for epoch in 1:1000
         Flux.train!((m,x,y) -> (m(x) - y)^2, model, data, optim)
       end
ERROR: UndefVarError: `Flux` not defined
Stacktrace:
 [1] top-level scope
   @ REPL[36]:2

julia>

julia> plot(x -> 2x-x^3, -2, 2, legend=false)
ERROR: UndefVarError: `plot` not defined
Stacktrace:
 [1] top-level scope
   @ REPL[37]:1

julia> scatter!(x -> model([x]), -2:0.1f0:2)


