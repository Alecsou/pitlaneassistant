def teamID(id):
    match (id):
        case 0:
            return "Mercedes"
        case 1:
            return "Ferrari"
        case 2:
            return "Red Bull Racing"
        case 3:
            return "Williams"
        case 4:
            return "Aston Martin"
        case 5:
            return "Alpine"
        case 6:
            return "Alpha Tauri"
        case 7:
            return "Haas"
        case 8:
            return "McLaren"
        case 9:
            return "Alfa Romeo"
        case 85:
            return "Mercedes 2020"
        case 86:
            return "Ferrari 2020"
        case 87:
            return "Red Bull 2020"
        case 88:
            return "Williams 2020"
        case 89:
            return "Racing Point 2020"
        case 90:
            return "Renault 2020"
        case 91:
            return "Alpha Tauri 2020"
        case 92:
            return "Haas 2020"
        case 93:
            return "McLaren 2020"
        case 94:
            return "Alfa Romeo 2020"
        case 95:
            return "Aston Martin DB11 V12"
        case 96:
            return "Aston Martin Vantage F1 Edition"
        case 97:
            return "Aston Martin Vantage Safety Car"
        case 98:
            return "Ferrari F8 Tributo"
        case 99:
            return "Ferrari Roma"
        case 100:
            return "McLaren 720S"
        case 101:
            return "McLaren Artura"
        case 102:
            return "Mercedes AMG GT Black Series Safety Car"
        case 103:
            return "Mercedes AMG GTR Pro"
        case 104:
            return "F1 Custom Team"
        case 106:
            return "Prema 2021"
        case 107:
            return "Uni-Virtuosi 2021"
        case 108:
            return "Carlin 2021"
        case 109:
            return "Hitech 2021"
        case 110:
            return "Art GP 2021"
        case 111:
            return "MP Motorsport 2021"
        case 112:
            return "Charouz 2021"
        case 113:
            return "Dams 2021"
        case 114:
            return "Campos 2021"
        case 115:
            return "BWT 2021"
        case 116:
            return "Trident 2021"
        case 117:
            return "Mercedes AMG GT Black Series"
        case 118:
            return "Mercedes 2022"
        case 119:
            return "Ferrari 2022"
        case 120:
            return "Red Bull Racing 2022"
        case 121:
            return "Williams 2022"
        case 122:
            return "Aston Martin 2022"
        case 123:
            return "Alpine 2022"
        case 124:
            return "Alpha Tauri 2022"
        case 125:
            return "Haas 2022"
        case 126:
            return "McLaren 2022"
        case 127:
            return "Alfa Romeo 2022"
        case 128:
            return "Konnersport 2022"
        case 129:
            return "Konnersport"
        case 130:
            return "Prema 2022"
        case 131:
            return "Virtuosi 2022"
        case 132:
            return "Carlin 2022"
        case 133:
            return "MP Motorsport 2022"
        case 134:
            return "Charouz 2022"
        case 135:
            return "Dams 2022"
        case 136:
            return "Campos 2022"
        case 137:
            return "Van Amersfoort Racing 2022"
        case 138:
            return "Trident 2022"
        case 139:
            return "Hitech 2022"
        case 140:
            return "Art GP 2022"
        case _:
            return "Invalid ID"
        
def driverID(id):
    match(id):
        case 0:
            return "Carlos Sainz"
        case 1:
            return "Danil Kvyat"
        case 2:
            return "Daniel Ricciardo"
        case 3:
            return "Fernando Alonso"
        case 4:
            return "Felipe Massa"
        case 6:
            return "Kimi Räikkönen"
        case 7:
            return "Lewis Hamilton"
        case 9:
            return "Max Verstappen"
        case 10:
            return "Nico Hulkenberg"
        case 11:
            return "Kevin Magnussen"
        case 12:
            return "Romain Grosjean"
        case 13:
            return "Sebastian Vettel"
        case 14:
            return "Sergio Perez"
        case 15:
            return "Valtteri Bottas"
        case 17:
            return "Esteban Ocon"
        case 19:
            return "Lance Stroll"
        case 20:
            return "Aaron Barnes"
        case 21:
            return "Martin Giles"
        case 22:
            return "Alex Murray"
        case 23:
            return "Lucas Roth"
        case 24:
            return "Igor Correia"
        case 25:
            return "Sophie Levasseur"
        case 26:
            return "Jonas Schiffer"
        case 27:
            return "Alain Forest"
        case 28:
            return "Jay Letourneau"
        case 29:
            return "Esto Saari"
        case 30:
            return "Yasar Atiyeh"
        case 31:
            return "Callisto Calabresi"
        case 32:
            return "Naota Izum"
        case 33:
            return "Howard Clarke"
        case 34:
            return "Wilheim Kaufmann"
        case 35:
            return "Marie Laursen"
        case 36:
            return "Flavio Nieves"
        case 37:
            return "Peter Belousov"
        case 38:
            return "Klimek Michalski"
        case 39:
            return "Santiago Moreno"
        case 40:
            return "Benjamin Coppens"
        case 41:
            return "Noah Visser"
        case 42:
            return "Gert Waldmuller"
        case 43:
            return "Julian Quesada"
        case 44:
            return "Daniel Jones"
        case 45:
            return "Artem Markelov"
        case 46:
            return "Tadasuke Makino"
        case 47:
            return "Sean Gelael"
        case 48:
            return "Nyck De Vries"
        case 49:
            return "Jack Aitken"
        case 50:
            return "George Russell"
        case 51:
            return "Maximilian Günther"
        case 52:
            return "Nirei Fukuzumi"
        case 53:
            return "Luca Ghiotto"
        case 54:
            return "Lando Norris"
        case 55:
            return "Sérgio Sette Câmara"
        case 56:
            return "Louis Delétraz"
        case 57:
            return "Antonio Fuoco"
        case 58:
            return "Charles Leclerc"
        case 59:
            return "Pierre Gasly"
        case 62:
            return "Alexander Albon"
        case 63:
            return "Nicholas Latifi"
        case 64:
            return "Dorian Boccolacci"
        case 65:
            return "Niko Kari"
        case 66:
            return "Roberto Merhi"
        case 67:
            return "Arjun Maini"
        case 68:
            return "Alessio Lorandi"
        case 69:
            return "Ruben Meijer"
        case 70:
            return "Rashid Nair"
        case 71:
            return "Jack Tremblay"
        case 72:
            return "Devon Butler"
        case 73: 
            return "Lukas Weber"
        case 74:
            return "Antonio Giovinazzi"
        case 75:
            return "Robert Kubica"
        case 76:
            return "Alain Prost"
        case 77:
            return "Ayrton Senna"
        case 78:
            return "Nobuharu Matsushita"
        case 79:
            return "Nikita Mazepin"
        case 80:
            return "Guanyu Zhou"
        case 81:
            return "Mick Schumacher"
        case 82:
            return "Callum Ilott"
        case 83:
            return "Juan Manuel Correa"
        case 84:
            return "Jordan King"
        case 85:
            return "Mahaveer Raghunathan"
        case 86:
            return "Tatiana Calderon"
        case 87:
            return "Antoine Hubert"
        case 88:
            return "Guiliano Alesi"
        case 89:
            return "Ralph Boschung"
        case 90:
            return "Michael Schumacher"
        case 91:
            return "Dan Ticktum"
        case 92:
            return "Marcus Armstrong"
        case 93:
            return "Christian Lundgaard"
        case 94:
            return "Yuki Tsunoda"
        case 95:
            return "Jehan Daruvala"
        case 96:
            return "Gulherme Samaia"
        case 97:
            return "Pedro Piquet"
        case 98:
            return "Felipe Drugovich"
        case 99:
            return "Robert Schwartzman"
        case 100:
            return "Roy Nissany"
        case 101:
            return "Marino Sato"
        case 102:
            return "Aidan Jackson"
        case 103:
            return "Casper Akkerman"
        case 109:
            return "Jenson Button"
        case 110:
            return "David Coulthard"
        case 111:
            return "Nico Rosberg"
        case 112:
            return "Oscar Piastri"
        case 113:
            return "Liam Lawson"
        case 114:
            return "Juri Vips"
        case 115:
            return "Theo Pourchaire"
        case 116:
            return "Richard Verschoor"
        case 117:
            return "Lirim Zendeli"
        case 118:
            return "David Beckmann"
        case 121:
            return "Alession Deledda"
        case 122:
            return "Bent Viscaal"
        case 123:
            return "Enzo Fittipaldi"
        case 125:
            return "Mark Webber"
        case 126:
            return "Jacques Villeneuve"
        case 127:
            return "Callie Mayer"
        case 128:
            return "Noah Bell"
        case 129:
            return "Jake Hughes"
        case 130:
            return "Frederik Vesti"
        case 131:
            return "Olli Caldwell"
        case 132:
            return "Logan Sargeant"
        case 133:
            return "Cem Bolukbasi"
        case 134:
            return "Ayumu Iwasa"
        case 135:
            return "Clement Novalak"
        case 136:
            return "Jack Doohan"
        case 137:
            return "Amaury Cordeel"
        case 138:
            return "Dennis Hauger"
        case 139:
            return "Calan Williams"
        case 140:
            return "Jamie Chadwick"
        case 141:
            return "Kamui Kobayashi"
        case 142:
            return "Pastor Maldonado"
        case 143:
            return "Mika Hakkinen"
        case 144:
            return "Nigel Mansell"
        case _:
            return "Invalid ID"

def trackID(id):
    match(id):
        case 0:
            return "Melbourne"
        case 1:
            return "Paul Ricard"
        case 2:
            return "Shanghai"
        case 3:
            return "Sakhir"
        case 4:
            return "Catalunya"
        case 5:
            return "Monaco"
        case 6:
            return "Montreal"
        case 7:
            return "Silverstone"
        case 8:
            return "Hockenheim"
        case 9:
            return "Hungaroring"
        case 10:
            return "Spa"
        case 11:
            return "Monza"
        case 12:
            return "Singapore"
        case 13:
            return "Suzuka"
        case 14:
            return "Abu Dhabi"
        case 15:
            return "Texas"
        case 16:
            return "Brazil"
        case 17:
            return "Austria"
        case 18:
            return "Sochi"
        case 19:
            return "Mexico"
        case 20:
            return "Baku"
        case 21:
            return "Sakhir Short"
        case 22:
            return "Silverstone Short"
        case 23:
            return "Texas Short"
        case 24:
            return "Suzuka Short"
        case 25:
            return "Hanoi"
        case 26:
            return "Zandvoort"
        case 27:
            return "Imola"
        case 28:
            return "Portimão"
        case 29:
            return "Jeddah"
        case 30:
            return "Miami"
        case 31:
            return "Las Vegas"
        case 32:
            return "Losail"
        case _:
            return "Invalid ID"

def nationalityID(id):
    match(id):
        case 1:
            return "America"
        case 2:
            return "Argentina"
        case 3:
            return "Australia"
        case 4:
            return "Asutria"
        case 5:
            return "Azerbaijan"
        case 6:
            return "Bahrain"
        case 7:
            return "Belgium"
        case 8:
            return "Bolivia"
        case 9:
            return "Brazil"
        case 10:
            return "Great-Britain"
        case 11:
            return "Bulgaria"
        case 12:
            return "Cameroon"
        case 13:
            return "Canada"
        case 14:
            return "Chile"
        case 15:
            return "China"
        case 16:
            return "Colombia"
        case 17:
            return "Costa Rica"
        case 18:
            return "Croatia"
        case 19:
            return "Cyprus"
        case 20:
            return "Czech Republic"
        case 21:
            return "Danemark"
        case 22:
            return "Netherlands"
        case 23:
            return "Ecuador"
        case 24:
            return "England"
        case 25:
            return "UAE"
        case 26:
            return "Estonia"
        case 27:
            return "Finland"
        case 28:
            return "France"
        case 29:
            return "Germany"
        case 30:
            return "Ghana"
        case 31:
            return "Greece"
        case 32:
            return "Guatemala"
        case 33:
            return "Honduras"
        case 34:
            return "Hong Kong"
        case 35:
            return "Hungary"
        case 36:
            return "Iceland"
        case 37:
            return "India"
        case 38:
            return "Indonesia"
        case 39:
            return "Ireland"
        case 40:
            return "Israel"
        case 41:
            return "Italian"
        case 42:
            return "Jamaica"
        case 43:
            return "Japan"
        case 44:
            return "Jordan"
        case 45:
            return "Kuwait"
        case 46:
            return "Latvia"
        case 47:
            return "Lebanon"
        case 48:
            return "Lithuania"
        case 49:
            return "Luxembourg"
        case 50:
            return "Malaysia"
        case 51:
            return "Malta"
        case 52:
            return "Mexico"
        case 53:
            return "Monaco"
        case 54:
            return "New Zealand"
        case 55:
            return "Nicaragua"
        case 56:
            return "Northern Ireland"
        case 57:
            return "Norway"
        case 58:
            return "Oman"
        case 59:
            return "Pakistan"
        case 60:
            return "Panama"
        case 61:
            return "Paraguay"
        case 62:
            return "Peru"
        case 63:
            return "Poland"
        case 64:
            return "Portugal"
        case 65:
            return "Qatar"
        case 66:
            return "Romania"
        case 67:
            return "Russia"
        case 68:
            return "Salavador"
        case 69:
            return "Saudi Arabia"
        case 70:
            return "Scotland"
        case 71:
            return "Serbia"
        case 72:
            return "Singapore"
        case 73:
            return "Slovakia"
        case 74:
            return "Slovenia"
        case 75:
            return "South Korea"
        case 76:
            return "South Africa"
        case 77:
            return "Spain"
        case 78:
            return "Sweden"
        case 79:
            return "Switzerland"
        case 80:
            return "Thailand"
        case 81:
            return "Turkey"
        case 82:
            return "Uruguay"
        case 83:
            return "Ukraine"
        case 84:
            return "Venezuela"
        case 85:
            return "Barbados"
        case 86:
            return "Wales"
        case 87:
            return "Vietnam"
        case _:
            return "Invalid ID"

def gameModeID(id):
    match(id):
        case 0:
            return "Event Mode"
        case 3:
            return "Grand Prix"
        case 4:
            return "Grand Prix 2023"
        case 5:
            return "Time Trial"
        case 6:
            return "Splitscreen"
        case 7:
            return "Online Custom"
        case 8:
            return "Online League"
        case 11:
            return "Career Invitational"
        case 12:
            return "Championship Invitational"
        case 13:
            return "Championship"
        case 14:
            return "Online Championship"
        case 15:
            return "Online Weekly Event"
        case 17:
            return "Story Mode"
        case 19:
            return "Career 2022"
        case 20:
            return "Career 2022 Online"
        case 21:
            return "Career 2023"
        case 22:
            return "Career 2023 Online"
        case 127:
            return "Benchmark"
        case _:
            return "Invalid ID"

def rulesetID(id):
    match(id):
        case 0:
            return "Practice & Qualifying"
        case 1:
            return "Race"
        case 2:
            return "Time Trial"
        case 4:
            return "Time Attack"
        case 6:
            return "Checkpoint Challenge"
        case 8:
            return "Autocross"
        case 9:
            return "Drift"
        case 10:
            return "Average Speed Zone"
        case 11:
            return "Rival Duel"
        case _:
            return "Invalid ID"

def surfaceID(id):
    match(id):
        case 0:
            return "Tarmac"
        case 1:
            return "Rumble strip"
        case 2:
            return "Concrete"
        case 3:
            return "Rock"
        case 4:
            return "Gravel"
        case 5:
            return "Mud"
        case 6:
            return "Sand"
        case 7:
            return "Grass"
        case 8:
            return "Water"
        case 9:
            return "Cobblestone"
        case 10:
            return "Metal"
        case 11:
            return "Ridged"
        case _:
            return "Invalid ID"

def penaltyID(id):
    match(id):
        case 0:
            return "Drive through"
        case 1:
            return "Stop Go"
        case 2:
            return "Grid penalty"
        case 3:
            return "Penalty reminder"
        case 4:
            return "Time penalty"
        case 5:
            return "Warning"
        case 6:
            return "Disqualified"
        case 7:
            return "Removed from formation lap"
        case 8:
            return "Parked too long timer"
        case 9:
            return "Tyre regulations"
        case 10:
            return "This lap invalidated"
        case 11:
            return "This and next lap invalidated"
        case 12:
            return "This lap invalidated without reason"
        case 13:
            return "This and next lap invalidated without reason"
        case 14:
            return "This and previous lap invalidated"
        case 15:
            return "This and previous lap invalidated without reason"
        case 16:
            return "Retired"
        case 17:
            return "Black flag timer"
        case _:
            return "Invalid ID"

def infrigementID(id):
    match(id):
        case 0:
            return "Blocking by slow driving"
        case 1:
            return "Blocking by wrong way driving"
        case 2:
            return "Reversing off the start line"
        case 3:
            return "Big Collision"
        case 4:
            return "Small Collision"
        case 5:
            return "Collision failed to hand back position single"
        case 6:
            return "Collision failed to hand back position multiple"
        case 7:
            return "Corner cutting gained time"
        case 8:
            return "Corner cutting overtake single"
        case 9:
            return "Corner cutting overtake multiple"
        case 10:
            return "Crossed pit exit lane"
        case 11:
            return "Ignoring blue flags"
        case 12:
            return "Ignoring yellow flags"
        case 13:
            return "Ignoring drive through"
        case 14:
            return "Too many drive through"
        case 15:
            return "Drive through reminder serve within n laps"
        case 16:
            return "Drive through reminder serve this lap"
        case 17:
            return "Pit lane speeding"
        case 18:
            return "Parked for too long"
        case 19:
            return "Ignoring tyre regulations"
        case 20:
            return "Too many penalties"
        case 21:
            return "Multiple warnings"
        case 22:
            return "Approaching disqualification"
        case 23:
            return "Tyre regulations select single"
        case 24:
            return "Tyre regulations select multiple"
        case 24:
            return "Lap invalidated corner cutting"
        case 26:
            return "Lap invalidated running wide"
        case 27:
            return "Corner cutting ran wide gained time minor"
        case 28:
            return "Corner cutting ran wide gained time significant"
        case 29:
            return "Corner cutting ran wide gained time extreme"
        case 30:
            return "Lap invalidated wall riding"
        case 31:
            return "Lap invalidated flashback used"
        case 32:
            return "Lap invalidated reset to track"
        case 33:
            return "Blocking the pitlane"
        case 34:
            return "Jump start"
        case 35:
            return "Safety car to car collision"
        case 36:
            return "Safety car illegal overtake"
        case 37:
            return "Safety car exceeding allowed pace"
        case 38:
            return "Virtual safety car falling too far back"
        case 39:
            return "Formation lap below allowed speed"
        case 40:
            return "Formation lap parking"
        case 41:
            return "Retired mechanical failure"
        case 42:
            return "Retired terminally damaged"
        case 43:
            return "Safety car falling too far back"
        case 44:
            return "Black flag timer"
        case 45:
            return "Unserved stop go penalty"
        case 46:
            return "Unserved drive through penalty"
        case 47:
            return "Engine component change"
        case 48:
            return "Gearbox change"
        case 49:
            return "Parc Fermé change"
        case 50:
            return "League grid penalty"
        case 51:
            return "Retry penalty"
        case 52:
            return "Illegal time gain"
        case 53:
            return "Mandatory pitstop"
        case 54:
            return "Attribute assigned"
        case _:
            return "Invalid ID"

