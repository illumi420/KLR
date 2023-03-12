# KLR
<h3>[EN]</h3>

This Command-Line Tool <b>"Kosten- und Leistungsrechnung"</b> Cost and performance accounting, abbreviated in German to <b>"KLR"</b>, 
is an instrument of internal accounting and deals with the costs and services of a company that are directly related 
to the internal production of services.

This Tool relays on Python module Pandas, and was Developed by me for me to train my Pandas skills and kind of understand 
how this KLR thing works "the math behind it" or at least  to have this math done by a computer.


<h1>NOTE!</h1>                                        

<b>In  Regard  the PDF  Files in the <a  href="https://github.com/illumi420/KLR/tree/main/Examples" target="_blank"}>Exampel</a> folder:</b>

<em>"The PDF files provided on this Repo are not my own creation, but rather the work of others. 
These files are provided for descriptive purposes only and are not intended to infringe upon any copyrights or intellectual property rights. 
I do not claim ownership or authorship of these files, and they are provided as-is, without any warranties or guarantees of accuracy or suitability 
for any particular purpose."</em>


<h1>For Whom this Tool aimed for ?</h1>

You are Doing a "Training/Retraining" in the direction of specialist information technology in Germany.  
And part of the Stuff you would handle while Fighting against the Final Bosses (IHK-Exams) through out your Studies, is this KLR science.

<h1>What can this tool do ?</h1>

<ul>
  <li>Trade Calculation - Input Friendliness = Can be challanging</li>
  <br>
  <li>Preliminary costing/Post calculation (product costing analysis) - Input Friendliness = Can be challanging</li>
  <br>
  <li>Operational accounting sheet - Input Friendliness = Horror</li>
  <br>
  <li>Overhead calculation industry (offer price) - Input Friendliness = Horror</li>
</ul>

<h1>What's on This  Repo ?</h1>

<ul>
  <li>The .py files that I think its ready to be published here. and the requierment.txt file</li>
  <br>
  <li>Example Folder That has Exercices PDFS which are solved by the PDF publisher and images for the solutions that are made by python in this Tool.</li>
  <br>
  <li>A GNU License and this beautiful README</li>
</ul>

<h1>How To run it ?</h1>

<h2>Linux</h2>

$ python3 -m pip install virtualenv <br>
after cloning KLR Localy <br>
$ python3 -m virtualenv  ~/KLR/klr-env <br>
$ chmod  +x  klr-env/bin/activate <br>
$ . klr-env/bin/activate <br>
$ pip install -r requirements.txt <br>
when you finish <br>
$ deactivate <br>

<h3>runner file is kostenleistungrechner.py</h3>

<h1>Usage:</h1>
<ul>
<li>the prompt Beschaffungskosten in Exercises has various names, but in the Exercises its always the costs before "Handlungskosten"</li>  
<li>in Handelskalkulation in all Three Modes it prompts <b>"+Handlungskosten€:"</b> and <b>"+Handlungskosten%:"</b> as in some cases its given in "€" in other cases in "%" so input <b>0</b> for the unavailable option</li>
</ul>

<h1>Plans for The Future of this Tool:</h1>
<ul>
<li>Web-Interface</li>
<li>Upload Exercise file, Fetch key infos, calculate</li> 
</ul>

<h4>+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-</h4>

<h3>[DE]</h3>

Dieses Command-Line Tool <b>"Kosten- und Leistungsrechnung" (KLR)</b> ist ein Instrument des internen Rechnungswesens und befasst sich mit 
den Kosten und Leistungen eines Unternehmens, die in direktem Zusammenhang mit der internen Leistungserstellung stehen.

Dieses Tool stützt sich auf das Python-Modul Pandas und wurde von mir entwickelt, um meine Pandas-Kenntnisse zu trainieren und irgendwie zu verstehen,
wie diese KLR-Sache "die Mathematik dahinter" funktioniert, oder zumindest, um diese Mathematik von einem Computer erledigen zu lassen.

<h1>NOTE!</h1>                                        

<b>In Bezug auf die PDF-Dateien im Ordner <a  href="https://github.com/illumi420/KLR/tree/main/Examples" target ="_blank">Exampel</a>:</b>

<em>"Die in diesem Repo bereitgestellten PDF-Dateien sind nicht meine eigene Kreation, sondern die Arbeit anderer. 
Diese Dateien werden nur zu Beschreibungszwecken zur Verfügung gestellt und sollen keine Urheberrechte oder geistigen Eigentumsrechte verletzen. 
Ich erhebe keinen Anspruch auf das Eigentum oder die Urheberschaft an diesen Dateien, und sie werden so wie sie sind zur Verfügung gestellt, ohne jegliche Garantien oder Gewährleistungen für die Richtigkeit oder Eignung für einen bestimmten Zweck."</em>
 
 
<h1>Für wen ist dieses Tool gedacht?</h1>

Du machst eine "Ausbildung/Umschulung" in Richtung Fachinformatik in Deutschland.  
Und ein Teil des Stoffes, den du während deines Studiums im Kampf gegen die Endgegner (IHK-Prüfungen) zu bewältigen hast, ist diese KLR-Wissenschaft.

<h1>Was kann dieses Tool ?</h1>


<ul>
  <li><a  href="https://studyflix.de/wirtschaft/handelskalkulation-1470" target="_blank">Handelskalkulation</a> - Eingabefreundlichkeit = Kann herausfordernd sein</li>
  <br>
  <li><a  href="https://5cube.digital/eine-erfolgreiche-vor-nachkalkulation-in-der-produktion/#:~:text=W%C3%A4hrend%20die%20Vorkalkulation%20ein%20Soll,Ergebnis%20(Ist%2DErgebnis)." target="_blank">Vor-Nachkalkulation</a> - Eingabefreundlichkeit = Kann herausfordernd sein</li>
  <br>
  <li><a  href="https://www.lexoffice.de/lexikon/betriebsabrechnungsbogen/#:~:text=Der%20Betriebsabrechnungsbogen%20(BAB)%20ist%20ein,anfallen%2C%20auf%20die%20Kostenstellen%20verteilt."  target="_blank">Betriebsabrechnungbogen</a> - Eingabefreundlichkeit = Horror</li>
  <br>
  <li><a href="https://studyflix.de/wirtschaft/zuschlagskalkulation-58" target="_blank">Zuschlagkalkulationindustrie(Angebotpreis)</a> - Eingabefreundlichkeit =  Horror</li>
</ul>

<h1>Was ist auf diesem Repo  ?</h1>

<ul>
  <li>Die .py Dateien, die ich denke, dass sie hier veröffentlicht werden können. und das requierment.txt datei</li>
  <br>
  <li>Beispielordner, der Übungs-PDFs enthält, die vom PDF-Herausgeber gelöst werden und Bilder für die Lösungen, die mit Python in diesem Tool gemacht werden.</li>
  <li>Eine GNU-Lizenz und dieses schöne README</li>
</ul>

<h1>Wie wird es ausgeführt  ?</h1>

$ python3 -m pip install virtualenv  <br>
after cloning KLR Localy  <br>
$ python3 -m virtualenv  ~/KLR/klr-env  <br>
$ chmod  +x  klr-env/bin/activate <br>
$ . klr-env/bin/activate  <br>
$ pip install -r requirements.txt <br>
when you finish  <br>
$ deactivate <br>

<h3>runner file is kostenleistungrechner.py</h3>

<h1>Nutzung:</h1>

<ul>
<li>Die Eingabeaufforderung Beschaffungskosten in Übungen hat verschiedene Namen, aber in den Übungen sind es immer die Kosten vor "Handlungskosten"</li>  
<li>in der Handelskalkulation wird in allen drei Modi <b>"+Handlungskosten€:"</b> und <b>"+Handlungskosten%:"</b> abgefragt, da in einigen Fällen "€" und in anderen Fällen "%" angegeben werden, also geben Sie <b>0</b> für die nicht verfügbare Option ein</li>
</ul>

<h1>Pläne für die Zukunft dieses Tools:</h1>
<ul>
<li>Webschnittstelle</li>
<li>Übungsdatei hochladen, Schlüsselinfos abrufen, berechnen</li> 
</ul>
