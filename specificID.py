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

## FLAG IDS CORRESPOND TO TRACK IDS
def trackFlagsID(id):
     match(id):
        case 0:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAeAAAADwBAMAAAAqW6qJAAAAJ1BMVEX///8BIWnkACvsQ2MsRoKnsstCWpD5wcvAyNp3iK/i5u4QLnL60NhIl/THAAAJAklEQVR42u3dz2sbRxQH8G/ANrJy8QNJSNpb/olcerCghCS9WNCW/LhI0IQ61/4DMqSBJBcJklBHlzUkIU4vNtQmco/9x3pYydaP3Zl5b1az2t2ZS2KQ1vvxjmY1s++9wV3Mte0O6RsA3JlrAGDwttoBgP9mb7pLGTXcYYtl4CUvsgOzxSLwsjdLMFcsAa94MwUzxQLwqjdbME/MB8d4MwazxGxwnDdrMEfMBcd6MwczxExwvDc78B9sMQ+c4M0OzBezwEneDMFsMQec6M0SzBUzwMne7MADttgcrPBWMgM32GJjsMrbzwxMbLEpeCO9BGKLDcGb6SUQW2wG3lAvgdhiI/CmeiMwT2wC3ljvFMwSG4A31zsDc8R68AZ7r8EMsRa8yd4bsLlYB167t9FPBWws1oDXf31bo3TApmI12EF/bp+kBDYUK8EuPr/7W2mBzcQqsJPxaribGthIrAC7GZ/DSnpgE3EyeO3eyTkRBUCHiGicCthAnAhe//Wtb3eIWsCIqHbQTQesFyeBXfTnsDKmJnBEk0H1PCWwVpwAdvL57QG/ngG3nwE7lBZYJ44Huxmv6gBCoAqgmx5YI44Fq7wdSq+Fs6MKezQlLL+pxHFgV17qzQ67Q2mCleI4sCsv1WfH7aYLVonjwK68FIR2PZqSH5IoxatgN97otGwODBKJV8COvMFwduhd6aAlazFdmtlkp/vi5gBfygC+P3+El8UHXyweYlx08GzAshoh8tWl/3l+/Ch6+y/Hz38qw6BFFERvl96G8weuRW/vlAZ8CVRDQDwBWzh1l028KA18egiMSgOuA52afO6QP3ATW0Q9HJUG3EafqIGT0oD3doiIerdKA94fERG1tkoDPoz++VAWcDD9ilUrzRW2bR7swR7swR7swR7swR7swR7swR7swXlciNesWpcN/KJs4GGnZOBwVC5wTb9AXyxwC1ulAb+LHjztEqnzfAoD3n9FRGeoENHkmyI+QBOYdt2uI9R+0IAXXph6YJrqMepph4bAOT1TBp5C5FVd4azEISr9ATD+qH54nARuKL3KLp2ReBpYHGoCT8H2JoYPr778rkvxdWCxOpQabG9ygHjG4tAolBpsryIFIFtxzyg5AGyvKskjU3HdKDkAbK8yjSdL8UQI1nnViVrpiCUp0Y3QKK4YbK8mFS8VcX3E9s5/bxgzwHqvLtkyDTE/JfomNwBAtW8MNvBq02lTEPNToj+aRlKD7dUnTNuL2SnRF+Hit71TM7CR1yAlPkFsPhIJUqJ/PHz/JLq6jz/8ZjhbMvOaFD2QiyfnRFSL4qEDZlJDM8rvocBwlDb0GpW1EIsnFinR7SnY8D5s6jUrXCIVBxYp0XtABdg2BBt7DUvTSMUWKdH7wGigq7YHtte0+JBQbJES3cMuNXWLR2B7jctLCcXylOghuhSEmoQXsL3mBcRkYnlK9HCbiK40CS9gexkl4kRieUr0oEtEQdjXgnleThFAkVicEv2ViIgejnRgppdV5lEglqdEv43e39WAuV5eIU+2WJ4SPYsd1wxabC+zVCtXbJ8Srbktsb3cYrwJ4oTzSSElmvEwzcjLLrccL9YtLstTos3BZl5+Qe1YscHznbWs/vG9gpLpceKE16eQEm0KNvVKiuLHiBWjrWVKtCHY2Cva9mD11yjeYJkSbQY298o2tlgRKxaYLVOijcAMr3DrkmVx8sttU6JNwByvdHOaJbFy9mCVEm0AZnnF2w8tilVrcTtE+/KUaP3Z87zyDaYWxKq1OLuUaO3ZM70WW4jNixVrcTtEFMhTonVnz/XabBI3J1asxY2IbFKiNWfP9lptA3gjTn6hbUq06br0xrTpH90sJbrWyT+Y1erdkoHPbpUMzH6wmnfwoFIucIM9q8ozOLh3+BfwWvn8u1Dg77Ob+tuyXOHpV5ntoCyf4VYEHpXlMzxdteet1+cbfAlw14LyDW6xe3TOwU0AzKWRfIPPUBngdonAveqoFe6UCDx8SnSxWx5w8I6I6EGpZkvs5sEe7MEeXBpwrVMysNWGi3kEN49KBt7fKhnYasPFPIIHlXKBg7XFUm0ouLW2SJsNBTeBo1KBz8BcXck7eKhNeysYeKBNeysWOFhjyOvmgPsLg/TCqn+jkOCP767/W19MpnpwWkjwd7ye9eI9YG6Y/isvtygmuAZ8nnbj3lx+YONgbQHdWQ9aQ6Aa5ZocALNhehLm5w7FBbcB4BXRLNKaiOh3AOsKfs0cHCUkfO5TIwL3qfZknSkK2d+Ho9TA6niaUtWdhCalBnIMbk8jZ95E/3yd/nhSWHAtvmpjp7DghSo/1y0/swj+d+mrOPBJgcG1XPdoyWzpIM89WgJur4L/LjS4sQruFxq82qfztPAhAbdz3KNF4EaOe7QIHCwVoOPXVMkZ+OPyFT4tNvj+6ij9ssjgi7hvWk+LC26FceDqqKjgRhg/Paz2iwkODpK2Mdg+LyR4mLxxg7sJRKPvDPxCtVXFF1dgq3ApFvi+enOOnx2B2yeOwBPddiRjN2CrcCkG+DLUgR0N1VbhUgxwcO/w/aNvSdhvfz7mpXnKW1hxNmgRUe3e8fs3C9e6+vXxsSPq5JyIgukS2tgNmIiWKrl1iXSlBtNqdYtizFbg5grYUbMoxmwFbme1Jm1RjNkKvDcPvuUQbFGM2Qq8Pw92GkQc2i6zQNqzYLa90Rr6tN1vlYGjOcTu0P1jh7rtUGkD7tbdg4PQcuFQBp4FtBw4X4aXF2O2AofTTlUHgKrLCywuxmwHxqx+8GB9+67qJuRfHIKD69T7724jTFMoxiwCNwBUzomIgoHLJy0XKUy/ReDWzQO0K7jLfEilGLMUPLstBKHLVI8UijGLwPW5J6RXbqdL1sWYReAmqte9qRa6DRy2LcYsArfx6eaHh25jli4tizGLwGfzf+CG22Qe22LMIvD+wlSl53R+aFuMWQTuLXSohtP5YRNbRD35uCEKeVgqG3voEmxbjFl0hZfuCf+6BO/tEBHJizHnrsqDbTHm3IFtizHnDTzbY6hWmits2zzYgz3Ygz3Ygz3Ygz3Ygz3Ygz3Ygz3Ygz3Ygz3Ygz040/Y/Rl8xdhTSHS0AAAAASUVORK5CYII="
        case 1:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWgAAADwAgMAAABQyRbcAAAACVBMVEUAI5XtKTn///+i/AH+AAAAaUlEQVR42u3MMQEAAAgDoJW0pCltsMsTApBUW00VtVqtVqvVarVarVar1Wq1Wq1Wq9VqtVqtVqvVarVarVar1Wq1Wq1Wq9VqtVqtVqvVarVarVar1Wq1Wq1Wq9VqtVqtVqvVarVarf6sD3KNBYUV+OhWAAAAAElFTkSuQmCC"
        case 2:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWgAAADwBAMAAADfieN8AAAAJFBMVEXuHCX//wDvLSHxQh71dRb3jRL/9gHzXBr80gb7vwr+5QP5qA0/BOFSAAAD1klEQVQYGe3Bv2sbdxwG4JfTyZKi6dWPs3RaTpS2xNO5Q+J6kkrJ4EmKaTpkyRWDyXYOJSGdrDgNhS6WIUsnq4amdJJIhv55/epsgmX77rSU733g8zxQSimllFL/qwHkqc8hz3gEScoxAJcDSFLyHwMPGEOUhfexFDGEKFvkH2QAUVwuQZgJSS+ELNs0ujFEqXHJf4yiKYVIdcSE9xEFUx4hTSli4vfvUDDVY6TZouG9f4HC6TeQwpnROEQBjdtIUaX/acFNFNCkgxT/fgrwFTdRPA4Z4E5OAMBlE8XjkgNkmDRQPFXyGBmOnqF4+mQDGernKJ4h2UIG5xTFMyW7yBKicBwaAWRxaQywhm9QGDUap1jDVoCi6NNoYA0bb7AUwL4hjRbWUO0EAL4NYd+URhdrqPEN8LoL+5yIhoc1lNkJXrMJ+1wmBsjnkn+Tc9hXY2KOfBUaXgD7Nph4hnwOjTYK4IiJTeTbo/ETCmDBRA+59rh0jAKImPCQZ4+JLuwYM0cbt/3CK6ewojJjJj/GHR4+fcelHuy4z0xnSHHEpTnseMQMB0jTZ+fV03c92FGaMVUnRJoNbgJ4GMKOOlPNkarKY9j0kikOka7GEDY5E96pGyBduQu7yrzTCBncJizb5R0ukKUyh2XOgrf0AmRxAtjmRrzBi1F4O7zhBAKMuaINCSozXuPHEGGb1zQhw5jXtCHDjNd0IEKJK0JIUOaKESSocsUxJOhzRQMSjLmiDQkmXNFBngqsc3jJi3gpQI57AWwr89LJDi8NkGN7BNuqTLSBMRPHyDE8h219LvkxUJlxqYEc0yZsG3LpDMZ9LrWQI+rBtimNAyQe0egiW4UeLHNodEIkShMaATLVyRh2uTTmuFKnMUCqr3/+/ocnZPe3f/6aw54ayQ/47CXJU6QqR7xyAIv6ZDfAZ86UbCDdDi/5ISwa0hvhmjLZQoYnTJzBpikvsGKXXWQoTWi0YZMT9QKscBYestRpjGCT68W4wY0GyFCncQ6b6ie4ZWeODPdoNGHTl7jDCBm26c3YgyxDXpTpQZZpN8AuY4gSjQBnPIcklUMYpT8hiRtgyYFS0rkh5HkQQhxnFkCSL2BUGUCS2tsAWBCiONHz2KUHWYb0F/QhS42GD1mciKQfQ5YhDX8folSZeBtAkG1e+gA5nBmXnu9DkCqNzo8QZUGjDVFceu/HbEOUo19jVNmCKC8AlKIW5Bm3IE91E/KUNiHQPgRyoJRSSimllFJKKaWUUkoppZRSSimllFJKKaWUUkoppZRSSimllFJKKaWUUkoppZRSSimllFIi/AdA6aWV/UhmKAAAAABJRU5ErkJggg=="
        case 3:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZAAAADwBAMAAADcEi8RAAAAGFBMVEX////aKRzbMybpfnb+9fT41tThU0nwqaQIATu+AAACEUlEQVR42u3aUVEAMRAE0XyAACRgARMIQAEm0I8GLktlMvXioKsyd7uTXuvP5+v9LfCsB+fzuwRkvX6UgKyXnxKQwKA8BYkLymOQtKA8BwkLyto5SUHZAkkKyh5IUFA2QXKCsrZPSFD2QUKCMgCSEZQJkIigrJlzPihDIOeDMgVyPChjIKeDsgbP0aBMghwNyijIyaDMghwMCpDqq9US9pLPb8sPsWVEaRkaS8b4lsWqZdVtKR9K6qCWgq6lMm0psUueFVoeelqe3loeQ0uep1uEgRaFo0WqqdGc+FrC7vPL1zI0GuMtVnwtdZCCjq91PwhfKxCEr5UHwtcKBOFr5YHwtVwtYedrGVEMjXwtq67yQR3E11Jie1bga90LwteKAuFrZYHwtYC4WnwtP0QjiqGRr2XVVT7wtVSmSuxhEL5WIAhfKw+ErxUIwtfKA+FruVrCztcyohga+VpWXeWDOoivpcT2rMDXuheErxUFwtfKAuFrAXG1+Fp+iEYUQyNfy6qrfOBrqUyV2MMgfK1AEL5WHghfKxCEr5UHwtdytYSdr2VEMTTytay6ygd1EF9Lie1Zga91LwhfKwqEr5UFwtcC4mrxtfwQjSiGRr6WVVf5wNdSmSqxh0H4WoEgfK08EL5WIAhfKw+Er+VqCTtfy4hiaORrWXWVD+ogvpYS27MCX+teEL5WFAhfKwuEr/Wf5xfMlsQlQg0JfwAAAABJRU5ErkJggg=="
        case 4:
            return "data:image/png;base64,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"
        case 5:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAADwAQMAAACAOMvWAAAABlBMVEXOESb///9W4q7JAAAAL0lEQVRo3u3KMQEAAAgDoPVPawOtsF+4SQAAAACgsI3RNE3TNE3TNE3TNE3TnrcDTcy4KA2FVlQAAAAASUVORK5CYII="
        case 6:
            return "data:image/png;base64,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"
        case 7:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAeAAAADwBAMAAAAqW6qJAAAAHlBMVEUBIWnIEC7////XUGaHl7kUMnTxw8r29/rw8vf219zf67YoAAAEnklEQVR42u3dzXHbUAwEYLSgFnhxKvBMCvA9B3WQDlJCWkjD8Y/k2FYkPgC7+17ixVUzJL9ZiqODiI377drcPQRozkc8XJnz56jzHX+cDvjr4lT3cbgu3h7+TfAt7xaHAz9jLfim9wnMz1gKvu19BtMzVoJ3vC9gdsZC8J73BCZnrAPves9gbsYy8L73FUzNWAUe8P4BMzMWgUe8b8DEjDXgIe9bME8sAY9534FpYgV40PsezBILwKPeD2CSmA8e9n4Ec8R08Lj3AkwRs8EJ7yWYISaDM94tvgvEXHDKu8UmEFPBOe8jWCBmgpPeJ3BKXPpdTQQft5z3GUzPmAfO5nsCs8U0cN57ApPFLHDBewZzxSRwxbvFT4GYAy55v8RRIKaAa97HCxeIGeCyVyEmgBtegRgPbnn5Yji46aWL0eC2ly0GgwFeshgLhni5YigY5KWKkWCYlykGgoFeohgHhnp5YhgY7KWJUWC4lyUGgQlekhgDpng5YgiY5KWIEWCalyEGgIlegrgPpnrx4jaY7IWLu2C6Fy1uggVesLgHlnix4hZY5IWKO2CZFylugIVeoLgOlnpx4jJY7IWJq2C5FyUugid4QeIaeIoXIy6BJ3kh4gp4mhchLoAnegHiPHiqty9Ogyd72+IseLq3KH69hCR4AW9TnAMv4e2JU+BFvC1xBryMtyNOgF9PMt/bEI+Dl/LWxcPgxbxl8Sh4OW9VPApez1sUj4IX9PbEY+C1vC3xEHg1b0c8Al7P2xAPgFf01sX7YIF3E87gU5o6BhtssMEGG2ywwQYbbLDBBhu8/W291H8+BhtssMEGG2ywwQYbbLDBBhtssMEGG2ywwQYbbLDBBhtssMEGG2ywwQYbbLDBBhtssMEGG2zw5wH7H/EGG2ywwQYbbLDBBhtssMEGf0Zwa4HY5VyuFPvaA1/fUTZhYVrSW0t4vrjsLd7Ss8V1b/U7PFfc8JYfWjPFHW/9KT1PXPKml/GuI6558+uWVxEXvYWF2muIq97KyvQVxGVvaSn+fHHdm6s9WEXc8CaLLdYQl7x3teqSFcQtb7qcZr64563XD80SN72Ngqk54q63UyE2Q9z2tkri9OK+t1cDqBYDvM2iR60Y4e1WeSrFEG+7rFUnxnj7dbwqMcgLKFzWiFFeRKW2QgzzQkrT+WKctwPWiYHeFlglRnp7YI0Y6m2CFWKstwvmi8HeNpgtRnv7YK4Y7gWAmWK8FwHmiQleCJglZngxYI6Y4gWBGWKOFwXGi0leGBgtZnlxYKyY5gWCkWKeFwnGiYleKBglZnqxYIyY6gWDEWKuFw3ui8leOLgrZnvx4J6Y7iWAO2K+lwGuiwVeCrgsFng54KI4BF4SuCYOgZcFLolD4KWBK+IQeHnggjgEXiI4jtk3Q0LgZYLTGYfASwVnxSHwcsFJcQi8ZHBOHAIvG5wSh8BLB2fEIfDywQlxCLwC8Lg4BF4FeFgcAq8EPCoOgVcDHhSHwCsCj4lD4FWBh8Qh8MrAI+IQeHXgb/viEHh14IGMQ+BVgnczDoFXCd7NOAReLXgn4xB4teCdjOPGfhXY66li8E3xb5DUNA2PqEXYAAAAAElFTkSuQmCC"
        case 8:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZAAAADwAgMAAABTUtqxAAAACVBMVEUAAADdAAD/zgDGIigcAAAAX0lEQVR42u3NMREAAAgEIEta0pSW8FweClAFAAAAAAAAAJzrBxKJRCKRSCQSiUQikUgkEolEIpFIJBKJRCKRpCXzQCKRSCQSiUQikUgkEolEIpFIJBKJRCKRSCSSsGQBFHUikiYoaNsAAAAASUVORK5CYII="
        case 9:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAeAAAADwAgMAAAClG18pAAAACVBMVEVHcFDOKTn////cu1yhAAAAbElEQVR42u3NMQEAAAgDIEta0pTeS6AHFKD6SInFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxOOI5IhaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8XijAEAAAAAAAAAAHhhAZgkXKw2b78MAAAAAElFTkSuQmCC"
        case 10:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARUAAADwBAMAAADcPu1UAAAAD1BMVEXvM0AAAAD92iWokRj5oS3UtkJ/AAAAp0lEQVR42u3OQQ0AMAgEMCxgAQlTMP+q0HBPklZBqyNvEr8yLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4u5y4LjuLi2VmYCrEAAAAASUVORK5CYII="
        case 11:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWgAAADwAgMAAABQyRbcAAAACVBMVEXOKzcAkkb///8vuYFFAAAAaUlEQVR42u3MMQEAAAgDoJW0pCltsMsTApCptkqnVqvVarVarVar1Wq1Wq1Wq9VqtVqtVqvVarVarVar1Wq1Wq1Wq9VqtVqtVqvVarVarVar1Wq1Wq1Wq9VqtVqtVqvVarVarVar1Z/1AeDdBYVnrJzbAAAAAElFTkSuQmCC"
        case 12:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWgAAADwBAMAAADfieN8AAAAG1BMVEXtKTn////3mJ/94ePvQU/xWmf6v8TtKDj0e4VnwWi7AAAEo0lEQVR42u2bv2/TQBTHX9NLXkYupqEjMaVzDQ1zAmpnQ0BijEtAjCcImDEGwd/NkPjss+9aQEJ+lr7fpY2T4ZPL996vs4kgCIIgCIIgqEe6el3+Z0wvgF+dv9Na62c3j9kYQ0TMLBx5+EgfND2rrspe7ldJyXyzqK8v92OZm5hSF1vNSuZo117aXCT21jLrne/9XCL0yjJv/B8QSD2yzKfOdU4Fb0IbN6KF+8ZDudCFXegG5OBCbAgJmYPo+ETqOm8zC92wML+cSIV+YZkvm2/NIqnQSWihiRItNHxUjj5ppkLV2plSFHD0lyQUUgRoYNncTZfbX2DO4sLeSwu9boSOQ/SeyitNVSgZEm2TcAHVrb4GE8vBOZeiM/i6ZVjV3oUyrFLFiEXrvbHWWl9Qb2LHvvLQWuv74jovXlpoz4ou9eSHFlh93NplFVGqskb1IcDUW8tcsSmLn22IPlVefyjY0oMyyagJEfGqZB1eCDH1sYWu9tvoXkmZEhHbBR5IaQh8OXx56nfx0USIqWeeSq6YBr5gJATal1oyHfqCCxnVki946EC3kgipq5vBYxjH8bnWT+I4dsK2iuM4Lq93HT5qndber9bj08CGnS46hz6y0A8MERHbHmsXqLoFOKQd8UaBWcLBSHMB4aNoh+kiUPGtDubovsbzhOlhoHhStk/oeqU9Nd444Nyh/T26hs7a0KNAbf3JFihyoNMqoESJPvGWVsm+9+0a2pPFC70Z+DbiUl+O99G7a2jLXJUb2aktjVz7T4hW++/WbXbxlR5RSqSyVvXBSUpksp1I6PGaiWjQCh9qQ0T0bS2gd2nbY7v/00oiioiIcwH2uHVS481GsqJH+hd5VF6clg99x4G4TM3+5YRCTmnaS+h1b6Dz8Mz0m8t5JQeam41trVFxX36v/d91YxscqfPMzTbvBEH7KqZD2nFjoKjT5lAeV+7OHIs6tA0F6oF71DKqbdTuB5Ch49rP7qniUW2jdg/tG6rvm6upG88lHRf5wscL99qqcaRrOof2ho/S6FFKRKSy0Nm5qDqvvOFtUxvfiLrrw5vIr/duYFP3y1yiqU8bhVTNDTMhs0drau/tHkt3rF74B6nCSurCmd9w5snzQiL1SaN33LmTBkH28Aa9rdZnWZUjhzp6k8i6ZczTvYz1nAf6XlV5bGgkYzZ9S/wYTZnzlX15PCHKi/sy0mFw+HG0M8TmQ0m4Sg3x9iOJ3or8moiIv5QfSA0R01AUdDtUi3xqodGT33Irsljx9p9Geh3LhCcJkvVHMz1pTxVVj4xIKubu0rVd6nmPDPLjrsegJD4pp3o5X68/2id/E1pq+xClPuvNUufmuU0yT5wkk8t9XpUNqV/WIu9r143oxeZcvT1/qvXTm58LY5iJmPtQPRGbYVqGNza9MTcTBEEQBEEQBP1v6R4K0IAGNKABDWhAAxrQgAY0oAENaEADGtCABjSgAQ1oQAMa0IAGNKABDWhAAxrQgAY0oAENaEADGtCABjSgAQ1oQAMa0IAGNKABDWhAAxrQgAY0oAENaEADGtCABjSgAQ1oQAMa0IAGNKABDWhAAxrQgAZ0p/oNj6ldKYt/L5cAAAAASUVORK5CYII="
        case 13:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWgAAADwBAMAAADfieN8AAAAIVBMVEW8AC3////RT23acovBEjvHKk/66+722uHww87qrrzjlademFPnAAADvElEQVR42u3dz08TQRQH8Ge7lR8npg3dwqkNoteWiFFPi8aIngoIerQqB2+s8aKnNurFE0SjV4gm+meqnAxCuzvzeG+efL9/QPtJs53dmXnzlpzBENBAAw000EADDTTQQAMNNNBAAw000EADDTTQQAMNNNBAAw000EADDTTQrEk/LW8/ypJ725u3ciPot6sZJXSchJKtHwbQL1fpRLa+RI7+l3webF70uz6dmtrNaNHpKp2ZrTxOdNqlManmMaLTNo1NJY8P3Zpg/q0exYZuTjT/Vg8iQ3+mAnkQF/oVFcq1mNCLWTF0chQPusgFzXlZs6A/UOE8jgW9SCVyFAm6XQZdiQO9W8ZMyU4M6LRfCk21PAL0eyqZdX30IpXOgTp6vzx6Rhu9QCT/U4eihz7odV10mvmgk1wV/YK8sqOK7vuha5roBnmmp4je90VP66GbmS86Gaih6+Sdjhq664+uaqFbFJBcCT0fgu4ooQ9D0LM6aP+xI3T8CEA3KCg9FfQwDD2lgm6HoSsa6JQCkyug66HojgJ6LxR9WQHdDUVX5dFNCs5AHN0IR/fE0fPh6A1x9DAcPS2O7oajq+LoLBydSKMXiCEHwug6B7ojjJ7jQK8Jo4cc6GlhdJcDXRVGtznQFWE0sUQW3eJBj0TRDR50TxRd50F3RNHzPOgNUfQcD/qSKHqPBz0lit7nQc+Iog950LOi6C4PuiqKbvOgK0BPSp8HXQNaYFprFp2IookpQP+XlweGPKDx7BEB2uSjqclJgMnplsmJrcklBJOLNSaXxUwuQJpc6jW5qG5z+8LkRpHJLbk5xXvLxdpmNrmhb7J0gmPMky9SMVkOxPCctyaONlniZrKY0GTZpntqsUA29J6YaJQimyz6NlleH7r2oXOQweSREZOHc8JWIUMOj4eggwY9rQNnqc6AdwEPUdo8rmryYLD/9EXxCLbNw+6+m6CB3XYC0bt+aN0GDiZbZZhsSuK3PDZSRptstOPT0uhIHV2sJyHrD82AbpUcQJJRBGj3uhz6vosB3Sx1W6wNokC752XQN1wc6DL/RZYuoRe3caXJFqHOPSuGvupiQhfrEvrExYV23yebH7rY0M3rk8x3B9GhJ6r5zJztycerGc2sjeDHqTnN3C33zxivk3hb7v+ZfZ16b6wcuJjRzn28cpJ85yf3d5zHCztW/npWrS1ZeGHHcd58W1nOks2l21/P5ePxEhqggQYaaKCBBhpooIEGGmiggQYaaKCBBhpooIEGGmiggQYaaKCBBhpoW/kFyKVe015rhv4AAAAASUVORK5CYII="
        case 14:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAeAAAADwAgMAAAClG18pAAAADFBMVEUAAAAAcy//AAD////KuWVOAAAAiUlEQVR42u3NoQ0AIBAEsFuSJVkSLIrkxbl2gWZ/rZqIxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisXgQnxqxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFk/i9IjFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKx+HUBrtYLCaJhKmYAAAAASUVORK5CYII="
        case 15:
            return "data:image/png;base64,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"
        case 16:
            return "data:image/png;base64,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"
        case 17:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWgAAADwAQMAAAAXaWwMAAAABlBMVEXIEC7///94b0yLAAAAMElEQVRo3u3KsQ0AAAgDoP7/tF7gYNIRZhIAAAAomA/btm3btm3btm3bPjYAAAAULKW1AsPybBZ7AAAAAElFTkSuQmCC"
        case 18:
            return "data:image/png;base64,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"
        case 19:
            return "data:image/png;base64,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"
        case 20:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAeAAAADwBAMAAAAqW6qJAAAAG1BMVEXvM0BQni8AteL////0dH3+6Or4nKP6v8TyUl0yrdN2AAAC4ElEQVR42u3cvW7bQAzAcQI5O1rzCn0CA/RHRgFG7YwBLhU6FpCNZDSgIlkFNG1fu4NlKY2lU9rN5J+j5eVnnXjU3dHyyVkIYMCAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYFNggiCIj8fr5iUuXnZ3TrjZXpsoag/ebdQ2Ft/tez/rX1E485oX/9azeLDsnXbO1e6uzl43leo3w+DqPFtt48Jurv7ZevPuwxC/WvWGPq9IiLlRcNnrFQmF8Rt8eH/l2uYt/tF4l+eXnkyCTyVlz+0MFr3Xjbc3J1ucmU5zcK8ts5uy5on3xtriiE4UklNTRea6KaETX5ncG8zRqTJyfWvwEU6N2nJpCDxpqsrUd9JXL/MRHsjRz80gyEVEHi3NwgNpaV0c8/hBRPZzE+DhsvI44AuRK9WZyF5N5OqQfoSD6rJeq86zcvBHuayYjszCUXVZqa5KNZK5JiN1Zdmt7tmYm5p34dnQ9asOPLM0Kx1GhvxYaXI5UY5gsg4sLsDdQ2ykvKyS07BIaJfoV7kHsL0t1JhY3nmzQ25nnzwmEtKv+H5DcXH5y7bqDexuSLtLWu6mJXeFxz+UlrUJsLuXB3evh+4WANwt8bhbxDuVWvnQiLe2TOtvId7dVstHNtOipc20oCPVtIhUlrZLRx7iY3UytwR2d+TB3aGWzNuxpbZc7lUZPJjm7+ihu8OlbQOAm+PD7g6Iu2sB8Nfk0bXxvF18NtzG469Rq78V7yCGY+us2dJfO62/hml/LfEiofvTg1x8RLZ5jF+ed7UQBEH8X9w4C8CAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYMCAAQMGDBgwYMCm4g9jtexJG+tzvwAAAABJRU5ErkJggg=="
        case 21:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZAAAADwBAMAAADcEi8RAAAAGFBMVEX////aKRzbMybpfnb+9fT41tThU0nwqaQIATu+AAACEUlEQVR42u3aUVEAMRAE0XyAACRgARMIQAEm0I8GLktlMvXioKsyd7uTXuvP5+v9LfCsB+fzuwRkvX6UgKyXnxKQwKA8BYkLymOQtKA8BwkLyto5SUHZAkkKyh5IUFA2QXKCsrZPSFD2QUKCMgCSEZQJkIigrJlzPihDIOeDMgVyPChjIKeDsgbP0aBMghwNyijIyaDMghwMCpDqq9US9pLPb8sPsWVEaRkaS8b4lsWqZdVtKR9K6qCWgq6lMm0psUueFVoeelqe3loeQ0uep1uEgRaFo0WqqdGc+FrC7vPL1zI0GuMtVnwtdZCCjq91PwhfKxCEr5UHwtcKBOFr5YHwtVwtYedrGVEMjXwtq67yQR3E11Jie1bga90LwteKAuFrZYHwtYC4WnwtP0QjiqGRr2XVVT7wtVSmSuxhEL5WIAhfKw+ErxUIwtfKA+FruVrCztcyohga+VpWXeWDOoivpcT2rMDXuheErxUFwtfKAuFrAXG1+Fp+iEYUQyNfy6qrfOBrqUyV2MMgfK1AEL5WHghfKxCEr5UHwtdytYSdr2VEMTTytay6ygd1EF9Lie1Zga91LwhfKwqEr5UFwtcC4mrxtfwQjSiGRr6WVVf5wNdSmSqxh0H4WoEgfK08EL5WIAhfKw+Er+VqCTtfy4hiaORrWXWVD+ogvpYS27MCX+teEL5WFAhfKwuEr/Wf5xfMlsQlQg0JfwAAAABJRU5ErkJggg=="
        case 22:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAeAAAADwBAMAAAAqW6qJAAAAHlBMVEUBIWnIEC7////XUGaHl7kUMnTxw8r29/rw8vf219zf67YoAAAEnklEQVR42u3dzXHbUAwEYLSgFnhxKvBMCvA9B3WQDlJCWkjD8Y/k2FYkPgC7+17ixVUzJL9ZiqODiI377drcPQRozkc8XJnz56jzHX+cDvjr4lT3cbgu3h7+TfAt7xaHAz9jLfim9wnMz1gKvu19BtMzVoJ3vC9gdsZC8J73BCZnrAPves9gbsYy8L73FUzNWAUe8P4BMzMWgUe8b8DEjDXgIe9bME8sAY9534FpYgV40PsezBILwKPeD2CSmA8e9n4Ec8R08Lj3AkwRs8EJ7yWYISaDM94tvgvEXHDKu8UmEFPBOe8jWCBmgpPeJ3BKXPpdTQQft5z3GUzPmAfO5nsCs8U0cN57ApPFLHDBewZzxSRwxbvFT4GYAy55v8RRIKaAa97HCxeIGeCyVyEmgBtegRgPbnn5Yji46aWL0eC2ly0GgwFeshgLhni5YigY5KWKkWCYlykGgoFeohgHhnp5YhgY7KWJUWC4lyUGgQlekhgDpng5YgiY5KWIEWCalyEGgIlegrgPpnrx4jaY7IWLu2C6Fy1uggVesLgHlnix4hZY5IWKO2CZFylugIVeoLgOlnpx4jJY7IWJq2C5FyUugid4QeIaeIoXIy6BJ3kh4gp4mhchLoAnegHiPHiqty9Ogyd72+IseLq3KH69hCR4AW9TnAMv4e2JU+BFvC1xBryMtyNOgF9PMt/bEI+Dl/LWxcPgxbxl8Sh4OW9VPApez1sUj4IX9PbEY+C1vC3xEHg1b0c8Al7P2xAPgFf01sX7YIF3E87gU5o6BhtssMEGG2ywwQYbbLDBBhu8/W291H8+BhtssMEGG2ywwQYbbLDBBhtssMEGG2ywwQYbbLDBBhtssMEGG2ywwQYbbLDBBhtssMEGG2zw5wH7H/EGG2ywwQYbbLDBBhtssMEGf0Zwa4HY5VyuFPvaA1/fUTZhYVrSW0t4vrjsLd7Ss8V1b/U7PFfc8JYfWjPFHW/9KT1PXPKml/GuI6558+uWVxEXvYWF2muIq97KyvQVxGVvaSn+fHHdm6s9WEXc8CaLLdYQl7x3teqSFcQtb7qcZr64563XD80SN72Ngqk54q63UyE2Q9z2tkri9OK+t1cDqBYDvM2iR60Y4e1WeSrFEG+7rFUnxnj7dbwqMcgLKFzWiFFeRKW2QgzzQkrT+WKctwPWiYHeFlglRnp7YI0Y6m2CFWKstwvmi8HeNpgtRnv7YK4Y7gWAmWK8FwHmiQleCJglZngxYI6Y4gWBGWKOFwXGi0leGBgtZnlxYKyY5gWCkWKeFwnGiYleKBglZnqxYIyY6gWDEWKuFw3ui8leOLgrZnvx4J6Y7iWAO2K+lwGuiwVeCrgsFng54KI4BF4SuCYOgZcFLolD4KWBK+IQeHnggjgEXiI4jtk3Q0LgZYLTGYfASwVnxSHwcsFJcQi8ZHBOHAIvG5wSh8BLB2fEIfDywQlxCLwC8Lg4BF4FeFgcAq8EPCoOgVcDHhSHwCsCj4lD4FWBh8Qh8MrAI+IQeHXgb/viEHh14IGMQ+BVgnczDoFXCd7NOAReLXgn4xB4teCdjOPGfhXY66li8E3xb5DUNA2PqEXYAAAAAElFTkSuQmCC"
        case 23:
            return "data:image/png;base64,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"
        case 24:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWgAAADwBAMAAADfieN8AAAAIVBMVEW8AC3////RT23acovBEjvHKk/66+722uHww87qrrzjlademFPnAAADvElEQVR42u3dz08TQRQH8Ge7lR8npg3dwqkNoteWiFFPi8aIngoIerQqB2+s8aKnNurFE0SjV4gm+meqnAxCuzvzeG+efL9/QPtJs53dmXnzlpzBENBAAw000EADDTTQQAMNNNBAAw000EADDTTQQAMNNNBAAw000EADDTTQrEk/LW8/ypJ725u3ciPot6sZJXSchJKtHwbQL1fpRLa+RI7+l3webF70uz6dmtrNaNHpKp2ZrTxOdNqlManmMaLTNo1NJY8P3Zpg/q0exYZuTjT/Vg8iQ3+mAnkQF/oVFcq1mNCLWTF0chQPusgFzXlZs6A/UOE8jgW9SCVyFAm6XQZdiQO9W8ZMyU4M6LRfCk21PAL0eyqZdX30IpXOgTp6vzx6Rhu9QCT/U4eihz7odV10mvmgk1wV/YK8sqOK7vuha5roBnmmp4je90VP66GbmS86Gaih6+Sdjhq664+uaqFbFJBcCT0fgu4ooQ9D0LM6aP+xI3T8CEA3KCg9FfQwDD2lgm6HoSsa6JQCkyug66HojgJ6LxR9WQHdDUVX5dFNCs5AHN0IR/fE0fPh6A1x9DAcPS2O7oajq+LoLBydSKMXiCEHwug6B7ojjJ7jQK8Jo4cc6GlhdJcDXRVGtznQFWE0sUQW3eJBj0TRDR50TxRd50F3RNHzPOgNUfQcD/qSKHqPBz0lit7nQc+Iog950LOi6C4PuiqKbvOgK0BPSp8HXQNaYFprFp2IookpQP+XlweGPKDx7BEB2uSjqclJgMnplsmJrcklBJOLNSaXxUwuQJpc6jW5qG5z+8LkRpHJLbk5xXvLxdpmNrmhb7J0gmPMky9SMVkOxPCctyaONlniZrKY0GTZpntqsUA29J6YaJQimyz6NlleH7r2oXOQweSREZOHc8JWIUMOj4eggwY9rQNnqc6AdwEPUdo8rmryYLD/9EXxCLbNw+6+m6CB3XYC0bt+aN0GDiZbZZhsSuK3PDZSRptstOPT0uhIHV2sJyHrD82AbpUcQJJRBGj3uhz6vosB3Sx1W6wNokC752XQN1wc6DL/RZYuoRe3caXJFqHOPSuGvupiQhfrEvrExYV23yebH7rY0M3rk8x3B9GhJ6r5zJztycerGc2sjeDHqTnN3C33zxivk3hb7v+ZfZ16b6wcuJjRzn28cpJ85yf3d5zHCztW/npWrS1ZeGHHcd58W1nOks2l21/P5ePxEhqggQYaaKCBBhpooIEGGmiggQYaaKCBBhpooIEGGmiggQYaaKCBBhpoW/kFyKVe015rhv4AAAAASUVORK5CYII="
        case 25:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWgAAADwBAMAAADfieN8AAAAHlBMVEXaJR3//wDkXBXtlA7fQRn87AL40gXztQncLxvpeRG+t6rEAAADWUlEQVR42u2bPW/aYBSFX2EHzNYbwtcWKnXHW0cYwhx3qJQNJLqHLSNQtVnD0P/bASgY/I1UnyOdZ85wotw8PtxrnBNCCCGEEEIIIYQQQgghhBBCCCGEEMI55/wJYWhvTBi6OScMPX0gDB12CEMveoTyMOPTR9vsg08eZnz6mJrx6WNnNuSThxmdPgIzszWfPPj00TIzeyULvTEzG/DJg08fKzOzPqE82PTR3ofm0kdrH5pLH5t96E9UoUf70Pd88mDTR7QP3WXKvLUDj3zy4NLH3TH0M588uPSxOobu88mDSh8NMz59eKfQYz55MOljdArNo4/wFLrDJw8ifZzJg0cf3nnoMZ88ePa90/PQD3zy4NHH4jw0yb7XtxgTPnmw6KMZDz3nkweLPsJ46CGfPKD0EXxOxS5I/8lJzUNQhf//3GlEt2bu1lAA328NvaxjrHdsw+Gcc/6CbTicc+7nLaHf6tLel+qZ63vkVB+QXo3dz6sa+mudD8aKA/Kt3qf5im04nPt3mi1H7Z8LZmzD4ZxzQenm1F8DLMHKNieEK3/wm6An3VitUZY3foTfk26q1ksHwx+24SjTnHCGo0S1fnNQFGpOL2ir0hV+T6pUrQH3p0/4Pal8tUboSQnVOoLvSWWr9dKBErINR85nL9xXZT0q3R1opoeew4aepofGPReFHJ00TkZBhb02+1menvDJA1cfzazQcz554Opjh7n6rywPWH342X0aszG1jbBPN7NDY+pjkx16wCcPVH3kfbBFzBzkrRDWBPLoRgT6aF0uGy+31q/48ni5WkoO4OXRm1xtrYfw8hhfF+w+ujwOy8b4gOCF3ibtk+JLyUdseXwkehBPH7+Sl43nS0m8bxeNkpeN5/f+e2B5xO9u2whYH1HaJnqG++2iRvoCLITVRyv9KHt6IQRNH3cZR9l3VH2MsgrGDlMfR7MlH2WPzamDKY+UNxs9SH00so+yx1dpsfTh5VzsDwMyBpTHOO+3esaTR+bF/glv3xvmHmWDFZw+IrNuzoqgHYHte/0iF/sZ2LnIK/KXD0IsfTQLvbzWiKD2vdNiL6/NoPQRFlzE7JD08aPgP5j/HUgehd9sbCHpQwghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIUZm/83sKPOqPjNoAAAAASUVORK5CYII="
        case 26:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWgAAADwAgMAAABQyRbcAAAACVBMVEUhRouuHCj///+QNKGcAAAAWUlEQVR42u3MQQ0AAAgEIEta0pR2cPNzgwBUvym1Wq1Wq9VqtVqtVqvVarVarVar1Wq1Wh1ezxu1Wq1Wq9VqtVqtVqvVarVarVar1Wq1Wp1eAwAAAAAAABwtoAYFhYXw5Z8AAAAASUVORK5CYII="
        case 27:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWgAAADwAgMAAABQyRbcAAAACVBMVEXOKzcAkkb///8vuYFFAAAAaUlEQVR42u3MMQEAAAgDoJW0pCltsMsTApCptkqnVqvVarVarVar1Wq1Wq1Wq9VqtVqtVqvVarVarVar1Wq1Wq1Wq9VqtVqtVqvVarVarVar1Wq1Wq1Wq9VqtVqtVqvVarVarVar1Z/1AeDdBYVnrJzbAAAAAElFTkSuQmCC"
        case 28:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWgAAADwCAMAAAAaeQ59AAAAyVBMVEX/AAD2AADZAgDPzwDLygDHxgACNJoAZgD//////wC2tQHV1AC8ugHc3ADCwQD29gDk4wDrAQDt7QCwsACsqwCYlQADVADFxcempgKOiwIDXgDBiYmiSwHs7vInUqienwTU0NFecwJ4fgCxZGOkegCOcQBEageuiwCZXgG2IQC6BgAoXwW5mACZOAC9dnbCNQDCOztvjMa3U1O4XwCdsNjXFgjd3uHMJhgISgDBpwCZmWWaHgD5+vxTdbrHraipqW4tVgF+h2JsPQAe6Mg3AAAVFElEQVR42u2dD1/aOhfHaZPM2yQN/YstVktroQWKOB0g4pju/b+oJ0kBAdnUPXPTNcd9uM7a6f328MvJyclJ4+idWeNfNQVagVagFWgFWoFWoBVoBVqBVqAVaAVagVagFWgFWoFWoBVoBVqBVqAVaAVagVagFWgFWoFWoBVoBVqBVqAVaAVagVagFWgFWoFWoBVoBVqBVqAVaAVagVagFWgFWoFWoBVoBVqBVqAVaAVagVagFWgFWoFWoBVoBVqBVqAVaAVagVagFWgFWoFWoBVoBfojgr65bx9pg4WtQL+dtVutm9Y9TZJugUf9gW5rCvRvZ3xz30tCjyHkI2gYkP8H0SArRhy3Av37ICc+RYhhD7NH0AwH/K+IZtFA1xTo/1+TexwyczEgVtPghivQWHzuWAS6LkI4W+gK9P9jrfuUIepCUzI29kFLa5rIpRAXA12B/lVnTjCkLnA2SLkDP0oHMK0Nfgd6DJYjXYH+JcwIushaM4aUK/TOYMi4aFO4pm0hDHCkK9CvFQ2O2SMrfwXY5Yixnya94X0FetSPiq6POW6Xrn0eeJB+bNR/ATMAK8xNwiEzL+3dtNri0rAC3Re/l6YPoi4fDCkmlV8TD9CRrUC/1IYe8cxKECh32jgdth6vbYGWpvczriOYViJDXJIPFOiXuXNKKJTUTB5ieOmwvfMQ9kELz+5nHg9E5LNpIgY+rH78WXdGBEvRNV0Iw17ryeWnoLnZUQihK1FbLgn6CvRz08DUolKcHQxgODz0HA6C5jYOIageEWEk0hTon7pzYHmSFWLkEOafgRaoAUXSqT0r0xXoH1sCCJOq4ZGg9yNl+THohhZ5oBpGKaETBfpH1jORlA0EYNI6+gXQPAYpIJROTX78PbUHnVgyRnNc02/9ZKz8KehGox+YroiqTQb6CvRBzo4cykxsJu2jXwfd0DNTRnoWNfsK9CHOnnBE6gX3rR/bzY3vYxr7i8FAH+g/sMjzhNQ7lPQV6B9wZg/Hv8UekAwRP5hP/4lx0MKSM7hdXp3v2UX18SM7qT527PSBVD79sXT6T8QbVOgzNNOHE1traPZotJis5hya+BB/VjZaLEa2dtD6i5G8pHfOQxMInWZsoEBvjXBAJJ6dIEjT2xORfdMxdceHfxktc93s4LxPa0QunsvbO7dl6Ab82ZnQ1RXozbzbI8SifswgCzjoCffLUVlwp37yvpfunOfidZ81d+fFKCv5rSNd7zwECKLAQxYhXU2BXllKQt9FzKPQtL6d2DMGaJHmJWRPnFrLIYpcr0CwfJJ2vkYoo2lEAeWgvzkm9DyEUBDAkQJdpUV7oe9xKHIF1uGg7cwvMnM+8uOn7/qRH/RNsx/40ZNnMInjETQjfjPX6G9NuQDGYspwsFCgxThIRXWGh+WClAO5dOhl0M3MMgrw04EsCugIwhENoqdTQuyNqFnkQWZzjV4vnDsoYHik1R50++Y+JiyIXQhdPw4o46CvU2lhmmb7+jAJ5dfFn9l+RnpzKY04aJcLNKkWE02uNVrtPfreXzueB0Gc3vPwru/7ue+Llyduy1WlsvzJM9AKf32tz8O7KKeQejGTsK30Y/j0m4J+LNsAXD9cDlpHjpXj2HTI7IkQX1vOnNK54zyN8MamAz2c82/g0nGu2Xo/yjBkngstw/w+qDnolmtsmYVkeGcZJSGwbDafRB12bkDAGATGgajD4M8AmHOD6AK0fC46H1ERxB4M7ZqD7jWNHXM46JlllbSJ5qbzVDrKZkkti5bN+RPpuG4iTJo4b5KJAM1dehyVxIcB5gE6/q7VGvQNM/ZA8/AuyrI89MM8y4p9mv1uloW+H2ZZd38yo/NLXNrFbSOh0VkJAfB8z2VW04wDVNQZdDtpHgA9vt7YfjJj8nhptnuFe/TGxjzqYJTHMKYjFrWEOsVxsqgv6PaNj0znCejtH335mJG7ONlJ2p1fbCX4rs53xk0OGm1KIH1ADIOAQq8v6JsQU4oDtlWVuw/66r+X2enlLuhv69pHgkPg8U88NKgt6HYvxS6OXVGoaP5+0I4JaYAhLFPI/3VAovp6dA9I+QxCDyEPOb8TNJ8ZugiCeRFN7L74MU2M9dqCTgnkE2QQNh3GIzAqllR/G2gE8mi82rgVCpdmYFFX0C0eeRkGJoEUU+xCGEPrGdBfvgr7/Pnz8c9Bn/d1u7EOnccAi8nQ+09Mv5VyiMDLoYG5noIHHPXtM6A/rezzM6C3odqeWCjz3v+q1lspBwAGn1GHj8GdGbjPgT47/frpE395DehGF8qfNKon6BsmCmY8mFpbcTR41qO/nHF//nL2KtB9KN87uV1L0L1KOUOEgfHSOPpOSMfXL6+Ujobti8Vflw5qCToFUNQzDnsQ0RdPWATjL6evBd0ooPhZcFFH0O3Ky+DN0VFgxs0Xe7RQDv7yOtB9yN895rtPLL1NcMfcJp9GBC1R5u+sNgc979Fn/33mnP/7/DrQOpY/LNdrCLoHqKhvSarKO8LYi0BP14Ph8atAayHiT9J97wHe2wV3CNyvsGMrcBwTrMM7kfg8ODP8WoXRZwdnhtrqNg56r51HIcrT4XsX6TcBLX0MC4le7RLyQhdBtioJK4podhD0nSR9dnoQ9DgqilVJGGPl9Xi27uahjcU2fYJG9QPdjpmIorEA3W4Nk5hDjkM5YRGrUFmWicz+oVzH8eevXw7lOvi3j/ltNvdkDpp6ooQB5dFMdvMYsEDEkkX9QLcoH54c6rda7R6HHIQ+FpUBQqNn3C8LmHGnHjeu7l6cVBpFUVEi/lJMZJq0aQHsBxDQ67Fu6wGfHTk4s2sH+h55Yu9lkmBAQ59uCos46ElZltdpmZXlq0BH/C6WFnlZ2o+Jf4e4YYBgNuqK/TFeoNcOdA9Sg/iUOx3eLLA0LUK5dNi5f50Z8yjE+mtAT9x4BIwo9zNNaPTjGpnDYu7Yvm8Z+J3PDd9kKwXyXAC9dUMO7nrIdZkcDCdZXhTzLMrz/mtAj/M8yudFlncncjB0YwzWC4cOCBhxXRfVELQPmbfq/uBADgVC6IbJ8OHEjrrS0m630ATos3Vq9HQvTbr+/NMdB213Nzbm4d04up7zwTAQdUrV6iGjxAtqB7odAn/VKQIGHoLIT3vtNv/6w4nWX2HudkfSo8/OREjHXyToz4L7Z5m9+7S+cCcHw81tsoCmoen6uCghpPGqnYeD2DvPlL7FWOgG62ZIAMTJsLXaWihA66ZhUsaI4cwq0F/uxGTwToLenoJ/Ohbppc5pBXrcNBhCc8egm5KwhqzAyxGMqx4TVowWdQOdyr2bnHIoPXnj6Rz0xDJy5OC5qL2rPFo4MX+RHv1V/OXryqNXFyToa64O2ASlYeo7U3BNH4wyCOTqbzMZ1Ax0Kxb9OIjX29skK6UDwdx1KB++osZKo+W6ylqjv0wfNbq6IEBrBZlzmEEG2OBJrsMeRIxg1Gx2a6fRPoUkDv37HX+WoPUiz0vfD8s8z+z1YChTSSvQm8S/AC0vCNB6Lm/z+W3X+6A1ezIKUkowqB/o0PSZgVEIYJz0Wu0d6RivbfaawVDeIG+bbIOWMl0SH2EzRiCp3WCIfGIYFMUowAAgv8eHw/YK9E6aVA6Gp9W6yt3eYHgmB8Pj6acfpUltHnhEOQM09kKxjBOEtHaDYYKAwaMET0xVGJ9aABiknHbrAOjPq1WVr2Jisl5hmf63c+EJaF0f9KNszoP1OBAbvjzERF+bpG6g24loB8FQ8Dgv9JiYs9w+BX1azVjOpluFHXKBZX3h9Cnoh5JBRIPHyWGAkPh577se/U1yHbLvBkw3PS9l61EaHwAtXJcPgasU9FQEIav1lTtx4fPdgRWWh5gHLVvNS0EK5YNd1E2jj+4hFZn4FIicxxaRb3ug10tYWzmP0+nWOgC/cAD09NtWJTBhASah6CKEa5jruEGuyMQnw8QFgHkerDYFNvcL0e9+qchxettcvUlY4CIA8qgr0ldBDbN3LVwl/ttH7XYv5bAh5kiIebv8JdDT2R5oxwQs8CiELC/GE1v3sWM0sV+/fHQrloWHuGpTxWEnPgIQ0odd0LPTF4Leab42mT64DEFYFtGkWjYcULGUxd73fOWNVsF3F2cF+2Gvlzwc67vI9oB+XtleucHuXbPpQ1aI8ujNVwbV4mwN1wyPEki2yg02NtxFZi9fVra7O4ReTmO0uxl0VJUb1HAVfLeAZsutj3fUVjt/Wdnu1c4vfN6JmbW90V7rVu+fOhbQ3IhZYVUStgt6l9muSN99OesI0J090LsSrZ0cE8tz8scvDjxREuZ6dSwJa/tsXeS4m7672FEBfflEOmQqaRf0bkyoH38TIQahmzfHAskix3c+Fr5R2W5S1YTtN3vt7Yr0boB3d7hs9+5y910wvRVRNGTmesvbqmx3VEvQQyHSFgrb+6PhbvOIXZf+UqWU9kDvhoSNq2lVcG3hVbcJvSoRRvUsRL9hoqegB/a0o7XcEmlN1xqXp88Nhqcz/o3bkcrxev8RF2rxDBZia0WTBnotQbdTwgM8SPbjjt5yxWMy0frluKFdbDHtrMt2t8vvuKpHeb8xm+wohzRmehOhHFylAHj3DQ7eaFfWkGC5/W077mi32vedSjsm19m4nA9se0c8VkUeZ4/Kfbfk37Kg2Wwe2Svl2GpOAQGd6HL7mwvruv2t5Yr/f0yGG8jDxGcAf7sQwOxrlEcZDbKuPjn+WdnucqJneYizKCeSNI85tvd5EcYisbHCYu+/C81bbVFOVluU5RpWOwkRQG7AQNwRGmAXOYCjrMzKRWN2/OOy3eWkMcrD+XWErO61Jh06BDv9gzAVGzfQ+99m+GagW0I7DI/ct9u9GABRYCB7ei1lKN2PIHKicB6DcWOy/FE26cTWxlZehlGTsmIgo5RlQPB2wxXLEx073A/QDvatQLd9wF2N4DQkwMVkU/6JRdKzX84X1pxz5joezeyTg2m86bk9u+ZQOWkKFqzkw+jVKbY8K7B2fBqaBHyAXj9vBZoPh644Pogwd0NZlO7Gt0t7kM+DMsrn3by0miEP0i6XT1Cfnswa+jwzSJ53uU/P/XmmTzpyVmjSbfmwKPPBoMag+TTcA6bL1pQt4HqQEJR2rhr965j7cxdhNs9l7zX7fLmzoNW5mAmFmcyzOXMRJz3H0UQ76chDKyA06RZpE8W1bl511KOWi5qrkzaFRhMcihKPHhcPrfDnZY6bTrrucWfPzped6fR0Oj1eXlyuT5qdzEPHoWVe+oVYzP22QourXvabgz0XdQbd7jm0ueLiAhAkvVZVtNR+WOp2NC+Nkln+dos7bTK7vJzpO3vbJvPAZIzrdKRdTr+t3x1O4NBHoXaCqNYePUyqMwsDQOJee6sMr708se0+NZplWD4b/k7mfm4YZV+bHB9vSTO2GNn8Jflea9CywyDxTBDf7OWlhx0e481MI5y/YJoxoZmBJg17OfXNLWVGAKy54+96vUEfcfEQsR2Iw2TYam1l8obTc60xzuYvms7xEZEHIMtpATYHqBqOyXxGUDXKLmrfbbcdOsILmZVy98Oi2HFNO+FBsv7SjYGTzNZPppfapCAgQKbJxH5OQlIKJPeu6h/dimUPL8OzQkhdBghhcVLh7k0v7BenJ7TJcnopa3SLMHb5PwOox0IzBqaoufsgZ4S8JWg+HppiwuxQUSMmmgJ6lGur3KE17CxffFbe7LgTRUU+5+8LIM+xNh0DQeoQ/uyc7w0FWhSWOqLPIA+hVyOXYxFEA+7dIFh2Zi/yafvqdBnzx0NdTCGxVi3nMREzfBKkmgJdzQ8tJI8Vit2tlrBNyyQouJ1ePB8uaLPl6YPPBOHmdtNvebgQn96rUyvWOs2kTCPLZ1xYt6ptRdHjcedSfwbzyelxsN2017EAdWksH58JwnCgQK9jvOqoLGqlPhQSy2Vj49vmbef4aqL9BPO0c7sO6ZqOSZjL1YNP5S0m98uC9KMo9J84lCypDn9DVtoa9tKAD2iIy+1KDNBtp3Mx0w+w1vRLgRkJwpYpnpAYSImXRYtQ+jMP0hfqrKwd0o4nz+S1/LZc0+qJRS0+ujGKPUyD2+PO8vxyspXi4IHc7OqiMz2+9SCPMjwsIkOC824kupLqsfTnpmt9nPObGn/o4MimJI3MeD0XF6W8SRpzgJy4e8vFunN8cnF1dcnt6vxi2Zl2lrdhwMREG83zIhr39VX9aN815YzQcz4U5z9zFGpqSNKA0J0C0zafuHDgHHkSPjx8W3ZWtvz28NDtFkUURWORzROnIK5/3xEioKrq+Fic/9DhvmlTJpAJNXuHD/dtt9utm5s4pjSOFwMB19YOCLfeNWWDdcd1ooYCfVCn5THKjmf9X8dVx6Ynl3ip9cH8+c8dwJ44Va9/RmDvVw9g7wJ52qxhso8zT/njoHk8Lao+uXy4Zjz8BdBa5BGXVKnoD3jQ/Z8DfTSkMsNkNBki6c0rQWujkDAmj590rXzQUKB/NhsPLSxX+iyXwOSm/XLQdhQC4sp7TWpFdkOBfma91oTSKw3iAZjet14GWueYQbW44lCAFg1NgX7O7gMTV7kLgdrv7br1IdB2v8tn7ZU4G4Ca2UeUjT8P+qiVwJUGGCamEKW9rZXbfdCa3i98CChe9RzzTLywGwr0C1GnJqqkWvQRQ4jFyf1NtZa4BVrTB/0iFb3cPLBO9UMS6Y2GAv3y8MMnaOWkhgVdzGm6fpr0hvcV6FFUdMOY8i/jTQtB04WgO/iY6vzXQB+1730C8cpTjSb3cE+ca438CrTPP2XUw2jTPRZgAIrBB6b8l0AL1DyQwPTxDD7HIpCtQIdsszQoS50wBeyjY/5boEUdUxIA6FKytU5FK9B4qyaXj4QA5qNB48Pb0d+zVivBEIo605X/7oB2TEJFK6Z5NLAbDQX6/2Xd40IhFZlBEK80GkDmctXmkLujgd74N+zob1u7dd9LwoDuDIYMl92CQ9Ya/4wdvQ9r3dzc3N+jMAhC9H0xGPxTjN8T6CrA7rXa9iCaNP41yO8NtLDGv2oKtAKtQCvQCrQCrUAr0Aq0Aq1AK9AKtAKtQCvQCrQCrUAr0Aq0Aq1AK9AKtAKtQCvQCrQCrUAr0Aq0Aq1AK9AKtAKtQCvQCrQCrUAr0Aq0Aq1AK9AKtAKtQCvQCrQCrUAr0Aq0Aq1AK9AKtAKtQCvQCrQCrUAr0Aq0Aq1AK9AKtAKtQCvQCrQCrUAr0Ar0C+1/zzOl+7YhRBMAAAAASUVORK5CYII="
        case 29:
            return "data:image/png;base64,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"
        case 30:
            return "data:image/png;base64,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"
        case 31:
            return "data:image/png;base64,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"
        case 32:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmMAAADwBAMAAAC+i36KAAAAIVBMVEWKFTj///+6dInJk6PXsLysWXKTJ0fkydGgQF3v3+T58vT4yERNAAADYElEQVR42u3cwYlcQQyE4U5hTss6gMEJLPhs2PuefH4x2Am8HNYhGJymcQgaeDWi9XUIP0gtlUpat6vel+/H2vPdrnuvbwdk1ffyDbLy+3OHrPw+f0BWfr9OyOqf5wlZ+fN8PyArf55vkNU/z6+Qld/vO2T1z/MDsvLn+fOErFxwQDYvMm/yf2NkL5tUGTFgr9vUsrGsv0/HFMr6O/XlCWCbSWZ6y3bINlIwMsi2nMxdSmyDhjKL7PNjLcgqpet9LchGCorZXLZpZN7k/2Z12Y5VBgWjY4+5m/8nM8K8QzZazMgNSk7Ixvp/kgOmTfw/2THmFupZelq+gUYLmcCU/hUZkCllNUzacuIPiREyQjb/9ROQGcoZ/V6MjMFAXGbSP7OUGiNSyjJ+shczsbcVf6xKzP4HcsK/ta/6+2u5cGrbGZ78WpR+4B94h2ye6CguWyNzwGZqr8nz0xSZk29TPT8xZM5XzhbLllO83ZA5+FxWyI4F2fR5HGQCU/pXZECmlNUwacuJPyRGyAjZxiVdkBnKGf2mjGaQsbHI/52QuffP+Mle3AsZE/tsyUxv2Q6ZtS+TOSusvZBZlK6WrtbxpwqK2VzmtIj8H6nLnEkarWAEe0wn38b7f0J6mfOVoyWz5DjuhGyo/yc7xnRWfKZGC5nAlP4VGZApZTVM2nLiD4kRMkI2//UTkBnKGf1ejIzBQFxm0j+zlBojUsoyfrIXM7G3FX+sSsz+B3LCv7Wv+nPvf2zbGZ78WpR+4B9w73+g6CguWyNzwGZqr8nz0xSZk29TPT8xZM5XzhbLllO83ZA5+FxWyI4F2fR5HGQCU/pXZECmlNUwacuJPyRGyAjZxiVdkBnKGf2mjGaQsbHI/52QuffP+Mle3AsZE/tsyUxv2Q6ZtS+TOSusvZBZlK6WrtbxpwqK2VzmtIj8H6nLnEkarWAEe0wn38b7f0J6mfOVoyWz5DjuhGyo/yc7xnRWfKZGC5nAlP4VGZApZTVM2nLiD4kRMkI2//UTkBnKGf1ejIzBQFxm0j+zlBojUsoyfrIXM7G3FX+sSsz+B3LCv7Wv+nPvf2zbGZ78WpR+4B9w73+g6CguWyNzwGZqr8nz0xSZk29TPT8xZM5XzhbLllO83ZA5+FxWyI4F2fR53P/3D2Ks7TFb6DJqAAAAAElFTkSuQmCC"
        case _:
            return "Invalid ID"
