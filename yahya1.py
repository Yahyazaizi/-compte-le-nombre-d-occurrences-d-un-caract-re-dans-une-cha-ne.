chaine=input( "chaîne contenant des caractères.:")
caractere_cible =input( "le caractères.:")
compteur = 0

for caractere in chaine:
    if caractere == caractere_cible:
        compteur += 1

print(f"Le caractère '{caractere_cible}' apparaît {compteur} fois dans la chaîne.")
