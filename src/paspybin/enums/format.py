"""
Module to store a str enum class representation the syntax highlighting format.
"""

from enum import StrEnum

__all__ = ["Format"]


class Format(StrEnum):
    """
    A str enum class that define valid syntax highlighting format.

    Attributes:
        NONE (str): `"text"`, None
        _4CS (str): `"4cs"`, 4CS
        _6502_ACME_CROSS_ASSEMBLER (str): `"6502acme"`, 6502 ACME Cross Assembler
        _6502_KICK_ASSEMBLER (str): `"6502kickass"`, 6502 Kick Assembler
        _6502_TASM_OR_64TASS (str): `"6502tasm"`, 6502 TASM/64TASS
        ABAP (str): `"abap"`, ABAP
        ACTIONSCRIPT (str): `"actionscript"`, ActionScript
        ACTIONSCRIPT3 (str): `"actionscript3"`, ActionScript 3
        ADA (str): `"ada"`, Ada
        AIMMS (str): `"aimms"`, AIMMS
        ALGOL68 (str): `"algol68"`, ALGOL 68
        APACHE_LOG (str): `"apache"`, Apache Log
        APPLESCRIPT (str): `"applescript"`, AppleScript
        APT_SOURCES (str): `"apt_sources"`, APT Sources
        ARDUINO (str): `"arduino"`, Arduino
        ARM (str): `"arm"`, ARM
        ASM (str): `"asm"`, ASM (NASM)
        ASP (str): `"asp"`, ASP
        ASYMPTOTE (str): `"asymptote"`, Asymptote
        AUTOCONF (str): `"autoconf"`, autoconf
        AUTOHOTKEY (str): `"autohotkey"`, Autohotkey
        AUTOIT (str): `"autoit"`, AutoIt
        AVISYNTH (str): `"avisynth"`, Avisynth
        AWK (str): `"awk"`, Awk
        BASCOM_AVR (str): `"bascomavr"`, BASCOM AVR
        BASH (str): `"bash"`, Bash
        BASIC4GL (str): `"basic4gl"`, Basic4GL
        BATCH (str): `"dos"`, Batch
        BIBTEX (str): `"bibtex"`, BibTeX
        BLITZ3D (str): `"b3d"`, Blitz3D
        BLITZ_BASIC (str): `"blitzbasic"`, Blitz Basic
        BLITZMAX (str): `"bmx"`, BlitzMax
        BNF (str): `"bnf"`, BNF
        BOO (str): `"boo"`, BOO
        BRAINFUCK (str): `"bf"`, BrainFuck
        C (str): `"c"`, C
        CSHARP (str): `"csharp"`, C#
        C_WINAPI (str): `"c_winapi"`, C (WinAPI)
        CPP (str): `"cpp"`, C++
        CPP_WINAPI (str): `"cpp_winapi"`, C++ (WinAPI)
        CPP_QT (str): `"cpp_qt"`, C++ (with Qt extensions
        C_LOADRUNNER (str): `"c_loadrunner"`, C: Loadrunner
        CAD_DCL (str): `"caddcl"`, CAD DCL
        CAD_LISP (str): `"cadlisp"`, CAD Lisp
        CEYLON (str): `"ceylon"`, Ceylon
        CFDG (str): `"cfdg"`, CFDG
        C_MACS (str): `"c_mac"`, C for Macs
        CHAISCRIPT (str): `"chaiscript"`, ChaiScript
        CHAPEL (str): `"chapel"`, Chapel
        C_INTERMEDIATE_LANGUAGE (str): `"cil"`, C Intermediate Language
        CLOJURE (str): `"clojure"`, Clojure
        CLONE_C (str): `"klonec"`, Clone C
        CLONE_CPP (str): `"klonecpp"`, Clone C++
        CMAKE (str): `"cmake"`, CMake
        COBOL (str): `"cobol"`, COBOL
        COFFEESCRIPT (str): `"coffeescript"`, CoffeeScript
        COLDFUSION (str): `"cfm"`, ColdFusion
        CSS (str): `"css"`, CSS
        CUESHEET (str): `"cuesheet"`, Cuesheet
        D (str): `"d"`, D
        DART (str): `"dart"`, Dart
        DCL (str): `"dcl"`, DCL
        DCPU16 (str): `"dcpu16"`, DCPU-16
        DCS (str): `"dcs"`, DCS
        DELPHI (str): `"delphi"`, Delphi
        DELPHI_PRISM_OXYGENE (str): `"oxygene"`, Delphi Prism (Oxygene)
        DIFF (str): `"diff"`, Diff
        DIV (str): `"div"`, DIV
        DOT (str): `"dot"`, DOT
        E (str): `"e"`, E
        EASYTRIEVE (str): `"ezt"`, Easytrieve
        ECMASCRIPT (str): `"ecmascript"`, ECMAScript
        EIFFEL (str): `"eiffel"`, Eiffel
        EMAIL (str): `"email"`, Email
        EPC (str): `"epc"`, EPC
        ERLANG (str): `"erlang"`, Erlang
        EUPHORIA (str): `"euphoria"`, Euphoria
        FSHARP (str): `"fsharp"`, F#
        FALCON (str): `"falcon"`, Falcon
        FILEMAKER (str): `"filemaker"`, Filemaker
        FO_LANGUAGE (str): `"fo"`, FO Language
        FORMULA_ONE (str): `"f1"`, Formula One
        FORTRAN (str): `"fortran"`, Fortran
        FREEBASIC (str): `"freebasic"`, FreeBasic
        FREESWITCH (str): `"freeswitch"`, FreeSWITCH
        GAMBAS (str): `"gambas"`, GAMBAS
        GAME_MAKER (str): `"gml"`, Game Maker
        GDB (str): `"gdb"`, GDB
        GDSCRIPT (str): `"gdscript"`, GDScript
        GENERO (str): `"genero"`, Genero
        GENIE (str): `"genie"`, Genie
        GETTEXT (str): `"gettext"`, GetText
        GO (str): `"go"`, Go
        GODOT_GLSL (str): `"godot-glsl"`, Godot GLSL)
        GROOVY (str): `"groovy"`, Groovy
        GWBASIC (str): `"gwbasic"`, GwBasic
        HASKELL (str): `"haskell"`, Haskell
        HAXE (str): `"haxe"`, Haxe
        HICEST (str): `"hicest"`, HicEst
        HQ9_PLUS (str): `"hq9plus"`, HQ9 Plus
        HTML (str): `"html4strict"`, HTML
        HTML5 (str): `"html5"`, HTML 5
        ICON (str): `"icon"`, Icon
        IDL (str): `"idl"`, IDL
        INI_FILE (str): `"ini"`, INI file
        INNO_SCRIPT (str): `"inno"`, Inno Script
        INTERCAL (str): `"intercal"`, INTERCAL
        IO (str): `"io"`, IO
        ISPF_PANEL_DEFINITION (str): `"ispfpanel"`, ISPF Panel Definition
        J (str): `"j"`, J
        JAVA (str): `"java"`, Java
        JAVA5 (str): `"java5"`, Java 5
        JAVASCRIPT (str): `"javascript"`, JavaScript
        JCL (str): `"jcl"`, JCL
        JQUERY (str): `"jquery"`, jQuery
        JSON (str): `"json"`, JSON
        JULIA (str): `"julia"`, Julia
        KIXTART (str): `"kixtart"`, KiXtart
        KOTLIN (str): `"kotlin"`, Kotlin
        KSP_KONTAKT_SCRIPT (str): `"ksp"`, KSP (Kontakt Script)
        LATEX (str): `"latex"`, Latex
        LDIF (str): `"ldif"`, LDIF
        LIBERTY_BASIC (str): `"lb"`, Liberty BASIC
        LINDEN_SCRIPTING (str): `"lsl2"`, Linden Scripting
        LISP (str): `"lisp"`, Lisp
        LLVM (str): `"llvm"`, LLVM
        LOCO_BASIC (str): `"locobasic"`, Loco Basic
        LOGTALK (str): `"logtalk"`, Logtalk
        LOL_CODE (str): `"lolcode"`, LOL Code
        LOTUS_FORMULAS (str): `"lotusformulas"`, Lotus Formulas
        LOTUS_SCRIPT (str): `"lotusscript"`, Lotus Script
        LSCRIPT (str): `"lscript"`, LScript
        LUA (str): `"lua"`, Lua
        M68000_ASSEMBLER (str): `"m68k"`, M68000 Assembler
        MAGIKSF (str): `"magiksf"`, MagikSF
        MAKE (str): `"make"`, Make
        MAPBASIC (str): `"mapbasic"`, MapBasic
        MARKDOWN (str): `"markdown"`, Markdown
        MATLAB (str): `"matlab"`, MatLab
        MERCURY (str): `"mercury"`, Mercury
        METAPOST (str): `"metapost"`, MetaPost
        MIRC (str): `"mirc"`, mIRC
        MIX_ASSEMBLER (str): `"mmix"`, MIX Assembler
        MK_61_OR_52 (str): `"MK-61/52"`, MK-61/52)/52)
        MODULA2 (str): `"modula2"`, Modula 2
        MODULA3 (str): `"modula3"`, Modula 3
        MOTOROLA_68000_HISOFT_DEV (str): `"68000devpac"`, Motorola 68000 HiSoft Dev
        MPASM (str): `"mpasm"`, MPASM
        MXML (str): `"mxml"`, MXML
        MYSQL (str): `"mysql"`, MySQL
        NAGIOS (str): `"nagios"`, Nagios
        NETREXX (str): `"netrexx"`, NetRexx
        NEWLISP (str): `"newlisp"`, newLISP
        NGINX (str): `"nginx"`, Nginx
        NIM (str): `"nim"`, Nim
        NULLSOFT_INSTALLER (str): `"nsis"`, NullSoft Installer
        OBERON2 (str): `"oberon2"`, Oberon 2
        OBJECK_PROGRAMMING_LANGUA (str): `"objeck"`, Objeck Programming Langua
        OBJECTIVE_C (str): `"objc"`, Objective C
        OCAML (str): `"ocaml"`, OCaml
        OCAML_BRIEF (str): `"ocaml-brief"`, OCaml Brief)
        OCTAVE (str): `"octave"`, Octave
        OPENBSD_PACKET_FILTER (str): `"pf"`, OpenBSD PACKET FILTER
        OPENGL_SHADING (str): `"glsl"`, OpenGL Shading
        OPEN_OBJECT_REXX (str): `"oorexx"`, Open Object Rexx
        OPENOFFICE_BASIC (str): `"oobas"`, Openoffice BASIC
        ORACLE8 (str): `"oracle8"`, Oracle 8
        ORACLE11 (str): `"oracle11"`, Oracle 11
        OZ (str): `"oz"`, Oz
        PARASAIL (str): `"parasail"`, ParaSail
        PARI_GP (str): `"parigp"`, PARI/GP
        PASCAL (str): `"pascal"`, Pascal
        PAWN (str): `"pawn"`, Pawn
        PCRE (str): `"pcre"`, PCRE
        PER (str): `"per"`, Per
        PERL (str): `"perl"`, Perl
        PERL6 (str): `"perl6"`, Perl 6
        PHIX (str): `"phix"`, Phix
        PHP (str): `"php"`, PHP
        PHP_BRIEF (str): `"php-brief"`, PHP Brief)
        PIC16 (str): `"pic16"`, Pic 16
        PIKE (str): `"pike"`, Pike
        PIXEL_BENDER (str): `"pixelbender"`, Pixel Bender
        PL_I (str): `"pli"`, PL/I
        PL_SQL (str): `"plsql"`, PL/SQL
        POSTGRESQL (str): `"postgresql"`, PostgreSQL
        POSTSCRIPT (str): `"postscript"`, PostScript
        POV_RAY (str): `"povray"`, POV-Ray
        POWERBUILDER (str): `"powerbuilder"`, PowerBuilder
        POWERSHELL (str): `"powershell"`, PowerShell
        PROFTPD (str): `"proftpd"`, ProFTPd
        PROGRESS (str): `"progress"`, Progress
        PROLOG (str): `"prolog"`, Prolog
        PROPERTIES (str): `"properties"`, Properties
        PROVIDEX (str): `"providex"`, ProvideX
        PUPPET (str): `"puppet"`, Puppet
        PUREBASIC (str): `"purebasic"`, PureBasic
        PYCON (str): `"pycon"`, PyCon
        PYTHON (str): `"python"`, Python
        PYTHON_FOR_S60 (str): `"pys60"`, Python for S60
        Q_KDBPLUS (str): `"q"`, q/kdb+
        QBASIC (str): `"qbasic"`, QBasic
        QML (str): `"qml"`, QML
        R (str): `"rsplus"`, R
        RACKET (str): `"racket"`, Racket
        RAILS (str): `"rails"`, Rails
        RBSCRIPT (str): `"rbs"`, RBScript
        REBOL (str): `"rebol"`, REBOL
        REG (str): `"reg"`, REG
        REXX (str): `"rexx"`, Rexx
        ROBOTS (str): `"robots"`, Robots
        ROFF_MANPAGE (str): `"roff"`, Roff Manpage
        RPM_SPEC (str): `"rpmspec"`, RPM Spec
        RUBY (str): `"ruby"`, Ruby
        RUBY_GNUPLOT (str): `"gnuplot"`, Ruby Gnuplot
        RUST (str): `"rust"`, Rust
        SAS (str): `"sas"`, SAS
        SCALA (str): `"scala"`, Scala
        SCHEME (str): `"scheme"`, Scheme
        SCILAB (str): `"scilab"`, Scilab
        SCL (str): `"scl"`, SCL
        SDLBASIC (str): `"sdlbasic"`, SdlBasic
        SMALLTALK (str): `"smalltalk"`, Smalltalk
        SMARTY (str): `"smarty"`, Smarty
        SPARK (str): `"spark"`, SPARK
        SPARQL (str): `"sparql"`, SPARQL
        SQF (str): `"sqf"`, SQF
        SQL (str): `"sql"`, SQL
        SSH_CONFIG (str): `"sshconfig"`, SSH Config
        STANDARDML (str): `"standardml"`, StandardML
        STONESCRIPT (str): `"stonescript"`, StoneScript
        SUPERCOLLIDER (str): `"sclang"`, SuperCollider
        SWIFT (str): `"swift"`, Swift
        SYSTEMVERILOG (str): `"systemverilog"`, SystemVerilog
        T_SQL (str): `"tsql"`, T-SQL
        TCL (str): `"tcl"`, TCL
        TERA_TERM (str): `"teraterm"`, Tera Term
        TEXGRAPH (str): `"texgraph"`, TeXgraph
        THINBASIC (str): `"thinbasic"`, thinBasic
        TYPESCRIPT (str): `"typescript"`, TypeScript
        TYPOSCRIPT (str): `"typoscript"`, TypoScript
        UNICON (str): `"unicon"`, Unicon
        UNREALSCRIPT (str): `"uscript"`, UnrealScript
        UPC (str): `"upc"`, UPC
        URBI (str): `"urbi"`, Urbi
        VALA (str): `"vala"`, Vala
        VBNET (str): `"vbnet"`, VB.NET
        VBSCRIPT (str): `"vbscript"`, VBScript
        VEDIT (str): `"vedit"`, Vedit
        VERILOG (str): `"verilog"`, VeriLog
        VHDL (str): `"vhdl"`, VHDL
        VIM (str): `"vim"`, VIM
        VISUALBASIC (str): `"vb"`, VisualBasic
        VISUALFOXPRO (str): `"visualfoxpro"`, VisualFoxPro
        VISUAL_PRO_LOG (str): `"visualprolog"`, Visual Pro Log
        WHITESPACE (str): `"whitespace"`, WhiteSpace
        WHOIS (str): `"whois"`, WHOIS
        WINBATCH (str): `"winbatch"`, Winbatch
        XBASIC (str): `"xbasic"`, XBasic
        XML (str): `"xml"`, XML
        XOJO (str): `"xojo"`, Xojo
        XORG_CONFIG (str): `"xorg_conf"`, Xorg Config
        XPP (str): `"xpp"`, XPP
        YAML (str): `"yaml"`, YAML
        YARA (str): `"yara"`, YARA
        Z80_ASSEMBLER (str): `"z80"`, Z80 Assembler
        ZXBASIC (str): `"zxbasic"`, ZXBasic

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

    NONE = "text"
    _4CS = "4cs"
    _6502_ACME_CROSS_ASSEMBLER = "6502acme"
    _6502_KICK_ASSEMBLER = "6502kickass"
    _6502_TASM_OR_64TASS = "6502tasm"
    ABAP = "abap"
    ACTIONSCRIPT = "actionscript"
    ACTIONSCRIPT3 = "actionscript3"
    ADA = "ada"
    AIMMS = "aimms"
    ALGOL68 = "algol68"
    APACHE_LOG = "apache"
    APPLESCRIPT = "applescript"
    APT_SOURCES = "apt_sources"
    ARDUINO = "arduino"
    ARM = "arm"
    ASM = "asm"
    ASP = "asp"
    ASYMPTOTE = "asymptote"
    AUTOCONF = "autoconf"
    AUTOHOTKEY = "autohotkey"
    AUTOIT = "autoit"
    AVISYNTH = "avisynth"
    AWK = "awk"
    BASCOM_AVR = "bascomavr"
    BASH = "bash"
    BASIC4GL = "basic4gl"
    BATCH = "dos"
    BIBTEX = "bibtex"
    BLITZ3D = "b3d"
    BLITZ_BASIC = "blitzbasic"
    BLITZMAX = "bmx"
    BNF = "bnf"
    BOO = "boo"
    BRAINFUCK = "bf"
    C = "c"
    CSHARP = "csharp"
    C_WINAPI = "c_winapi"
    CPP = "cpp"
    CPP_WINAPI = "cpp_winapi"
    CPP_QT = "cpp_qt"
    C_LOADRUNNER = "c_loadrunner"
    CAD_DCL = "caddcl"
    CAD_LISP = "cadlisp"
    CEYLON = "ceylon"
    CFDG = "cfdg"
    C_MACS = "c_mac"
    CHAISCRIPT = "chaiscript"
    CHAPEL = "chapel"
    C_INTERMEDIATE_LANGUAGE = "cil"
    CLOJURE = "clojure"
    CLONE_C = "klonec"
    CLONE_CPP = "klonecpp"
    CMAKE = "cmake"
    COBOL = "cobol"
    COFFEESCRIPT = "coffeescript"
    COLDFUSION = "cfm"
    CSS = "css"
    CUESHEET = "cuesheet"
    D = "d"
    DART = "dart"
    DCL = "dcl"
    DCPU16 = "dcpu16"
    DCS = "dcs"
    DELPHI = "delphi"
    DELPHI_PRISM_OXYGENE = "oxygene"
    DIFF = "diff"
    DIV = "div"
    DOT = "dot"
    E = "e"
    EASYTRIEVE = "ezt"
    ECMASCRIPT = "ecmascript"
    EIFFEL = "eiffel"
    EMAIL = "email"
    EPC = "epc"
    ERLANG = "erlang"
    EUPHORIA = "euphoria"
    FSHARP = "fsharp"
    FALCON = "falcon"
    FILEMAKER = "filemaker"
    FO_LANGUAGE = "fo"
    FORMULA_ONE = "f1"
    FORTRAN = "fortran"
    FREEBASIC = "freebasic"
    FREESWITCH = "freeswitch"
    GAMBAS = "gambas"
    GAME_MAKER = "gml"
    GDB = "gdb"
    GDSCRIPT = "gdscript"
    GENERO = "genero"
    GENIE = "genie"
    GETTEXT = "gettext"
    GO = "go"
    GODOT_GLSL = "godot-glsl"
    GROOVY = "groovy"
    GWBASIC = "gwbasic"
    HASKELL = "haskell"
    HAXE = "haxe"
    HICEST = "hicest"
    HQ9_PLUS = "hq9plus"
    HTML = "html4strict"
    HTML5 = "html5"
    ICON = "icon"
    IDL = "idl"
    INI_FILE = "ini"
    INNO_SCRIPT = "inno"
    INTERCAL = "intercal"
    IO = "io"
    ISPF_PANEL_DEFINITION = "ispfpanel"
    J = "j"
    JAVA = "java"
    JAVA5 = "java5"
    JAVASCRIPT = "javascript"
    JCL = "jcl"
    JQUERY = "jquery"
    JSON = "json"
    JULIA = "julia"
    KIXTART = "kixtart"
    KOTLIN = "kotlin"
    KSP_KONTAKT_SCRIPT = "ksp"
    LATEX = "latex"
    LDIF = "ldif"
    LIBERTY_BASIC = "lb"
    LINDEN_SCRIPTING = "lsl2"
    LISP = "lisp"
    LLVM = "llvm"
    LOCO_BASIC = "locobasic"
    LOGTALK = "logtalk"
    LOL_CODE = "lolcode"
    LOTUS_FORMULAS = "lotusformulas"
    LOTUS_SCRIPT = "lotusscript"
    LSCRIPT = "lscript"
    LUA = "lua"
    M68000_ASSEMBLER = "m68k"
    MAGIKSF = "magiksf"
    MAKE = "make"
    MAPBASIC = "mapbasic"
    MARKDOWN = "markdown"
    MATLAB = "matlab"
    MERCURY = "mercury"
    METAPOST = "metapost"
    MIRC = "mirc"
    MIX_ASSEMBLER = "mmix"
    MK_61_OR_52 = "MK-61/52"
    MODULA2 = "modula2"
    MODULA3 = "modula3"
    MOTOROLA_68000_HISOFT_DEV = "68000devpac"
    MPASM = "mpasm"
    MXML = "mxml"
    MYSQL = "mysql"
    NAGIOS = "nagios"
    NETREXX = "netrexx"
    NEWLISP = "newlisp"
    NGINX = "nginx"
    NIM = "nim"
    NULLSOFT_INSTALLER = "nsis"
    OBERON2 = "oberon2"
    OBJECK_PROGRAMMING_LANGUA = "objeck"
    OBJECTIVE_C = "objc"
    OCAML = "ocaml"
    OCAML_BRIEF = "ocaml-brief"
    OCTAVE = "octave"
    OPENBSD_PACKET_FILTER = "pf"
    OPENGL_SHADING = "glsl"
    OPEN_OBJECT_REXX = "oorexx"
    OPENOFFICE_BASIC = "oobas"
    ORACLE8 = "oracle8"
    ORACLE11 = "oracle11"
    OZ = "oz"
    PARASAIL = "parasail"
    PARI_GP = "parigp"
    PASCAL = "pascal"
    PAWN = "pawn"
    PCRE = "pcre"
    PER = "per"
    PERL = "perl"
    PERL6 = "perl6"
    PHIX = "phix"
    PHP = "php"
    PHP_BRIEF = "php-brief"
    PIC16 = "pic16"
    PIKE = "pike"
    PIXEL_BENDER = "pixelbender"
    PL_I = "pli"
    PL_SQL = "plsql"
    POSTGRESQL = "postgresql"
    POSTSCRIPT = "postscript"
    POV_RAY = "povray"
    POWERBUILDER = "powerbuilder"
    POWERSHELL = "powershell"
    PROFTPD = "proftpd"
    PROGRESS = "progress"
    PROLOG = "prolog"
    PROPERTIES = "properties"
    PROVIDEX = "providex"
    PUPPET = "puppet"
    PUREBASIC = "purebasic"
    PYCON = "pycon"
    PYTHON = "python"
    PYTHON_FOR_S60 = "pys60"
    Q_KDBPLUS = "q"
    QBASIC = "qbasic"
    QML = "qml"
    R = "rsplus"
    RACKET = "racket"
    RAILS = "rails"
    RBSCRIPT = "rbs"
    REBOL = "rebol"
    REG = "reg"
    REXX = "rexx"
    ROBOTS = "robots"
    ROFF_MANPAGE = "roff"
    RPM_SPEC = "rpmspec"
    RUBY = "ruby"
    RUBY_GNUPLOT = "gnuplot"
    RUST = "rust"
    SAS = "sas"
    SCALA = "scala"
    SCHEME = "scheme"
    SCILAB = "scilab"
    SCL = "scl"
    SDLBASIC = "sdlbasic"
    SMALLTALK = "smalltalk"
    SMARTY = "smarty"
    SPARK = "spark"
    SPARQL = "sparql"
    SQF = "sqf"
    SQL = "sql"
    SSH_CONFIG = "sshconfig"
    STANDARDML = "standardml"
    STONESCRIPT = "stonescript"
    SUPERCOLLIDER = "sclang"
    SWIFT = "swift"
    SYSTEMVERILOG = "systemverilog"
    T_SQL = "tsql"
    TCL = "tcl"
    TERA_TERM = "teraterm"
    TEXGRAPH = "texgraph"
    THINBASIC = "thinbasic"
    TYPESCRIPT = "typescript"
    TYPOSCRIPT = "typoscript"
    UNICON = "unicon"
    UNREALSCRIPT = "uscript"
    UPC = "upc"
    URBI = "urbi"
    VALA = "vala"
    VBNET = "vbnet"
    VBSCRIPT = "vbscript"
    VEDIT = "vedit"
    VERILOG = "verilog"
    VHDL = "vhdl"
    VIM = "vim"
    VISUALBASIC = "vb"
    VISUALFOXPRO = "visualfoxpro"
    VISUAL_PRO_LOG = "visualprolog"
    WHITESPACE = "whitespace"
    WHOIS = "whois"
    WINBATCH = "winbatch"
    XBASIC = "xbasic"
    XML = "xml"
    XOJO = "xojo"
    XORG_CONFIG = "xorg_conf"
    XPP = "xpp"
    YAML = "yaml"
    YARA = "yara"
    Z80_ASSEMBLER = "z80"
    ZXBASIC = "zxbasic"
