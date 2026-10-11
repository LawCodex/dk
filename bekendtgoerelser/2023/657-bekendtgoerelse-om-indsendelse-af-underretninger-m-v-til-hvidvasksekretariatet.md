---
title: "Bekendtgørelse om indsendelse af underretninger m.v. til Hvidvasksekretariatet"
identifier: "BEK nr 657 af 26/05/2023"
eli: "https://www.retsinformation.dk/eli/lta/2023/657"
accession_number: "B20230065705"
type: "executive_order"
jurisdiction: "dk"
language: "da"
date: 2023-05-26
status: "in_force"
ministry: "Erhvervsministeriet"
source: "https://www.retsinformation.dk/eli/lta/2023/657"
retrieved: 2026-10-11
---

# Bekendtgørelse om indsendelse af underretninger m.v. til Hvidvasksekretariatet

*BEK nr 657 af 26/05/2023*

I medfør af § 26, stk. 8, og § 78, stk. 6, i lov om forebyggende foranstaltninger mod hvidvask og finansiering af terrorisme (hvidvaskloven), jf. lovbekendtgørelse nr. 316 af 11. marts 2022, fastsættes:

## Anvendelsesområde

### § 1.

Denne bekendtgørelse finder anvendelse på de virksomheder, personer og myndigheder, som er omfattet af lov om forebyggende foranstaltninger mod hvidvask og finansiering af terrorisme.

*Stk. 2.* Bekendtgørelsen finder anvendelse på underretninger om transaktioner eller henvendelser, hvor der er mistanke om, at transaktionen eller henvendelsen har eller har haft tilknytning til hvidvask eller finansiering af terrorisme, til Hvidvasksekretariatet, jf. § 26 i lov om forebyggende foranstaltninger mod hvidvask og finansiering af terrorisme.

## Digital indsendelse

### § 2.

Underretning mv. jf, § 1, stk. 2, skal indsendes digitalt til til Hvidvasksekretariatet via www.hvidvask.dk, medmindre andet er aftalt med Hvidvasksekretariatet.

*Stk. 2.* Underretningen skal indgives i det XML-format, som er gengivet på www.hvidvask.dk.

*Stk. 3.* Underretteren skal efter indsendelse, jf. § 2, stk. 1, og inden udløbet af den efterfølgende bankdag kontrollere, om underretningen er accepteret eller afvist.

## Indhold

### § 3.

Underretning, jf. § 1, stk. 2, skal indeholde de oplysninger, som er beskrevet i bilag 1 til denne bekendtgørelse.

## Sprogkrav

### § 4.

Underretning, jf. § 1, stk. 2, skal som udgangspunkt være affattet på dansk. Er dette ikke er muligt, kan underretningen affattes på engelsk.

## Nedbrud i de digitale underretningsløsninger

### § 5.

Ved længerevarende IT-problemer på hjemmesiden www.hvidvask.dk skal underretning i XML-format ske ved e-mail eller andet elektronisk medie efter aftale med Hvidvasksekretariatet.

*Stk. 2.* Med længerevarende IT-problemer, jf. stk. 1, menes nedbrud eller midlertidig kapacitetsnedgang mv., som indebærer, at hjemmesiden www.hvidvask.dk er utilgængelig 8 timer i træk i tidsrummet mellem kl. 8 og 16 på en hverdag. Heri medregnes dog ikke planlagte nedlukninger med henblik på opdatering, som har været annonceret forinden på hjemmesiden.

## Straf

### § 6.

Forsætlig eller grov uagtsom overtrædelse af §§ 2-4 og 5, stk. 1, straffes med bøde.

*Stk. 2.* Der kan pålægges selskaber mv. (juridiske personer) strafansvar efter reglerne i straffelovens 5. kapitel.

## Ikrafttræden

### § 7.

Bekendtgørelsen træder i kraft den 1. juli 2023.

*Stk. 2.* Bekendtgørelse nr. 1403 af 1. december 2017 om indsendelse af underretninger m.v. til Statsadvokaten for Særlig Økonomisk og International Kriminalitet ophæves.

Finanstilsynet, den 26. maj 2023

Kristian Vie Madsen

/ Heidi Ravnholt

## Bilag 1

Beskrivelse af XML filens struktur

XML filens opbygning afhænger af mistanken, der er grundlaget for underretningen.

Underretninger, der vedrører konkrete mistænkelige finansielle transaktioner, består af følgende elementer og er struktureret som følger:

| ● Forside |  |  |  |
|---|---|---|---|
|  | ◦ Transaktion(er) |  |  |
|  |  | ▪ Afsender |  |
|  |  |  | ● Part |
|  |  | ▪ Modtager |  |
|  |  |  | ● Part |

Underretninger, som vedrører konkrete mistænkelige hændelser og ikke vedrører mistænkelige finansielle transaktioner, består af følgende elementer og er struktureret som følger:

| ● Forside |  |  |
|---|---|---|
|  | ◦ Hændelse |  |
|  |  | ▪ Part(er) |

**Beskrivelse af XML filens elementer og definitioner**

**Forside**

Forsiden skal indeholde grundinformation om underretningen, herunder oplysninger om underretter, dato for underretning, om mistanken vedrører hvidvask (STR) eller terrorfinansiering (TFR) samt beskrivelse af mistanken eller angivelse af indikatorer.

**Transaktion(er)**

Transaktionen skal indeholde information om den eller de enkelte transaktion(er), herunder oplysninger om transaktionsnummer, transaktionsdato, transaktionstype, beløb omregnet til DKK, samt afsender og modtager.

**Afsender**

Afsender skal indeholde information, der vedrører transaktionens afsender/kilde, herunder oplysninger om kildeland, type af midler og den part, som er afsender.

**Modtager**

Modtager skal indeholde information, der vedrører transaktionens modtager/destination, herunder oplysninger om destinationsland, type af midler og den modtagende part.

**Part**

Med part menes der oplysninger om konto, samt person eller virksomhed.

**Konto**

Med konto menes der bankkonto, depot, kreditkort, spillekonto eller tilsvarende. Der skelnes mellem konti, og der skelnes mellem konti tilhørende faste kunder og øvrige konti.

**Person**

Med person forstås en fysisk person. Der skelnes mellem personer, der er faste kunder, og øvrige personer.

**Virksomhed**

Med virksomheder menes alle juridiske personer inklusiv foreninger, fonde og lignende. Der skelnes mellem virksomheder der er faste kunder, og øvrige virksomheder.

**Beskrivelse af minimumskrav til XML-filens indhold**

Indgår ovennævnte elementer i underretningen ud fra beskrivelsen af strukturen, skal de enkelte elementer som minimum indeholde nedennævnte oplysninger:

Forside

● Underretter

● Dato for underretning

● Manuel eller elektronisk udfyldelse

● Underretningstype (STR) eller (TFR)

● Lokal valuta (DKK)

● Mistanke eller indikator

Transaktion

● Unikt transaktionsnummer

● Transaktionsdato

● Transaktionstype

● Beløb i DKK

Afsender

● Fondstype (type af midler)

● Kildeland

● Afsenderpart (se parter)

Modtager

● Fondstype (type af midler)

● Destinationsland

● Modtagerpart (se parter)

Hændelse

● Part(er)

Parter

**Person (Fast kunde)**

● Fornavn(e)

● Efternavn

● Fødselsdato

● CPR-nr. eller andet ID (se ID oplysninger)

● Adresse (se adresse)

**Person**

● Fornavn(e)

● Efternavn

**Konto (fast kunde)**

● Pengeinstitut

● SWIFT eller andet PI ID (eksempelvis registreringsnummer)

● Kontonummer

● Konto-/fuldmagtshaver (se person og virksomhed)

● Rolle (eksempelvis konto eller fuldmagtshaver)

**Konto**

● SWIFT eller andet PI ID (eksempelvis registreringsnummer)

● Kontonummer

**Virksomhed (fast kunde)**

● Navn

● CVR-nr. (hvis dansk virksomhed)

● Registreringsland

● Adresse (se adresse)

**Virksomhed**

● Navn

Øvrige elementer

**Adresse**

● Adressetype

● Adresse

● Postnummer (hvis dansk adresse)

● By

● Land

**ID Oplysning**

● ID type

● ID nummer

● Udstedende land
