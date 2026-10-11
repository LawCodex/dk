---
title: "Bekendtgørelse om energiforsyningsvirksomhedernes indberetningspligt til Bygnings- og Boligregistret (BBR)"
identifier: "BEK nr 69 af 26/01/2018"
eli: "https://www.retsinformation.dk/eli/lta/2018/69"
accession_number: "B20180006905"
type: "executive_order"
jurisdiction: "dk"
language: "da"
date: 2018-01-26
status: "in_force"
ministry: "Skatte- og Vækstministeriet"
source: "https://www.retsinformation.dk/eli/lta/2018/69"
retrieved: 2026-10-11
---

# Bekendtgørelse om energiforsyningsvirksomhedernes indberetningspligt til Bygnings- og Boligregistret (BBR)

*BEK nr 69 af 26/01/2018*

I medfør af § 4, stk. 4 og 5, og § 8, stk. 2, i lov om bygnings- og boligregistrering, jf. lovbekendtgørelse nr. 1080 af 5. september 2013, fastsættes:

## § 1.

Energiforsyningsvirksomheder, der leverer fjernvarme, naturgas eller fyringsolie til slutbrugeren, skal meddele oplysninger om den enkelte slutbrugers forbrug til BBR efter de anvisninger, der fremgår af bilag 1.

*Stk. 2.* Fra meddelelsespligten undtages:

- 1\) Leverancer af energi, hvor leverandøren ikke er aftalepart i forhold til slutbrugeren. Dette kan f.eks. være tilfældet, hvis leverandøren gør brug af et ledningsnet, der ejes af et andet selskab.
- 2\) Energiforsyningsvirksomheder, der leverer energi til færre end 10 slutbrugere, hvis dette omfatter færre end 10 boligenheder.

*Stk. 3.* Energinet skal meddele oplysninger om den enkelte slutbrugers forbrug af elektricitet til BBR efter de anvisninger, der fremgår af bilag 1.

## § 2.

Alle energiforsyningsvirksomheder, der skal indberette energiforbrugsoplysninger, jf. § 1, skal senest 3 måneder efter, at energiforsyningsselskabets regnskabsår er afsluttet, meddele energiforbrugsoplysningerne til BBR. Meddelelsen skal omfatte afregningsperioder afsluttet i løbet af det pågældende regnskabsår.

*Stk. 2.* Alle afregningsperioder, der indeholder tidspunktet 1. januar 2010 kl. 1.00 og alle tidspunkter derefter, er omfattet af meddelelsespligten. Energinet skal levere data, der indeholder tidspunktet 1. marts 2013 kl. 1.00, og alle tidspunkter er derefter omfattet af meddelelsespligten.

*Stk. 3.* Energinet skal minimum én gang årligt levere oplysninger om den enkelte slutbrugers forbrug af elektricitet til BBR. Energinet skal foretage første indberetning senest den 1. april 2018.

## § 3.

Alle energiforsyningsvirksomheder, der skal indberette energiforbrugsoplysninger, jf. § 1, skal ved meddelelse af data til BBR angive forbruget i de samme tidsperioder og værdier, som energiforsyningsvirksomhederne afregner over for slutbrugeren.

*Stk. 2.* Såfremt der sker ændringer i de oplysninger, der er indberettet efter stk. 1, skal energiforsyningsvirksomheden senest indberette de korrigerede oplysninger i forbindelse med den næste indberetning af data til BBR efter §§ 1 og 2.

## § 4.

Energinet skal minimum én gang årligt indberette målerstamdata samt forbrugsdata til BBR i de samme tidsperioder og værdier, som energiforsyningsvirksomhederne har meddelt til Energinets datahub inklusiv oversigt over eventuelle korrektioner og ændringer i målerstamdata, jf. dog stk. 2.

*Stk. 2.* Målinger af forbrug fra målere, der aflæses månedligt, indberettes med det månedlige forbrug. Målinger af forbrug fra målere, der aflæses i tidsintervaller kortere end en måned, skal summeres op svarende til en kalendermåned. Målinger af forbrug fra målere, der aflæses i tidsintervaller længere end en måned, skal indberettes i de tidsintervaller, de modtages fra energivirksomheden. Slutafregnes forbruget for en måler, skal perioden altid indberettes, også selv om perioden er kortere end en måned.

## § 5.

Medmindre højere straf er forskyldt efter øvrig lovgivning, straffes med bøde den, der forsætligt eller ved grov uagtsomhed undlader rettidigt at meddele oplysninger, der afkræves efter § 1, stk. 1 og 3, og §§ 2-4.

## § 6.

Bekendtgørelsen træder i kraft den 1. februar 2018.

*Stk. 2.* Bekendtgørelse nr. 152 af 18. februar 2013 om energiforsyningsselskabernes indberetningspligt til Bygnings- og Boligregistret (BBR) ophæves.

Skatteministeriet, den 26. januar 2018

Karsten Lauritzen

/ Camilla Christensen

## Bilag 1

Krav til dataformat ved indberetning af elforbrugsdata fra Energinet

Dette bilag beskriver datastruktur og -format for de data, som Energinet skal indberette. Formatet på filen er en csv, som består af en eller flere linjer.

Csv-filer skal for hver linje indeholde én fuldstændig transaktion forstået således, at alle nødvendige data til aflevering af den afregnede energileverance til BBR skal være indeholdt i én linje. Hver linje skal afsluttes med 'ny linje' (ASCII CR+LF), og de enkelte datafelter i linjen skal adskilles af et separatortegn, et semikolon (; ). Tegnsæt, jævnfør Codepage 865.

Rækkefølgen af datafelter skal være som angivet nedenfor:

Dataformat for datoer skal være: "dd-mm-åååå".

Decimal separator for numeriske felter skal være komma (,).

Tusinde tals separator må ikke anvendes i numeriske felter.

Dataformatet ASCII(50) angiver, at feltet må indeholde alfanumeriske tegn. I dette tilfælde maksimalt 50 alfanumeriske tegn. For alfanumeriske felter gælder det endvidere, at værdien skal være omgivet af citationstegn (". .").

Dataformater NUMBER(10,1) angiver, at feltet kun må indeholde et decimaltal. I dette tilfælde er tallet, bestående af maksimalt 10 betydende cifre, hvoraf maksimalt ét ciffer må være efter decimalseparatoren.

| **Felt nummer** | **Datafelt** | **Dataformat** | **Bemærkning** |
|---|---|---|---|
| 1 | Energiforsyningsselskab |  | Ikke krævet for elektricitet. |
| 2 | Leverancested ID | ASCII(18) | Elforsyningsvirksomhedens nummerering af målersted/leverancested.<br>GSRN nummeret. |
| 3 | Metode leverancested | ASCII(1) | Metode for angivelse af leverancestedets geografiske placering, se note 1).<br>Kun følgende værdier er tilladte: "1" eller "2".<br>Eksempel: "1" eller "2".<br>Oplysningen er krævet. |
| 4 | Adgangsadresse ID |  | Ikke krævet for elektricitet. |
| 5 | Enhedsadresse ID |  | Ikke krævet for elektricitet. |
| 6 | Postnummer | ASCII(4) | Postnummer for leverancestedets geografiske placering. Dataformat jævnfør: OIOXML PostCodeIdentifier.<br>Eksempel: "7800".<br>Vedrørende krav til oplysningen, se note 1). |
| 7 | Supplerende bynavn |  | Ikke krævet for elektricitet. |
| 8 | Kommunekode | ASCII(4) | Kommunekode som angiver den kommune, hvori leverancestedet geografisk er placeret. Eventuelle foranstående nuller medtages. Dataformat jævnfør: OIOXML AuthorityCode.<br>Eksempel: "0751".<br>Vedrørende krav til oplysningen, se note 1). |
| 9 | Vejkode | ASCII(4) | Vejkode som angiver det vejnavn, som leverancestedet geografisk er placeret ved. Eventuelle foranstående nuller medtages. Dataformat jævnfør: OIOXML StreetCode.<br>Eksempel: "0179".<br>Vedrørende krav til oplysningen, se note 1). |
| 10 | Vejnavn | ASCII(40) | Vejnavn for leverancestedets geografiske placering. Dataformat jævnfør: OIOXML StreetName.<br>Eksempel: "Alexander Kiellands Vej".<br>Vedrørende krav til oplysningen, se note 1). |
| 11 | Husnummer | ASCII(10) | Husnummer inklusive eventuelt bogstav, som angiver leverancestedets geografiske placering. Dataformat jævnfør: OIOXML StreetBuildingIdentifier.<br>Angives som 1-999 dvs. uden foranstående nuller og uden mellemrum før evt. stort bogstav A-Z.<br>Eksempel: "7" eller "14A".<br>Vedrørende krav til oplysningen, se note 1). |
| 12 | Etagebetegnelse | ASCII(2) | Etagebetegnelse for leverancested. Dataformat jævnfør: OIOXML FloorIdentifier.<br>Eksempler: "1", "2", "st" eller "kl".<br>Oplysningen er krævet, hvis den indgår som en del af leverancestedets adresse. |
| 13 | Dørbetegnelse | ASCII(4) | Dørbetegnelse, dvs. sidebetegnelse, dørnummer el. lign. for leverancested. Dataformat jævnfør: OIOXML SuiteIdentifier.<br>Eksempel: "tv", "th", "mf", "1" eller "2".<br>Oplysningen er krævet, hvis den indgår som en del af leverancestedets adresse. |
| 14 | Ejendomsnummer |  | Ikke krævet for elektricitet. |
| 15 | Bygningsnummer |  | Ikke krævet for elektricitet. |
| 16 | X koordinat |  | Oplyses, såfremt det er kendt. |
| 17 | Y koordinat |  | Oplyses, såfremt det er kendt. |
| 18 | Forsyningsart | ASCII(15) | Elektricitet: Her angives værdien ”Elektricitet”. |
| 19 | Indberettet dato | ASCII(10) | Dato for indberetning. Det vil sige dato for generering af datafil. Datoformat: dd-mm-åååå.<br>Eksempel: "13-12-2010", som angiver den 13. december 2010.<br>Oplysningen er krævet. |
| 20 | Periode start | ASCII(10) | Tidspunktet for udførelse af den aflæsning, der indleder leveranceperioden. Datoformat: dd-mm-åååå.<br>Eksempel: "13-12-2010", som angiver den 13. december 2010.<br>Oplysningen er krævet. |
| 21 | Periode slut | ASCII(10) | Tidspunktet for udførelse af den aflæsning, der afslutter leveranceperioden. Datoformat: dd-mm-åååå.<br>Oplysningen er krævet. |
| 22 | Måleenhed | ASCII(5) | Elektricitet: "kWh".<br>Oplysningen er krævet. |
| 23 | Mængde | NUMBER(10,1) | Den aflæste mængde i perioden fra Periode Start til Periode Slut (leveranceperioden). Angives uden tusindtals separator og med højst 1 decimal.<br>Eksempel: 4321,5.<br>Oplysningen er krævet. |
| 24 | Status for aflæsning | ASCII(10) | Status for aflæsning.<br>Status kan antage en af følgende værdier: "Aflæst" eller ”Estimeret”.<br>"Aflæst" - Hvis mængden er normalt aflæst.<br>"Estimeret" – Hvis mængden er baseret på et forventet forbrug.<br>Eksempel: "Aflæst".<br>Oplysningen er krævet. |

Note 1)

Forbrugsstedets geografiske placering skal angives på én eller flere af følgende 2 måder:

Metode leverancested = 1: Kræver oplysninger i Felt nr. 6 (Postnummer) + Felt nr. 10 (Vejnavn) + Felt nr. 11 (Husnummer) + evt. felt 12 (Etagebetegnelse) + evt. felt 13 (Dørbetegnelse). Hvis oplysningen i Felt nr. 8 (Kommunekode) kendes, oplyses den ligeledes.

Metode leverancested = 2: Kræver oplysningerne i Felt nr. 8 (Kommunekode) + Felt nr. 9 (Vejkode) + Felt nr. 11 (Husnummer) + evt. felt 12 (Etagebetegnelse) + evt. felt 13 (Dørbetegnelse).
