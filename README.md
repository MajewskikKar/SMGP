<b>Skrypt do wycinania map Szczegółowej Mapy Geologicznej Polski</b>

Ogólne info:

Pracujac z plikami rastrowymi w aplikacjach gisowych, każdorazowo jesteśmy zmuszeni do ręcznego georeferowania rastra. W zależności od naszych potrzeb, często jesteśmy również zmuszeni do wycięcia ramki mapy.

Poniższy skrypt umożliwia zautomatyzowanie tych czynności dla map SMGP dostępnych na stronach Instytutu Geologicznego.

Działanie sktypyu jest możliwe dzięki dwów sprzyjającym okolicznościom:
1. Instytut udostępnia swoje mapy, których ramki są niemal identyczne we wszysktich mapach,
    (odwiedź: <a>https://geologia.pgi.gov.pl/karto_geo/</a>)
3. Instytut udostępnia ramkę dla wszysktich arkuszy w postaci pliku shapefile. Umożliwiło to wyciągnięcie koordynatów i wyeksportowanie ich do tabeli excelowskiej.

Skrypt może stanowić ciekawą bazę pod wycinanie innych rodzajów map. 

Film prezentujący działanie skryptu:
<a>https://www.youtube.com/watch?v=tFIOSC5ues8</a>

Pliki i foldery konieczne do działania skryptu:

1. folder 'rogi' z czterema jpegami przezentującymi rogi,
2. folder 'excel' z czterema plikami zawierającymi koordynatami map,
3. foldery do zapisu map wyciętych i całych (domyslnie 'cale1', 'wyc1'),
4. pusta geobaza do zapisu map zgeoreferowanych (domyslnie 'georeferencja.gdb')

Skrypt testowano z pomocą pythona 3.9 przy użyciu aplikacji pycharm.

WAŻNE: 
Konieczne do działania skryptu jest posiadanie biblioteki arcpy, która dostępna jest tylko w przypadku posiadania zainstalowanego pakietu arcgis!
Biblioteki (cv2,shutil,openpyxl) należy niestety instalować w interpreterze arcgisowym co jest niestety dość upierdliwe.

W razie pytań zachęcam do kontaktu majewskikar@gmail.com

Skrypt stworzony przez Karola Majewskiego
