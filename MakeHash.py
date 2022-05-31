#Programma che prende una parola che l'utente digita e la trasforma in hash 
#e la porta dentro una tuple che salva dentro un file

#dopo aver fatto il programma:
#- Fai con print il titolo del programma 
#- Fai con print una breve descrizione del programma

print("*     *   *****  *   *  *****     *****  *****  *****  *****  *   *  *   *  *****  *****  ****   ")
print("*  *  *   *   *  * *    *         *   *  *   *  *      *      *   *  *   *  *   *  *   *  *   * ")
print("*     *   *****  *  *   *****     *****  *****  *****  *****  * * *  * * *  *   *  ****   *    * ")
print("*     *   *   *  *   *  *         *      *   *      *      *  * * *  * * *  *   *  *   *  *    * ")
print("*     *   *   *  *   *  *****     *      *   *  *****  *****  ** **  *****  *****  *   *  ****  ")

print("\n")
print("Istruzioni:")
print("Questo programma è stato creato da Federico ed questa è la versione beta.")
print("Il programma è fatto per il momento solo in python quindi per usarlo devi")
print("scaricarti Python. Questo Tool è stato creato per fare una conversione di")
print("parole, lettere, numeri e simboli in hash.\n")
print("Warning:")
print("La prima volta che digiti la password che vuoi trasformare la ristamperà ")
print("schermo, mentre la seconda,terza ecc.... volta che digiterai la password ")
print("la ristamperà in output sottoforma di tuple quindi in modo disordinato.\n")


utente1 = input("Digita la password: ")
lista_password = {""}
password1 = int(hash(utente1))
lista_password.add(password1)
print(lista_password)
Question =  input("Vuoi Inserire un'altra password? (Yes/No) ")
if Question == "Yes" or Question == "yes":
    utente2 = input("Digita la password: ")
    password2 = int(hash(utente2))
    lista_password.add(password2)
    print(lista_password)

elif Question == "No" or Question == "no":
    print("Ok")

Question2 =  input("Sei sicuro di non voler mettere un'altra password un'altra password? (Yes/No)")
while Question2 == "No" or Question2 == "no":
    lista_password.add(int(hash(input("Digita la password: "))))
    print(lista_password)
    Question2 =  input("Vuoi Inserire un'altra password? (Yes/No)")
    if Question2 == "Yes" or Question2 == "yes":
        lista_password.add(int(hash(input("Digita la password: "))))
        print(lista_password)
    else:
        break



print("Ecco tutti gli hash che hai crato:", lista_password)




