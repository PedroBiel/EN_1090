"""
UNE-EN 1090-2:2011

EJECUCIÓN DE ESTRUCTURAS DE ACERO Y ALUMINIO

Parte 2: Requisitos técnicos para la ejecución de estructuras de acero

6.6 Perforación

03/05/2024

__author__ = Pedro Biel

__version__ = 0.0.0

__email__ = pedro.biel@abalsirengineering.com
"""

class Perforacion:

    def __init__(self, d_nom: float) -> None:
        """
        UNE-EN 1090-2:2011

        EJECUCIÓN DE ESTRUCTURAS DE ACERO Y ALUMINIO

        Parte 2: Requisitos técnicos para la ejecución de estructuras de acero

        6.6 Perforación

        Obtención de agujeros para las uniones con elementos de fijación mecánicos y bulones.

        :param d_nom: [mm] Diámetro nominal del perno o bulón.
        """

        if d_nom <= 0:
            raise ValueError(':( El diámetro del taladro debe ser mayor que cero.')

        self.d_nom = d_nom

    def holgura_nominal(self, tipo_agujero: str) -> int:
        """
        Holgura nominal para pernos y bulones según la tabla 11.

        Tipos de agujero:

        - Agujeros redondos normales
        - Agujeros redondos de tamaño extra
        - Agujeros ovalados cortos
        - Agujeros ovalados largos

        :param tipo_agujero: [] Tipo de agujero

        :return: holgura [mm]
        """

        if tipo_agujero.lower() == 'agujeros redondos normales':
            holgura = self.agujero_redondo_normal()
        elif tipo_agujero.lower() == 'agujeros redondos de tamaño extra':
            holgura = self.agujero_redondo_tamano_extra()
        elif tipo_agujero.lower() == 'agujeros ovalados cortos':
            holgura = self.agujero_ovalado_corto()
        else:
            holgura = self.agujero_ovalado_largo()

        return holgura

    def agujero_redondo_normal(self) -> int:
        """
        Holgura nominal para pernos y bulones con agujeros redondos normales.

        En Oficina Técnica se emplea holgura = 2 mm para M12 y superiores.

        :return holgura; [mm]
        """

        if self.d_nom < 12:
            holgura = 1
        elif self.d_nom <= 14:  # En Oficina Técnica se emplea holgura = 2 mm para M12 y superiores.
            holgura = 2
        elif self.d_nom <= 24:
            holgura = 2
        else:
            holgura = 3

        return holgura

    def agujero_redondo_tamano_extra(self) -> int:
        """
        Holgura nominal para pernos y bulones con agujeros redondos de tamño extra.

        :return holgura; [mm]
        """

        if self.d_nom <= 14:
            holgura = 3
        elif self.d_nom <= 22:
            holgura = 4
        elif self.d_nom == 24:
            holgura = 6
        else:
            holgura = 8

        return holgura

    def agujero_ovalado_corto(self) -> int:
        """
        Holgura nominal para pernos y bulones con agujeros ovalados cortos.

        :return holgura; [mm]
        """

        if self.d_nom <= 14:
            holgura = 4
        elif self.d_nom <= 22:
            holgura = 6
        elif self.d_nom == 24:
            holgura = 8
        else:
            holgura = 10

        return holgura

    def agujero_ovalado_largo(self) -> float:
        """
        Holgura nominal para pernos y bulones con agujeros ovalados largos.

        :return holgura; [mm]
        """

        holgura = 1.5 * self.d_nom

        return holgura


if __name__ == '__main__':

    import random
    from prettytable import PrettyTable

    tabla = PrettyTable()
    tabla.field_names = ('agujero', 'd.nom [mm]', 'holgura [mm]')
    for _ in range(10):
        a = random.choice([
            'Agujeros redondos normales', 'Agujeros redondos de tamaño extra', 'Agujeros ovalados cortos',
            'Agujeros ovalados largos'
        ])
        d = random.randint(0, 40)
        perforacion = Perforacion(d)
        h = perforacion.holgura_nominal(a)
        tabla.add_row([a, d, h])
    print(tabla)
