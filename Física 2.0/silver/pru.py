
class FormulHaze():
    """
    Esto almacena las diferentes fórmulas. Básicamente, admite el nombre de a que variable resuelven,
    y con que variables faltantes funcionan
    """    
    def __init__(self, nombre_variable, lista_formulas):
        self.nombre = nombre_variable
        self.VF = lista_formulas["VF"]
        self.VI = lista_formulas["VI"]
        self.A = lista_formulas["A"]
        self.T = lista_formulas["T"]
        self.X = lista_formulas["X"]

# Creamos los diccionarios
vf_formu = {
    "VF": "None",
    "VI": "a*t/2 + x/t",
    "A": "2*x/t - vi",
    "T": "(vi**2 + 2*a*x)**0.5",
    "X": "vi + a*t"
}

vi_formu = {
    "VF": "x/t - a*t/2",
    "VI": "None",
    "A": "2*x/t - vf",
    "T": "(vf**2 - 2*a*x)**0.5",
    "X": "vf - a*t"
}

a_formu = {
    "VF": "2*(x - vi*t)/(t**2)", 
    "VI": "2*(vf*t - x)/(t**2)",
    "A": "None",
    "T": "((vf**2)-(vi**2))/(2*x)",
    "X": "(vf - vi)/t"
}

t_formu = {
    "VF": "(-vi + (vi**2 + 2*a*x)**0.5) / a",
    "VI": "(vf + (vf**2 - 2*a*x)**0.5) / a",
    "A": "2*x/(vf + vi)",
    "T": "None",
    "X": "(vf - vi)/a"  
}

x_formu = {
    "VF": "vi*t + a*(t**2)/2",
    "VI": "vf*t - a*(t**2)/2",
    "A": "t*(vf + vi)/2",
    "T": "((vf)**2 - (vi)**2) /(2*a)",
    "X": "None"
}


# Creamos los objetos que almacenen las fórmulas ;)
obj_VF = FormulHaze("VF", vf_formu)
obj_VI = FormulHaze("VI", vi_formu)
obj_A = FormulHaze("A", a_formu)
obj_T = FormulHaze("T", t_formu)
obj_X = FormulHaze("X", x_formu)

print(obj_A.VF)
print(obj_VF.VF)
print(obj_VF.X)
































