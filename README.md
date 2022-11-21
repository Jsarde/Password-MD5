# Password-MD5
Programma per controllare la sicurezza di una Password

Una password è considerata sicura se:

1. Rispetta i requisiti minimi
    - Lunghezza minima di 8 caratteri
    - Presenza di almeno un carattere numerico
    - Presenza di almeno una lettera maiuscola
    - Presenza di almeno una lettera minuscola
    - Presenza di almeno un carattere speciale 

2. Non è presente nel database di MD5online.it 
   il programma effettua un controllo per verosimiglianza tra la password inserita (convertita con la crittografia MD5) 
   e quelle presenti nel sito. 
   Per maggiori informazioni sull'MD5 --> https://it.wikipedia.org/wiki/MD5 


La libreria utilizzata per effettuare il Web Scraping è BeautifulSoup
