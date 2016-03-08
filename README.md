# Tutorial

#### A. Instalacja narzędzi

Narzędzia wykorzystywane w tej części laboratorium są dość stare (czasy pythona 2.4). Do uruchomienia ich potrzebna była modyfikacja kodu źródłowego. Projekt został opakowany w virtualenv, posprzątanie go powinno sprowadzać się do usunięcia folderu, w którym nastąpi instalacja.

Wymagania: python 2, virtualenv

Instrukcja:

	0. apt-get python2 / yum install python2/ pacman -S python2/ ...
	   easy_install virtualenv / pip install virtualenv

	1. git clone https://github.com/wuwer/ISZ-lab1.git
	2. cd ISZ-lab1
	3. ./init.sh

Jeśli wszystko wykonało się poprawnie, wykonanie pliku test.py powinno spowodować wyświetlenie okna z zbiorem Mandelbrota.

#### B. Rysowanie fraktali

Biblioteka chaos zawiera narzędzia do rysowania fraktali (Krzywa Kocha, Krzywa Hilberta).
Aby narysować Krzywą Kocha należy:
	
	1. Uruchomić interpreter pythona należący do virtualevna:
		./venv/bin/python
	2.  from chaos.koch import * 

Analogiczna instrukcja służąca do narysowania Krzywej Hilberta:

	from chaos.hilbert import *

Wykonanie ćwiczeń może być wygodniejsze, jeśli zmodyfikuje się odpowiednio plik test.py

#### C. Liczenie wymiaru pudełkowego (box dimension) fraktala

Wymiary fraktala definiuje się na kilka różnych sposobów. Można stwierdzić, że są miarami skomplikowania fraktala. Zajmiemy się liczeniem wymiaru pudełkowego.

Opis:
http://zasoby1.open.agh.edu.pl/dydaktyka/matematyka/c_fraktale_i_chaos/fraktale.php?rozdzial=8#wymiarpudelkowy


Instrukcje:

	1. from chaos.box import *
	2. B = Box(<ścieżka_obrazka>, 1)

Obrazki z kolejnymi iteracjami rysowania Krzywej Kocha znajdują się w folderze ./koch

#### D. 'Ręczne' rysowanie fraktali

Pewna klasa fraktali może zostać wygenerowana za pomocą tzw. Gry w Chaos. Gra wygląda następująco:
	1. Definiujemy n prekształceń przyjmujących jako argumenty współrzędne punktu i zwracających współrzędne punktu
	2. Losujemy punkt początkowy
	3. Wybieramy kolejne punkty poprzez przetworzenie ostatniego punktu przez losowo wybrane ze zdefiniowanych przekształceń
	4. Zaznaczamy na obrazku otrzymane punkty

Przekształcenia mają formę
	x' = a*x + b*y + e
	y' = c*x + d*y + f

W pliku ifs.py przygotowano szablon programu. Na jego podstawie należy stworzyć program rysujący Trójkąt Sierpińskiego.
Każde z przekształceń pozwalające na uzyskanie Trójkąta zwracaja punkt znajdujący się w połowie odległości między punktem-argumentem, a jednym z wierzchołków Trójkąta.

Uwaga: wymiary obrazu według PIL
https://automatetheboringstuff.com/images/000004.jpg

Jaki jest wymiar pudełkowy Trójkąta Sierpińskiego?




Źródła:
[1]http://homepages.math.uic.edu/~culler/chaos/

[2]http://zasoby1.open.agh.edu.pl/dydaktyka/matematyka/c_fraktale_i_chaos/fraktale.php?rozdzial=8

[3]http://blackhole.ovh.org/fraktale.php
