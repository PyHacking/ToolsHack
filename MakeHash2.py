import pyfiglet

Header = pyfiglet.figlet_format("\nTable Hash :)")
print(Header)

#print("*     *   *****  *   *  *****     *****  *****  *****  *****  *   *    *****  *****  ****   ")
#print("*  *  *   *   *  * *    *         *   *  *   *  *      *      *   *    *   *  *   *  *   * ")
#print("*     *   *****  *  *   *****     *****  *****  *****  *****  * * *    *   *  ****   *    * ")
#print("*     *   *   *  *   *  *         *      *   *      *      *  * * *    *   *  *   *  *    * ")
#print("*     *   *   *  *   *  *****     *      *   *  *****  *****  ** **    *****  *   *  ****  ")

print("\n")
print("Istruzioni:")
print("Questo programma è stato creato da Federico Agostini  ed è la versione beta.Il programma è in python. ")
print("Questo Tool è stato creato per fare una conversione di una password in hash che viene associata a un nome.")
print("Quindi in sostanza crea una Table Hash.\n")
print("Warning:")
print("La prima volta che digiti la password che vuoi trasformare la ristamperà a schermo.")
print("Mentre la seconda,terza ecc.... volta che digiterai la password la ristamperà in output. \n")
print("GitHub:")
print("Per avere il codice completo basta visitare nel mio account di GitHub, \"PyHacking\", la Repositories è \"MakeHash.py\". ")
print("Il Link della Repositories è  \"https://github.com/PyHacking/ToolsHack \" \n")


listahash = {}

utente1_nick = input("Come ti chiami: ")
utente1_pass = hash(input("Digita la password: "))

listahash.update({utente1_nick:utente1_pass})
print("%-10s %10s" % (utente1_nick,utente1_pass ) )
 
Question1 = input("Vuoi continuare? (Yes/No)")

if Question1 == "Yes" or Question1 == "yes":
    while Question1 == "Yes" or Question1 == "yes":
        utente_nick = input("Come ti chiami: ")
        utente_pass = hash(input("Digita la password: "))
        listahash.update({utente_nick:utente_pass})
        Question1 = input("Vuoi continuare? (Yes/No)")
    else:
        print("I Nomi:") 
        for utenti in listahash:        
          print("%-10s" % (utenti))
        print("Le password:")  
        for valori in listahash :       
          print("%-10s" % (listahash[valori]))
elif Question1 == "No" or Question1 == "no":
    print("Ok")


        




