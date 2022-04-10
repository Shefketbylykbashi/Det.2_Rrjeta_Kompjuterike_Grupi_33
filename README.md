# Det.2_Rrjeta_Kompjuterike_Grupi_33
Detyra e dyte ne rrjeta kompjuterike

Pershkrimi i detyres:
Programimi me socketa ne gjuhen programuese python ne protokollin TCP

Kemi krijuar nje server(Server.py) i cili varesisht nga lloji i klientit 
-klienti 1 (Client_WRE) i cili ekzekutohet ne te njejten paisje ku ne menyr automatike e 
merr IP addresen e paisjes dhe ka privilegjin:
-->te beje Upload nje file nga client_data ne server_data
-->te beje Delete nje file nga server_data
-->te lexoje filet te cilat i permban server_data

-klient 2 (Client_R) i cili ekzekutohet ne cilendo paisje dhe nevojitet ip addresa 
e paisjes ne te cilen eshte duke u ekzekutuar serveri dhe ka privilegjin:
-->te lexoje filet te cilat i permban server_data

Komandat:
HELP -->Shfaqe menyne
UPLOAD client_data/test1.txt --> bene upload ne server_data filen test1.txt
DELETE test1.txt --> fshien file-n nga server_data
LOGOUT -->Shkyqet nga serveri