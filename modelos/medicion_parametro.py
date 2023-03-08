from modelos.parametros_fisiologicos import ParametrosFisiologicos
class MedicionParametro:
    def __init__(self, id_detalle_medicion:int = 0, parametro:ParametrosFisiologicos = None, medida_parametro_fisiologico:float = 0):
        self.id_detalle_medicion = id_detalle_medicion
        self.parametro = parametro
        self.medida_parametro_fisiologico = medida_parametro_fisiologico

    def asignar_color(self):
        # '' normal, + alto, - bajo
        # amarillo -> #FFBF00 ; verde -> #00C040 ; rojo -> #FF0211 ; gris -> #F5F5F5
        if self.medida_parametro_fisiologico <= self.parametro.critico_bajo:
            return ("#F5F5F5", '', self.medida_parametro_fisiologico)

        if self.parametro.critico_bajo < self.medida_parametro_fisiologico < self.parametro.alerta_bajo:
            return ("#FF0211", '-', self.medida_parametro_fisiologico)

        if self.parametro.alerta_bajo <= self.medida_parametro_fisiologico < self.parametro.min_estandar:
            return ("#FFBF00", '-', self.medida_parametro_fisiologico)

        if self.parametro.min_estandar <= self.medida_parametro_fisiologico <= self.parametro.max_estandar:
            return ("#00C040", '', self.medida_parametro_fisiologico)

        if (self.parametro.alerta_alto):
            if self.parametro.max_estandar < self.medida_parametro_fisiologico <= self.parametro.alerta_alto:
                return ("#FFBF00", '+', self.medida_parametro_fisiologico)

            if (self.parametro.critico_alto):
                if self.parametro.alerta_alto < self.medida_parametro_fisiologico <= self.parametro.critico_alto:
                    return ("#FF0211", '+', self.medida_parametro_fisiologico)

                if self.parametro.critico_alto < self.medida_parametro_fisiologico:
                    return ("#FF0211", '', self.medida_parametro_fisiologico)
            else:
                if self.parametro.alerta_alto < self.medida_parametro_fisiologico:
                    return ("#FF0211", '+', self.medida_parametro_fisiologico)
        else:
            if self.parametro.max_estandar < self.medida_parametro_fisiologico:
                return ("#F5F5F5", '', self.medida_parametro_fisiologico)

prueba = MedicionParametro(1, ParametrosFisiologicos(1, "Temperatura", 36, 37, 40, 34, 46, 29.99), 50)

print(prueba.asignar_color())
