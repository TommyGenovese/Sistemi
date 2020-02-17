import subprocess

ipaddress = input("inserisci l'indirizzo IP: ")
#mask = int(input("inserisci la mask: "))

ipaddress_splitted = [int(i) for i in ipaddress.split(".")]         #splitta la stringa e crea una lista di 4 interi

ipaddress_bin = 0
for e, group in enumerate(ipaddress_splitted):                      #enumerate cicla sia sull'elemento della lista(e) che sull'indice(group)
    ipaddress_bin = ipaddress_bin + group*(2**(((3-e)*8)))          #in "ipaddress_bin" ci finirà la conversione dell' IP (tutto) in binario(da decimale a binario)

ipaddress_host = ipaddress_bin                                      #
#for c in range(1,2**(32-mask)-1):                                   #aggiungo uno a quanti sono gli host
#    ipaddress_host = ipaddress_host + 1                                 
#    l = '.'.join([str(int(bin(ipaddress_host)[i:i+8],2)) for i in range(2,34,8)])   #"bin(ipaddress_host)" :converte in binario, prendo i caratteri della stringa da i a i+8
                                                                                    # da 2(i primi due non sono dell'indirizzo) a 34.
                                                                                    #str è una stringa
#il metodo join viene usato per unire i componenti della lista tramite il carattere selezionato:   ';'.join(lista) = 192;168;10;0

print("\n\nping dell'indirizzo ip in corso...")
p = subprocess.Popen(['ping', ipaddress], stdout=subprocess.PIPE)
ping = p.communicate()
print(ping[0].decode())


      
