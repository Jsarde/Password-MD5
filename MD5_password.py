from bs4 import BeautifulSoup as bs
import requests
import hashlib



class Password:
    def __init__(self,password) :
        self.password = password
    
    # la Password deve avere almeno 8 caratteri
    def __len(self):
        if len(self.password) >= 8:
            return True
        else:
            return False
    
    # la Password deve contenere almeno un numero
    def __num(self):
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        flag = False
        for elem in self.password:
            if elem in numbers:
                flag = True
                break
        return flag
    
    # la Password deve avere almeno un carattere Maiuscolo
    def __upper(self):
        upper = self.password.upper()
        if upper == self.password:
            return False
        else:
            return True

    # la Password deve avere almeno un carattere Minuscolo
    def __lower(self):
        lower = self.password.lower()
        if lower == self.password:
            return False
        else:
            return True
    
    # la Password deve contenere almeno un carattere speciale
    def __special(self):
        special = ['@','!','?','#','$' '%','^','&','~','_','-','+','=','|','/','<','>']
        flag = False
        for elem in self.password:
            if elem in special:
                flag = True
                break            
        return flag
    
    # Controllo parametri minimi della Password
    def check(self):
        if self.__len() == self.__num() == self.__upper() == self.__lower() == self.__special() == True:
            return True
        else:
            if self.__len() == False:
                print('Problema: --> lunghezza minima 8 caratteri!')
            if self.__num() == False:
                print('Problema: --> deve contenere almeno un numero! ')
            if self.__upper() == False:
                print('Problema: --> deve avere almeno una lettera maiuscola! ')
            if self.__lower() == False:
                print('Problema: --> deve avere almeno una lettera minuscola! ')
            if self.__special() == False:
                print('Problema: --> deve contenere almeno un carattere speciale! ')
            print(' ')
            print('PASSWORD NON SICURA ⚠⚠⚠ ')
            return False
    
    # Controllo database password MD5online.it
    def MD5(self):
        md5_psw = hashlib.md5(self.password.encode('utf-8')).hexdigest()
        print(f'la versione MD5 della Password è --> {md5_psw}')
        url = 'http://md5online.it/index.lm?key_decript=' + md5_psw
        r = requests.get(url)
        soup = bs(r.text, 'html.parser')
        ris_md5 = soup.find_all('font')
        if ris_md5[3].get_text() == 'NESSUN RISULTATO':
            return True
        elif ris_md5[3].get_text() == self.password:
            return False
        else:
            print('Ops, qualcosa è andato storto...')



if __name__ == '__main__':

    while True:

        try:
            print('')
            password = str(input('Inserisci una password: '))

            #termino il programma se la password è 0
            if password=='0':
                break
                
            psw = Password(password)
            if psw.check() == True:
                if psw.MD5() == True:
                    print('PASSWORD SICURAAAAA :) :)')
                else:
                    print('PASSWORD NON SICURA ⚠⚠⚠ ')
            else:
                continue

        except:
            print('Errore, password non valida!!')
