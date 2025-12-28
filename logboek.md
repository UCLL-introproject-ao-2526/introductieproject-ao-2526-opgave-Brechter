# Algemeen

Mijn idee voor dit spel is om het zo hard mogelijk te laten lijken op de versie van het casino. Ik ben deze zomer voor het plezier in Sofia, Bulgarije naar een casino gegaan en heb daar wat geblackjacket dus ik heb nog wel een goed idee van de regels, en zou ze zo ook graag implementeren.

Ook heb ik me voorgenomen om tijdens dit hele project geen AI te gebruiken, ik heb mezelf soms wel eens betrapt op de gemini-samenvatting van google te gebruiken, maar ik heb maar 1 keer Chatgpt gebruikt en dat was voor inspiratie van designs, dus ik zou zeggen dat me dat redelijk goed gelukt is.

## 17-12-2025

ik ben begonnen voor ik de opdracht volledig gelezen had met alles wat ik al wist van blacjack (hoe kaarten werken en hoe punten werken) in te programmeren zodat ik me tijdens het lezen van de opdracht al kon bezighouden met intuïtief te redeneren hoe ik de volgende stappen ging doen.

### Commit: eerste versie

Ik heb als eerst voor ik pygame uitzocht en de video bekeek al een file Cards.py gemaakt, waar ik 2 classes: Card en Deck en 1 functie makenewdeck in zette. Card heeft als properties suit, number en name suit is niet heel belangrijk in Blackjack, maar dat is leuk als ik later kaarten erin wil toevoegen. Deck heeft een functie draw() waar hij kaarten returnt en die ook ineens verwijderd.

Ook ben ik begonnen na het bekijken van de video met pygame, dit heb ik gedaan in het file GameTech.py, zodat mijn main file echt zo weinig mogelijk code bevat.

Gameplay.py bevat een class Hand die een lijst heeft van kaarten, en Points, Aces en Score als attributen, ik heb dit niet in Card.py gezet omdat ik schrik heb voor cross-imports. Points is de score zonder de azen, dit is belangrijk voor de functies van Pointsystem.py. Ook is er een functie AddCard() die kaarten uit de deck trekt en toevoegt aan de hand, en een functie Evaluatescore() die de score berekent, deze werkt wel nog niet volledig. In dit file ben ik ook van plan om de functie Play() te zetten die de game start.

Pointsystem.py heeft voorlopig 3 functies: Addpoints(), die een kaart bekijkt en Hand.Points en Hand.Aces update. Totalpoints() die met de laatste 2 waarden de optimale score berekent voor de speler. En Comparescores() die de punten van de dealer en de speler vergelijkt om te zeggen wie er wint, en of de speler of de dealer een blackjack heeft.

Tot slot heb je het file Wallet.py waar er een class Bundle is die als objecten zowel de wallet van de speler als zijn inzet kan aannemen, en als ik later een insurance mechanic wil toevoegen is dit ook heel handig. Deze class heeft 1 property: amount, en 1 functie: Addmoney() spreekt voor zich wat beide doen.

## 22-12-2025

vandaag ben ik begonnen aan het ontwerp van het scherm, Ik heb gekozen voor een groene achtergrond zoals de matten van het casino, ook ben ik al een beetje begonnen aan het kaartsysteem maar dat is nog niet volledig af, wel heb ik al alle kaarten gedesigned op piskel. Ik heb ook besloten een file te maken genaamd globals, zo kan ik dat naast mijn main file (Game) ook elders gebruiken.

### Commit: new changes

Als eerste ben ik begonnen met een file Game.py te maken, dit wordt mijn main file, momenteel heb ik wel enkel een paar dingen van GameTech.py gekopiëerd want ik weet niet wat waar gaat komen uiteindelijk.

Ook heb ik mijn Hand class echt zijn eigen file gegeven, wederom omwille van die angst voor cross-imports. En ik heb een functie Betreset() gemaakt, zodat je ook terug naar 0 kan gaan

### Commit: Wallet fixed

Ik heb BetAdd() en BetReset() in Wallet.py gezet zodat ik alles wat geld betreft in één file heb. Ook heb ik al een fundering gelegd voor het insurance mechanic met BetInsurance(). Dit was vooral zodat ik aan PayOut() kon werken, waar je, afhankelijk van de ronde, je geld terugkrijgt.

Ik heb uiteindelijk ook besloten om GameTech.py toch maar niet te gebruiken en alles wat het opbouwen van de game betreft, bevindt zich nu ook in Game.py.

Tot slot heb ik ook nog een beetje gewerkt aan de look van de game, kleuren bepaald enzo. Ik heb voor ronde knoppen gekozen omdat ik denk dat dat wel een leuk effect geeft aan het spel

### Commit: first version cards

Ik had even geen zin meer om te coderen, dus ik heb besloten om te beginnen met de kaarten. Ik heb volgens mij het hele internet afgezocht om uiteindelijk een goed programma te vinden voor sprites te gebruiken: Piskel. Ik ben toen begonnen met het design van de kaarten en de achterkant. De klaveren waren wat lastig omdat ik langs de horizontale as werkte met een oneven aantal pixels, ik ben er niet heel trots op maar het is wat het is

Daarna heb ik dus ook een revealed property aan card gegeven en een functie reveal() die die property op True zet. Daarmee heb ik ook mijn Draw() functie uitgebreid zodat je nu ook kaarten kan trekken zonder ze te laten zien aan de speler.

In Game.py heb ik een startknop toegevoegd aan het betmenu, zodat je het spel ook kan starten. Ook heb ik frameworks toegevoegd aan mijn code voor insurance en een score voor de speler.

Ik heb ook de class Hand terug in Gameplay.py gezet, want ik begin echt wel veel te veel files te krijgen, en in Wallet.py heb ik ervoor gezorgd dat de wallet niet negatief kan gaan zowel bij insurance als bij bet.

In Pointsystem.py heb ik de getalletjes aangepast die win(2), loss(0), tie(1) en blackjack(3) aanduiden zodat het gemakkelijker is voor payout. Ook heb ik dealerblackjack een variable gemaakt, zodat één blackjack de andere niet uitsluit.

### Commit: einde 22 december

Ik heb eigenlijkmaar 2 dingen gedaan voor de laatste commit van de dag:
Ik had door toen ik een setter aan een attribute probeerde toe te voegen dat dit niet ging, dus heb ik elk attribute private gemaakt en in properties vervormd.
Ook heb ik een file gemaakt om bijna alle globals in één file te zetten zodat het Game.py file niet té veel lijnen ging krijgen en dat ik die globals ook elders kan gebruiken, hier heb ik de functie simulatecard() aan toegevoegd want die ga ik nog veel nodig hebben

## 23-12-2025

Vandaag heb ik mijn eerste speelbare spel gemaakt, waarmee mijn game nu in the alpha-versie is gekomen. Het is belange na nog niet klaar: als je meer dan 7 kaarten trekt crasht de game, als je boven de 21 komt kan je blijven trekken etc. maar in dit stadium kan je al wel beginnen met spelen als je nauw de regeltjes volgt. Mijn idee is om de game zo hard mogelijk te laten lijken op hoe ze het echt spelen in het casino, vandaar de limiet op 7 kaarten etc.

### Alpha 1.0

Vandaag was het doel om een eerste speelbare versie te maken van het spel. Ik heb dus vanalles gedaan. Ik bespreek het file voor file.

In Globals.py heb ik vanalle coördinaten toegevoegd voor het deck en de handen van player en dealer. de x-positie is in de vorm van een list zodat meerdere kaarden dezelfde variabele kunnen gebruiken. Er zijn er zo wel 2, 1 voor een even aantal kaarten en 1 voor een oneven aantal, dit zodat de hand altijd gecentreerd is. Ik heb win-, tie- en lose-screens toegevoegd die een geel, blauw en rood scherm krijgen respectievelijk. Daarnaast heb ik ook nog globals toegevoegd die de dealerbeurt initiëren, aanduiden en beëindigen.

In Game.py heb ik dus ook de dealerhand gedefiniëerd en zijn mechanics uitgeschreven in de functie dealerplay(). Ik heb ook de functie Drawcards() toegevoegd die de kaarten van beide handen op het scherm tekent op de juiste positie met de list van de x-posities. Ik heb ook de game_end condition en endscreens in mijn gameloop gezet. In de plaats van te werken met de timer heb ik ook besloten te werken met de variabele frame, het handige is dat ik deze telkens weer op 0 kan zetten zodat 1. Ik gewoon kan kijken of frame groter is dan een bepaalde waarde mocht een functie om een of andere reden soms maar in actie schieten. en 2. er een vaste tijd is tussen 2 momenten, dus ipv if timer%60 == 0: doe ik nu gewoon if frame > 60: frame = 0. Zo kan ik ook zeggen dat het eindbeeld exact 3 seconden blijft staan voor het naar het endscreen gaat wat 5 seconden duurt voor het terug naar het betting menu gaat enzovoort.

In Gameplay.py heb ik de retrieve() functie toegevoegd zodat een hand een kaart kan trekken uit het deck en dan ook ineens de score kan optellen. Er is ook een empty() functie zodat we de hand terug leegmaken op het einde van een ronde.

Er bleek een glitch te zijn dat het endscreen niet startte, dit was omdat ik vergeten was bij comparescores() in Pointsystem.py aan een van de returns 2 argumenten toe te voegen terwijl ik wel altijd 2 variabelen vroeg, dus veel problemen met None.

Maar ondanks de problemen kan ik nu eindelijk mijn game eens deftig starten.

## 24-12-2025

Ik ben de dag begonnen met de glitches van gisteren op te lossen, er staat nu een hard limit op 7 kaarten, en als je boven de 21 zit, ga je dood en is het automatisch de beurt aan de dealer. Ook heb ik er nu voor gezorgd dat op het einde van de ronde een endscreen komt dat zegt of je gewonnen bent, verloren of gelijkgespeeld hebt. Daarna ga je terug naar het wedscherm.
Nu al dit gedaan is, is mijn game ongeveer foolproof, en kan hij dus niet meer crashen door wat je doet in de game. de game is dus officiëel speelbaar en we zitten dus in de Beta.

### Alpha 1.1

Ik heb besloten de Hand class toch aan Cards.py toe te voegen nadat ik een flowchart gemaakt had van al mijn imports en besefte dat er helemaal geen import-conflicten zijn. Gameplay.py is nu dus ook leeg, dus ik heb het uit mijn imports gehaald op verschillende plaatsen en verwijderd.

Ik heb Game.py ook nog een beetje opgekuist en vanalles bij de globals gezet. Behalve een paar variabelen die Cards.py nodig hadden, daar heb ik een aparte file voor gemaakt: Setup.py, dit is voor deck, playerhand, dealerhand, en de setupfunctie die de eerste 4 kaarten uitdeelt en de laatste van die 4 gedekt houdt.

Daarnaast heb ik ook het hele insurance mechanic op het scherm gezet zodat het nu werkt en er knoppen verschijnen etc.

### Alpha 1.1.1

Deze commit was voornamelijk om mijn code te cleanen en comments toe te voegen waar nodig. Maar dat is niet het enige wat ik gedaan heb: Als de score van de speler nu boven de 21 gaat kan de speler nu geen kaarten meer trekken, wat vermijdt dat de speler nadat hij dood is kaarten blijft trekken tot hij aan 7 zit en wint.

### Beta 1.0

Ik heb met deze commit eindelijk een versie gecreërd die alles fixt hierna zal het werk vooral zijn om de game mooier te maken en eventuele kleine glitches nog op te lossen.

Ten eerste heb ik in Setup.py nog een klein probleempje opgelost dat de game vastliep als er geen aas als eerste kaart kwam, zodat je ook de game kan spelen als er geen insurance gevraagd wordt.

In Game.py heb ik heel veel coördinaten aan constanten van Globals.py gekoppeld. Ook heb ik een dealerscore toegevoegd aan de UI. Dat zorgde er wel voor dat mijn hitknop voor de score stond en dus heb ik een heleboel knoppen lichtjes verplaatst. Toen ik besefte dat het x-coördinaat van de no insurance knop heel dicht bij de hit-button's x-coördinaat lag, heb ik deze twee ook maar gelijkgetrokken.

Maar veruit de grootste verandering zat hem in het feit dat de game niet meer kon crashen als je gewoon aan het spelen was. De enige manier dat dit voordien kon was door 8 kaarten te trekken, dit omdat HAND_POS_X_EVEN maar 6 waarden had en de computer dus niet wist waar hij de 8ste kaart moest plaatsen, dit heb ik gelimiteerd door len(phand.cards) aan te halen in mijn loop. en te checken dat deze zeker niet boven de 7 ging. Ik dacht hier eerst niet aan omdat die waarde ergens anders al te vinden was, maar ik besefte dat het niet heel erg is om dat 2 keer te berekenen als het mij uren werk bespaart.

### Beta 1.0.1

In deze commit heb ik 2 kleine dingen gedaan: Een setupanimation state gedefiniëerd zodat de kaarten er niet al meteen liggen als het spel begint, in deze fase zijn de hit en stand knoppen er nog niet dus er kunnen geen kaarten tussen de gedealde kaarten komen en de speler kan zich focussen op de animatie die ik van plan ben te implementeren. Ten tweede heb ik ook het betmenu mooier gemaakt want dat was verwarrend en lelijk.

## 26-12-2025

Vandaag heb ik grotendeels gewerkt aan de game mooier te maken: Nieuwe kaarten verschijnen nu altijd aan de rechterkant van jouw en de dealer zijn hand (Beta 1.1). ipv dat de kaart gewoon verschijnt in je hand als je hem trekt, zie je hem nu van de stapel naar je hand gaan, idem voor de dealer (Beta 1.2). Ik heb nu icoontjes gedesigned voor wallet, table en insurance en je kan nu ook niet meer spelen zonder geld in te zetten (Beta 1.3). Daarnaast bleef de insurance op het scherm staan en werd hij ook niet uitbetaald, dat is ook gefixt (Beta 1.3.2). Toen alles in orde was heb ik een Pre-release gedaan omdat ik dacht dat mijn game volledig klaar was, maar dat bleek een slecht idee, ik ben dus verder gegaan met Beta 1.3.3 en 1.3.4 waar ik een endscreen heb toegevoegd voor als je geld op is, en mijn bestanden proper heb gemaakt.

### Beta 1.1

Mijn eerste taak van de dag was het probleem op te lossen dat het niet duidelijk is waar de volgende kaart ligt. Dat is omdat HAND_POS_X_EVEN en ...\_ODD beginnen vanuit het centrum, dit is echter wel nodig als er weinig kaarten zijn. Oorspronkelijk ben ik head first dit probleem beginnen afhandelen, maar dit zorgde voor zo veel problemen dat ik na anderhalf uur besloten heb terug te gaan naar de laatste commit en dus eigenlijk heel veel werk voor niets heb gedaan.

Na een beetje afleiding besloot ik mij er niet te veel van aan te trekken en ben ik opnieuw begonnen met pen en papier en daaruit volgde de functie add_to_list() in Cards.py die hand.cards herschikt telkens er een nieuwe kaart bijkomt waardoor nu alle nieuwe kaarten aan de rechterkant van de hand verschijnen. Dit zorgde echter wel voor een aantal problemen met insurance, gedekte kaarten etc. want deze mechanics steunden op de positie van de kaart in de lijst. Na lang zoeken kwam ik hier ook achter en heb ik dit overal vervangen.

Het scherm bleef nog wel heel vaak hangen telkens ik een nieuwe feature implementeerde, dit kwam omdat heel veel statements die de frame op 0 zetten, vaker True waren, statements zoals not gamestate of phand.cards != 7. ik heb al deze eruit gehaald en veel nieuwe gamestates hiervoor gedefiniëerd, zoals volgende

Ik maakte geen onderscheid in gamestate tussen de beurt van de dealer en de beurt van de speler, wat voor problemen zorgde. Daarom heb ik de gamestate ingame toegevoegd, dit heeft heel veel problemen opgelost. Bij nader inzien is dit een slechte naam maar ondertussen staat hij overal, dus is het een beetje laat om het op te lossen.

### Beta 1.2

In deze commit wou ik eindelijk fixen dat de kaarten niet zomaar verschijnen in de hand van de speler, maar er ook effectief naartoe gaan, daarvoor heb ik de gamestates pcardanimation en dcardanimation toegevoegd, voor spamprevention werken de knoppen hit en stand niet tijdens deze state, maar voor visual effect blijven ze nog wel staan.

Als eerste heb ik de functie cardanimation() gedefinieerd, die origineel vroeg voor de card, eposx (eindpositie x), eposy, bposx en bposy, maar de beginpositie was toch altijd dezelfde, dus die heb ik er al snel uitgehaald. De kaart verscheen ook altijd al in de hand tijdens de animatie, dat heb ik opgelost door vanalles aan te passen in drawcards() waar nu optionele variabelen plinvis en dlinvis zijn die de laatste kaart niet projecteerden, maar dit was redelijk moeilijk omdat sinds Beta 1.1 alle kaarten geshuffled zitten in hand.cards, dus drawcards() is nu een veel langere functie geworden. Daarmee heb ik weer de variabelen van cardanimation() moeten veranderen en nu is het phand, dhand, frame en pcardanim, de laatste vraagt of het de beurt is aan de speler of aan de dealer, die moest erin staan omdat globals in andere bestanden niet per sé dezelfde waarde hebben. Maar voorlopig is de animation voor kaarten trekken gefixt, er rest alleen nog de animation voor kaarten uitdelen.

Alles ging de hele tijd fout en ik was maar nieuwe gamestates aan het definieren maar altijd ging er iets anders fout, de reden dat het uiteindelijk gelukt is, is tweevoudig: Ten eerste was ik bang voor glitches als ik dcardanimation of pcardanimation tegelijk True had staan als setupanimation, en er waren er ook een heleboel, maar ik heb alles eruit gehaald en drawgame() aangepast. Toen ik eindelijk de kaarten zag bewegen ging er nog vanalles fout: ze gingen te ver (frame issue), enkel de eerste kaart kreeg een animation, de gedekte kaart van de dealer kreeg nooit een animation. Dit is volgens mij een goddelijke interventie geweest want op een bepaald moment verwijderde ik een stuk code waarvan ik dacht dat het essentiëel was en alles werkte.

Voor de rest was er ook nog een klein foutje met TotalPoints() in Pointsystem.py waar het vaak azen als 11 telde terwijl het als 1 moest tellen, dit heb ik gefixt gekregen door de 11 te splitsen in 1 en 10 en de 10 er pas op het einde bij te tellen eens de rest van de score berekend was.

### Beta 1.3

Beta 1.3 is een commit die eigenlijk te klein was om 1.3 genoemd te worden ipv 1.2.1 maar hij was dan ook weer te groot om 1.2.1 genoemd te worden, maar bon er wel een paar dingetjes gebeurt.

ik heb icoontjes gedesigned voor de wallet, bet en insurance, en ik heb er ook voor gezorgd dat je geen ronde kan starten zonder geld uit te geven. Nu komt er een berichtje als je dat probeert, ik ben er niet trots op, maar ook dit heb ik opgelost met een global value waardoor het in mijn ogen als gamestate telt.

Daarnaast heb ik ook een scherm gemaakt dat "YOU'RE BROKE" zegt als je verliest en niet genoeg geld hebt om nog een ronde te spelen.

### Beta 1.3.1, Beta 1.3.2, Pre-release 1, Beta 1.3.3 en Beta 1.3.4

Deze vijf commits groepeer ik samen omdat ze allemaal redelijk klein zijn.

Beta 1.3.1: Ik zag tijdens het playtesten dat het insurance-icoontje blijft staan nadat de ronde gedaan is en je hebt insurance niet gewonnen dit was gemakkelijk gefixt door tijdens de endscreen insur op False te zetten en de Insurance-bundle te legen.

Beta 1.3.2: Ik merkte ook dat insurance niet terugbetaald werd bij een dealerblackjack, het duurde langer dan ik durf toe te geven voor ik ontdekte dat Payout() 3 variabelen neemt waarvan 2 optioneel state moet gegeven worden, maar dealerbj en insur niet, ik was vergeten tijdens het oproepen van Payout() om insur te definiëren waardoor dit altijd op False stond.

Pre-release 1: Ik vind dat mijn game grotendeels af is, dus heb ik nog een paar testing clean-ups gedaan en de eerste Pre-release gecommit.

Beta 1.3.3: Er waren bij nader inzien toch een heleboel zaken die nog gefixt moesten worden dus de Pre-release was een slecht idee. Ik wou dus van die branch afgaan maar dan kon ik niet meer git push doen, daardoor ben ik een paar dingen kwijtgeraakt maar wat ik heb onthouden is "YOU'RE BROKE" te veranderen naar "GAME OVER".

Beta 1.3.4: Ik heb in deze commit vooral lege files verwijderd en ervoor gezorgd dat ze nergens geïmport worden en daarnaast ook nog wat cache verwijderd, that's it.

## 27-12-2025

Vandaag stond volledig in thema van playtesters zoeken, extra mechanics en het homescreen mooi maken. Ten eerste heb ik in de klasse deck een count toegevoegd die je nu kan aanzetten als je wilt. ook heb ik een rules tab gemaakt voor mensen die het spel niet kennen. en dan heb ik nog naar mijn vrienden gestuurd voor feedback.

### Beta 1.4

Vlak voor ik deze versie heb gecommit heb ik nog wat playtesters gezocht tussen mijn vrienden en familie. Voor de rest heb ik een card count mechanic toegevoegd, iets wat volgens de regels van het casino niet mag omdat je dan een grotere kans hebt op winnen, maar ik heb dit wel als optie toegevoegd gezien ik hier geen geld aan verdien. Dit is de eerste (en voorlopig ook de enige) cheat die ik toegevoegd heb.

Ik heb tot voordien alle dynamische tekst aan de linkerkant van mijn scherm gezet omdat ik niet wist hoe je iets vastzet in het midden of rechts. Vandaag wou ik echter wel de count aan de rechterkant zetten, dus heb ik opgezocht op het internet hoe zoiets moet en toen heb ik de get_rect() functie ontdekt wat ik voor elke mechanic die ik in deze commit heb toegevoegd nu gebruikt heb.

Mijn vader, die voor mij playtestte zei me dat hij de regels van blackjack eigenlijk niet goed kent, dus heb ik ook een rules knop toegevoegd aan het startscherm die een rules tab opent. De tekst zelf heb ik in een .txt-file gezet en met readlines() en een forloop op het scherm gezet heb.

Ik heb ook Global.py nog wat opgekuist waardoor bepaalde globals nu in de juiste cathegorie staan

Tot slot heb ik voor deze commit ook nog de startpagina gepimpt met een logo dat ik op canva gemaakt heb. Spijtig genoeg staat de gratis versie van canva niet toe dat je png-bestanden maakt dus ik heb dit door een online png-converter gehaald. Dit had al het wit weggehaald, ook dat van het logo, dus ik heb daarachter een witte ellips gezet waarop ik dan de png projecteerde.

### Beta 1.4.1

Na wat feedback van een playtester bleek het dat de game kan crashen als je je muis spamt tijdens de beurt van de dealer of tijdens de endscreen, dat was snel gefixt door gewoon te checken welke gamestate het was alvorens te checken welke knoppen er waren

Ook heb ik gefixt dat insurance nu alleen gevraagd wordt als de speler genoeg geld heeft.
Daarnaast heb ik mijn logboek ook eindelijk van een lokaal .txt-file naar een .md-file overgezet.

Omdat het rood van het logo niet hetzelfde was als het rood van de knoppen en het verliesscherm, en die laatste twee veel makkelijker aan te passen waren heb ik dus de knoppen en het verliesscherm dezelfde tint rood gemaakt als in het logo.

En tot slot heb ik ook een "back to menu" knop toegevoegd aan het betting-scherm zodat je de regels nog eens kan lezen of de cheats aan of uit kan zetten

### Beta 1.4.2

In deze versie heb ik nog een icoontje gedesigned voor de card count dat nu ook rechts vaststaat. Omdat die wat lelijk was op WIDTH-10 en mooier op WIDTH-8 heb ik ook alle andere icoontjes op afstand 8 ipv 10 van de rand van het scherm gezet. Tot slot heb ik alle backslashes naar forwardslashes veranderd zodat linux-gebruikers ook mijn programma kunnen gebruiken.

## 28-12-2025

Vandaag heb ik voornamelijk muziek toegevoegd, en daarbij heb ik nog wat leuke animations geïmplementeerd. Het wordt echt wel tijd om het project af te ronden. Waarschijnlijk zijn alle commits hierna wel Pre-releases en uiteindelijk de full release.

### Beta 1.5

Vandaag heb ik muziek toegevoegd aan mijn game, Smooth jazz leek me zeer toepasselijk want dat geeft een rustige casinosfeer. Natuurlijk heb ik ook een mechanic toegevoegd om die uit te zetten en dus ook op piskel nog 2 pictogrammetjes toegevoegd. Wel bleek dat je images niet als knoppen kunt toevoegen, dus heb ik achter de image een rectangle getekend in de kleur van de achtergrond. Ik heb deze dan sowieso op het einde van de lijst gezet en altijd actief, zodat ik gewoon button_list[-1].collidepoint(event.pos) kon doen op elk moment.

### Beta 1.5.1

In deze commit heb ik nog een animation toegevoegd voor de muntjes als je een bet plaatst, het is de bedoeling om daar nog een ander prentje voor te zetten en dit ook te doen voor insurance, maar voor nu werkt het.

Daarnaast heb ik nog wat backslashes vervangen voor slashes en mijn logboek geüpdated.

### Beta 1.5.2

Wat ik gezegd heb dat ik nog wou in Beta 1.5.2 heb ik gedaan, ik heb mijn coinsprite gebaseert op de muntjes van mario bros (met de streep in het midden), voor de rest verliep alles redelijk vlot.

Er waren ook nog enkele witte pixels aan de buitenkand van het logo, die heb ik weggedaan door de witte ellips 2px kleiner te maken aan elke kant

### Beta 1.5.3

Ik heb nog een paar QOL-veranderingen gedaan zoals bet_prevent afzetten eens je op BET drukt en andere kleine details. Maar wat ik ook heb toegevoegd is een coinfest als je een ronde wint en dubbel coinfest bij een blackjack. dat betekent dat op het endscreen gewoon heel veel muntjes verschijnen. Wel volledig dezelfde animatie als bij de BET en insurance maar het maakt winnen wel veel leuker. Ik liet de muntjes op een random x-waarde starten, wat niet heel gemakkelijk was, maar snel op te lossen met een nieuwe global lijst.

### Pre-release 2

Hier heb ik een soft-lock als je 10 coins hebt opgelost, en een bug dat de muziek niet vanaf het begin begint. Kleine update, weinig werk, maar we zijn nu wel echt klaar voor de pre-release stage.
