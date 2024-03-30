from dta import attributes, gini, ID3_cat
import pprint

#
# main
#

if __name__ == "__main__":

    S = [
        { "Cielo": "Sol",     "Temperatura": "Calor",    "Humedad": "Alta",   "Viento": "Debil",  "label": "no"},
        { "Cielo": "Sol",     "Temperatura": "Calor",    "Humedad": "Alta",   "Viento": "Fuerte", "label": "no"},
        { "Cielo": "Nublado", "Temperatura": "Calor",    "Humedad": "Alta",   "Viento": "Debil",  "label": "si"},
        { "Cielo": "Lluvia",  "Temperatura": "Templado", "Humedad": "Alta",   "Viento": "Debil",  "label": "si"},
        { "Cielo": "Lluvia",  "Temperatura": "Frio",     "Humedad": "Normal", "Viento": "Debil",  "label": "si"},
        { "Cielo": "Lluvia",  "Temperatura": "Frio",     "Humedad": "Normal", "Viento": "Fuerte", "label": "no"},
        { "Cielo": "Nublado", "Temperatura": "Frio",     "Humedad": "Normal", "Viento": "Fuerte", "label": "si"},
        { "Cielo": "Sol",     "Temperatura": "Templado", "Humedad": "Alta",   "Viento": "Debil",  "label": "no"},
        { "Cielo": "Sol",     "Temperatura": "Frio",     "Humedad": "Normal", "Viento": "Debil",  "label": "si"},
        { "Cielo": "Lluvia",  "Temperatura": "Templado", "Humedad": "Normal", "Viento": "Debil",  "label": "si"},
        { "Cielo": "Sol",     "Temperatura": "Templado", "Humedad": "Normal", "Viento": "Fuerte", "label": "si"},
        { "Cielo": "Nublado", "Temperatura": "Templado", "Humedad": "Alta",   "Viento": "Fuerte", "label": "si"},
        { "Cielo": "Nublado", "Temperatura": "Calor",    "Humedad": "Normal", "Viento": "Debil",  "label": "si"},
        { "Cielo": "Lluvia",  "Temperatura": "Templado", "Humedad": "Alta",   "Viento": "Fuerte", "label": "no"}
    ]
    attrs = attributes(S)
    metric = gini
    h = 2

    print(f"S:")
    pprint.pp(S)
    print(f"\nattrs:")
    pprint.pp(attrs)
    print(f"\nmetric: {metric.__name__}")
    print(f"\ndecision tree (unbounded):")
    pprint.pp(ID3_cat(S, attrs, gini))
