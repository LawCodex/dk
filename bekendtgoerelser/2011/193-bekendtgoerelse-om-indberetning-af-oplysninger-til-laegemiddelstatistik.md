---
title: "Bekendtgørelse om indberetning af oplysninger til lægemiddelstatistik"
identifier: "BEK nr 193 af 14/02/2011"
eli: "https://www.retsinformation.dk/eli/lta/2011/193"
accession_number: "B20110019305"
type: "executive_order"
jurisdiction: "dk"
language: "da"
date: 2011-02-14
status: "in_force"
ministry: "Indenrigs- og Sundhedsministeriet"
source: "https://www.retsinformation.dk/eli/lta/2011/193"
retrieved: 2026-10-11
---

# Bekendtgørelse om indberetning af oplysninger til lægemiddelstatistik

*BEK nr 193 af 14/02/2011*

Bilag 1

Bilag 2

I medfør af § 11, stk. 1, nr. 7, § 58, stk. 4, og § 61 d, stk. 2, i lov om apoteksvirksomhed, jf. lovbekendtgørelse nr. 855 af 4. august 2008, som ændret ved lov nr. 100 af 10. februar 2009 samt § 84, stk. 1, i lov nr. 1180 af 12. december 2005 om lægemidler, fastsættes efter bemyndigelse i § 1, stk. 4, i bekendtgørelse nr. 797 af 17. august 2009 om indberetning af oplysninger om omsætning mv. af lægemidler mv.:

#### § 1.

Indberetning af omsætningsoplysninger til Lægemiddelstyrelsens lægemiddelstatistikregister i henhold til bekendtgørelse om indberetning af oplysninger om omsætning mv. af lægemidler mv. skal foretages som anført i bilag 1 og 2 til denne bekendtgørelse.

#### § 2.

Bekendtgørelsen træder i kraft den 1. april 2011.

*Stk. 2.* Bekendtgørelse nr. 816 af 28. august 2009 om indberetning af oplysninger til lægemiddelstatistik ophæves*.*

Lægemiddelstyrelsen, den 14. februar 2011

Jytte Lyngvig

/ Anne-Marie Vangsted

## Bilag 1

Beskrivelse af de oplysninger, der skal indsendes til Lægemiddelstyrelsen i elektronisk læsbar form

## 1. Generelt

De indsamlede oplysninger indgår i en lægemiddelstatistikdatabase til brug for udarbejdelse af statistik, analyser, prisindeks og overvågning af lægemiddelsalget i Danmark.

Afsnit 2 angiver de tekniske og indholdsmæssige krav til filer.

Afsnit 3 er en beskrivelse af - og en samlet oversigt over - oplysningerne, der skal indberettes. Afsnittet indeholder endvidere en oversigt over de enkelte felters placering i filen, længde og type mv.

Afsnit 4 indeholder en oversigt over koder og tabeller.

## 2. Krav til indberetningerne

### 2.1 Indberetningsmåde

*2.1.1* Medmindre der forefindes en særlig aftale med Lægemiddelstyrelsen om, at der indberettes på anden måde, skal:

- – apoteker og sygehusapoteker indberette elektronisk til FTP-server via Medicinnettet.
- – forhandlere af receptpligtige lægemidler til produktionsdyr1) indberette elektronisk via FTP.lmsdetail.dk.
- – producenter og forhandlere af radioaktive lægemidler indberette via indtastningsskema på www.lmsdetail.dk.
- – virksomheder, der er indehaver af Lægemiddelstyrelsens tilladelse til forhandling og udlevering af diacetylmorphin2) indberette via FTP.lmsdetail.dk ved anvendelse af SSH File Transfer Protocol (SFTP).
- – øvrige indberetningspligtige indberette elektronisk via FTP.lmsdetail.dk.

Ved elektronisk indberetning via www.lmsdetail.dk og til FTP-server via Medicinnettet anvendes et brugernavn og password, der udleveres af Lægemiddelstyrelsen efter anmodning.

### 2.2 Indberetningsformater for de månedlige indberetninger

*2.2.1* Ved elektronisk indberetning ved brug af FTP

Apoteker anvender følgende filnavn:

NUMFI.MM

hvor

»NUM» er den indberetningspligtiges nummer (3 cifre, evt. med foranstillede nuller),

»FI» er enhedsnummer for underenheder, fx filial eller apoteksudsalg (2 cifre, evt. med foranstillet nul) og »MM» er månedens nummer (2 cifre, evt. med foranstillet nul).

Ved indberetning af salg af receptpligtige lægemidler til produktionsdyr, skal indberetningerne af den del af oplysningerne, der ikke indgår i apotekets samlede indberetning (jf. afsnittet ovenfor), ske i én samlet fil med følgende filnavn:

NUMFI.MMV

hvor

»NUM« er den indberetningspligtiges nummer (3 cifre, evt. med foranstillede nuller),

»FI« er enhedsnummer for underenheder, fx filial eller apoteksudsalg (2 cifre, evt. med foranstillet nul), »MM« er månedens nummer (2 cifre, evt. med foranstillet nul) og »V« betyder, at det er en veterinær indberetning.

Forhandlere af receptpligtige lægemidler til produktionsdyr, der ikke er apotek, anvender følgende filnavn:

NNNNNNNNNN.MMV

hvor

»NNNNNNNNNN« er forhandlerens P-nummer (10 cifre), »MM« er månedens nummer (2 cifre, evt. med foranstillet nul) og »V« betyder, at det er en veterinær indberetning.

Virksomheder, der er indehaver af Lægemiddelstyrelsens tilladelse til forhandling og udlevering af diacetylmorphin, jf. bekendtgørelse om euforiserende stoffer § 7 stk. 1, anvender følgende filnavn:

NNNNNNNNNN.MMH

Hvor

»NNNNNNNNNN« er forhandlerens P-nummer (10 cifre), »MM« er månedens nummer (2 cifre, evt. med foranstillet nul) og »H« betyder, at det en indberetning angående diacetylmorphin.

*2.2.2* Sker indberetning i henhold til en særlig aftale med Lægemiddelstyrelsen, jf. punkt 2.1, oplyses de specifikke særlige krav til filens udformning ved aftalens indgåelse.

*2.2.3* Følgende krav gælder for alle filer med de månedlige indberetninger:

<table>
<tr>
<td colspan="6"></td>
</tr>
<tr>
<td colspan="6">Den første linie i filen (headerlinien) skal have følgende indhold:</td>
</tr>
<tr>
<td>Nr.</td>
<td>Type</td>
<td>Fra</td>
<td>Til</td>
<td>Længde</td>
<td>Beskrivelse af feltindhold</td>
</tr>
<tr>
<td>F1</td>
<td>A</td>
<td>1</td>
<td>6</td>
<td>6</td>
<td>Snitfladeidentifikation</td>
</tr>
<tr>
<td>F2</td>
<td>A</td>
<td>7</td>
<td>21</td>
<td>15</td>
<td>Edb–leverandøridentifikation</td>
</tr>
<tr>
<td>F3</td>
<td>A</td>
<td>22</td>
<td>26</td>
<td>5</td>
<td>Edb–systemets godkendelsesnummer</td>
</tr>
<tr>
<td>F4</td>
<td>N</td>
<td>27</td>
<td>32</td>
<td>6</td>
<td>Udskriftsdato (ÅÅMMDD)</td>
</tr>
<tr>
<td>F5</td>
<td>N</td>
<td>33</td>
<td>37</td>
<td>5</td>
<td>Den indberetningspligtiges nummer</td>
</tr>
<tr>
<td>F6</td>
<td>N</td>
<td>38</td>
<td>41</td>
<td>4</td>
<td>Omsætningsmåned/år (ÅÅMM)</td>
</tr>
<tr>
<td>F 7</td>
<td>N</td>
<td>42</td>
<td>53</td>
<td>12</td>
<td>Antal records på filen (000000000001–999999999999)</td>
</tr>
<tr>
<td>F 8</td>
<td>A</td>
<td>54</td>
<td>63</td>
<td>10</td>
<td>Indberetterens CVR-nummer</td>
</tr>
</table>

<table>
<tr>
<td colspan="3">Felterne F1, F2, F3, F5 og F8 i headerlinien udfyldes efter følgende retningslinier:</td>
</tr>
<tr>
<td>Nr.</td>
<td>Feltindhold</td>
<td>Udfyldelse</td>
</tr>
<tr>
<td>F1</td>
<td>Snitfladeidentifikation</td>
<td>STAT06</td>
</tr>
<tr>
<td>F2</td>
<td>Edb-leverandøridentifikation</td>
<td>Indholdet fastlægges af den indberetningspligtiges edb-leverandør</td>
</tr>
<tr>
<td>F3</td>
<td>Edb-systemets godkendelsesnummer</td>
<td>Indholdet fastlægges af den indberetningspligtiges edb-leverandør</td>
</tr>
<tr>
<td>F5</td>
<td>Indberetternummer (udfyldes kun af apoteker)</td>
<td>Er indberetter ikke i besiddelse af et indberetternummer, udfyldes feltet med »00000«.</td>
</tr>
<tr>
<td>F8</td>
<td>Indberetterens CVR-nummer</td>
<td>Indberetterens 8-cifrede CVR-nummer (Det Centrale Virksomhedsregister) angives med foranstillet bogstavkode »CV«.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</table>

Den månedlige fil skal være en tekstfil i ASCII-format (hver linie i filen afsluttes med CR og LF henholdsvis ASCII 13 og ASCII 10).

Efter headerlinien følger linievis de i afsnit 3 specificerede oplysninger per ekspederet varenummer (linierne i filen skal have samme længde, jf. afsnit 3.3).

### 2.3 Indberetningsformater for **de daglige indberetninger** af receptpligtige lægemidler til produktionsdyr

*2.3.1* Ved elektronisk indberetning ved brug af FTP

Apoteker: For den del af omsætningsoplysningerne mv., der håndteres via apotekets primære system, skal apotekerne anvende følgende filnavn:

ANUMFITYYYYMMDD.DAT

hvor

»A« betyder, at indberetninger er fra et apotek, »NUM« er den indberetningspligtiges nummer,

»FI« er enhedsnummer for underenheder, fx filial eller apoteksudsalg, »T« betyder, at der kommer en tidsangivelse, »YYYY« er årstallet, »MM« er måneden (2 cifre, evt. med foranstillet nul), »DD«

er datoen, og »DAT« er filens suffix.

Apoteker: For den del af omsætningsoplysningerne mv., der håndteres via et særskilt system for de receptpligtige lægemidler til produktionsdyr, skal indberetningen ske i én samlet fil med følgende filnavn:

AVNUMFITYYYYMMDD.DAT

hvor

»A« betyder, at indberetninger er fra et apotek, »V« betyder, at data stammer fra et særskilt system for de receptpligtige lægemidler til produktionsdyr, »NUM« er den indberetningspligtiges nummer,

»FI« er enhedsnummer for underenheder, fx filial eller apoteksudsalg, »T« betyder, at der kommer en tidsangivelse, »YYYY« er årstallet, »MM« er måneden (2 cifre, evt. med foranstillet nul), »DD«

er datoen, og »DAT« er filens suffix.

Forhandlere af lægemidler til produktionsdyr, der ikke er apotek, anvender følgende filnavn:

NNNNNNNNNNTYYYYMMDD.DAT

hvor

»NNNNNNNNNN« er forhandlerens P-nummer (10 cifre), »YYYY« er årstallet, »MM« er månedens nummer (2 cifre, evt. med foranstillet nul) og »DD« er datoen (2 cifre, evt. med foranstillet nul).

*2.3.2* Indberetningen af de daglige omsætningstal skal være indsendt til Lægemiddelstyrelsen senest den efterfølgende dag kl. 20.00, og indberetningen skal foretages for alle kalenderdage uanset omsætningens størrelse, således at der også indberettes dage med nul omsætning.

*2.3.3* Følgende krav gælder for alle filer med de daglige indberetninger:

<table>
<tr>
<td colspan="6"></td>
</tr>
<tr>
<td colspan="6">Den første linie i filen (headerlinien) skal have følgende indhold:</td>
</tr>
<tr>
<td>Nr.</td>
<td>Type</td>
<td>Fra</td>
<td>Til</td>
<td>Længde</td>
<td>Beskrivelse af feltindhold</td>
</tr>
<tr>
<td>F1</td>
<td>A</td>
<td>1</td>
<td>6</td>
<td>6</td>
<td>Snitfladeidentifikation</td>
</tr>
<tr>
<td>F2</td>
<td>A</td>
<td>7</td>
<td>21</td>
<td>15</td>
<td>Edb-leverandøridentifikation</td>
</tr>
<tr>
<td>F3</td>
<td>A</td>
<td>22</td>
<td>26</td>
<td>5</td>
<td>Edb-systemets godkendelsesnummer</td>
</tr>
<tr>
<td>F4</td>
<td>N</td>
<td>27</td>
<td>32</td>
<td>6</td>
<td>Udskriftsdato (ÅÅMMDD)</td>
</tr>
<tr>
<td>F5</td>
<td>N</td>
<td>33</td>
<td>37</td>
<td>5</td>
<td>Indberetternummer (udfyldes kun af apoteker)</td>
</tr>
<tr>
<td>F6</td>
<td>N</td>
<td>38</td>
<td>45</td>
<td>8</td>
<td>Omsætningsdato (YYYYMMDD)</td>
</tr>
<tr>
<td>F7</td>
<td>N</td>
<td>46</td>
<td>50</td>
<td>5</td>
<td>Antal records i filen (00000-99999)</td>
</tr>
<tr>
<td>F8</td>
<td>A</td>
<td>51</td>
<td>60</td>
<td>10</td>
<td>Indberetters CVR-nummer</td>
</tr>
</table>

<table>
<tr>
<td colspan="3">Felterne F1, F2, F3, F5 og F8 i headerlinien udfyldes efter følgende retningslinier:</td>
</tr>
<tr>
<td>Nr.</td>
<td>Feltindhold</td>
<td>Udfyldelse</td>
</tr>
<tr>
<td>F1</td>
<td>Snitfladeidentifikation</td>
<td>VET001</td>
</tr>
<tr>
<td>F2</td>
<td>Edb-leverandøridentifikation</td>
<td>Indholdet fastlægges af den indberetningspligtiges edb-leverandør.</td>
</tr>
<tr>
<td>F3</td>
<td>Edb-systemets godkendelsesnummer</td>
<td>Indholdet fastlægges af den indberetningspligtiges edb-leverandør.</td>
</tr>
<tr>
<td>F5</td>
<td>Indberetternummer</td>
<td>Er indberetter ikke i besiddelse af et indberetternummer, udfyldes feltet med »00000«.</td>
</tr>
<tr>
<td>F8</td>
<td>Indberetterens CVR-nummer</td>
<td>Indberetterens 8-cifrede CVR-nummer (Det Centrale Virksomhedsregister) angives med foranstillet bogstavkode »CV«.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</table>

Den daglige indberetningsfil skal være en tekstfil i ASCII-format (hver linie i filen afsluttes med

CR og LF henholdsvis ASCII 13 og ASCII 10) og indberettes elektronisk.

Efter headerlinien følger linievis de i afsnit 3 specificerede oplysninger per ekspederet varenummer (linierne i filen skal have samme længde, jf. afsnit 3.3).

## 3. Indberetningspligtige oplysninger

### 3.1 Generelle bemærkninger

Der anvendes samme snitflade vedrørende felterne 1 - 43 for alle indberetningspligtige og for alle typer indberetninger. Som de eneste skal sygehusapoteker herudover, også indberette tre ekstra felter, felt 44, 45 og 46.

Felter, der ikke kan udfyldes, skal være blanke.

Der skal indberettes foranstillede nuller i alle felter, der udfyldes, medmindre andet er angivet.

Det er ekspeditionsdatoen, dvs. datoen for gennemført kassetransaktion/debitering, der er afgørende for, hvilken måned ekspeditionen vedrører.

Alle beløbsfelter og antal pakninger indberettes med negativt fortegn (-) ved tilbageførsler. Det eventuelle fortegn placeres i feltets første position.

Ved udligning af for meget eller for lidt udbetalt medicintilskud indberettes nogle af beløbsfelterne med negativt fortegn. Hvis patienten har fået udbetalt for lidt i medicintilskud, indberettes det yderligere tilskud positivt i felt 20, mens tilbagebetalingen til patienten indberettes negativt i felt 17. Korrigeres der samtidig for for meget udbetalt kommunalt tilskud, indberettes tilbagebetaling af kommunalt tilskud negativt i felt 23. Hvis patienten i stedet skal tilbagebetale medicintilskud, indberettes det tilbagebetalte medicintilskud negativt, patientens yderligere betaling positivt og et eventuelt yderligere kommunalt tilskud positivt. Ved udligning gælder det, at medicintilskud + patientens egenbetaling + kommunalt tilskud = 0.

Ved salg af dosisdispenserede lægemidler til enkeltpersoner skal det receptekspederende apotek indberette én linie for hvert lægemiddel (varenummer), som indgår i dosispakningen – herunder hvor mange enheder af hvert lægemiddel, der indgår i pakningen. Dosisekspeditionsgebyret og dosispakningsgebyret indberettes på hver sin linie. Der anvendes ekspeditionstypen DD og et af varenumrene fra bilag 2.10.

Ved salg af dosispakninger mellem to apoteker indberetter det apotek, som pakker dosispakningen, den solgte dosispakning på én linie med varenummeret 688000. Afregning af dosispakningsgebyret indberettes ligeledes på én linie. Der anvendes ekspeditionstypen SD.

### 3.2 Gennemgang af hvad felterne skal udfyldes med

| Felt 01 Ekspeditionsdato |
|---|
| Feltet udfyldes med dato for gennemført kassetransaktion/debitering/udlevering. |

| Felt 02 Ekspeditionsnummer |
|---|
| Feltet skal altid udfyldes, når der til enkeltpersoner ekspederes de lægemidler, der er nævnt i receptbekendtgørelsens § 4<sup>3)</sup>. Feltet må endvidere gerne udfyldes ved andre ekspeditioner. |
| <sup>3)</sup> Bekendtgørelse nr. 155 af 20. februar 2007 om recepter. |

<table>
<tr>
<td>Felt 03 Ekspeditionstype</td>
<td>Kode</td>
</tr>
<tr>
<td><strong>Private apoteker</strong><br>Receptursalg<br>Enkeltpersoner (ej erhverv) og mindre salg til læger (erhverv)<sup>4)</sup><br>- ikke dosisdispenserede lægemidler<br>- dosisdispenserede lægemidler og gebyr herfor<br>Sygehuse mv. og større salg til læger<sup>4)</sup><br>Større salg til dyrlæger<sup>4)</sup><br>Alle andre dyrlægeordinationer<br>Andre apoteker mv., ikke dosisdispenserede lægemidler<br>Andre apoteker mv., dosisdispenserede lægemidler og gebyr herfor<br>Andre apoteker mv., andet</td>
<td>EI<br>DD<br>LI<br>DI<br>ID<br>SL<br>SD<br>SA</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>Andet<br>Håndkøbslægemidler<br>Frihandelsvarer<br>Andre driftsindtægter<br>Udligning af for meget eller for lidt udbetalt tilskud (CTR)</td>
<td>HA<br>HF<br>AD<br>UL</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>Sygehusapoteker mv.<br>Sygehusafdelinger, lægemidler ej unit-dose<br>Sygehusafdelinger, lægemidler unit-dose<br>Sygehusapoteker, lægemidler<br>Private apoteker, lægemidler<br>Lægemidler til andre, herunder universitet, ambulancetjeneste, hospice m.fl.</td>
<td>AI<br>UD<br>SI<br>PI<br>LA</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>Forhandlere af receptpligtige lægemidler til produktionsdyr<br>Receptursalg til produktionsdyr</td>
<td>DI</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>Statens Serum Institut<br>Læger med ydernummer<br>Læger uden ydernummer<br>Sygehusafdelinger<br>Sygehusapoteker<br>Private apoteker<br>Andre, herunder forsvaret, asylcentre m.fl.</td>
<td>KM<br>KU<br>KA<br>KS<br>KP<br>KK</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>For virksomheder, der er indehaver af Lægemiddelstyrelsens tilladelse til forhandling og udlevering af diacetylmorphin<br>Diacetylmorphin til misbrugsbehandlingssteder</td>
<td>HE</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>Producenter og forhandlere af radioaktive lægemidler<br>Salg af radioaktive lægemidler</td>
<td>RA</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>Veterinærinstituttet DTU og Veterinærapoteket, Københavns Universitet<br>Receptursalg engros til apoteker og andre forhandlere<br>Andre dyrlægeordinationer</td>
<td>PI<br>VI</td>
</tr>
<tr>
<td colspan="2"><sup>4)</sup>Afgrænsningen af, om der er tale om et større eller mindre salg til læger/dyrlæger følger bekendtgørelse nr. 388 af 16. april 2010 om beregning af forbrugerpriser mv. på lægemidler § 2, stk. 1, og § 2 stk. 5, jf. stk. 3, hvor der skelnes mellem køb af lægemidler til speciallægeklinikker og sundhedspersoner for mere eller mindre end 500.000 kr. i det foregående kalenderår.</td>
</tr>
</table>

| Felt 04 Den indberetningspligtiges nummer |
|---|
| Entydig identifikation af den indberetningspligtige.<br>Apoteksnumre angives ved 3 cifre efterfulgt af et apoteks enhedsnummer angivet ved 2 cifre.<br>Reglerne for tildeling af enhedsnummeret er:<br>00 Hovedapoteket<br>01 – 09 Filialenheder<br>10 – 99 Apoteksudsalg<br>Lægemiddelstyrelsen kan tildele numre til øvrige indberetningspligtige. |

| Felt 05 Udleveringssted |
|---|
| Følgende kodeværdier anvendes: |
| 0 Hovedapotek, filial eller apoteksudsalg<br>1 Håndkøbsudsalg<br>2 Medicinudleveringssted |

<table>
<tr>
<td colspan="2">Felt 06 Identifikation af modtageren af lægemidlet</td>
<td>Kode</td>
</tr>
<tr>
<td colspan="2">Person med CPR-nummer<br>Receptsalg af både tilskudsberettiget og ikke tilskudsberettiget medicin.<br>Feltet udfyldes med<br>Dette gælder også, hvis en læge eller tandlæge ordinerer et lægemiddel til behandling af sig selv (»Til eget brug«)<br>Person uden CPR-nummer<br>Gruppen omfatter<br>- dansk statsborger med bopæl i Danmark, hvor CPR-nummeret ikke er korrekt oplyst, og nyfødt som endnu ikke har et sundhedskort (berettiget til medicintilskud)<br>- udenlandsdansker (berettiget til medicintilskud afhængig af bopælsland)<br>- statsborger fra Færøerne, Grønland, Nordisk land eller EU/EØS land (berettiget til medicintilskud efter særlige regler)<br>- diplomat og grænsegænger (berettiget til medicintilskud efter særlige regler)<br>- udlænding fra andre end ovennævnte lande/kategorier, tilflytter fra udlandet, der endnu ikke har et sundhedskort, og asylansøger (ikke berettiget til medicintilskud).<br>Receptsalg af tilskudsberettiget medicin til person, der er berettiget<br>til medicintilskud.</td>
<td>CPR-nummer</td>
</tr>
<tr>
<td colspan="2">Feltet udfyldes med<br>som tildeles af Lægemiddelstyrelsens Centrale Tilskudsregister.</td>
<td>det fiktive CPR-nummer</td>
</tr>
<tr>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td colspan="2">Det fiktive CPR-nummer er på formen 4xxxllllll eller 5xxxllllll, hvor<br>llllll er et individuelt løbenummer, og hvor landekoden (xxx) kan<br>antage følgende værdier:</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Landekode</td>
<td>Land</td>
<td></td>
</tr>
<tr>
<td>006<br>014<br>022<br>030<br>049<br>057<br>065<br>081<br>332<br>340<br>359<br>367<br>375<br>383<br>391<br>405<br>413<br>421<br>448<br>456<br>464<br>472<br>480<br>499<br>502<br>510<br>529<br>537<br>545<br>553<br>561<br>588<br>596<br>618</td>
<td>Norge<br>Sverige<br>Island<br>Finland<br>Grønland<br>Færøerne<br>Danmark<br>Tyrkiet<br>Storbritannien<br>Italien<br>Holland<br>Belgien<br>Luxemburg<br>Frankrig<br>Tyskland<br>Irland<br>Grækenland<br>Spanien<br>Portugal<br>Østrig<br>Liechtenstein<br>Schweiz<br>Estland<br>Letland<br>Litauen<br>Polen<br>Tjekkiet<br>Slovakiet<br>Ungarn<br>Slovenien<br>Malta<br>Cypern<br>Bulgarien<br>Rumænien</td>
<td></td>
</tr>
<tr>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td colspan="2">For diplomat og grænsegænger anvendes<br>(CPR-nummer eller den system-genererede kode) fra det Særlige Sundhedskort.</td>
<td>det individuelle nummer</td>
</tr>
<tr>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td colspan="2">Receptsalg af ikke tilskudsberettiget medicin til person, der ellers er berettiget til tilskud - og receptsalg af både tilskudsberettiget og ikke tilskudsberettiget medicin til person, der ikke er berettiget til tilskud<strong>.</strong><br>Feltet udfyldes med erstatningskoderne:</td>
<td></td>
</tr>
<tr>
<td colspan="2">1) dansk statsborger med bopæl i Danmark uden gyldigt CPR-nummer og barn uden sundhedskort<br>2) udlænding, udenlandsdansker, diplomat og grænsegænger<br>3) asylansøger</td>
<td>4000000995<br>4000000999<br>4000005555</td>
</tr>
<tr>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td colspan="2">Feltet kan alternativt udfyldes med personens fiktive CPR-nummer fra<br>CTR eller det individuelle nummer fra det Særlige Sundhedskort,<br>såfremt et sådant haves.</td>
<td></td>
</tr>
<tr>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td colspan="2">Til brug i egen praksis<br>Feltet udfyldes med følgende koder:<br>1) læge- og speciallægepraksis<br>2) dyrlægepraksis<br>hvor xxxx er praksisnummeret.<br>3) tandlægepraksis</td>
<td>3200000000<br>330000xxxx<br>3400000000</td>
</tr>
<tr>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td colspan="2">Apoteker eller andre med tilladelse til receptursalg, inkl. sygehusapoteker<br>Feltet udfyldes med<br>hvor xxxxx er det modtagende apoteks indberetternummeret jf. felt 04.</td>
<td>40000xxxxx</td>
</tr>
<tr>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td colspan="2">Institution med sygehus-afdelingsklassifikationskode, jf. Sundhedsvæsenets Organisationsregister (SOR)<br>Ved leverance til institutioner anført i SOR udfyldes feltet med<br>hvor xxxxxxx er sygehus- og afdelingskode.<br>Ved manglende afdelingskode udfyldes feltet med<br>hvor xxxx er sygehusets 4-cifrede kode.<br>Ved manglende institutions-, sygehus- og afdelingskode anvendes erstatningskoden</td>
<td>SORxxxxxxx<br>SORxxxx000<br>SOR0000000</td>
</tr>
<tr>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td colspan="2">Institution uden sygehus-afdelingsklassifikationskode, jf. SOR<br>Ved leverance til misbrugsbehandlingsinstitutioner jf. Sundhedsstyrelsens liste over behandlingssteder anvendes erstatningskoden<br>Ved leverance af diacetylmorphin til misbrugsbehandlingsinstitutioner udfyldes feltet med<br>hvor xxxxxxxx er behandlingsstedets CVR-nummer.<br>Ved leverance til andre institutioner, skibskister mv. udfyldes med</td>
<td>4700000000<br>CVxxxxxxxx<br>4600000000</td>
</tr>
<tr>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td colspan="2">Produktionsdyr, erhverv<br>Ved dyrehold med CHR-nummer udfyldes feltet med<br>hvor xxxxxx er det 6-cifrede CHR-nummer.<br>Ved uoplyst CHR-nummer anføres i stedet erstatningskoden</td>
<td>0000xxxxxx<br>0000999999</td>
</tr>
<tr>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td colspan="2">Hobby-/kæledyr<br>Feltet udfyldes med</td>
<td>4800000000</td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
</table>

Felt 07 udgår

| Felt 08 Identifikation af receptudsteder/rekvirent | Kode |
|---|---|
| Feltet skal udfyldes, uanset om ordinationen er tilskudsberettiget eller ej. |  |
| Alment praktiserende læge, vagtlæge, speciallæge eller tandlæge |  |
| Feltet udfyldes med | ydernummeret |
| Hvis ydernummeret ikke kan fremskaffes eller er forkert oplyst anvendes erstatningskoden | 0990027 |
| Sygehusansat læge |  |
| Feltet udfyldes med<br>hvor xxxxxxx er sygehus- og afdelingskode for den afdeling lægen er ansat på, jf. Sundhedsvæsenets Organisationsregister (SOR). | xxxxxxx |
| Ved manglende afdelingskode udfyldes feltet med<br>hvor xxxx er sygehuskoden. | xxxx000 |
| Ved manglende sygehus- og afdelingskode anvendes erstatningskoden | 0994057 |
| **Læge/tandlæge uden for ovenstående kategorier,** men med dansk autorisation |  |
| Feltet udfyldes med erstatningskoden | 0990027 |
| **Læge/tandlæge uden dansk autorisation,** men med autorisation fra enten Færøerne, Grønland, Nordisk land eller EU/EØS land |  |
| Feltet udfyldes med | U000xxx |
| hvor landekoden (xxx) kan antage de samme værdier som nævnt i felt 06. |  |
| Dyrlæge |  |
| Feltet udfyldes med | Vxxxxxx |
| hvor xxxxxx er det 6-cifrede autorisationsnummer (eventuelt med foranstillede nuller), som er tildelt af Fødevarestyrelsen. V anvendes som 1. karakter i feltet for at undgå sammenfald mellem lægers/tandlægers ydernummer og autorisationsnummeret. |  |
| Ved uoplyst autorisationsnummer benyttes erstatningskoden | V000000 |
| For udenlandsk dyrlæge benyttes erstatningskoden | V999999 |
| Institution med sygehus-afdelingsklassifikationskode, jf. (SOR) |  |
| Ved leverance til institutioner anført i SOR udfyldes feltet med | xxxxxxx |
| hvor xxxxxxx er sygehus- og afdelingskode. |  |
| Ved manglende afdelingskode udfyldes feltet med | xxxx000 |
| hvor xxxx er sygehusets 4-cifrede kode. |  |
| Ved manglende institutions-, sygehus- og afdelingskode anvendes erstatningskoden | 0994057 |
| Institution uden sygehus-afdelingskode, jf. SOR |  |
| Ved leverance til misbrugsbehandlingsinstitutioner, jf. Sundhedsstyrelsens liste over behandlingssteder, og ved leverance til andre behandlingsinstitutioner mv. anvendes den rekvirerende læges/tandlæges | ydernummer |
| Ved manglende ydernummer anvendes erstatningskoden | 4600000 |
| Rekvisitioner fra andre (fx jordemødre, sygeplejersker, skibsførere) |  |
| Feltet udfyldes med | 4700000 |

| Felt 09 Lægens CPR-nummer | Kode |
|---|---|
| Lægens CPR-nummer indberettes, når der til enkeltpersoner ekspederes de lægemidler, der er nævnt i receptbekendtgørelsens § 4<sup>3)</sup> medmindre ordinationen sker ved en elektroniske recept eller ved den af Sundhedsstyrelsens særligt udformede receptblanket (narkocheck). |  |
| Lægens CPR-nummer skal dog kun indberettes, hvor det ikke er muligt at indberette lægens autorisationsID i henhold til receptbekendtgørelsen. |  |
| Ved skibsførere, der kan rekvirere morfin mv. til »skibskisten« udfyldes feltet med erstatningskoden | 4000000103 |
| Undtaget er også udenlandske læger, der ordinerer kopieringspligtige lægemidler i henhold til § 25 i receptbekendtgørelsen. For disse udfyldes feltet med erstatningskoden | 4000000999 |

| Felt 10 Det ordinerede varenummer |
|---|
| Feltet udfyldes med det ordinerede varenummer. Der benyttes samme regler for det ordinerede som det udleverede varenummer, jf. felt 12. |

| Felt 11 Receptens løbenummer |
|---|
| Receptens løbenummer skal indberettes, når ordinationen er foretaget på den særlige receptblanket med løbenummer som er udformet af Sundhedsstyrelsen (narkocheck) til ordination af de kopieringspligtige lægemidler ifølge receptbekendtgørelsens § 4, jf. felt 09. |
| Receptens løbenummer skal dog kun indberettes, hvor det ikke er muligt at indberette lægens autorisationsID i henhold til receptbekendtgørelsen. |

| Felt 12 Det udleverede varenummer |
|---|
| Ved indberetning af salg af **lægemidler** anvendes<br>- det nordiske varenummer, der er påtrykt den udleverede pakning. Nordiske varenumre ligger i intervallerne 000001 – 199999 og 370000 – 599999,<br>- et varenummer til lægemiddelpakninger fra Amgros og Danmarks Apotekerforening. Disse ligger i intervallet 700000 – 749999.<br>Hvis lægemiddelpakningen ikke har et af disse varenumre, anvendes i stedet et varenummer tildelt af Lægemiddelstyrelsen, jf. bilag 2 i denne bekendtgørelse. Disse varenumre ligger i intervallet 685000 – 689999. Varenumre i dette interval må ikke anvendes af andre eller til andre formål end det, der fremgår af bilaget. |
| Til indberetning af salg af lægemidler må der ikke anvendes varenumre uden for ovenstående intervaller. |
| For **gebyrer, udligning af tilskud mv.** anvendes ligeledes varenumre fra bilag 2. |
| For **frihandelsvarer mv.** anvendes apotekernes og grossisternes fælles varenummerliste (varenumre i intervallerne 200000 – 249999, 660000 – 679999 og 750000 – 799999). |
| Varenumre i intervallerne 680000 – 684999, 690000 – 699999 og 800000 – 999999 er udelukkende til internt brug i virksomheder. |

| Felt 13 Antal pakninger eller enheder af det ekspederede varenummer |
|---|
| Ved salg af ikke dosisdispenserede lægemiddelpakninger udfyldes feltet med antal pakninger.<br>Ved salg af radioaktive lægemidler kan antal pakninger også være: antal vials, antal generatorer eller antal kit.<br>Ved dosisdispenserede lægemidler (felt 03 = DD) udfyldes feltet med antal enheder (tabletter eller kapsler).<br>Feltet skal ikke udfyldes ved ekspedition af serviceprodukter fra sygehusapoteker, jf. bilag 2.2 og bilag 2.3.<br>Ved udligning af for meget eller for lidt udbetalt tilskud (felt 12 = 100015) udfyldes feltet med 1. |

<table>
<tr>
<td colspan="2">Felt 14 Reiterationsnummer</td>
</tr>
<tr>
<td colspan="2">Nummeret angiver, hvilken gang det ordinerede er udleveret.</td>
</tr>
<tr>
<td>00</td>
<td>Éngangsordination</td>
</tr>
<tr>
<td>01-99</td>
<td>Aktuelt nummer på udlevering af en flergangsordination</td>
</tr>
</table>

Felt 15 er udgået.

| Felt 16 Ekspeditionens pris i øre inkl. moms |
|---|
| For receptekspeditioner til enkeltpersoner på apoteker beregnes ekspeditionens samlede pris som: |
| (Gældende medicinpris + recepturgebyr + evt. færdigblandingsgebyr) x antal pakninger |
| Ved gældende medicinpris forstås lægemidlets pris inkl. moms, ekskl. recepturgebyr.<br>I de tilfælde, hvor der ikke udløses recepturgebyr, medregnes recepturgebyr ikke.<br>Priser skal anføres i øre inkl. moms. Ved momsfrit salg skal det indberettede beløb være tillagt moms. |
| Sygehusapoteker skal indberette pakningens sidst registrerede indkøbspris (SRIP) tillagt moms. |
| Ved apotekers dosisdispensering til enkeltpersoner beregnes prisen på det enkelte varenummer, der indgår i dosispakningen som: |
| Pris per enhed x antal enheder |
| Beregningen af pris per enhed fremgår af bekendtgørelse om beregning af forbrugerpriser på apoteksforbeholdte lægemidler mv.<sup>5)</sup> |
| <sup>5)</sup> Bekendtgørelse nr. 112 af 11. februar 2011 om beregning af forbrugerpriser på apoteksforbeholdte lægemidler mv. |

Felt 17 Modtagers betaling i øre inkl. moms

<table>
<tr>
<td colspan="2">Felt 18 Nummeret på den refusionsgivende region</td>
</tr>
<tr>
<td colspan="2">Ved receptekspeditioner til enkeltpersoner defineres regionens nummer ud fra den sikredes adresse. Ved ekspedition af lægemidler til brug i praksis defineres regionens nummer ud fra praksisadressen.</td>
</tr>
<tr>
<td colspan="2"></td>
</tr>
<tr>
<td colspan="2">Følgende regionskoder skal anvendes:</td>
</tr>
<tr>
<td>081</td>
<td>Region Nordjylland</td>
</tr>
<tr>
<td>082</td>
<td>Region Midtjylland</td>
</tr>
<tr>
<td>083</td>
<td>Region Syddanmark</td>
</tr>
<tr>
<td>084</td>
<td>Region Hovedstaden</td>
</tr>
<tr>
<td>085</td>
<td>Region Sjælland</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">Er den sikrede fra Norden eller EU anføres 041.</td>
</tr>
</table>

<table>
<tr>
<td colspan="2">Felt 19 Det regelnummer, hvorefter patienten er berettiget til medicintilskud, jf. sundhedslovens kapitel 42 og 44</td>
</tr>
<tr>
<td colspan="2">Gyldige regelnumre i forbindelse med enkeltpersoner:</td>
</tr>
<tr>
<td>41</td>
<td>Generelt medicintilskud</td>
</tr>
<tr>
<td>42</td>
<td>Enkelttilskud</td>
</tr>
<tr>
<td>43</td>
<td>Forhøjet tilskud</td>
</tr>
<tr>
<td>44</td>
<td>Udligning af tilskud (CTR)</td>
</tr>
<tr>
<td>45</td>
<td>Ernæringspræparater</td>
</tr>
<tr>
<td>59</td>
<td>Uspecificeret tilskud</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">Gyldige regelnumre i forbindelse med brug i praksis:</td>
</tr>
<tr>
<td>11</td>
<td>Rekvisition af lægemidler fra alment praktiserende læger og vagtlæger</td>
</tr>
<tr>
<td>13</td>
<td>Rekvisition af lægemidler fra speciallæger</td>
</tr>
<tr>
<td>14</td>
<td>Rekvisition af forbindsstoffer fra speciallæger</td>
</tr>
<tr>
<td>16</td>
<td>Rekvisition af forbindsstoffer fra alment praktiserende læger og vagtlæger</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">Hvis flere regelnumre anvendes (eksempelvis 41 og 43), indberettes det højeste regelnummer.</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">Hvis patienten er berettiget til tilskud, men befinder sig på den del af tilskudsskalaen, hvor der er fuld egenbetaling, udfyldes feltet også med det korrekte regelnummer, felt 20 udfyldes med 0, felt 18 udfyldes med regionskoden, og felt 34 udfyldes med patienttypen.</td>
</tr>
</table>

Felt 20 Medicintilskud efter sundhedslovens kapitel 42 og 44 i øre inkl. moms

| Felt 21 Nummeret på den refusionsgivende kommune. |
|---|
| Oversigt over kommunenumre findes i CPR-registrets myndighedsoplysninger for kommuner og regioner. |

<table>
<tr>
<td colspan="2">Felt 22 Regelnummer, hvorefter kommunen har ydet tilskud nr. 1</td>
</tr>
<tr>
<td colspan="2">Gyldige kommunale regelnumre:</td>
</tr>
<tr>
<td>61</td>
<td>Lov om social service § 41</td>
</tr>
<tr>
<td>62</td>
<td>Lov om social service § 100</td>
</tr>
<tr>
<td>63</td>
<td>Lov om social service § 112</td>
</tr>
<tr>
<td>64</td>
<td>Lov om social service § 122</td>
</tr>
<tr>
<td>71</td>
<td>Lov om integration § 36</td>
</tr>
<tr>
<td>72</td>
<td>Lov om aktiv socialpolitik § 82</td>
</tr>
<tr>
<td>75</td>
<td>Lov om social pension § 14 og Lov om højeste, mellemste og forhøjet almindelig og almindelig førtidspension mv. § 18</td>
</tr>
<tr>
<td>76</td>
<td>Lov om social pension § 14, stk. 1, og Lov om højeste, mellemste og forhøjet almindelig og almindelig førtidspension mv. § 17, stk. 2</td>
</tr>
<tr>
<td>79</td>
<td>Uspecificeret tilskud</td>
</tr>
</table>

Felt 23 1. kommunale tilskud i øre inkl. moms

| Felt 24 Regelnummer, hvorefter kommunen har ydet tilskud nr. 2 |
|---|
| Se bemærkningerne under punkt 3.22 ovenfor.<br>Hvis flere regelnumre anvendes, indberettes det laveste regelnummer. |

| Felt 25 2. kommunale tilskud i øre inkl. moms |
|---|
| Et eventuelt 2. tilskud fra kommunen anføres her. |

| Felt 26 Andre refusionsordninger |
|---|
| Feltet anvendes til refusioner, der ikke kan indpasses i øvrige felter. |
| Følgende kodeværdi er i anvendelse: |
| 21 Forsvaret |

Felt 27 Eventuelle andre tilskud anføres her i øre inkl. moms

Felterne 28 - 30 er udgået.

| Felt 31 Fravalg af substitution |
|---|
| Feltet udfyldes med et »S« for fravalg af substitution, hvis der på recepten er anført »Ej S«. |

Felt 32 er udgået.

| Felt 33 Tidsstempel |
|---|
| Klokkeslæt for gennemført kassetransaktion/debitering*.* |

<table>
<tr>
<td colspan="2">Felt 34 Patienttype</td>
</tr>
<tr>
<td colspan="2">Ved ekspedition af lægemidler, hvor patienten er berettiget til tilskud, udfyldes feltet med en af følgende koder:</td>
</tr>
<tr>
<td>00</td>
<td>Almen, voksen</td>
</tr>
<tr>
<td>01</td>
<td>Almen, barn</td>
</tr>
<tr>
<td>10</td>
<td>Kroniker, voksen</td>
</tr>
<tr>
<td>11</td>
<td>Kroniker, barn</td>
</tr>
<tr>
<td>88</td>
<td>Person i infertilitetsbehandling</td>
</tr>
<tr>
<td>99</td>
<td>Terminalpatient</td>
</tr>
</table>

| Felt 35 Tilskudspris i øre inkl. moms (IBGP, Beregningsgrundlagspris) |
|---|
| Det beløb, der ligger til grund for beregning af medicintilskud. Beløbet beregnes ud fra den tilskudspris, som er angivet i Medicinpriser. |
| Ved salg af pakninger: tilskudspris x antal pakninger.<br>Ved dosisdispensering: tilskudspris per enhed x antal enheder.<br>Hvis der er tale om forhøjet tilskud eller terminaltilskud, er tilskudsprisen dog lig med ekspeditionsprisen. |
| Feltet udfyldes, når patienten er berettiget til medicintilskud – også selvom patienten befinder sig på den del af tilskudsskalaen, hvor der er fuld egenbetaling. |

<table>
<tr>
<td colspan="3">Felt 36 Dyreart</td>
</tr>
<tr>
<td colspan="3">Ved dyrlægers ordination til erhverv udfyldes feltet med dyreart efter følgende koder:</td>
</tr>
<tr>
<td>Kvæg</td>
<td>12</td>
<td></td>
</tr>
<tr>
<td>Får, geder</td>
<td>13</td>
<td></td>
</tr>
<tr>
<td>Svin</td>
<td>15</td>
<td></td>
</tr>
<tr>
<td>Pelsdyr</td>
<td>24</td>
<td></td>
</tr>
<tr>
<td>Fjerkræ</td>
<td>30</td>
<td></td>
</tr>
<tr>
<td>Akvakulturer</td>
<td>51</td>
<td></td>
</tr>
<tr>
<td>Andre produktionsdyr</td>
<td>95</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">Ved dyrlægers ordination til hobby-/kæledyr udfyldes feltet med dyreart efter følgende koder:</td>
</tr>
<tr>
<td>Heste</td>
<td>11</td>
<td></td>
</tr>
<tr>
<td>Andre hobby-/kæledyr</td>
<td>90</td>
<td></td>
</tr>
</table>

<table>
<tr>
<td colspan="3">Felt 37 Aldersgruppe</td>
</tr>
<tr>
<td colspan="3">Ved dyrlægers ordination til erhverv udfyldes feltet med følgende koder for aldersgrupper:</td>
</tr>
<tr>
<td>Svin</td>
<td>Pattegrise, søer, gylte og orner</td>
<td>55</td>
</tr>
<tr>
<td></td>
<td>Smågrise mellem 7 og 30 kg</td>
<td>56</td>
</tr>
<tr>
<td></td>
<td>Svin over 30 kg, undtagen søer,</td>
<td></td>
</tr>
<tr>
<td></td>
<td>gylte og orner</td>
<td>57</td>
</tr>
<tr>
<td>Kvæg</td>
<td>Køer, tyre</td>
<td>61</td>
</tr>
<tr>
<td></td>
<td>Kalve under 12 mdr.</td>
<td>62</td>
</tr>
<tr>
<td></td>
<td>Ungdyr, stude over 12 mdr.</td>
<td>63</td>
</tr>
<tr>
<td>Får, geder</td>
<td>Dyr over 12 mdr.</td>
<td>68</td>
</tr>
<tr>
<td></td>
<td>Lam, kid under 12 mdr.</td>
<td>69</td>
</tr>
<tr>
<td>Fjerkræ</td>
<td>Slagtefjerkræ</td>
<td>75</td>
</tr>
<tr>
<td></td>
<td>Æglæggere</td>
<td>76</td>
</tr>
<tr>
<td></td>
<td>Opdræt</td>
<td>77</td>
</tr>
<tr>
<td colspan="3">For andre produktionsdyr, heste og hobby-/kæledyr udfyldes feltet med erstatningskoden 00.</td>
</tr>
</table>

<table>
<tr>
<td colspan="2">Felt 38 Ordinationsgruppe</td>
</tr>
<tr>
<td colspan="2">Ved dyrlægers ordination til svin, kvæg, får, geder og pelsdyr anvendes følgende ordinationsgrupper:</td>
</tr>
<tr>
<td>Reproduktion, urogenitalsystem</td>
<td>10</td>
</tr>
<tr>
<td>Yver</td>
<td>11</td>
</tr>
<tr>
<td>Gastrointestinale lidelser</td>
<td>12</td>
</tr>
<tr>
<td>Respirationsvejslidelser</td>
<td>13</td>
</tr>
<tr>
<td>Led, lemmer, klove, centralnervesystem, hud</td>
<td>14</td>
</tr>
<tr>
<td>Stofskifte, fordøjelse, kredsløb</td>
<td>15</td>
</tr>
<tr>
<td>Andet (kan kun anvendes ved pelsdyr)</td>
<td>16</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">Ved dyrlægers ordination til akvakulturer anvendes følgende ordinationsgrupper:</td>
</tr>
<tr>
<td>Rødmundesyge</td>
<td>20</td>
</tr>
<tr>
<td>Furunkulose</td>
<td>21</td>
</tr>
<tr>
<td>Yngelsyndrom</td>
<td>22</td>
</tr>
<tr>
<td>Andet</td>
<td>23</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">Ved dyrlægers ordination til fjerkræ anvendes følgende ordinationsgrupper:</td>
</tr>
<tr>
<td>Bughinde- og bughuleorganer:</td>
<td></td>
</tr>
<tr>
<td>Coccidiose</td>
<td>30</td>
</tr>
<tr>
<td>Enteritis</td>
<td>31</td>
</tr>
<tr>
<td>Hepatitis</td>
<td>32</td>
</tr>
<tr>
<td>Salpingitis</td>
<td>33</td>
</tr>
<tr>
<td>Andet</td>
<td>34</td>
</tr>
<tr>
<td>Respirationsveje og -organer</td>
<td>35</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">Ved dyrlægers ordination af vacciner og sera udfyldes feltet med 99.</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">Ved dyrlægers ordination til andre produktionsdyr, heste og hobby-/kæledyr udfyldes feltet med 00.</td>
</tr>
</table>

| Felt 39 Takseringsdato |
|---|
| Dato for prisfastsættelse af lægemiddelekspeditionen. |

| Felt 40 Salgsstedets P-nummer |
|---|
| Feltet udfyldes med salgsstedets P- nummer (nummer for produktionsenhed ifølge Det Centrale Virksomhedsregister). |

| Felt 41 Indikation for ordination |
|---|
| Feltet udfyldes med en kode for indikation for ordination. |

| Felt 42 Dosering for ordination |
|---|
| Feltet udfyldes med kode for dosering for ordination. |

| Felt 43 AutorisationsID for receptudsteder |
|---|
| Feltet udfyldes med autorisationsID for alle læger og tandlæger. |

| Felt 44 Typen af mængden af parenterale serviceprodukter fra sygehusapoteker |
|---|
| Feltet udfyldes med typen af mængden af parenterale serviceprodukter inden for ATC-gruppe J01 og L01. Liste med typer kan fås ved henvendelse til Lægemiddelstyrelsen. Feltet udfyldes uden foranstillet nul i de tilfælde, hvor typen kun er to karakterer. |

| Felt 45 Mængden af parenterale serviceprodukter fra sygehusapoteker |
|---|
| Feltet udfyldes med ekspeditionens totale mængde (numerisk værdi x 1000) af parenterale serviceprodukter inden for ATC-gruppe J01 og L01. Varenumre til serviceprodukterne fremgår af bilag 2.2 og bilag 2.3. |

| Felt 46 Delmængde af pakning, unit-doseret lægemiddel fra sygehusapoteker |
|---|
| Feltet udfyldes med den ekspederede delmængde af den pakning unit-doseringen er foretaget fra. |

### 3.3 Oversigt over felternes placering i filen, samt felternes type og længde

Positionen i nedenstående feltoversigt angiver felternes placering i filen.

Der skelnes mellem to typer felter: N, der er numeriske felter (udelukkende cifre) og A, der er alfanumeriske felter (tekst, eventuelt bogstaver og cifre i kombination). Feltets længde (antal karakterer) følger umiddelbart efter feltets type (fx N4 eller A6).

<table>
<tr>
<td>Felt nr.</td>
<td>Beskrivelse</td>
<td>Type/<br>Længde</td>
<td>Position</td>
<td>Typiske værdier</td>
</tr>
<tr>
<td>01</td>
<td>Ekspeditionsdato</td>
<td>N6</td>
<td>1- 6</td>
<td>ÅÅMMDD:000101-991231</td>
</tr>
<tr>
<td>02</td>
<td>Ekspeditionsnummer</td>
<td>N5</td>
<td>7-11</td>
<td>00001-99999</td>
</tr>
<tr>
<td>03</td>
<td>Ekspeditionstype</td>
<td>A2</td>
<td>12-13</td>
<td>EI, EM, DD</td>
</tr>
<tr>
<td>04</td>
<td>Indberetters nummer</td>
<td>N5</td>
<td>14-18</td>
<td>00000-99999</td>
</tr>
<tr>
<td>05</td>
<td>Udleveringssted</td>
<td>N1</td>
<td>19-19</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>06</td>
<td>Modtager af lægemiddel</td>
<td>A10</td>
<td>20-29</td>
<td></td>
</tr>
<tr>
<td>08</td>
<td>Receptudsteder</td>
<td>A7</td>
<td>33-39</td>
<td></td>
</tr>
<tr>
<td>09</td>
<td>Læges CPR-nummer</td>
<td>N10</td>
<td>40-49</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>Ordineret varenummer</td>
<td>N6</td>
<td>50-55</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>Receptens løbenummer</td>
<td>A7</td>
<td>56-62</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>Udleveret varenummer</td>
<td>N6</td>
<td>63-68</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>Pakningsantal eller antal enheder</td>
<td>N4</td>
<td>69-72</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>Reiterationsnummer</td>
<td>N2</td>
<td>73-74</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>Ekspeditionspris</td>
<td>N10</td>
<td>75-84</td>
<td>0000010025, -000010025</td>
</tr>
<tr>
<td>17</td>
<td>Modtagerbetaling</td>
<td>N10</td>
<td>85-94</td>
<td>0000010025, -000010025</td>
</tr>
<tr>
<td>18</td>
<td>Regionsnummer</td>
<td>N3</td>
<td>95-97</td>
<td>081, 082, 083, 084, 085</td>
</tr>
<tr>
<td>19</td>
<td>Regelnummer for medicintilskud</td>
<td>N2</td>
<td>98-99</td>
<td>41, 42, 43</td>
</tr>
<tr>
<td>20</td>
<td>Medicintilskud</td>
<td>N10</td>
<td>100-109</td>
<td>0000010025, -000010025</td>
</tr>
<tr>
<td>21</td>
<td>Kommunenummer</td>
<td>N3</td>
<td>110-112</td>
<td></td>
</tr>
<tr>
<td>22</td>
<td>Kommune, 1. regel</td>
<td>N2</td>
<td>113-114</td>
<td>61, 62, 63, 64</td>
</tr>
<tr>
<td>23</td>
<td>Kommune, 1. tilskud</td>
<td>N10</td>
<td>115-124</td>
<td>0000010025, -000010025</td>
</tr>
<tr>
<td>24</td>
<td>Kommune, 2. regel</td>
<td>N2</td>
<td>125-126</td>
<td>61, 62, 63, 64</td>
</tr>
<tr>
<td>25</td>
<td>Kommune, 2. tilskud</td>
<td>N10</td>
<td>127-136</td>
<td>0000010025, -000010025</td>
</tr>
<tr>
<td>26</td>
<td>Anden refusion</td>
<td>N2</td>
<td>137-138</td>
<td>21</td>
</tr>
<tr>
<td>27</td>
<td>Andre tilskud</td>
<td>N10</td>
<td>139-148</td>
<td>0000010025, -000010025</td>
</tr>
<tr>
<td>31</td>
<td>Fravalg af substitution</td>
<td>A1</td>
<td>152-152</td>
<td>S eller blank</td>
</tr>
<tr>
<td>33</td>
<td>Tidsstempel</td>
<td>N4</td>
<td>154-157</td>
<td>TTMM:0000-2359</td>
</tr>
<tr>
<td>34</td>
<td>Patienttype</td>
<td>N2</td>
<td>158-159</td>
<td>00, 01,10, 11, 99</td>
</tr>
<tr>
<td>35</td>
<td>Tilskudspris</td>
<td>N10</td>
<td>160-169</td>
<td>0000010025, -000010025</td>
</tr>
<tr>
<td>36</td>
<td>Dyreart</td>
<td>N2</td>
<td>170-171</td>
<td>11, 12, 13, 95</td>
</tr>
<tr>
<td>37</td>
<td>Aldersgruppe</td>
<td>N2</td>
<td>172-173</td>
<td>00, 55, 56, 77</td>
</tr>
<tr>
<td>38</td>
<td>Ordinationsgruppe</td>
<td>N2</td>
<td>174-175</td>
<td>00, 10, 11, 99</td>
</tr>
<tr>
<td>39</td>
<td>Takseringsdato</td>
<td>N6</td>
<td>176-181</td>
<td>ÅÅMMDD:000101-991231</td>
</tr>
<tr>
<td>40</td>
<td>Salgsstedets P-nummer</td>
<td>N10</td>
<td>182-191</td>
<td></td>
</tr>
<tr>
<td>41</td>
<td>Indikation for ordination</td>
<td>N7</td>
<td>192-198</td>
<td></td>
</tr>
<tr>
<td>42</td>
<td>Dosering for ordination</td>
<td>N7</td>
<td>199-205</td>
<td></td>
</tr>
<tr>
<td>43</td>
<td>Receptudsteders autorisationsID</td>
<td>A6</td>
<td>206-211</td>
<td></td>
</tr>
<tr>
<td colspan="5">Sygehusapoteker skal endvidere indberette:</td>
</tr>
<tr>
<td>44</td>
<td>Typen af mængden af parenterale serviceprodukter</td>
<td>A3</td>
<td>212-214</td>
<td>DW, DWK, DWG, DDK, TU, MG, GA</td>
</tr>
<tr>
<td>45</td>
<td>Mængde af parenterale serviceprodukter</td>
<td>N12</td>
<td>215-226</td>
<td></td>
</tr>
<tr>
<td>46</td>
<td>Delmængde af pakning, unit-doseret lægemiddel</td>
<td>A20</td>
<td>227-246</td>
<td></td>
</tr>
</table>

### 3.4 Eksempler på feltudfyldelse

Nedenstående tabel viser, hvilke felter der – såfremt oplysninger foreligger – skal udfyldes ved henholdsvis:

| 1. | Apotekeres salg af receptpligtige lægemidler og receptordinerede håndkøbslægemidler ordineret af alment praktiserende læger, vagtlæger, speciallæger, tandlæger og sygehuslæger til enkeltpersoner og til brug i egen praksis (ekspeditionstyperne EI og DD). |
|---|---|
| 2. | Apotekeres salg af dyrlægeordinerede lægemidler (ekspeditionstyperne DI og ID). |
| 3. | Apotekeres salg af håndkøbslægemidler og frihandelsvarer (ekspeditionstyperne HA, HF og SA). |
| 4. | Apotekeres leverancer af lægemidler til sygehusafdelinger, behandlingsinstitutioner mm. (ekspeditionstype LI). |
| 5. | Apotekeres salg af lægemidler til andre apoteker (ekspeditionstyperne SL og SD). |
| 6. | Apotekernes udligning af for meget eller for lidt udbetalt tilskud (CTR) (ekspeditionstype UL) |
| 7. | Apotekeres ekspedition af gebyrer (ekspeditionstype AD og DD). Administrationsgebyrerne kan dog indberettes på én samlet linie pr. måned. |
| 8. | Sygehusapotekeres og Statens Serum Instituts salg af lægemidler (ekspeditionstyperne AI, SI, PI, LA, KM, KU, KA, KS, KP og KK) |
| 9. | Salg af lægemidler fra Veterinærinstituttet DTU og Veterinærapoteket, Københavns Universitet (ekspeditionstyperne VI og PI). |
| 10. | Producenter og forhandlere af radioaktive lægemidler (ekspeditionstype RA). Der indberettes én linie pr. solgt varenummer pr. måned. |
| 11. | Forhandlere af receptpligtige lægemidler til produktionsdyr (ekspeditionstype DI). |
| 12. | Virksomheder, der er indehaver af Lægemiddelstyrelsens tilladelse til forhandling og udlevering af diacetylmorphin (ekspeditionstype HE). |
| 13. | Daglige indberetninger fra apotekere og andre forhandlere af lægemidler til produktionsdyr (ekspeditionstype DI). |
| 14. | Sygehusapotekers ekspedition af serviceprodukter (ekspeditionstype AI og SI) |
| 15. | Sygehusapotekers ekspedition af unit-doserede lægemidler (ekspeditionstype UD) |

| Felt<br>Nr. | Beskrivelse | 1. | 2. | 3. | 4. | 5. | 6. | 7. | 8. | 9. | 10. | 11. | 12. | 13. | 14. | 15. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | Ekspeditionsdato | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
| 02 | Ekspeditionsnummer | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 03 | Ekspeditionstype | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
| 04 | Indberetters nummer | + | + | + | + | + | + | + | + | + |  | + |  | + | + | + |
| 05 | Udleveringssted | + | + | + | + | + | + | + |  |  |  |  |  |  |  |  |
| 06 | Modtager af lægemiddel | + | + |  | + | + | + | + | + | + | + | + | + | + | + | + |
| 08 | Receptudsteder | + | + |  | + |  |  |  | + | + |  | + | + | + | + | + |
| 09 | Læges CPR-nummer | + |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 10 | Ordineret varenummer | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | Receptens løbenummer | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 12 | Udleveret varenummer | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
| 13 | Pakningsantal | + | + | + | + | + | + | + | + | + | + | + | + | + |  |  |
| 14 | Reiterationsnummer | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 16 | Ekspeditionspris | + | + | + | + | + |  | + | + | + | + | + |  |  | + | + |
| 17 | Modtagerbetaling | + |  | + | + | + | + | + |  |  |  |  |  |  |  |  |
| 18 | Regionsnummer | + |  |  |  |  | + |  |  |  |  |  | + |  |  |  |
| 19 | Regelnummer for medicintilskud (tidl. sygesikringstilskud) | + |  |  |  |  | + | + |  |  |  |  |  |  |  |  |
| 20 | Medicintilskud (tidl. sygesikringstilskud) | + |  |  |  |  | + | + |  |  |  |  |  |  |  |  |
| 21 | Kommunenummer | + |  |  |  |  | + | + |  |  |  |  |  |  |  |  |
| 22 | Kommune, 1. regel | + |  |  |  |  | + | + |  |  |  |  |  |  |  |  |
| 23 | Kommune, 1. tilskud | + |  |  |  |  | + | + |  |  |  |  |  |  |  |  |
| 24 | Kommune, 2. regel | + |  |  |  |  | + | + |  |  |  |  |  |  |  |  |
| 25 | Kommune, 2. tilskud | + |  |  |  |  | + | + |  |  |  |  |  |  |  |  |
| 26 | Anden refusion | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 27 | Andre tilskud | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 31 | Fravalg af substitution | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 33 | Tidsstempel | + | + | + | + | + | + | + |  |  |  |  |  |  |  |  |
| 34 | Patienttype | + |  |  |  |  | + | + |  |  |  |  |  |  |  |  |
| 35 | Tilskudspris | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 36 | Dyreart |  | + |  |  |  |  |  |  | + |  | + |  | + |  |  |
| 37 | Aldersgruppe |  | + |  |  |  |  |  |  | + |  | + |  | + |  |  |
| 38 | Ordinationsgruppe |  | + |  |  |  |  |  |  | + |  | + |  | + |  |  |
| 39 | Takseringsdato | + | + | + | + | + | + | + |  |  |  | + |  |  |  |  |
| 40 | Salgsstedets P-nummer | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
| 41 | Indikation for ordination | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 42 | Dosering for ordination | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 43 | AutorisationsID | + |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
|  | Kun for sygehusapoteker: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 44 | Serviceprodukt, type |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |
| 45 | Serviceprodukt, mængde |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |
| 46 | Delmængde af pakning, unit-doseret lægemiddel |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |

## 4. Koder og tabeller

### 4.1 Generelle bemærkninger

En række tabeller af mindre omfang er angivet i feltbeskrivelserne i afsnit 3 ovenfor.

### 4.2 Øvrige tabeller

For apotekeres vedkommende anvendes de gældende apoteksnumre. Enhedsnumre til apoteker, filialer og apoteksudsalg skal meddeles til Lægemiddelstyrelsen.

Numre på øvrige indberetningspligtige (sygehusapoteker, serumlaboratorier mv.) fastlægges af Lægemiddelstyrelsen.

Sundhedsvæsenets Organisationsregister (SOR) anvendes til identifikation af sygehuse og sygehusafdelinger.

CPR-registrets myndighedsoplysninger for kommuner og regioner anvendes, hvor kommune eller region skal indberettes.

Til identifikation af receptudsteder anvendes Danske Regioners identifikation og Sundhedsstyrelsens autorisationsID. For dyrlæger anvendes Fødevarestyrelsens autorisationskoder.

Til identifikation af lægemidler anvendes pakningernes påtrykte varenumre. Pakninger uden varenummer tildeles et varenummer af Lægemiddelstyrelsen, jf. Bilag 2.

Til identifikation af dyrehold anvendes Fødevareministeriets CHR-numre.

Til identifikation af indberetteren og salgsstedet anvendes numre fra Det Centrale Virksomhedsregister (henholdsvis CVR-nummer og P-nummer).

Til identifikation af indikation for ordinationen anvendes de i Medicinpriser anførte koder (LMS 25). Koderne er identiske med dem, der er anført i Lægeforeningens elektroniske medicinfortegnelse.

Til identifikation af dosering for ordinationen anvendes de i Medicinpriser anførte koder (LMS 27). Koderne er identiske med dem, der er anført i Lægeforeningens elektroniske medicinfortegnelse.

## Bilag 2

Varenumre, som skal anvendes ved indberetning af salg af lægemidler, når lægemiddelpakningen ikke er forsynet med et nordisk varenummer eller et særligt varenummer til lægemiddelpakninger fra Amgros og Danmarks Apotekerforening, samt varenumre til brug ved indberetning af gebyrer, udligning af tilskud mv.

Listen opdateres jævnligt, og en opdateret liste i elektronisk form kan fås ved henvendelse til Lægemiddelstyrelsen, Statistik og Analyse. Ønskes varenumre til nye produkter skal henvendelse ligeledes ske hertil.

<table>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="5"><strong>Bilag 2.1 Varenumre til magistrelle lægemidler mv. til humant brug</strong></td>
</tr>
<tr>
<td><strong>Lægemiddel</strong></td>
<td><strong>Lægemiddelform</strong></td>
<td><strong>Styrke</strong></td>
<td><strong>Pakningsstørrelse</strong></td>
<td><strong>Varenummer</strong></td>
</tr>
<tr>
<td>Amphetamin</td>
<td>Injektionsvæske</td>
<td>50 mg/ml</td>
<td>10 amp. a 1 ml</td>
<td>685008</td>
</tr>
<tr>
<td>Amphetamin</td>
<td>Tabletter</td>
<td>5 mg</td>
<td>10 stk.</td>
<td>685016</td>
</tr>
<tr>
<td>Amphetamin</td>
<td>Tabletter</td>
<td>5 mg</td>
<td>25 stk.</td>
<td>685024</td>
</tr>
<tr>
<td>Amphetamin</td>
<td>Tabletter</td>
<td>5 mg</td>
<td>100 stk.</td>
<td>685032</td>
</tr>
<tr>
<td>Amphetamin</td>
<td>Diverse former</td>
<td></td>
<td>0-50 stk./ml</td>
<td>685081</td>
</tr>
<tr>
<td>Amphetamin</td>
<td>Diverse former</td>
<td></td>
<td>51-75 stk./ml</td>
<td>685099</td>
</tr>
<tr>
<td>Amphetamin</td>
<td>Diverse former</td>
<td></td>
<td>76 stk./ml og derover</td>
<td>685107</td>
</tr>
<tr>
<td>Cocain</td>
<td>Øjendråber</td>
<td>2%</td>
<td>10 ml</td>
<td>685123</td>
</tr>
<tr>
<td>Cocain</td>
<td>Øjendråber</td>
<td>4%</td>
<td>10 ml</td>
<td>685131</td>
</tr>
<tr>
<td>Dexamfetamin</td>
<td>Tabletter</td>
<td>5 mg</td>
<td>100 stk.</td>
<td>685180</td>
</tr>
<tr>
<td>Lytisk væske (chlorpromazin-hydrochlorid/ pethidin-hydrochlorid/ promethazin-hydrochlorid)</td>
<td>Injektionsvæske</td>
<td>7 mg + 28 mg + 7 mg</td>
<td>2 ml</td>
<td>685149</td>
</tr>
<tr>
<td>Melatonin</td>
<td>Tabletter</td>
<td>3 mg</td>
<td>100 stk.</td>
<td>685200</td>
</tr>
<tr>
<td>Metadon</td>
<td>Oral opløsning (sukkerfri)</td>
<td>1 mg/ml</td>
<td>1000 ml og derunder</td>
<td>685172</td>
</tr>
<tr>
<td>Morfatropin-papaverin (atropinsulfat/mor-phinhydrochlorid/papaverin-hydrochlorid)</td>
<td>Tabletter</td>
<td>0,5 mg + 10 mg + 40 mg</td>
<td>100 stk.</td>
<td>685156</td>
</tr>
<tr>
<td>Oseltamivir (beredskabsmedicin)</td>
<td></td>
<td>15 mg/ml</td>
<td>50 ml</td>
<td>685514</td>
</tr>
<tr>
<td>Oseltamivir (beredskabsmedicin)</td>
<td></td>
<td>15 mg/ml</td>
<td>18 x 50 ml</td>
<td>685515</td>
</tr>
<tr>
<td>Pethidin</td>
<td>Dråber</td>
<td>50 mg/ml</td>
<td>30 ml</td>
<td>685164</td>
</tr>
</table>

<table>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3"><strong>Bilag 2.2 Varenumre til parenterale serviceprodukter i ATC-gruppe J01 fra sygehusapoteker</strong></td>
</tr>
<tr>
<td><strong>Lægemiddel</strong></td>
<td><strong>ATC-kode</strong></td>
<td><strong>Varenummer</strong></td>
</tr>
<tr>
<td>Amikacin</td>
<td>J01GB06</td>
<td>687228</td>
</tr>
<tr>
<td>Ampicillin</td>
<td>J01CA01</td>
<td>687200</td>
</tr>
<tr>
<td>Azithromycin</td>
<td>J01FA10</td>
<td>687201</td>
</tr>
<tr>
<td>Aztreonam</td>
<td>J01DF01</td>
<td>687202</td>
</tr>
<tr>
<td>Benzathin benzylpenicillin</td>
<td>J01CE08</td>
<td>687229</td>
</tr>
<tr>
<td>Benzylpenicillin</td>
<td>J01CE01</td>
<td>687203</td>
</tr>
<tr>
<td>Cefotaxim</td>
<td>J01DD01</td>
<td>687204</td>
</tr>
<tr>
<td>Ceftazidim</td>
<td>J01DD02</td>
<td>687205</td>
</tr>
<tr>
<td>Ceftriaxon</td>
<td>J01DD04</td>
<td>687206</td>
</tr>
<tr>
<td>Cefuroxim</td>
<td>J01DC02</td>
<td>687207</td>
</tr>
<tr>
<td>Ciprofloxacin</td>
<td>J01MA02</td>
<td>687208</td>
</tr>
<tr>
<td>Clarithromycin</td>
<td>J01FA09</td>
<td>687209</td>
</tr>
<tr>
<td>Clindamycin</td>
<td>J01FF01</td>
<td>687210</td>
</tr>
<tr>
<td>Colistin</td>
<td>J01XB01</td>
<td>687275</td>
</tr>
<tr>
<td>Daptomycin</td>
<td>J01XX09</td>
<td>687211</td>
</tr>
<tr>
<td>Dicloxacillin</td>
<td>J01CF01</td>
<td>687212</td>
</tr>
<tr>
<td>Doripenem</td>
<td>J01DH04</td>
<td>687213</td>
</tr>
<tr>
<td>Doxycyclin</td>
<td>J01AA02</td>
<td>687276</td>
</tr>
<tr>
<td>Ertapenem</td>
<td>J01DH03</td>
<td>687214</td>
</tr>
<tr>
<td>Erythromycin</td>
<td>J01FA01</td>
<td>687215</td>
</tr>
<tr>
<td>Flucloxacillin</td>
<td>J01CF05</td>
<td>687277</td>
</tr>
<tr>
<td>Fusidinsyre</td>
<td>J01XC01</td>
<td>687216</td>
</tr>
<tr>
<td>Gentamicin</td>
<td>J01GB03</td>
<td>687217</td>
</tr>
<tr>
<td>Imipenem og enzyminhibitor</td>
<td>J01DH51</td>
<td>687278</td>
</tr>
<tr>
<td>Linezolid</td>
<td>J01XX08</td>
<td>687218</td>
</tr>
<tr>
<td>Mecillinam</td>
<td>J01CA11</td>
<td>687219</td>
</tr>
<tr>
<td>Meropenem</td>
<td>J01DH02</td>
<td>687220</td>
</tr>
<tr>
<td>Metronidazol</td>
<td>J01XD01</td>
<td>687221</td>
</tr>
<tr>
<td>Moxifloxacin</td>
<td>J01MA14</td>
<td>687222</td>
</tr>
<tr>
<td>Piperacillin og enzym-hæmmer</td>
<td>J01CR05</td>
<td>687223</td>
</tr>
<tr>
<td>Sulfamethoxazol og trimethoprim</td>
<td>J01EE01</td>
<td>687279</td>
</tr>
<tr>
<td>Teicoplanin</td>
<td>J01XA02</td>
<td>687224</td>
</tr>
<tr>
<td>Tigecyklin</td>
<td>J01AA12</td>
<td>687225</td>
</tr>
<tr>
<td>Tobramycin</td>
<td>J01GB01</td>
<td>687226</td>
</tr>
<tr>
<td>Vancomycin</td>
<td>J01XA01</td>
<td>687227</td>
</tr>
</table>

<table>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="4"><strong>Bilag 2.3 Varenumre til parenterale serviceprodukter i ATC-gruppe L01 fra sygehusapoteker</strong></td>
</tr>
<tr>
<td><strong>Lægemiddel</strong></td>
<td><strong>Måleværdi</strong></td>
<td><strong>ATC-kode</strong></td>
<td><strong>Varenummer</strong></td>
</tr>
<tr>
<td>Alemtuzumab</td>
<td>Gram (GA)</td>
<td>L01XC04</td>
<td>687230</td>
</tr>
<tr>
<td>Amsacrin</td>
<td>Gram (GA)</td>
<td>L01XX01</td>
<td>687281</td>
</tr>
<tr>
<td>Arsentrioxid</td>
<td>Gram (GA)</td>
<td>L01XX27</td>
<td>687282</td>
</tr>
<tr>
<td>Asparaginase</td>
<td>Tusinde enheder (TU)</td>
<td>L01XX02</td>
<td>687283</td>
</tr>
<tr>
<td>Azacitidin</td>
<td>Gram (GA)</td>
<td>L01BC07</td>
<td>687231</td>
</tr>
<tr>
<td>Bevacizumab</td>
<td>Gram (GA)</td>
<td>L01XC07</td>
<td>687232</td>
</tr>
<tr>
<td>Bleomycin</td>
<td>Tusinde enheder (TU)</td>
<td>L01DC01</td>
<td>687233</td>
</tr>
<tr>
<td>Bortezomib</td>
<td>Milligram (MG)</td>
<td>L01XX32</td>
<td>687234</td>
</tr>
<tr>
<td>Busulfan</td>
<td>Gram (GA)</td>
<td>L01AB01</td>
<td>687235</td>
</tr>
<tr>
<td>Carboplatin</td>
<td>Gram (GA)</td>
<td>L01XA02</td>
<td>687236</td>
</tr>
<tr>
<td>Carmustin</td>
<td>Gram (GA)</td>
<td>L01AD01</td>
<td>687284</td>
</tr>
<tr>
<td>Catumaxomab</td>
<td>Milligram (MG)</td>
<td>L01XC09</td>
<td>687274</td>
</tr>
<tr>
<td>Cetuximab</td>
<td>Gram (GA)</td>
<td>L01XC06</td>
<td>687237</td>
</tr>
<tr>
<td>Cisplatin</td>
<td>Gram (GA)</td>
<td>L01XA01</td>
<td>687238</td>
</tr>
<tr>
<td>Cladribin</td>
<td>Gram (GA)</td>
<td>L01BB04</td>
<td>687239</td>
</tr>
<tr>
<td>Clofarabin</td>
<td>Gram (GA)</td>
<td>L01BB06</td>
<td>687240</td>
</tr>
<tr>
<td>Cyclophosphamid</td>
<td>Gram (GA)</td>
<td>L01AA01</td>
<td>687241</td>
</tr>
<tr>
<td>Cytarabin</td>
<td>Gram (GA)</td>
<td>L01BC01</td>
<td>687242</td>
</tr>
<tr>
<td>Dacarbazin</td>
<td>Gram (GA)</td>
<td>L01AX04</td>
<td>687243</td>
</tr>
<tr>
<td>Dactinomycin</td>
<td>Gram (GA)</td>
<td>L01DA01</td>
<td>687285</td>
</tr>
<tr>
<td>Daunorubicin</td>
<td>Gram (GA)</td>
<td>L01DB02</td>
<td>687244</td>
</tr>
<tr>
<td>Docetaxel</td>
<td>Gram (GA)</td>
<td>L01CD02</td>
<td>687245</td>
</tr>
<tr>
<td>Doxorubicin</td>
<td>Gram (GA)</td>
<td>L01DB01</td>
<td>687246</td>
</tr>
<tr>
<td>Epirubicin</td>
<td>Gram (GA)</td>
<td>L01DB03</td>
<td>687247</td>
</tr>
<tr>
<td>Etoposid</td>
<td>Gram (GA)</td>
<td>L01CB01</td>
<td>687248</td>
</tr>
<tr>
<td>Fludarabin</td>
<td>Gram (GA)</td>
<td>L01BB05</td>
<td>687249</td>
</tr>
<tr>
<td>Fluorouracil</td>
<td>Gram (GA)</td>
<td>L01BC02</td>
<td>687250</td>
</tr>
<tr>
<td>Gemcitabin</td>
<td>Gram (GA)</td>
<td>L01BC05</td>
<td>687251</td>
</tr>
<tr>
<td>Idarubicin</td>
<td>Gram (GA)</td>
<td>L01DB06</td>
<td>687252</td>
</tr>
<tr>
<td>Ifosfamid</td>
<td>Gram (GA)</td>
<td>L01AA06</td>
<td>687253</td>
</tr>
<tr>
<td>Irinotecan</td>
<td>Gram (GA)</td>
<td>L01XX19</td>
<td>687254</td>
</tr>
<tr>
<td>Melphalan</td>
<td>Gram (GA)</td>
<td>L01AA03</td>
<td>687286</td>
</tr>
<tr>
<td>Methotrexat</td>
<td>Milligram (MG)</td>
<td>L01BA01</td>
<td>687255</td>
</tr>
<tr>
<td>Mitoguazon</td>
<td>Gram (GA)</td>
<td>L01XX16</td>
<td>687287</td>
</tr>
<tr>
<td>Mitomycin</td>
<td>Gram (GA)</td>
<td>L01DC03</td>
<td>687256</td>
</tr>
<tr>
<td>Mitoxantron</td>
<td>Gram (GA)</td>
<td>L01DB07</td>
<td>687257</td>
</tr>
<tr>
<td>Nelarabin</td>
<td>Gram (GA)</td>
<td>L01BB07</td>
<td>687258</td>
</tr>
<tr>
<td>Oxaliplatin</td>
<td>Gram (GA)</td>
<td>L01XA03</td>
<td>687259</td>
</tr>
<tr>
<td>Paclitaxel</td>
<td>Gram (GA)</td>
<td>L01CD01</td>
<td>687260</td>
</tr>
<tr>
<td>Panitumumab</td>
<td>Gram (GA)</td>
<td>L01XC08</td>
<td>687261</td>
</tr>
<tr>
<td>Pegaspargase</td>
<td>Gram (GA)</td>
<td>L01XX24</td>
<td>687288</td>
</tr>
<tr>
<td>Pemetrexed</td>
<td>Gram (GA)</td>
<td>L01BA04</td>
<td>687262</td>
</tr>
<tr>
<td>Porfimer</td>
<td>Gram (GA)</td>
<td>L01XD01</td>
<td>687289</td>
</tr>
<tr>
<td>Rituximab</td>
<td>Gram (GA)</td>
<td>L01XC02</td>
<td>687263</td>
</tr>
<tr>
<td>Temoporfin</td>
<td>Gram (GA)</td>
<td>L01XD05</td>
<td>687264</td>
</tr>
<tr>
<td>Temsirolimus</td>
<td>Gram (GA)</td>
<td>L01XE09</td>
<td>687265</td>
</tr>
<tr>
<td>Topotecan</td>
<td>Milligram (MG)</td>
<td>L01XX17</td>
<td>687266</td>
</tr>
<tr>
<td>Trabectedin</td>
<td>Milligram (MG)</td>
<td>L01CX01</td>
<td>687267</td>
</tr>
<tr>
<td>Trastuzumab</td>
<td>Gram (GA)</td>
<td>L01XC03</td>
<td>687268</td>
</tr>
<tr>
<td>Treosulfan</td>
<td>Gram (GA)</td>
<td>L01AB02</td>
<td>687269</td>
</tr>
<tr>
<td>Vinblastin</td>
<td>Gram (GA)</td>
<td>L01CA01</td>
<td>687270</td>
</tr>
<tr>
<td>Vincristin</td>
<td>Gram (GA)</td>
<td>L01CA02</td>
<td>687271</td>
</tr>
<tr>
<td>Vinflunin</td>
<td>Gram (GA)</td>
<td>L01CA05</td>
<td>687272</td>
</tr>
<tr>
<td>Vinorelbin</td>
<td>Gram (GA)</td>
<td>L01CA04</td>
<td>687273</td>
</tr>
</table>

<table>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="4"><strong>Bilag 2.4 Varenumre til magistrelle lægemidler fra sygehusapoteker og andre producenter af lægemidler til anvendelse på sygehuse</strong></td>
</tr>
<tr>
<td><strong>Magistrelle lægemidler</strong></td>
<td><strong>Mængde</strong></td>
<td><strong>Styrke</strong></td>
<td><strong>Varenummer</strong></td>
</tr>
<tr>
<td>Akutbakke</td>
<td>1 stk.</td>
<td></td>
<td>685529</td>
</tr>
<tr>
<td>Bupivacain-morphin blanding</td>
<td></td>
<td></td>
<td>685537</td>
</tr>
<tr>
<td>Calciumcarbonat, tablet</td>
<td>250 stk.</td>
<td>450 mg</td>
<td>685552</td>
</tr>
<tr>
<td>Calciumcarbonat, tablet</td>
<td>10 x 250 stk.</td>
<td>450 mg</td>
<td>685562</td>
</tr>
<tr>
<td>Dosisdispenserede lægemidler, ekskl. akutbakker</td>
<td></td>
<td></td>
<td>685610</td>
</tr>
<tr>
<td>Ganciclovir (Cymevene) blanding</td>
<td></td>
<td></td>
<td>685644</td>
</tr>
<tr>
<td>Heparin infusionsvæske</td>
<td>1000 ml</td>
<td>3.000 IE/l</td>
<td>685530</td>
</tr>
<tr>
<td>Heparin infusionsvæske</td>
<td>10 x 1000 ml</td>
<td>3.000 IE/l</td>
<td>685563</td>
</tr>
<tr>
<td>Heparin infusionsvæske</td>
<td>500 ml</td>
<td>10.000 IE/l</td>
<td>685534</td>
</tr>
<tr>
<td>Heparin injektionsvæske</td>
<td>10 x 500 ml</td>
<td>10.000 IE/l</td>
<td>685564</td>
</tr>
<tr>
<td>Heparin injektionsvæske</td>
<td>1000 ml</td>
<td>10.000 IE/l</td>
<td>685565</td>
</tr>
<tr>
<td>Heparin injektionsvæske</td>
<td>10 x 1000 ml</td>
<td>10.000 IE/l</td>
<td>685566</td>
</tr>
<tr>
<td>Heparin injektionsvæske</td>
<td>10 x 10 ml</td>
<td>50 IE/ml</td>
<td>685535</td>
</tr>
<tr>
<td>Immunglobulin blanding</td>
<td>1 stk.</td>
<td></td>
<td>685636</td>
</tr>
<tr>
<td>Morfin injektionsvæske</td>
<td>10 x 1 ml</td>
<td>1 mg/ml</td>
<td>685536</td>
</tr>
<tr>
<td>Morfin injektionsvæske</td>
<td>1 ml</td>
<td>40 mg/ml</td>
<td>685693</td>
</tr>
<tr>
<td>Morfin suppositorium</td>
<td>10 stk.</td>
<td>5 mg</td>
<td>685538</td>
</tr>
<tr>
<td>Morfin suppositorium</td>
<td>10 stk.</td>
<td>10 mg</td>
<td>685540</td>
</tr>
<tr>
<td>Orale opløsninger</td>
<td></td>
<td></td>
<td>685541</td>
</tr>
<tr>
<td>Næsedråber</td>
<td></td>
<td></td>
<td>685542</td>
</tr>
<tr>
<td>Paracetamol suppositorium</td>
<td>10 stk.</td>
<td>50 mg</td>
<td>685544</td>
</tr>
<tr>
<td>Peritonealdialysevæske</td>
<td></td>
<td></td>
<td>685602</td>
</tr>
<tr>
<td>Prednisolon suppositorium</td>
<td>10 stk.</td>
<td>10 mg</td>
<td>685546</td>
</tr>
<tr>
<td>Smertepumpe ekskl. bupivacain-morphin blanding</td>
<td>1 stk.</td>
<td></td>
<td>685701</td>
</tr>
<tr>
<td>Total parenteral ernæring</td>
<td>1 stk.</td>
<td></td>
<td>685719</td>
</tr>
<tr>
<td>Øvrige infusionsvæske</td>
<td></td>
<td></td>
<td>685547</td>
</tr>
<tr>
<td>Øvrige injektionsvæske</td>
<td></td>
<td></td>
<td>685548</td>
</tr>
<tr>
<td>Øvrige suppositorier</td>
<td></td>
<td></td>
<td>685549</td>
</tr>
<tr>
<td>Tabletter, ATC-gr. L01</td>
<td></td>
<td></td>
<td>685555</td>
</tr>
<tr>
<td>Øvrige tabletter uden for ATC-gr. L01</td>
<td></td>
<td></td>
<td>685550</td>
</tr>
<tr>
<td>Øvrige parenterale serviceprodukter uden for ATC-gr. J01 og L01</td>
<td></td>
<td></td>
<td>687280</td>
</tr>
<tr>
<td>Øvrige magistrelle lægemidler, humane</td>
<td></td>
<td></td>
<td>685990</td>
</tr>
<tr>
<td>Lægemidler til kliniske forsøg</td>
<td></td>
<td></td>
<td>685554</td>
</tr>
</table>

<table>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3"><strong>Bilag 2.5 Varenumre til lægemiddelpakninger fra Statens Serum Institut</strong></td>
</tr>
<tr>
<td><strong>Lægemiddel</strong></td>
<td><strong>Styrke/mængde</strong></td>
<td><strong>Varenummer</strong></td>
</tr>
<tr>
<td>Anthrax</td>
<td>10 x 0,5 ml</td>
<td>687132</td>
</tr>
<tr>
<td>Anthrax</td>
<td>5 x 0,5 ml</td>
<td>687133</td>
</tr>
<tr>
<td>BCG Kultur frysetørret</td>
<td>1 ampul á 30 mg</td>
<td>687100</td>
</tr>
<tr>
<td>Botulisme antitoxin type A,B & E</td>
<td>250 ml</td>
<td>687101</td>
</tr>
<tr>
<td>Botulisme antitoxin type E</td>
<td>5000 IE</td>
<td>687127</td>
</tr>
<tr>
<td>Botulisme antitoxin type A & B</td>
<td>7500 IE + 5500 IE</td>
<td>687128</td>
</tr>
<tr>
<td>Botulisme Antitoxin type ABCDEFG</td>
<td></td>
<td>687140</td>
</tr>
<tr>
<td>Centraleuropæisk encephalitisvaccine</td>
<td>1 dosis</td>
<td>687102</td>
</tr>
<tr>
<td>Difteri antitoxin</td>
<td>1 x 10.000 IE</td>
<td>687134</td>
</tr>
<tr>
<td>Difteri antitoxin</td>
<td>10 x 10.000 IE</td>
<td>687103</td>
</tr>
<tr>
<td>Difteri-Tetanus vaccine til børn (u/alumi.)</td>
<td></td>
<td>687104</td>
</tr>
<tr>
<td>Faktor VIII konc. Octonativ-M</td>
<td>500 IE</td>
<td>687105</td>
</tr>
<tr>
<td>Faktor VIII konc. Octonativ-M</td>
<td>1000 IE</td>
<td>687106</td>
</tr>
<tr>
<td>Gul feber vaccine (Arilvax)</td>
<td>5 x 1 dosis</td>
<td>687137</td>
</tr>
<tr>
<td>Hepatitis B immunoglobulin P Behring</td>
<td>1 dosis</td>
<td>687151</td>
</tr>
<tr>
<td>Humant Tetanus Immunglobulin</td>
<td>250 IE, 1 ml</td>
<td>687107</td>
</tr>
<tr>
<td>Humant Rabies Immunglobulin</td>
<td>2 ml</td>
<td>687108</td>
</tr>
<tr>
<td>Humant Rabies Immunglobulin</td>
<td>10 ml</td>
<td>687109</td>
</tr>
<tr>
<td>Humant Varizella Zoster Imm.glob.</td>
<td>85 IE</td>
<td>687110</td>
</tr>
<tr>
<td>Humant Varizella Zoster Imm.glob.</td>
<td>200 IE</td>
<td>687130</td>
</tr>
<tr>
<td>Humant Varizella Zoster Imm.glob.</td>
<td>340 IE</td>
<td>687111</td>
</tr>
<tr>
<td>Influenza vaccine</td>
<td>1 dosis</td>
<td>687112</td>
</tr>
<tr>
<td>Influenza vaccine</td>
<td>10 dosis</td>
<td>687113</td>
</tr>
<tr>
<td>Influenza vaccine til den sydlige halvkugle</td>
<td></td>
<td>687139</td>
</tr>
<tr>
<td>Japansk Encephalitis</td>
<td>3 x 1 dosis</td>
<td>687114</td>
</tr>
<tr>
<td>Japansk Encephalitis vaccine GCC inj.</td>
<td></td>
<td>687141</td>
</tr>
<tr>
<td>Kolera vaccine, oral</td>
<td>2 x 1 dosis</td>
<td>687115</td>
</tr>
<tr>
<td>Mannan Bindende Lectin (MBL)</td>
<td>1 mg</td>
<td>687116</td>
</tr>
<tr>
<td>Meningokok vaccine A,C,Y+W-135</td>
<td>0,5 ml</td>
<td>687117</td>
</tr>
<tr>
<td>Meningokok A,C,W,Y</td>
<td>1 x 10 doser</td>
<td>687131</td>
</tr>
<tr>
<td>Mæslinge vaccine</td>
<td>1 dosis</td>
<td>687136</td>
</tr>
<tr>
<td>Pandemrix, risikopt. 6 md. til 64 år, 1. vacc.</td>
<td>50 doser</td>
<td>687142</td>
</tr>
<tr>
<td>Pandemrix, risikopt. over 65 år, 1. vacc.</td>
<td>50 doser</td>
<td>687143</td>
</tr>
<tr>
<td>Pandemrix, risikopt. 6 md. til 64 år, 2. vacc.</td>
<td>50 doser</td>
<td>687144</td>
</tr>
<tr>
<td>Pandemrix, risikopt. over 65 år, 2. vacc</td>
<td>50 doser</td>
<td>687145</td>
</tr>
<tr>
<td>Pandemrix, kritisk/prioriteret sundhedspers, regioner</td>
<td>500 doser</td>
<td>687146</td>
</tr>
<tr>
<td>Pandemrix, kritisk/prioriteret sundhedspers, regioner og kommuner</td>
<td>50 doser</td>
<td>687147</td>
</tr>
<tr>
<td>Pandemrix, sundhedspersonale i øvrigt, regioner og kommuner</td>
<td>50 doser</td>
<td>687148</td>
</tr>
<tr>
<td>Pandemrix, nøglepersoner</td>
<td>50 doser</td>
<td>687149</td>
</tr>
<tr>
<td>Pandemrix</td>
<td>5 x 10 doser</td>
<td>685512</td>
</tr>
<tr>
<td>Pandemrix</td>
<td>1 x 10 doser</td>
<td>685513</td>
</tr>
<tr>
<td>Pandemrix, generel befolkning</td>
<td>50 doser</td>
<td>687150</td>
</tr>
<tr>
<td>Rubella vaccine</td>
<td>1 dosis</td>
<td>687135</td>
</tr>
<tr>
<td>Sensitin M. Avium RS 10</td>
<td>1,5 ml</td>
<td>687119</td>
</tr>
<tr>
<td>Sensitin M. Bovis RS 7</td>
<td>1,5 ml</td>
<td>687120</td>
</tr>
<tr>
<td>Sensitin M. Fortuitum RS 20</td>
<td>1,5 ml</td>
<td>687121</td>
</tr>
<tr>
<td>Sensitin M. Intracelluare RS 23</td>
<td>1,5 ml</td>
<td>687122</td>
</tr>
<tr>
<td>Sensitin M. Kansasii RS 30</td>
<td>1,5 ml</td>
<td>687123</td>
</tr>
<tr>
<td>Sensitin M. Marinum RS 170</td>
<td>1,5 ml</td>
<td>687124</td>
</tr>
<tr>
<td>Sensitin M. Scrofulaceum RS 95</td>
<td>1,5 ml</td>
<td>687125</td>
</tr>
<tr>
<td>Serum mod hugorme</td>
<td>10 ml</td>
<td>687126</td>
</tr>
<tr>
<td>Serum mod hugorme</td>
<td>4 ml</td>
<td>687129</td>
</tr>
<tr>
<td>Serum Hugorme (ViperaTab)</td>
<td>2 htgl. a 100mg</td>
<td>687138</td>
</tr>
<tr>
<td>Viperfav</td>
<td>1 dosis á 4 ml</td>
<td>687152</td>
</tr>
</table>

<table>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3"><strong>Bilag 2.6 Varenumre til radioaktive lægemidler fra sygehusapoteker og producenter af radioaktive lægemidler</strong></td>
</tr>
<tr>
<td><strong>Lægemiddelgruppe</strong></td>
<td><strong>ATC-kode</strong></td>
<td><strong>Varenummer</strong></td>
</tr>
<tr>
<td>Diagnostiske radioaktive lægemidler – centralnervesystemet</td>
<td>V09A</td>
<td>686002</td>
</tr>
<tr>
<td>Diagnostiske radioaktive lægemidler – knogler</td>
<td>V09B</td>
<td>686003</td>
</tr>
<tr>
<td>Diagnostiske radioaktive lægemidler – nyre og urinveje</td>
<td>V09C</td>
<td>686004</td>
</tr>
<tr>
<td>Diagnostiske radioaktive lægemidler – lever, galde, knoglemarv og lymfesystemet</td>
<td>V09D</td>
<td>686005</td>
</tr>
<tr>
<td>Diagnostiske radioaktive lægemidler – åndedrætsorganer</td>
<td>V09E</td>
<td>686006</td>
</tr>
<tr>
<td>Diagnostiske radioaktive lægemidler – skjoldbruskkirtel</td>
<td>V09F</td>
<td>686007</td>
</tr>
<tr>
<td>Diagnostiske radioaktive lægemidler – hjerte og kredsløb</td>
<td>V09G</td>
<td>686008</td>
</tr>
<tr>
<td>Diagnostiske radioaktive lægemidler - betændelsestilstande og infektionspåvisning</td>
<td>V09H</td>
<td>686009</td>
</tr>
<tr>
<td>Diagnostiske radioaktive lægemidler – tumor påvisning</td>
<td>V09I</td>
<td>686010</td>
</tr>
<tr>
<td>Magistrelle radioaktive lægemidler, hvor ATC-kode ikke kan angives</td>
<td></td>
<td>686000</td>
</tr>
<tr>
<td>Radioaktive lægemidler på udleveringstilladelse i henhold til lægemiddellovens § 25, stk. 2. Anvendes kun, hvis ATC-kode ikke kan angives</td>
<td></td>
<td>686001</td>
</tr>
<tr>
<td>Terapeutiske radioaktive lægemidler - midler mod betændelsestilstande</td>
<td>V10A</td>
<td>686012</td>
</tr>
<tr>
<td>Terapeutiske radioaktive lægemidler - smertelindrende</td>
<td>V10B</td>
<td>686013</td>
</tr>
<tr>
<td>Øvrige diagnostiske radioaktive lægemidler</td>
<td>V09X</td>
<td>686011</td>
</tr>
<tr>
<td>Øvrige terapeutiske radioaktive lægemidler</td>
<td>V10X</td>
<td>686014</td>
</tr>
</table>

<table>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="5"><strong>Bilag 2.7 Varenumre til diacetylmorphin fra virksomheder, der er indehaver af Lægemiddelstyrelsens tilladelse til forhandling og udlevering af diacetylmorphin</strong></td>
</tr>
<tr>
<td><strong>Lægemiddel</strong></td>
<td><strong>ATC-kode</strong></td>
<td><strong>Form</strong></td>
<td><strong>Styrke/mængde</strong></td>
<td><strong>Varenummer</strong></td>
</tr>
<tr>
<td>Diaphin</td>
<td>N02AA09</td>
<td>Pulver til injektionsvæske</td>
<td>100mg/ml - 15 htgl. x 10 g.</td>
<td>689001</td>
</tr>
</table>

<table>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="5"><strong>Bilag 2.8 Varenumre til magistrelle lægemidler til veterinær brug</strong></td>
</tr>
<tr>
<td><strong>Lægemiddel</strong></td>
<td><strong>Form</strong></td>
<td><strong>Mængde</strong></td>
<td><strong>Styrke</strong></td>
<td><strong>Varenummer</strong></td>
</tr>
<tr>
<td>Acetylcystein</td>
<td>Klysma</td>
<td>200 ml</td>
<td>40 mg/ml</td>
<td>686189</td>
</tr>
<tr>
<td>Acetylcystein-Gentamycin</td>
<td>Øjendråber</td>
<td>5 ml</td>
<td>50 + 3 mg/ml</td>
<td>686190</td>
</tr>
<tr>
<td>Ammoniumchlorid</td>
<td>Infusions-<br>koncentrat</td>
<td>100 ml</td>
<td>5,3 g/l</td>
<td>686171</td>
</tr>
<tr>
<td>Apomorphinhydrochlorid</td>
<td>Injektions-<br>væske</td>
<td>1 ml</td>
<td>10 mg/ml</td>
<td>686137</td>
</tr>
<tr>
<td>Atropinsulfat</td>
<td>Injektions-<br>væske</td>
<td>10 ml</td>
<td>1 mg/ml</td>
<td>686149</td>
</tr>
<tr>
<td>Atropinsulfat</td>
<td>Injektions-<br>væske</td>
<td>10 ml</td>
<td>10 mg/ml</td>
<td>686172</td>
</tr>
<tr>
<td>Bromhexidhydrochlorid</td>
<td>Oralt pulver</td>
<td>125 g</td>
<td>30 mg/gr</td>
<td>686191</td>
</tr>
<tr>
<td>Citrat-glukose, stærk</td>
<td>Opløsning</td>
<td>100 ml</td>
<td>citronsyre 8 mg/ml, natriumcitrat 22 mg/ml, glucose 25 mg/ml</td>
<td>686173</td>
</tr>
<tr>
<td>Glucose</td>
<td>Infusions-<br>koncentrat</td>
<td>1 L</td>
<td>50%</td>
<td>686174</td>
</tr>
<tr>
<td>Kalium/natrium/glucose</td>
<td>Infusions-<br>koncentrat</td>
<td>1 L</td>
<td>15 g/l + 23 g/l + 500 g/l</td>
<td>686175</td>
</tr>
<tr>
<td>Kaliumbromid</td>
<td>Oral opløsning</td>
<td>500 ml</td>
<td>100 mg/ml</td>
<td>686192</td>
</tr>
<tr>
<td>Kaliumbromid</td>
<td>Oral opløsning</td>
<td>500 ml</td>
<td>200 mg/ml</td>
<td>686193</td>
</tr>
<tr>
<td>Kaliumchlorid</td>
<td>Infusions-<br>koncentrat</td>
<td>20 ml</td>
<td>14,9 g/l</td>
<td>686176</td>
</tr>
<tr>
<td>Kaliumcitrat</td>
<td>Tabletter</td>
<td>100 stk.</td>
<td>500 mg</td>
<td>686194</td>
</tr>
<tr>
<td>Kaliumiodid</td>
<td>Afdelte pulvere</td>
<td>5 g</td>
<td>100 %</td>
<td>686177</td>
</tr>
<tr>
<td>L-lysinhydrochlorid</td>
<td>Tabletter</td>
<td>20 stk.</td>
<td>500 mg</td>
<td>686195</td>
</tr>
<tr>
<td>Lobelinhydrochlorid</td>
<td>Injektions-<br>væske</td>
<td>10 ml</td>
<td>10 mg/ml</td>
<td>686154</td>
</tr>
<tr>
<td>Medicinsk kul</td>
<td>Oral opløsning</td>
<td>1 L</td>
<td>160 mg/ml</td>
<td>686196</td>
</tr>
<tr>
<td>Mepyramin</td>
<td>Injektionsvæske</td>
<td>20 ml</td>
<td>25 mg/ml</td>
<td>686197</td>
</tr>
<tr>
<td>Methyltestosteron, 17 alfa</td>
<td>Opløseligt pulver</td>
<td>20 mg</td>
<td>100 %</td>
<td>686178</td>
</tr>
<tr>
<td>Natriumbicarbonat</td>
<td>Infusions-<br>væske</td>
<td>500 ml</td>
<td>84 mg/ml</td>
<td>686179</td>
</tr>
<tr>
<td>Natriumchlorid</td>
<td>Infusions-<br>koncentrat</td>
<td>1 L</td>
<td>90g/l</td>
<td>686180</td>
</tr>
<tr>
<td>Natriumchlorid</td>
<td>Infusions-<br>væske</td>
<td>1 L</td>
<td>75g/l</td>
<td>686181</td>
</tr>
<tr>
<td>Natriumdioctylsulfosuccinat</td>
<td>Oral opløsning</td>
<td>100 ml</td>
<td>50 mg/ml</td>
<td>686155</td>
</tr>
<tr>
<td>Neostigmin</td>
<td>Injektions-<br>væske</td>
<td>10 ml</td>
<td>2,5 mg/ml</td>
<td>686182</td>
</tr>
<tr>
<td>Polyvidon</td>
<td>Skyllevæske</td>
<td>500 ml</td>
<td>20 mg/ml</td>
<td>686198</td>
</tr>
<tr>
<td>Prednisolon</td>
<td>Afdelte pulvere</td>
<td>20 stk.</td>
<td>100 mg</td>
<td>686199</td>
</tr>
<tr>
<td>Prednisolon</td>
<td>Afdelte pulvere</td>
<td>10 stk.</td>
<td>500 mg</td>
<td>686200</td>
</tr>
<tr>
<td>Prednisolon og mepyramin</td>
<td>Afdelte pulvere</td>
<td>10 stk.</td>
<td>40 mg + 1 g</td>
<td>686201</td>
</tr>
<tr>
<td>Ringer acetat</td>
<td>Infusions-<br>væske</td>
<td>250 ml</td>
<td>komb.</td>
<td>686183</td>
</tr>
<tr>
<td>Ringer chlorid</td>
<td>Infusions-<br>koncentrat</td>
<td>1 L</td>
<td>komb.</td>
<td>686184</td>
</tr>
<tr>
<td>Sulfacombin: Sulfadiazin/sulfadimidin/sulfamerazin/saccharinnatrium/saccharose/carboxymethylcelluloseslim</td>
<td>Mikstur</td>
<td>40 ml</td>
<td>100 mg/ml (33 + 33 + 33 mg/ml)</td>
<td>686202</td>
</tr>
<tr>
<td>Taurin</td>
<td>Tabletter</td>
<td>100 stk.</td>
<td>250 mg</td>
<td>686203</td>
</tr>
<tr>
<td>Thiaminhydrochlorid</td>
<td>Injektionsvæske</td>
<td>10 ml</td>
<td>250 mg/ml</td>
<td>686144</td>
</tr>
<tr>
<td>Zinkchlorid</td>
<td>Vandig<br>opløsning</td>
<td>100 ml</td>
<td>50%</td>
<td>686204</td>
</tr>
<tr>
<td>Zinkoxid</td>
<td>Premix</td>
<td>1 kg</td>
<td>100% (80% Zn)</td>
<td>686167</td>
</tr>
<tr>
<td>Zinkoxid</td>
<td>Premix</td>
<td>5 kg</td>
<td>100% (80% Zn)</td>
<td>686168</td>
</tr>
<tr>
<td>Zinkoxid</td>
<td>Premix</td>
<td>10 kg</td>
<td>100% (80% Zn)</td>
<td>686169</td>
</tr>
<tr>
<td>Zinkoxid</td>
<td>Premix</td>
<td>25 kg</td>
<td>100% (80% Zn)</td>
<td>686170</td>
</tr>
<tr>
<td>Zinkoxid</td>
<td>Oralt pulver</td>
<td>1 kg</td>
<td>100% (80% Zn)</td>
<td>686185</td>
</tr>
<tr>
<td>Zinkoxid</td>
<td>Oralt pulver</td>
<td>5 kg</td>
<td>100% (80% Zn)</td>
<td>686186</td>
</tr>
<tr>
<td>Zinkoxid</td>
<td>Oralt pulver</td>
<td>10 kg</td>
<td>100% (80% Zn)</td>
<td>686187</td>
</tr>
<tr>
<td>Zinkoxid</td>
<td>Oralt pulver</td>
<td>25 kg</td>
<td>100% (80% Zn)</td>
<td>686188</td>
</tr>
<tr>
<td>Veterinære lægemidler på udleveringstilladelse:</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Avatec</td>
<td>Premix</td>
<td>20 kg</td>
<td>150 mg/g</td>
<td>686301</td>
</tr>
<tr>
<td>Florfenicol (Aquaflor)</td>
<td>Premix</td>
<td>100 g</td>
<td>50%</td>
<td>686692</td>
</tr>
<tr>
<td>Florfenicol (Aquaflor)</td>
<td>Premix</td>
<td>2 kg</td>
<td>50%</td>
<td>686693</td>
</tr>
<tr>
<td>Lignocain</td>
<td>Injektions-<br>væske</td>
<td>100 ml</td>
<td>20 mg + 0,0125 mg/ml</td>
<td>686051</td>
</tr>
</table>

<table>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="4"><strong>Bilag 2.9 Varenumre til lægemiddelpakninger fra Veterinærinstituttet DTU</strong></td>
</tr>
<tr>
<td><strong>Varenavn</strong></td>
<td><strong>Enhed</strong></td>
<td><strong>ATC-kode</strong></td>
<td><strong>Varenummer</strong></td>
</tr>
<tr>
<td>Alphaject 3000</td>
<td>500 ml</td>
<td>QI10A</td>
<td>689133</td>
</tr>
<tr>
<td>Autovac. E-coli til høns</td>
<td>1000 doser</td>
<td>QI01A</td>
<td>689146</td>
</tr>
<tr>
<td>Autovac Furunculose</td>
<td>1 dosis</td>
<td>QI07A</td>
<td>689152</td>
</tr>
<tr>
<td>Autovaccine impetigo Vet.</td>
<td>20 doser</td>
<td>QI09A</td>
<td>689141</td>
</tr>
<tr>
<td>Autovaccine impetigo VET.</td>
<td>100 doser</td>
<td>QI09A</td>
<td>689142</td>
</tr>
<tr>
<td>Avinew</td>
<td>1000 doser</td>
<td>QI01A</td>
<td>689123</td>
</tr>
<tr>
<td>Avinew</td>
<td>2000 doser</td>
<td>QI01A</td>
<td>689124</td>
</tr>
<tr>
<td>AviPro ILT</td>
<td>1000 doser</td>
<td>QI01A</td>
<td>689114</td>
</tr>
<tr>
<td>Coglamune</td>
<td>50 ml</td>
<td>QI09A</td>
<td>689109</td>
</tr>
<tr>
<td>Coliserum Vet.</td>
<td>1 dosis</td>
<td>QI02A</td>
<td>689144</td>
</tr>
<tr>
<td>Covexin 8 A</td>
<td>50 ml</td>
<td>QI09A</td>
<td>689108</td>
</tr>
<tr>
<td>Cunivac Jet</td>
<td>1 dosis</td>
<td>QI08A</td>
<td>689155</td>
</tr>
<tr>
<td>Diluant Palmipede</td>
<td>500 doser</td>
<td>QI01A</td>
<td>689126</td>
</tr>
<tr>
<td>Dindoral</td>
<td>1000 doser</td>
<td>QI01C</td>
<td>689129</td>
</tr>
<tr>
<td>Distox Plus (IR)</td>
<td>250 doser</td>
<td>QI20C</td>
<td>689132</td>
</tr>
<tr>
<td>Emulsibac-SS</td>
<td>100 ml</td>
<td>QI09A</td>
<td>689110</td>
</tr>
<tr>
<td>Farrowsure Plus B</td>
<td>10 doser</td>
<td>QI09A</td>
<td>689111</td>
</tr>
<tr>
<td>Gallimune FluH5N9</td>
<td>1000 doser</td>
<td>QI01A</td>
<td>689149</td>
</tr>
<tr>
<td>Gallimune ND-IB-EDS-ART(407)</td>
<td>1000 doser</td>
<td>QI01A</td>
<td>689118</td>
</tr>
<tr>
<td>Haemo shield 4 Vet.</td>
<td>100 ml</td>
<td>QI09A</td>
<td>689106</td>
</tr>
<tr>
<td>Hepatovax m.solvens</td>
<td>500 doser</td>
<td>QI01B</td>
<td>689148</td>
</tr>
<tr>
<td>Hybermune-RE</td>
<td>1000 ml</td>
<td>QI05A</td>
<td>689153</td>
</tr>
<tr>
<td>Hyobac App2 Vet.</td>
<td>100 ml</td>
<td>QI09A</td>
<td>689105</td>
</tr>
<tr>
<td>Hyosin DNT Vet.</td>
<td>10 doser</td>
<td>QI09A</td>
<td>689102</td>
</tr>
<tr>
<td>Hyosin DNT Vet.</td>
<td>25 doser</td>
<td>QI09A</td>
<td>689103</td>
</tr>
<tr>
<td>Nobilis CAV P4 m/solvens</td>
<td>1000 doser</td>
<td>QI01A</td>
<td>689119</td>
</tr>
<tr>
<td>Nobilis Dilavia</td>
<td>1000 doser</td>
<td>QI01A</td>
<td>689120</td>
</tr>
<tr>
<td>Nobilis Erysipelas</td>
<td>500 doser</td>
<td>QI01C</td>
<td>689130</td>
</tr>
<tr>
<td>Nobilis Reo Inact.</td>
<td>1000 doser</td>
<td>QI01A</td>
<td>689116</td>
</tr>
<tr>
<td>Nobilis Rhino CV</td>
<td>1000 doser</td>
<td>QI01A</td>
<td>689117</td>
</tr>
<tr>
<td>Norvax Minova 4WD</td>
<td>500 ml</td>
<td>QI10</td>
<td>689147</td>
</tr>
<tr>
<td>Palmivax Vet. m/solvens</td>
<td>500 doser</td>
<td>QI01D</td>
<td>689127</td>
</tr>
<tr>
<td>Pirodog</td>
<td>1 dosis</td>
<td>QI07A</td>
<td>689154</td>
</tr>
<tr>
<td>Porcilis AR-T w/o</td>
<td>20 ml</td>
<td>QI09A</td>
<td>689100</td>
</tr>
<tr>
<td>Poulvac diluent</td>
<td>400 ml</td>
<td>QI01C</td>
<td>689151</td>
</tr>
<tr>
<td>Poulvac I-ND</td>
<td>500 ml</td>
<td>QI01A</td>
<td>689122</td>
</tr>
<tr>
<td>Poulvac Marek HVT m.solv.</td>
<td>2000 doser</td>
<td>QI01C</td>
<td>689150</td>
</tr>
<tr>
<td>Poulvac NDW</td>
<td>2000 doser</td>
<td>QI01A</td>
<td>689121</td>
</tr>
<tr>
<td>Poulvac Pabac 4</td>
<td>1000 doser</td>
<td>QI01A</td>
<td>689115</td>
</tr>
<tr>
<td>Poulvac TRT-kun til kalkuner</td>
<td>2000 doser</td>
<td>QI01C</td>
<td>689128</td>
</tr>
<tr>
<td>Salmonella dublin serum Vet.</td>
<td>1 dosis</td>
<td>QI02A</td>
<td>689145</td>
</tr>
<tr>
<td>Serum mod tarmbrand (USA)</td>
<td>50 ml</td>
<td>QI09A</td>
<td>689107</td>
</tr>
<tr>
<td>Suivac APP</td>
<td>50 doser</td>
<td>QI09A</td>
<td>689104</td>
</tr>
<tr>
<td>Suivac DNT</td>
<td>25 doser</td>
<td>QI09A</td>
<td>689101</td>
</tr>
<tr>
<td>Suivac EDT</td>
<td>100 doser</td>
<td>QI09A</td>
<td>689112</td>
</tr>
<tr>
<td>Suivac PRRS - IN</td>
<td>50 doser</td>
<td>QI09A</td>
<td>689113</td>
</tr>
<tr>
<td>Ødemsyge serum</td>
<td>50 ml</td>
<td>QI09A</td>
<td>689143</td>
</tr>
<tr>
<td>Artervac</td>
<td>1 dosis</td>
<td>QI05A</td>
<td>689135</td>
</tr>
<tr>
<td>Cunivak Myxo</td>
<td>10 x 1 ml</td>
<td>QI08A</td>
<td>689138</td>
</tr>
<tr>
<td>Cunivak Myxo</td>
<td>10 ml</td>
<td>QI08A</td>
<td>689139</td>
</tr>
<tr>
<td>Cunivak Myxo</td>
<td>1 ml</td>
<td>QI08A</td>
<td>689140</td>
</tr>
<tr>
<td>Duramune 8 DAPPI + LC</td>
<td>25 x 1 doser</td>
<td>QI07A</td>
<td>689136</td>
</tr>
<tr>
<td>Eurican Herpes</td>
<td>1 dosis</td>
<td>QI07A</td>
<td>689137</td>
</tr>
<tr>
<td>Febrivac Dist</td>
<td>5 x 1 doser</td>
<td>QI20D</td>
<td>689131</td>
</tr>
<tr>
<td>Tetanusserum</td>
<td>5 ml</td>
<td>QI05A</td>
<td>689134</td>
</tr>
<tr>
<td>Vaxiduk (+ Palmipede)</td>
<td>500 doser</td>
<td>QI01B</td>
<td>689125</td>
</tr>
</table>

<table>
<tr>
<td>Varenumre til anden anvendelse</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>Bilag 2.10 Diverse</strong></td>
<td></td>
</tr>
<tr>
<td></td>
<td><strong>Varenummer</strong></td>
</tr>
<tr>
<td>Homøopatiske lægemidler</td>
<td>685802</td>
</tr>
<tr>
<td>Tryghedskasse, lægemidler</td>
<td>685244</td>
</tr>
<tr>
<td>Tryghedskasse, ikke lægemidler</td>
<td>685245</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>Varenummer uoplyst</strong></td>
<td></td>
</tr>
<tr>
<td>Håndkøb, frihandelsvarer</td>
<td>222222</td>
</tr>
<tr>
<td>Industrispecialitet</td>
<td>555555</td>
</tr>
<tr>
<td>Magistrelle lægemidler, der er underkastet § 4 i receptbekendtgørelsen, når de ikke er nævnt andet sted i bilag 2</td>
<td>666666</td>
</tr>
<tr>
<td>Lægemidler på udleveringstilladelse i henhold til lægemiddellovens § 29</td>
<td>685800</td>
</tr>
<tr>
<td>Sprit (magistrel)</td>
<td>777777</td>
</tr>
<tr>
<td>Magistrelle lægemidler, hvis de ikke er nævnt andet sted i bilag 2</td>
<td>888888</td>
</tr>
<tr>
<td>Uden avance</td>
<td>999999</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>Gebyrer</strong></td>
<td></td>
</tr>
<tr>
<td>Telefonreceptgebyr</td>
<td>100000</td>
</tr>
<tr>
<td>Udbringningsgebyr</td>
<td>100030</td>
</tr>
<tr>
<td>Administrationsgebyr</td>
<td>100035</td>
</tr>
<tr>
<td>Vagtgebyr</td>
<td>100050</td>
</tr>
<tr>
<td>Leverancehonorar</td>
<td>100090</td>
</tr>
<tr>
<td>Dosispakningsgebyr – pakket fra eget apotek</td>
<td>688001</td>
</tr>
<tr>
<td>Dosispakningsgebyr – pakket fra andet apotek</td>
<td>688002</td>
</tr>
<tr>
<td>Dosisekspeditionsgebyr</td>
<td>688003</td>
</tr>
<tr>
<td>Servicegebyr (dosispakning – pakket fra eget apotek)</td>
<td>688004</td>
</tr>
<tr>
<td>Servicegebyr (dosispakning – pakket fra andet apotek)</td>
<td>688005</td>
</tr>
<tr>
<td>Servicegebyr (dosisekspedition)</td>
<td>688006</td>
</tr>
<tr>
<td>Dosispakningsgebyr ved salg mellem apoteker</td>
<td>688007</td>
</tr>
<tr>
<td>Levering af apoteksforbeholdte lægemidler fra håndkøbsudsalg</td>
<td>688010</td>
</tr>
<tr>
<td>Udbringningsgebyr - beboere på institutioner og udbringning via hjemmeplejen</td>
<td>688017</td>
</tr>
<tr>
<td>Udbringningsgebyr - e-handel</td>
<td>688018</td>
</tr>
<tr>
<td colspan="2">Recepturgebyr og eventuelt færdigblandingsgebyr indgår i ekspeditionens pris, jf. punkt 3.16.</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2"><strong>Rabatter</strong></td>
</tr>
<tr>
<td>Rabat på liberaliserede lægemidler til produktionsdyr</td>
<td>686310</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2"><strong>Udligning</strong></td>
</tr>
<tr>
<td>Udligning af for meget eller for lidt udbetalt tilskud (CTR)</td>
<td>100015</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2"><strong>Salg af dosisdispenserede lægemidler til andre apoteker</strong></td>
</tr>
<tr>
<td>Salg af dosisdispenserede lægemidler mellem to apoteker.</td>
<td>688000</td>
</tr>
</table>

## Officielle noter

1\) jf. § 39 stk. 1 i lov nr. 1180 af 12. december 2005 om lægemidler

2\) jf. § 7 stk. 1 i bekendtgørelse nr. 749 af 1. juli 2008 om euforiserende stoffer
