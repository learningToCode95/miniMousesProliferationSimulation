#! /usr/bin/env python3
#coding: utf-8

""" mini-simulation de croissance de population de souris
hypothèses : 
l'élevage tourne en vase clos.
Le but étant de s'inquiéter suffisamment tôt de l'augmentation de population, 
le couple de départ est adulte et copule tout de suite. Lui et sa descendance ne se
reposent jamais. Une fois la gestation terminée et les souriceaux nés la gestation 
suivante débute immédiatement
"""

def main():
    # nombre de semaines au bout desquelles la souris est capable de se reproduire
    adulte = 6
    # temps de gestation en semaines
    gestation = 3
    # 8 souriceaux par portee, supposns en moyenne 4 mâles et 4 femelles donc 4 couples
    portee = 4
    # population maximale
    plafondPopulation = 550
    seuilAlertePopulation = plafondPopulation * 0.8 # on s'inquiète si la population dépasse 80% des 550 souris
    # population exprimée en couple reproducteurs par simplification
    # la consanguinité est tolérée
    couples = 1
    # une variable pour la population, on commence avec un couple de souris supposées être
    # en état de procréer d'au-moins 6 semaines (population[0][0]) 
    # et sur le point de mettre bas au terme de 3 semaines de gestation (population[0][1])
    population = [[0,0]]
    # une variable pour le temps, on commence à la semaine 0
    semaine = 0
    # initialisation des naissances de la semaine
    naissances = [] 
    while couples * 2 < plafondPopulation:
        print("semaine :"+ str(semaine) +", population : "+ str(couples * 2))
        if couples * 2 > seuilAlertePopulation: 
            print("Alerte : la population a dépassé " + str(seuilAlertePopulation) + " en semaine "+ str(semaine))
            break
        else:
            for c in range(len(population)):
                # couple adulte et pas de gestation en cours 
                if population[c][0] == 0 and population[c][1] == 0:
                    population[c][1] = gestation # la gestation commence
                 
                #couple en âge de procréer et troisième semaine de gestation : naissance imminente
                elif population[c][0] == 0 and population[c][1] == 1:
                    couples = couples + portee
                    for nouveauxNes in range(portee):
                        naissances.append([adulte,0])
                    population[c][1] = gestation # dès la naissance le couple souhaite de nouveau agrandir la famille et la gestation commence

                elif population[c][0] > 0: # couple pas encore adulte
                    population[c][0] = population[c][0] - 1 # l'âge adulte approche d'une semaine

                #couple en âge de procréer et gestation en cours
                elif population[c][0] == 0 and population[c][1] > 0: 
                    population[c][1] = population[c][1] - 1 # la naissance s'est rapprochée d'une semaine, bientôt des souriceaux!

            # ajout des portées de la semaine à la population de couples
            for n in range(len(naissances)):
                population.append(naissances[n])

            naissances = [] # réinitialisation de la liste des naissances de la semaine pour la semaine prochaine

            semaine = semaine + 1 # le temps passe...

if __name__ == "__main__":
    main()