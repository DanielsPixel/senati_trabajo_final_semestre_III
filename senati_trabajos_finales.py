# Trabajo Final Semestre III POO
class Trabajador:
    def __init__(self, nom: str, h_extra: int, min_tardanza: int, cat: str):
        self.__nombre = nom
        self.__descuento_t = min_tardanza * 1.5
        self.__h_extra = h_extra

        if cat.upper() == "A" or cat.upper == "B" or cat.upper() == "C":
            self.__cat = cat.upper()
        else:
            self.__cat = "No definida"

        match self.__cat:
            case "A":
                self.__sueldo = 3000.00
            case "B":
                self.__sueldo = 2500.00
            case "C":
                self.__sueldo = 2000.00
            case "No definida":
                self.__sueldo = 0.0

        match self.__cat:
            case "A":
                self.__ph_extra = self.__h_extra * (self.__sueldo / 240 * 4)
            case "B":
                self.__ph_extra = self.__h_extra * (self.__sueldo / 240 * 2)
            case "C":
                self.__ph_extra = round(self.__h_extra * (self.__sueldo / 240 * 2))
            case "No definida":
                self.__ph_extra = 0.0

    def __str__(self):
        return f"Nombre: {self.__nombre}, Categoria: {self.__cat}, Horas extra: {self.__h_extra}, Tardanza_m: " \
               f"{self.__descuento_t / 1.5}"

    @property
    def nombre(self):
        return self.__nombre

    @property
    def categoria(self):
        return self.__cat

    @property
    def sueldo(self):
        return self.__sueldo

    @property
    def ph_extra(self):
        return self.__ph_extra

    @property
    def descuento_t(self):
        return self.__descuento_t

    @property
    def sueldo_neto(self):
        return self.__sueldo + float(self.__ph_extra) - self.__descuento_t


class Boleta:
    def __init__(self, t: Trabajador):
        self.__boleta = f"*** BOLETA DE PAGO ***\n" \
                        f"NOMBRE:\t\t\t\t\t\t\t{t.nombre}\n" \
                        f"CATEGORIA:\t\t\t\t\t\t{t.categoria}\n" \
                        f"SUELDO BASICO:\t\t\t\t\t{t.sueldo}\n" \
                        f"DESCUENTO TARDANZAS:\t\t\t{t.descuento_t}\n" \
                        f"PAGO HORAS EXTRA:\t\t\t\t{t.ph_extra}\n" \
                        f"SUELDO NETO:\t\t\t\t\t{t.sueldo_neto}"

    def crear_boleta(self):
        return self.__boleta


class ProgramaPrincipal:
    def __init__(self):
        self.__trabajadores = {}
        self.menu()

    def menu(self):
        while True:
            print("----------------------------\n"
                  "1.Agregar Trabajadores\n"
                  "2.Ver lista de Trabajadores\n"
                  "3.Generar Boletas\n"
                  "4.Eliminar Trabajador\n"
                  "----------------------------\n")
            match input("_"):
                case "1":
                    self.agregar_trabajadores()
                case "2":
                    if len(self.__trabajadores) > 0:
                        for i in self.__trabajadores:
                            print(f"|{i}: {self.__trabajadores[i]}|")
                    else:
                        print("No existen trabajadores")
                case "3":
                    self.crear_boletas()
                case "4":
                    self.eliminar_trabajador()

    def agregar_trabajadores(self):
        cantidad = int(input("Ingresar número de trabajadores a crear: "))
        print("-----------------------")
        for i in range(cantidad):
            l_dict = len(self.__trabajadores)
            nombre = input(f"Nombre del trabajador {l_dict}: ")
            horas_extra = int(input(f"Horas extra del trabajador {l_dict}: "))
            m_tardanza = int(input(f"Minutos de tardanza del trabajador {l_dict}: "))
            categoria = input(f"Categoria del trabajador {l_dict}: ")
            self.__trabajadores.update({l_dict: (Trabajador(nombre, horas_extra, m_tardanza, categoria))})
            print("-----------------------")

    def crear_boletas(self):
        if len(self.__trabajadores) > 0:
            for i in self.__trabajadores:
                print(f"|{i}: {self.__trabajadores[i]}|")
            trabajadores = input("Elije el numero de trabajador o trabajadores con los que se creara la boleta: ")
            trabajadores = trabajadores.replace(" ", "").split(",")
            for i in trabajadores:
                print(f"Boleta del trabajador {i}:\n" + "-----------------------\n" +
                      f"{Boleta(self.__trabajadores[int(i)]).crear_boleta()}" + " \n" + "-----------------------")
        else:
            print("No existen trabajadores con los que crear una boleta \n"
                  "Primero ingrese un trabajor")

    def eliminar_trabajador(self):
        if len(self.__trabajadores) > 0:
            for i in self.__trabajadores:
                print(f"|{i}: {self.__trabajadores[i]}|")
            print('***Para eliminar todos los trabajadores escriba "todos"***')
            trabajadores = input("Elije el numero de trabajador o trabajadores a eliminar: ")
            if trabajadores == "todos":
                self.__trabajadores.clear()
            else:
                trabajadores = trabajadores.replace(" ", "").split(",")
                for i in trabajadores:
                    del self.__trabajadores[int(i)]
        else:
            print("Ni un trabajador en la lista de trabajadores \n"
                  "Primero ingrese un trabajor")
