# Ordliste — Decision-Driven Design (dansk)

En arbejdsoversættelse af rammeværkets kernebegreber, til brug i samtaler med dansktalende kolleger.
Engelsk term i parentes, så teksten stadig kan følges op mod det engelske materiale.

*Dette er en oversættelse af vokabularet, ikke en genformulering af rammeværket. Hvor dansk og
engelsk er uenige, vinder det engelske kildemateriale — oversættelsen skal tjene forståelsen, ikke
erstatte den.*

---

## De to primitiver (the two primitives)

| Dansk | Engelsk | Note |
|---|---|---|
| **beslutning** | decision | Det, der afgøres. Grundenheden. |
| **grund** | ground | Det, en beslutning afgøres *imod* — det læsbare underlag, aktøren inspicerer for at handle. Bærer samme "fundament, man står på"-betydning på dansk. |

*Kernepåstanden: der findes kun beslutninger og grund. Handlingen **er** en beslutning — den sidste
i kæden, tættest på verden.*

---

## Det centrale begreb (the central quantity)

| Dansk | Engelsk | Note |
|---|---|---|
| **vurderingsbehov** | judgment demand | Antallet af styrende beslutninger, der skal afgøres *pr. kørsel* af en aktør, der læser grund — frem for at arves fra det indkodede lager. Enheden tragt og modning måles i. |
| **specifikationsbehov** | specification demand | Det samme, navngivet i software-projektionen (se *ingeniør-projektionen*). |
| **determinationsbehov** | determination demand | Det aktør-generelle navn på samme størrelse. |

*Bemærk: **behov**, ikke **efterspørgsel**. Det er "det, der skal leveres", ikke markedsefterspørgsel.*

---

## De fire lagre (the four stores)

Hvor kilden til en afgørelse kan bo. Enhver styrende beslutning lander i præcis ét.

| Dansk | Engelsk | Betydning |
|---|---|---|
| **indkodet** | encoded | En begrænsning, afgjort *på forhånd*, af en regel. Amortiseres. Billig at formulere, **dyr at finde**. |
| **mekanisk verificeret** | mechanically verified | Et kriterium, afgjort *bagefter*, af et tjek. Betaler **eksekverbarhedsafgiften** — billig at stole på. |
| **vurdering** | judgment | Afgøres *i øjeblikket*, af en aktør, der læser grund. Amortiseres ikke — går ud ad døren med aktøren. |
| **ikke-truffet** | escaped | Afgjort af **ingen**. Se den udvidede note nedenfor — dette er det begreb, oversættelsen skal være mest omhyggelig med. |

### Om "ikke-truffet" (escaped)

Det engelske *escaped* fungerer metaforisk: beslutningen "slap væk". Men **det er ikke pointen** —
pointen er, at *ingen traf den*. En direkte oversættelse (*undsluppet*) antyder en aktør, der flygtede;
her er der tværtimod ingen handling overhovedet.

Derfor:

> **ikke-truffet** *(henstående)* — beslutninger truffet af ingen.

- **ikke-truffet** siger mekanismen rent: beslutningen blev *ikke truffet* af nogen (*at træffe en
  beslutning*). Præcis, utvetydig, ikke-moraliserende.
- **henstående** som gloss fanger den konnotation *escaped* også bærer på engelsk: noget, der *står hen*
  uhåndteret, mens omkostningen løber på — som en ubetalt regning, der *henstår*.

Dette er det eneste lager, der er **gratis i afgørelsesøjeblikket** — man undlader blot at træffe
beslutningen. Regningen kommer senere, som en fejl, når den er dyrest. Det er derfor alt driver mod
dette lager, og hvorfor det er den **eneste forbudte tilstand**.

*Undgå: **uafgjort** (betyder "uafgjort kamp" — kolliderer), **forsømt** (moraliserer — antyder skyld,
men escape er ofte bare fravær af en beslutning, ikke forsømmelse).*

---

## Aktør-modellen (the actor model)

| Dansk | Engelsk | Note |
|---|---|---|
| **aktør** | actor | Hvad som helst, der træffer beslutninger imod grund. |
| **fastlåsningsopløsning** | pinning resolution | Hvor stramt en aktørs adfærd kan bindes. |
| — ved **værdi** | by value | Program — et punkt. Alle beslutninger truffet på forhånd. |
| — ved **binding** | by binding | Model — en fordeling, der kan fryses. |
| — ved **klassifikation** | by classification | Menneske — en **kapabilitetsramme** (rang, certificering, udvælgelse). |
| **kapabilitetsramme** | capability envelope | Det, man får af et menneske: en ramme, ikke en fordeling. Individuel, udløbende, ikke instans-generel. |

### Udvælgelse vs. træning (selection vs. training)

| Dansk | Engelsk |
|---|---|
| **træning** | training |
| **udvælgelse** | selection |

> **Træning** er, hvad man gør, når acceptprædikatet **lukker**.
> **Udvælgelse** er, hvad man gør, når det **ikke** gør.
> *Man kan ikke tjekke arbejdet, så man tjekker arbejderen.*

**Udvælgelsesintensitet er omvendt proportional med prædikatlukning.**

---

## Gulvet og prædikatet (the floor and the predicate)

| Dansk | Engelsk | Note |
|---|---|---|
| **gulvet** | the floor | Den del af vurderingsbehovet, der **ikke** kan flyttes væk fra aktøren. |
| **acceptprædikat** | acceptance predicate | Tjekket, der afgør, om en afgørelse er rigtig. |
| **lukker / lukning** | closes / closure | Om acceptprædikatet kan afgøres over digital grund. |
| **stidegenererethed** | path-degeneracy | Uendeligt mange forskellige afgørelser, der alle rammer et tilstrækkeligt resultat. |

> **Gulvet ligger i acceptprædikatet, ikke i beslutningen.** Nul, hvor prædikatet lukker (og der gør
> stidegenererethed nullet robust — kun en *tilstrækkelig* afgører kræves, ikke en bestemt). Ikke-nul,
> hvor det ikke lukker — og *om* det lukker er generelt uafgørligt (Rice).

---

## Sammensætning og sømme (composition and seams)

| Dansk | Engelsk | Note |
|---|---|---|
| **søm** | seam | Grænsefladen mellem dekomponerede dele. |
| **sømbehov** | seam demand | De beslutninger, der kun opstår *mellem* delene. `|D_komp| = |D_enkelt| + |S|`. |
| **sømbesættelse** | seam occupancy | Hvad der sidder i sømmen — en aktør eller en mekanisme. |
| **orkestrator** | orchestrator | En aktør i sømmen. Fleksibel, men flaskehals og forgiftbart centrum. |
| **mekanisme** | mechanism | Encoding i sømmen (udvælgelse, stigmergi, prisdannelse). Skalerer, men stiv. |
| **det matchede par** | the matched pair | Man må ikke flytte sømbehov fra vurdering til indkodet **uden samtidig** at tilføje et mekanisk tjek på sømmen. Det er, hvad thymus er. |

---

## De to projektioner (the two projections)

| Dansk | Engelsk | Note |
|---|---|---|
| **tragt** | funnel | Dybde-projektionen: vurderingsbehov pr. beslutning falder *ned gennem én kørsel*, efterhånden som indkodet grund samler sig. |
| **modning** | maturation | Gentagelses-projektionen: vurderingsbehov pr. kørsel falder *over gentagne kørsler*. |
| **den sammensatte effekt** | the compound | Betal én gang, arv derefter. Begge projektioner er den samme mekanisme på to akser. |
| **kanalen er platformen** | the channel is the platform | Uden en tilbageskrivningskanal fra vurdering til indkodet fordamper de dyre opdagelser. |

> **Tragten måler vurderingsbehov, aldrig antal.** Antallet af beslutninger er fastlagt af opgaven; kun
> behovet falder — og kun til gulvet.

---

## Grund-disciplinen (the ground discipline)

| Dansk | Engelsk | Note |
|---|---|---|
| **indkod/verificér-delingen** | the encode/verify split | Indkod grund, du kontrollerer; verificér grund, du ikke gør. |
| **forgiftet grund** | poisoned ground | Når en aktør forbruger sit eget tidligere output som grund. Fejl bliver *korrekte slutninger over falske præmisser*. |
| **lukningsprincippet** | the closure principle | En aktørs eget tidligere output er ikke grund. |

---

## Registernote (a note on register)

Rammeværkets centrale påstand hedder et **princip**, ikke en **lov** — der findes ingen målbar enhed.
På dansk: **Konservationsprincippet for determinationsbehov** *(the Conservation Principle of
Determination Demand)*. Ordet "lov" bruges kun som hyldest til Tesler og Ashby, aldrig om rammeværkets
egen påstand.
