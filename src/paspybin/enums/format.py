"""
Module to store a str enum class representation the syntax highlighting format.
"""

from enum import StrEnum

__all__ = ["Format"]


class Format(StrEnum):
    """
    A str enum class that define valid syntax highlighting format.

    Attributes:
        NONE: `"text"`, None
        _4CS: `"4cs"`, 4CS
        _6502_ACME_CROSS_ASSEMBLER: `"6502acme"`, 6502 ACME Cross Assembler
        _6502_KICK_ASSEMBLER: `"6502kickass"`, 6502 Kick Assembler
        _6502_TASM_OR_64TASS: `"6502tasm"`, 6502 TASM/64TASS
        ABAP: `"abap"`, ABAP
        ACTIONSCRIPT: `"actionscript"`, ActionScript
        ACTIONSCRIPT3: `"actionscript3"`, ActionScript 3
        ADA: `"ada"`, Ada
        AIMMS: `"aimms"`, AIMMS
        ALGOL68: `"algol68"`, ALGOL 68
        APACHE_LOG: `"apache"`, Apache Log
        APPLESCRIPT: `"applescript"`, AppleScript
        APT_SOURCES: `"apt_sources"`, APT Sources
        ARDUINO: `"arduino"`, Arduino
        ARM: `"arm"`, ARM
        ASM: `"asm"`, ASM (NASM)
        ASP: `"asp"`, ASP
        ASYMPTOTE: `"asymptote"`, Asymptote
        AUTOCONF: `"autoconf"`, autoconf
        AUTOHOTKEY: `"autohotkey"`, Autohotkey
        AUTOIT: `"autoit"`, AutoIt
        AVISYNTH: `"avisynth"`, Avisynth
        AWK: `"awk"`, Awk
        BASCOM_AVR: `"bascomavr"`, BASCOM AVR
        BASH: `"bash"`, Bash
        BASIC4GL: `"basic4gl"`, Basic4GL
        BATCH: `"dos"`, Batch
        BIBTEX: `"bibtex"`, BibTeX
        BLITZ3D: `"b3d"`, Blitz3D
        BLITZ_BASIC: `"blitzbasic"`, Blitz Basic
        BLITZMAX: `"bmx"`, BlitzMax
        BNF: `"bnf"`, BNF
        BOO: `"boo"`, BOO
        BRAINFUCK: `"bf"`, BrainFuck
        C: `"c"`, C
        CSHARP: `"csharp"`, C#
        C_WINAPI: `"c_winapi"`, C (WinAPI)
        CPP: `"cpp"`, C++
        CPP_WINAPI: `"cpp_winapi"`, C++ (WinAPI)
        CPP_QT: `"cpp_qt"`, C++ (with Qt extensions
        C_LOADRUNNER: `"c_loadrunner"`, C: Loadrunner
        CAD_DCL: `"caddcl"`, CAD DCL
        CAD_LISP: `"cadlisp"`, CAD Lisp
        CEYLON: `"ceylon"`, Ceylon
        CFDG: `"cfdg"`, CFDG
        C_MACS: `"c_mac"`, C for Macs
        CHAISCRIPT: `"chaiscript"`, ChaiScript
        CHAPEL: `"chapel"`, Chapel
        C_INTERMEDIATE_LANGUAGE: `"cil"`, C Intermediate Language
        CLOJURE: `"clojure"`, Clojure
        CLONE_C: `"klonec"`, Clone C
        CLONE_CPP: `"klonecpp"`, Clone C++
        CMAKE: `"cmake"`, CMake
        COBOL: `"cobol"`, COBOL
        COFFEESCRIPT: `"coffeescript"`, CoffeeScript
        COLDFUSION: `"cfm"`, ColdFusion
        CSS: `"css"`, CSS
        CUESHEET: `"cuesheet"`, Cuesheet
        D: `"d"`, D
        DART: `"dart"`, Dart
        DCL: `"dcl"`, DCL
        DCPU16: `"dcpu16"`, DCPU-16
        DCS: `"dcs"`, DCS
        DELPHI: `"delphi"`, Delphi
        DELPHI_PRISM_OXYGENE: `"oxygene"`, Delphi Prism (Oxygene)
        DIFF: `"diff"`, Diff
        DIV: `"div"`, DIV
        DOT: `"dot"`, DOT
        E: `"e"`, E
        EASYTRIEVE: `"ezt"`, Easytrieve
        ECMASCRIPT: `"ecmascript"`, ECMAScript
        EIFFEL: `"eiffel"`, Eiffel
        EMAIL: `"email"`, Email
        EPC: `"epc"`, EPC
        ERLANG: `"erlang"`, Erlang
        EUPHORIA: `"euphoria"`, Euphoria
        FSHARP: `"fsharp"`, F#
        FALCON: `"falcon"`, Falcon
        FILEMAKER: `"filemaker"`, Filemaker
        FO_LANGUAGE: `"fo"`, FO Language
        FORMULA_ONE: `"f1"`, Formula One
        FORTRAN: `"fortran"`, Fortran
        FREEBASIC: `"freebasic"`, FreeBasic
        FREESWITCH: `"freeswitch"`, FreeSWITCH
        GAMBAS: `"gambas"`, GAMBAS
        GAME_MAKER: `"gml"`, Game Maker
        GDB: `"gdb"`, GDB
        GDSCRIPT: `"gdscript"`, GDScript
        GENERO: `"genero"`, Genero
        GENIE: `"genie"`, Genie
        GETTEXT: `"gettext"`, GetText
        GO: `"go"`, Go
        GODOT_GLSL: `"godot-glsl"`, Godot GLSL)
        GROOVY: `"groovy"`, Groovy
        GWBASIC: `"gwbasic"`, GwBasic
        HASKELL: `"haskell"`, Haskell
        HAXE: `"haxe"`, Haxe
        HICEST: `"hicest"`, HicEst
        HQ9_PLUS: `"hq9plus"`, HQ9 Plus
        HTML: `"html4strict"`, HTML
        HTML5: `"html5"`, HTML 5
        ICON: `"icon"`, Icon
        IDL: `"idl"`, IDL
        INI_FILE: `"ini"`, INI file
        INNO_SCRIPT: `"inno"`, Inno Script
        INTERCAL: `"intercal"`, INTERCAL
        IO: `"io"`, IO
        ISPF_PANEL_DEFINITION: `"ispfpanel"`, ISPF Panel Definition
        J: `"j"`, J
        JAVA: `"java"`, Java
        JAVA5: `"java5"`, Java 5
        JAVASCRIPT: `"javascript"`, JavaScript
        JCL: `"jcl"`, JCL
        JQUERY: `"jquery"`, jQuery
        JSON: `"json"`, JSON
        JULIA: `"julia"`, Julia
        KIXTART: `"kixtart"`, KiXtart
        KOTLIN: `"kotlin"`, Kotlin
        KSP_KONTAKT_SCRIPT: `"ksp"`, KSP (Kontakt Script)
        LATEX: `"latex"`, Latex
        LDIF: `"ldif"`, LDIF
        LIBERTY_BASIC: `"lb"`, Liberty BASIC
        LINDEN_SCRIPTING: `"lsl2"`, Linden Scripting
        LISP: `"lisp"`, Lisp
        LLVM: `"llvm"`, LLVM
        LOCO_BASIC: `"locobasic"`, Loco Basic
        LOGTALK: `"logtalk"`, Logtalk
        LOL_CODE: `"lolcode"`, LOL Code
        LOTUS_FORMULAS: `"lotusformulas"`, Lotus Formulas
        LOTUS_SCRIPT: `"lotusscript"`, Lotus Script
        LSCRIPT: `"lscript"`, LScript
        LUA: `"lua"`, Lua
        M68000_ASSEMBLER: `"m68k"`, M68000 Assembler
        MAGIKSF: `"magiksf"`, MagikSF
        MAKE: `"make"`, Make
        MAPBASIC: `"mapbasic"`, MapBasic
        MARKDOWN: `"markdown"`, Markdown
        MATLAB: `"matlab"`, MatLab
        MERCURY: `"mercury"`, Mercury
        METAPOST: `"metapost"`, MetaPost
        MIRC: `"mirc"`, mIRC
        MIX_ASSEMBLER: `"mmix"`, MIX Assembler
        MK_61_OR_52: `"MK-61/52"`, MK-61/52)/52)
        MODULA2: `"modula2"`, Modula 2
        MODULA3: `"modula3"`, Modula 3
        MOTOROLA_68000_HISOFT_DEV: `"68000devpac"`, Motorola 68000 HiSoft Dev
        MPASM: `"mpasm"`, MPASM
        MXML: `"mxml"`, MXML
        MYSQL: `"mysql"`, MySQL
        NAGIOS: `"nagios"`, Nagios
        NETREXX: `"netrexx"`, NetRexx
        NEWLISP: `"newlisp"`, newLISP
        NGINX: `"nginx"`, Nginx
        NIM: `"nim"`, Nim
        NULLSOFT_INSTALLER: `"nsis"`, NullSoft Installer
        OBERON2: `"oberon2"`, Oberon 2
        OBJECK_PROGRAMMING_LANGUA: `"objeck"`, Objeck Programming Langua
        OBJECTIVE_C: `"objc"`, Objective C
        OCAML: `"ocaml"`, OCaml
        OCAML_BRIEF: `"ocaml-brief"`, OCaml Brief)
        OCTAVE: `"octave"`, Octave
        OPENBSD_PACKET_FILTER: `"pf"`, OpenBSD PACKET FILTER
        OPENGL_SHADING: `"glsl"`, OpenGL Shading
        OPEN_OBJECT_REXX: `"oorexx"`, Open Object Rexx
        OPENOFFICE_BASIC: `"oobas"`, Openoffice BASIC
        ORACLE8: `"oracle8"`, Oracle 8
        ORACLE11: `"oracle11"`, Oracle 11
        OZ: `"oz"`, Oz
        PARASAIL: `"parasail"`, ParaSail
        PARI_GP: `"parigp"`, PARI/GP
        PASCAL: `"pascal"`, Pascal
        PAWN: `"pawn"`, Pawn
        PCRE: `"pcre"`, PCRE
        PER: `"per"`, Per
        PERL: `"perl"`, Perl
        PERL6: `"perl6"`, Perl 6
        PHIX: `"phix"`, Phix
        PHP: `"php"`, PHP
        PHP_BRIEF: `"php-brief"`, PHP Brief)
        PIC16: `"pic16"`, Pic 16
        PIKE: `"pike"`, Pike
        PIXEL_BENDER: `"pixelbender"`, Pixel Bender
        PL_I: `"pli"`, PL/I
        PL_SQL: `"plsql"`, PL/SQL
        POSTGRESQL: `"postgresql"`, PostgreSQL
        POSTSCRIPT: `"postscript"`, PostScript
        POV_RAY: `"povray"`, POV-Ray
        POWERBUILDER: `"powerbuilder"`, PowerBuilder
        POWERSHELL: `"powershell"`, PowerShell
        PROFTPD: `"proftpd"`, ProFTPd
        PROGRESS: `"progress"`, Progress
        PROLOG: `"prolog"`, Prolog
        PROPERTIES: `"properties"`, Properties
        PROVIDEX: `"providex"`, ProvideX
        PUPPET: `"puppet"`, Puppet
        PUREBASIC: `"purebasic"`, PureBasic
        PYCON: `"pycon"`, PyCon
        PYTHON: `"python"`, Python
        PYTHON_FOR_S60: `"pys60"`, Python for S60
        Q_KDBPLUS: `"q"`, q/kdb+
        QBASIC: `"qbasic"`, QBasic
        QML: `"qml"`, QML
        R: `"rsplus"`, R
        RACKET: `"racket"`, Racket
        RAILS: `"rails"`, Rails
        RBSCRIPT: `"rbs"`, RBScript
        REBOL: `"rebol"`, REBOL
        REG: `"reg"`, REG
        REXX: `"rexx"`, Rexx
        ROBOTS: `"robots"`, Robots
        ROFF_MANPAGE: `"roff"`, Roff Manpage
        RPM_SPEC: `"rpmspec"`, RPM Spec
        RUBY: `"ruby"`, Ruby
        RUBY_GNUPLOT: `"gnuplot"`, Ruby Gnuplot
        RUST: `"rust"`, Rust
        SAS: `"sas"`, SAS
        SCALA: `"scala"`, Scala
        SCHEME: `"scheme"`, Scheme
        SCILAB: `"scilab"`, Scilab
        SCL: `"scl"`, SCL
        SDLBASIC: `"sdlbasic"`, SdlBasic
        SMALLTALK: `"smalltalk"`, Smalltalk
        SMARTY: `"smarty"`, Smarty
        SPARK: `"spark"`, SPARK
        SPARQL: `"sparql"`, SPARQL
        SQF: `"sqf"`, SQF
        SQL: `"sql"`, SQL
        SSH_CONFIG: `"sshconfig"`, SSH Config
        STANDARDML: `"standardml"`, StandardML
        STONESCRIPT: `"stonescript"`, StoneScript
        SUPERCOLLIDER: `"sclang"`, SuperCollider
        SWIFT: `"swift"`, Swift
        SYSTEMVERILOG: `"systemverilog"`, SystemVerilog
        T_SQL: `"tsql"`, T-SQL
        TCL: `"tcl"`, TCL
        TERA_TERM: `"teraterm"`, Tera Term
        TEXGRAPH: `"texgraph"`, TeXgraph
        THINBASIC: `"thinbasic"`, thinBasic
        TYPESCRIPT: `"typescript"`, TypeScript
        TYPOSCRIPT: `"typoscript"`, TypoScript
        UNICON: `"unicon"`, Unicon
        UNREALSCRIPT: `"uscript"`, UnrealScript
        UPC: `"upc"`, UPC
        URBI: `"urbi"`, Urbi
        VALA: `"vala"`, Vala
        VBNET: `"vbnet"`, VB.NET
        VBSCRIPT: `"vbscript"`, VBScript
        VEDIT: `"vedit"`, Vedit
        VERILOG: `"verilog"`, VeriLog
        VHDL: `"vhdl"`, VHDL
        VIM: `"vim"`, VIM
        VISUALBASIC: `"vb"`, VisualBasic
        VISUALFOXPRO: `"visualfoxpro"`, VisualFoxPro
        VISUAL_PRO_LOG: `"visualprolog"`, Visual Pro Log
        WHITESPACE: `"whitespace"`, WhiteSpace
        WHOIS: `"whois"`, WHOIS
        WINBATCH: `"winbatch"`, Winbatch
        XBASIC: `"xbasic"`, XBasic
        XML: `"xml"`, XML
        XOJO: `"xojo"`, Xojo
        XORG_CONFIG: `"xorg_conf"`, Xorg Config
        XPP: `"xpp"`, XPP
        YAML: `"yaml"`, YAML
        YARA: `"yara"`, YARA
        Z80_ASSEMBLER: `"z80"`, Z80 Assembler
        ZXBASIC: `"zxbasic"`, ZXBasic

    Examples:
        >>> Format("text")
        <Format.NONE: 'text'>
        >>> Format["NONE"]
        <Format.NONE: 'text'>
        >>> Format.NONE
        <Format.NONE: 'text'>
        >>> Format.NONE == "text"
        True
        >>> print(Format.NONE)
        text

    Note:
        `NONE` is special format, as it name suggest it has no syntax highlighting.
    """

    NONE: str = "text"
    _4CS: str = "4cs"
    _6502_ACME_CROSS_ASSEMBLER: str = "6502acme"
    _6502_KICK_ASSEMBLER: str = "6502kickass"
    _6502_TASM_OR_64TASS: str = "6502tasm"
    ABAP: str = "abap"
    ACTIONSCRIPT: str = "actionscript"
    ACTIONSCRIPT3: str = "actionscript3"
    ADA: str = "ada"
    AIMMS: str = "aimms"
    ALGOL68: str = "algol68"
    APACHE_LOG: str = "apache"
    APPLESCRIPT: str = "applescript"
    APT_SOURCES: str = "apt_sources"
    ARDUINO: str = "arduino"
    ARM: str = "arm"
    ASM: str = "asm"
    ASP: str = "asp"
    ASYMPTOTE: str = "asymptote"
    AUTOCONF: str = "autoconf"
    AUTOHOTKEY: str = "autohotkey"
    AUTOIT: str = "autoit"
    AVISYNTH: str = "avisynth"
    AWK: str = "awk"
    BASCOM_AVR: str = "bascomavr"
    BASH: str = "bash"
    BASIC4GL: str = "basic4gl"
    BATCH: str = "dos"
    BIBTEX: str = "bibtex"
    BLITZ3D: str = "b3d"
    BLITZ_BASIC: str = "blitzbasic"
    BLITZMAX: str = "bmx"
    BNF: str = "bnf"
    BOO: str = "boo"
    BRAINFUCK: str = "bf"
    C: str = "c"
    CSHARP: str = "csharp"
    C_WINAPI: str = "c_winapi"
    CPP: str = "cpp"
    CPP_WINAPI: str = "cpp_winapi"
    CPP_QT: str = "cpp_qt"
    C_LOADRUNNER: str = "c_loadrunner"
    CAD_DCL: str = "caddcl"
    CAD_LISP: str = "cadlisp"
    CEYLON: str = "ceylon"
    CFDG: str = "cfdg"
    C_MACS: str = "c_mac"
    CHAISCRIPT: str = "chaiscript"
    CHAPEL: str = "chapel"
    C_INTERMEDIATE_LANGUAGE: str = "cil"
    CLOJURE: str = "clojure"
    CLONE_C: str = "klonec"
    CLONE_CPP: str = "klonecpp"
    CMAKE: str = "cmake"
    COBOL: str = "cobol"
    COFFEESCRIPT: str = "coffeescript"
    COLDFUSION: str = "cfm"
    CSS: str = "css"
    CUESHEET: str = "cuesheet"
    D: str = "d"
    DART: str = "dart"
    DCL: str = "dcl"
    DCPU16: str = "dcpu16"
    DCS: str = "dcs"
    DELPHI: str = "delphi"
    DELPHI_PRISM_OXYGENE: str = "oxygene"
    DIFF: str = "diff"
    DIV: str = "div"
    DOT: str = "dot"
    E: str = "e"
    EASYTRIEVE: str = "ezt"
    ECMASCRIPT: str = "ecmascript"
    EIFFEL: str = "eiffel"
    EMAIL: str = "email"
    EPC: str = "epc"
    ERLANG: str = "erlang"
    EUPHORIA: str = "euphoria"
    FSHARP: str = "fsharp"
    FALCON: str = "falcon"
    FILEMAKER: str = "filemaker"
    FO_LANGUAGE: str = "fo"
    FORMULA_ONE: str = "f1"
    FORTRAN: str = "fortran"
    FREEBASIC: str = "freebasic"
    FREESWITCH: str = "freeswitch"
    GAMBAS: str = "gambas"
    GAME_MAKER: str = "gml"
    GDB: str = "gdb"
    GDSCRIPT: str = "gdscript"
    GENERO: str = "genero"
    GENIE: str = "genie"
    GETTEXT: str = "gettext"
    GO: str = "go"
    GODOT_GLSL: str = "godot-glsl"
    GROOVY: str = "groovy"
    GWBASIC: str = "gwbasic"
    HASKELL: str = "haskell"
    HAXE: str = "haxe"
    HICEST: str = "hicest"
    HQ9_PLUS: str = "hq9plus"
    HTML: str = "html4strict"
    HTML5: str = "html5"
    ICON: str = "icon"
    IDL: str = "idl"
    INI_FILE: str = "ini"
    INNO_SCRIPT: str = "inno"
    INTERCAL: str = "intercal"
    IO: str = "io"
    ISPF_PANEL_DEFINITION: str = "ispfpanel"
    J: str = "j"
    JAVA: str = "java"
    JAVA5: str = "java5"
    JAVASCRIPT: str = "javascript"
    JCL: str = "jcl"
    JQUERY: str = "jquery"
    JSON: str = "json"
    JULIA: str = "julia"
    KIXTART: str = "kixtart"
    KOTLIN: str = "kotlin"
    KSP_KONTAKT_SCRIPT: str = "ksp"
    LATEX: str = "latex"
    LDIF: str = "ldif"
    LIBERTY_BASIC: str = "lb"
    LINDEN_SCRIPTING: str = "lsl2"
    LISP: str = "lisp"
    LLVM: str = "llvm"
    LOCO_BASIC: str = "locobasic"
    LOGTALK: str = "logtalk"
    LOL_CODE: str = "lolcode"
    LOTUS_FORMULAS: str = "lotusformulas"
    LOTUS_SCRIPT: str = "lotusscript"
    LSCRIPT: str = "lscript"
    LUA: str = "lua"
    M68000_ASSEMBLER: str = "m68k"
    MAGIKSF: str = "magiksf"
    MAKE: str = "make"
    MAPBASIC: str = "mapbasic"
    MARKDOWN: str = "markdown"
    MATLAB: str = "matlab"
    MERCURY: str = "mercury"
    METAPOST: str = "metapost"
    MIRC: str = "mirc"
    MIX_ASSEMBLER: str = "mmix"
    MK_61_OR_52: str = "MK-61/52"
    MODULA2: str = "modula2"
    MODULA3: str = "modula3"
    MOTOROLA_68000_HISOFT_DEV: str = "68000devpac"
    MPASM: str = "mpasm"
    MXML: str = "mxml"
    MYSQL: str = "mysql"
    NAGIOS: str = "nagios"
    NETREXX: str = "netrexx"
    NEWLISP: str = "newlisp"
    NGINX: str = "nginx"
    NIM: str = "nim"
    NULLSOFT_INSTALLER: str = "nsis"
    OBERON2: str = "oberon2"
    OBJECK_PROGRAMMING_LANGUA: str = "objeck"
    OBJECTIVE_C: str = "objc"
    OCAML: str = "ocaml"
    OCAML_BRIEF: str = "ocaml-brief"
    OCTAVE: str = "octave"
    OPENBSD_PACKET_FILTER: str = "pf"
    OPENGL_SHADING: str = "glsl"
    OPEN_OBJECT_REXX: str = "oorexx"
    OPENOFFICE_BASIC: str = "oobas"
    ORACLE8: str = "oracle8"
    ORACLE11: str = "oracle11"
    OZ: str = "oz"
    PARASAIL: str = "parasail"
    PARI_GP: str = "parigp"
    PASCAL: str = "pascal"
    PAWN: str = "pawn"
    PCRE: str = "pcre"
    PER: str = "per"
    PERL: str = "perl"
    PERL6: str = "perl6"
    PHIX: str = "phix"
    PHP: str = "php"
    PHP_BRIEF: str = "php-brief"
    PIC16: str = "pic16"
    PIKE: str = "pike"
    PIXEL_BENDER: str = "pixelbender"
    PL_I: str = "pli"
    PL_SQL: str = "plsql"
    POSTGRESQL: str = "postgresql"
    POSTSCRIPT: str = "postscript"
    POV_RAY: str = "povray"
    POWERBUILDER: str = "powerbuilder"
    POWERSHELL: str = "powershell"
    PROFTPD: str = "proftpd"
    PROGRESS: str = "progress"
    PROLOG: str = "prolog"
    PROPERTIES: str = "properties"
    PROVIDEX: str = "providex"
    PUPPET: str = "puppet"
    PUREBASIC: str = "purebasic"
    PYCON: str = "pycon"
    PYTHON: str = "python"
    PYTHON_FOR_S60: str = "pys60"
    Q_KDBPLUS: str = "q"
    QBASIC: str = "qbasic"
    QML: str = "qml"
    R: str = "rsplus"
    RACKET: str = "racket"
    RAILS: str = "rails"
    RBSCRIPT: str = "rbs"
    REBOL: str = "rebol"
    REG: str = "reg"
    REXX: str = "rexx"
    ROBOTS: str = "robots"
    ROFF_MANPAGE: str = "roff"
    RPM_SPEC: str = "rpmspec"
    RUBY: str = "ruby"
    RUBY_GNUPLOT: str = "gnuplot"
    RUST: str = "rust"
    SAS: str = "sas"
    SCALA: str = "scala"
    SCHEME: str = "scheme"
    SCILAB: str = "scilab"
    SCL: str = "scl"
    SDLBASIC: str = "sdlbasic"
    SMALLTALK: str = "smalltalk"
    SMARTY: str = "smarty"
    SPARK: str = "spark"
    SPARQL: str = "sparql"
    SQF: str = "sqf"
    SQL: str = "sql"
    SSH_CONFIG: str = "sshconfig"
    STANDARDML: str = "standardml"
    STONESCRIPT: str = "stonescript"
    SUPERCOLLIDER: str = "sclang"
    SWIFT: str = "swift"
    SYSTEMVERILOG: str = "systemverilog"
    T_SQL: str = "tsql"
    TCL: str = "tcl"
    TERA_TERM: str = "teraterm"
    TEXGRAPH: str = "texgraph"
    THINBASIC: str = "thinbasic"
    TYPESCRIPT: str = "typescript"
    TYPOSCRIPT: str = "typoscript"
    UNICON: str = "unicon"
    UNREALSCRIPT: str = "uscript"
    UPC: str = "upc"
    URBI: str = "urbi"
    VALA: str = "vala"
    VBNET: str = "vbnet"
    VBSCRIPT: str = "vbscript"
    VEDIT: str = "vedit"
    VERILOG: str = "verilog"
    VHDL: str = "vhdl"
    VIM: str = "vim"
    VISUALBASIC: str = "vb"
    VISUALFOXPRO: str = "visualfoxpro"
    VISUAL_PRO_LOG: str = "visualprolog"
    WHITESPACE: str = "whitespace"
    WHOIS: str = "whois"
    WINBATCH: str = "winbatch"
    XBASIC: str = "xbasic"
    XML: str = "xml"
    XOJO: str = "xojo"
    XORG_CONFIG: str = "xorg_conf"
    XPP: str = "xpp"
    YAML: str = "yaml"
    YARA: str = "yara"
    Z80_ASSEMBLER: str = "z80"
    ZXBASIC: str = "zxbasic"
