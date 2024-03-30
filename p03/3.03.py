from dta import attributes, gini, delta_metric, split_values
import pprint

#
# main
#

if __name__ == "__main__":

    S = [
       { "Nombre":"Samuel", "Calvo":1, "Rubio":0, "Barba":0, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Pepe", "Calvo":0, "Rubio":1, "Barba":0, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Pablo", "Calvo":0, "Rubio":0, "Barba":0, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Jorge", "Calvo":0, "Rubio":0, "Barba":0, "Sombrero":1, "label": "hombre"},
       { "Nombre":"Felipe", "Calvo":0, "Rubio":0, "Barba":1, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Clara", "Calvo":0, "Rubio":0, "Barba":0, "Sombrero":1, "label": "mujer"},
       { "Nombre":"Anita", "Calvo":0, "Rubio":1, "Barba":0, "Sombrero":0, "label": "mujer"},
       { "Nombre":"Alfredo", "Calvo":0, "Rubio":0, "Barba":1, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Susana", "Calvo":0, "Rubio":0, "Barba":0, "Sombrero":0, "label": "mujer"},
       { "Nombre":"Ricardo", "Calvo":1, "Rubio":0, "Barba":1, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Paco", "Calvo":0, "Rubio":0, "Barba":0, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Manuel", "Calvo":0, "Rubio":0, "Barba":1, "Sombrero":0, "label": "hombre"},
       { "Nombre":"German", "Calvo":1, "Rubio":0, "Barba":0, "Sombrero":0, "label": "hombre"},
       { "Nombre":"David", "Calvo":0, "Rubio":1, "Barba":1, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Bernardo", "Calvo":0, "Rubio":0, "Barba":0, "Sombrero":1, "label": "hombre"},
       { "Nombre":"Alejandro", "Calvo":0, "Rubio":0, "Barba":1, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Tomas", "Calvo":1, "Rubio":0, "Barba":0, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Roberto", "Calvo":0, "Rubio":0, "Barba":0, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Pedro", "Calvo":0, "Rubio":0, "Barba":0, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Maria", "Calvo":0, "Rubio":0, "Barba":0, "Sombrero":1, "label": "mujer"},
       { "Nombre":"Guillermo", "Calvo":1, "Rubio":0, "Barba":0, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Ernesto", "Calvo":0, "Rubio":1, "Barba":0, "Sombrero":1, "label": "hombre"},
       { "Nombre":"Carlos", "Calvo":0, "Rubio":1, "Barba":1, "Sombrero":0, "label": "hombre"},
       { "Nombre":"Ana", "Calvo":0, "Rubio":0, "Barba":0, "Sombrero":0, "label": "mujer"},
    ]
    attrs = attributes(S)
    metric = gini

    print(f"S:")
    pprint.pp(S)
    print(f"\nattrs:")
    pprint.pp(attrs)
    print(f'\ngini_gain(S, Calvo): {delta_metric(S, gini, split_values(S, "Calvo"))}')
    print(f'gini_gain(S, Rubio): {delta_metric(S, gini, split_values(S, "Rubio"))}')
    print(f'gini_gain(S, Barba): {delta_metric(S, gini, split_values(S, "Barba"))}')
    print(f'gini_gain(S, Sombrero): {delta_metric(S, gini, split_values(S, "Sombrero"))}')
