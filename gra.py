import random,math,time
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

##############################################################definicja bazowych wartości zmiennych#############################################################
sila=20
dfc=50
maxhp=100
spd=1
ddg=0
aim=20
martwy=False
hp=100
poziom=0
xp=0
liczba_punktow_na_start=5
item=""
enemy_name=""

final=False
straznik_wiezy=True
kanye=True

enemy_sila=0
enemy_hp=0
enemy_dfc=0
enemy_spd=0
enemy_xp=0


ammo=5
bron=""
sila_broni=0
ammo_us=0
aim_broni=0

miasto_unlocked=False


ucieczka=False

alfabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
##########################################################Przedmioty Specjalne########################################################################
przedmioty=[]
#possible "jablko","Podejrzany_pistolet",
def wybor_przedmiotu():
    if item=="jablko":
        jablko()
    elif item=="podejrzany_pistolet":
        mlg()
    elif item=="czarna_pomarancza":
        czarna_pomarancza()
    elif item=="zolw":
        zolw()
    elif item=="chipsy":
        chipsy()
    elif item=="denaturat":
        denaturat()
    elif item=="lomza":
        lomza()
MLG=[]
def czarna_pomarancza():
    global aim
    aim+=5
def zolw():
    global dfc
    dfc+=30
def chipsy():
    global sila
    sila+=10
def denaturat():
    global sila
    sila+=30
def lomza():
    global hp,maxhp
    hp=maxhp
def jablko():
    global hp
    hp+=15
    print("Po zjedzeniu jabłka zostałeś uleczony o 15hp")
    przedmioty.remove("jablko")
def mlg():
    print("Co się stało? Przeciwnik po prostu zniknął bez śladu... *Wydaje mi się że nie powinienem tego używać*")
    MLG.append(enemy_name)
    enemy_hp-=10000000
def finalmlg():
    print("Okazało się że przeciwnicy którzy znikali z powodu tajemniczego pistoletu byli teleportowani do tego pokoju")
    print("Musisz teraz zmierzyć się z każdym z nich...")
    print("Powodzenia, Inkwizytorze.")
    print(MLG)
    i=0
    while i<len(MLG):
        if MLG[i]=="ork_boy":
            ork_boy()
            walka()
        elif MLG[i]=="grot":
            grot()
            walka()
        elif MLG[i]=="ork_nob":
            ork_nob()
            walka()
        elif MLG[i]=="kanye_west":
            kanye_west()
            walka()
        elif MLG[i]=="ork_evyboy":
            ork_evyboy()
            walka()
        elif MLG[i]=="malpa":
            malpa()
            walka()
        elif MLG[i]=="cum_monster":
            cummonster()
            walka()
        elif MLG[i]=="kobieta":
            kobieta()
            walka()
        elif MLG[i]=="duch":
            duch()
            walka()
        elif MLG[i]=="zyd":
            zyd()
            walka()
        i+=1
    else:
        print("udało ci się pokonać ich wszystkich")



##########################################################Przeciwnicy##########################################################################################
przeciwnicy=["ork_boy","grot","ork_nob","kanye_west","ork_evyboy","Hitler","malpa","cum_monster","kobieta","zyd"]
def kobieta():
    global enemy_hp,enemy_dfc,enemy_sila,enemy_spd,enemy_xp,enemy_name
    enemy_sila=10
    enemy_hp=85
    enemy_dfc=10
    enemy_spd=random.randint(2,18)
    enemy_xp=25
    enemy_name="kobieta"
def duch():
    global enemy_hp,enemy_dfc,enemy_sila,enemy_spd,enemy_xp,enemy_name
    enemy_sila=40
    enemy_hp=100
    enemy_dfc=10
    enemy_spd=random.randint(12,20)
    enemy_xp=70
    enemy_name="duch"
def zyd():
    global enemy_hp,enemy_dfc,enemy_sila,enemy_spd,enemy_xp,enemy_name
    enemy_sila=30
    enemy_hp=20
    enemy_dfc=1
    enemy_spd=100
    enemy_xp=30
    enemy_name="palacy_się_żyd"
def grot():
    global enemy_hp,enemy_dfc,enemy_sila,enemy_spd,enemy_xp,enemy_name
    enemy_sila=5
    enemy_hp=5
    enemy_dfc=5
    enemy_spd=random.randint(6,8)
    enemy_xp=1
    enemy_name="grot"

def malpa():
    global enemy_hp,enemy_dfc,enemy_sila,enemy_spd,enemy_xp,enemy_name
    enemy_sila=10
    enemy_hp=25
    enemy_dfc=20
    enemy_spd=random.randint(3,6)
    enemy_xp=random.randint(1,2)
    enemy_name="malpa"
def ork_boy():
    global enemy_hp,enemy_dfc,enemy_sila,enemy_spd,enemy_xp,enemy_name
    enemy_sila=20
    enemy_hp=40
    enemy_dfc=40
    enemy_spd=random.randint(0,3)
    enemy_xp=random.randint(2,5)
    enemy_name="ork_boy"
def ork_nob():
    global enemy_hp,enemy_dfc,enemy_sila,enemy_spd,enemy_xp,enemy_name
    enemy_sila=25 
    enemy_hp=60 
    enemy_dfc=50 
    enemy_spd=random.randint(0,3) 
    enemy_xp=random.randint(10,30) 
    enemy_name="ork_nob"


def kanye_west():
    global enemy_hp,enemy_dfc,enemy_sila,enemy_spd,enemy_xp,enemy_name
    enemy_sila=40
    enemy_hp=80
    enemy_dfc=150
    enemy_spd=random.randint(1,3)
    enemy_xp=random.randint(50,200)
    enemy_name="kanye_west"

def ork_evyboy():
    global enemy_hp,enemy_dfc,enemy_sila,enemy_spd,enemy_xp
    enemy_sila=20
    enemy_hp=50
    enemy_dfc=100
    enemy_spd=random.randint(0,1)
    enemy_xp=random.randint(15,65)

def cummonster():
    global enemy_hp,enemy_dfc,enemy_sila,enemy_spd,enemy_xp,enemy_name
    enemy_sila=5
    enemy_hp=1000
    enemy_dfc=1
    enemy_spd=1
    enemy_exp=random.randint(10,30)
    enemy_name="cummonster"
def Hitler():
    global enemy_hp,enemy_dfc,enemy_sila,enemy_spd,enemy_xp,final
    final==True
    enemy_sila=55
    enemy_hp=256
    enemy_dfc=random.randint(180,200)
    enemy_spd=random.randint(2,6)
    enemy_xp=random.randint(15,100)
###########################################################Broń#################################################################################
guns=["bolt_pistol"]
#possible "bolt_pistol","scar""cumpistol"
def wybor_broni():
    global sila_broni,ammo_us,aim_broni
    if bron=="bolt_pistol":
        sila_broni=15
        ammo_us=1
        aim_broni=10
    elif bron=="scar":
        sila_broni=20
        ammo_us=2
        aim_broni=40
    elif bron=="cumpistol":
        sila_broni=random.randint(25,60)
        ammo_us=5
        aim_broni=30
    elif bron=="rpg":
        sila_broni=random.randint(100,200)
        ammo_us=45
        aim_broni=100
    elif bron=="latające_wąsy":
        sila_broni=70
        ammo_us=4
        aim_broni=40
##############################################################Mechaniki############################################################################
def kreator_postaci():
    global hp,liczba_punktow_na_start
    print("Masz do rozdania ",liczba_punktow_na_start," pkt umiejętności")
    print("W jakich umiejętnościach chcesz je wykorzystać?")
    for i in range(liczba_punktow_na_start):
        print("1.siła")
        print("2.obrona")
        print("3.szybkość")
        print("4.celność")
        print("5.wytrzymałaść")
        print("6.dodge")
        inp=float(input(""))
        if inp == 1:
            global sila
            sila+=5
            print("twoja siła wzrosła o 1 pkt")
        elif inp == 2:
            global dfc
            dfc+=10
            print("twoja obrona wzrosła o 1 pkt")
        elif inp == 3:
            global spd
            spd+=1
            print("twoja prędkość wzrosła o 1 pkt")
        elif inp == 4:
            global aim
            aim+=7
            print("twoja celność wzrosła o 1 pkt ")
        elif inp == 5:
            global maxhp
            maxhp+=25
            print("twoje punkty zdrowia wzrosły o 1 pkt")
        elif inp == 6:
            global ddg
            ddg+=1
            print("twoje dodgowanie wzrosło o 1 pkt")
        else:
            print("nie ma takiej opcji")
            liczba_punktow_na_start+=1
    print("siła=",sila)
    print("obrona=",dfc)
    print("prędkość ataku=",spd)
    print("celność=",aim)
    print("wytrzymałaść=",maxhp)
    print("dodge=",ddg)
    hp=maxhp/2

def reakcja():
    global ddg,alfabet
    print("wpisz sekwencję, która pojawi się na ekranie, aby uniknąć ataku")
    time.sleep(random.randint(1,3))
    i1=random.randint(0,25)
    i2=random.randint(0,25)
    i3=random.randint(0,25)
    print(alfabet[i1],alfabet[i2],alfabet[i3])
    reakcjalista=[]
    reakcjalista.append(alfabet[i1])
    reakcjalista.append(alfabet[i2])
    reakcjalista.append(alfabet[i3])
    lista="".join(reakcjalista)
    starttime=time.time()
    inp=input().lower()
    endtime=time.time()
    if inp==lista and endtime-starttime<(math.sqrt(ddg)+1):
        return True
    else:
        return False

def walka_twoja_tura():
    global enemy_hp,ammo,bron,enemy_dfc,ammo_us,sila_broni,sila,guns,ucieczka,aim_broni,item
    print("Co chcesz zrobic?")
    print("1-Atak wręcz")
    print("2-Atak zasięgowy")
    print("3-Przedmioty")
    print("4-Ucieczka")
    inp=float(input())
    if inp==1:
        print("atakujesz wręcz")
        enemy_hp=enemy_hp-sila*(random.randint(70,110)/100)*(100/(100+enemy_dfc))
        print("przeciwnikowi zostało",round(enemy_hp,2),"hp")
    elif inp==2:
        print("masz",ammo,"sztuk amunicji")
        print("czym chcesz strzelić(numer broni na liście)")
        print(guns)
        inp=float(input())
        wybor=int(inp-1)
        bron=guns[wybor]
        wybor_broni()
        if ammo<ammo_us:
            print("nie masz wystarczająco amunicji")
        else:
            ammo-= ammo_us
            if aim+aim_broni>=random.randint(0,100):
                print("trafiles")
                enemy_hp=enemy_hp-sila_broni
                print("twojemu przciwnikowi zostało",round(enemy_hp,2),"hp")
            else:
                print("nie trafiłes")
    elif inp==3:
        print("jakiego przedmiotu chcesz użyc?(numer na liście)")
        print(przedmioty)
        inp=float(input())
        wybor=inp-1
        item=przedmioty[wybor]
        wybor_przedmiotu()
    elif inp==4:
        if spd+50-enemy_spd>random.randint(0,100) and final==False:
            print("uciekłeś")
            ucieczka=True
        else:
            print("nie udało ci się uciec")
        if final:
            print("nie mozesz uciec z finałowych bitew")
            print("nie bądź tchórzem, Inkwizytorze")

    else:
        print("nie ma takiej opcji")
        walka_twoja_tura()

def walka_tura_przeciwnika():
    global hp,enemy_sila,dfc
    print("przeciwnik cię atakuje")
    if reakcja():
        print("uniknąłeś ataku")
    else:
        print("przeciwnik cię trafia")
        hp=hp-enemy_sila*(random.randint(60,150)/100)*(100/(100+dfc))
        print("zostało ci ",round(hp,2),"hp")

def walka():
    global martwy, xp,enemy_xp,enemy_name
    print("walczysz z ",enemy_name)
    a=input()
    while enemy_hp>0:
        if spd>=enemy_spd:
            print("twój przeciwnik ma",round(enemy_hp,2),"hp")
            walka_twoja_tura()
            walka_tura_przeciwnika()

        else:

            walka_tura_przeciwnika()
            print("twój przeciwnik ma",round(enemy_hp,2),"hp")
            walka_twoja_tura()
        if ucieczka and final==False:
                break
        if hp<=0:
            print("umarłeś")
            exit()
    if enemy_hp<=0:
        xp+=enemy_xp
    lvl_up()
def dodatkowy_punkt_xp():
    global xp,enemy_xp
    print("Wydaj 1 punkt umiejętności")
    print("1.siła")
    print("2.obrona")
    print("3.szybkość")
    print("4.celność")
    print("5.wytrzymałaść")
    print("6.dodge")
    inp=float(input(""))
    if inp == 1:
        global sila
        sila+=5
        print("twoje siła wzrosła o 1 pkt")
    elif inp == 2:
        global dfc
        dfc+=10
        print("twoja obrona wzrosła o 1 pkt")
    elif inp == 3:
        global spd
        spd+=1
        print("twoja prędkość wzrosła o 1 pkt")
    elif inp == 4:
        global aim
        aim+=7
        print("twoja celność wzrosła o 1 pkt ")
    elif inp == 5:
        global maxhp
        maxhp+=25
        print("twoje punkty zdrowia wzrosły o 1 pkt")
    elif inp == 6:
        global ddg
        ddg+=1
        print("twoje dodgowanie wzrosło o 1 pkt")
    else:
        print ("nie ma takiej opcji ")
        dodatkowy_punkt_xp()
    print("siła=",sila)
    print("obrona=",dfc)
    print("prędkość ataku=",spd)
    print("celność=",aim)
    print("wytrzymałaść=",maxhp)
    print("dodge=",ddg)

def lvl_up():
    global xp,poziom
    if xp>=2**poziom:
        print("---------LEVEL UP---------")
        xp-=2**poziom
        dodatkowy_punkt_xp()
        poziom+=1
        if poziom%5==0:
            dodatkowy_punkt_xp()
            print("dostajesz dodatkowy punkt, ponieważ twój poziom jest podzielny przez 5")
        print("twój poziom to teraz poziom",poziom)
    return




##################################################################LOKACJE#########################################################################


def intro_gry():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    inp = input
    print('"Wiaj w grze "Święty jan vs orkowie naziści" ')
    print("Teksty wypowiadane przez twoją postać, są napisane", Fore.GREEN + 'kolorem zielonym,',"a przeciwnika" ,Fore.RED + 'kolorem czerwonym.')
    print("Aby czytać dalszą część historii kliknij Enter")
    inp=input()
    print("Jesteś Inkwizytorem, bardzo znanym i uznanym...")
    inp=input()
    print("Wraz z oddziałem swoich uznanych pomocników lecisz na misję")
    inp=input()
    print("polega ona na zniesieniu niewolnictwa, wprowadzenia pokoju na świecie, oraz pogodzeniu galaktycznych ras")
    inp=input()
    print("Oczywiście żartowałem, twoim celem jest niesienie śmierci HERETYKOM")
    inp=input()
    print("jest godzina",current_time, ",nagle słyszysz wybuch")
    inp=input()
    print("wstaleś, aby sprawdzić co się stało")
    inp=input()
    print(Fore.GREEN + "ROZJEBE SIĘ, ROZJEBE SIĘ, TO NIE LATA")
    inp=input()
    print(Fore.GREEN + 'AŁA! Kurwa, jak mnie wszystko boli')
    inp=input()
    print('*rozglądasz się po statku*')
    inp=input()
    print('za szybą widzisz jak silnik twojego statku zajął się w ogniu')
    inp=input()
    print("*Nagle słychać huk, tracisz przytomność*")
    inp=input()
    print("PIĘĆ TERRAŃSKICH GODZIN PÓŹNIEJ...")
    print("co teraz?")
def statek():
    print("*Budzisz się z ranną ręką i wychodzisz na czworaka ze statku*")
    inp=input()
    print("Zorientowałeś się, że cała załoga nie żyje...")
    print("W oddali widisz jakąś pokraczną istotę, która wydaje dziwne dzwięki (jesteś zdezorientowany, gdy tylko istota cię widzi, ucieka)")
    inp=input()
    print("Przypominasz sobie, że w statku zostawiłeś pistolet i amunicję. Wracasz zatem do dymiącego się statku i zabierasz wyposażenie.")
    print("*Wychodisz ze statku* NAGLE GOBLIN SIĘ NA CIEBIE RZUCA!")
    grot()
    walka()
    print("gratulacje pokonałeś pierwszego przeciwinika")
    print("wychodząc ze statku widzisz dziennik")
    print("podnosisz go i czytasz:")
    inp=input()
    print("""                       Dziennik Pokładowy: Statek Inkwizytora Jana
    -----------------------------------------------------------------------------------------------------------------------------------
        Dzień 1:                                                                                                                      
                Wyruszamy na misję walki z herezją, lecimy na planetę Armageddon.                                                     
                W imię Boga, w imię naszego Boga Imperatora! Za Imperium ludzkości!                                                  
                Dopilnujemy, by misja zakończyła się sukcesem, szczególnie z taką załogą!
                Jest z nami Święty Jan, Inkwizytor, jak i kapitan Inkwizycji, znany wśród 
                wszystkich jako zasłużony wielkiemu Imperium, morale podniosły się ku górze.
                
        Dzień 8:
                Mijamy wiele planet, wkrótce wylecimy ze strefy skolonizowanej przez Imperium ludzkości.
                Na swej drodze spotkaliśmy piratów, ale kto by byl na tyle głupi by atakować nasz statek?
                Kto? No właśnie... Pytał Kapitan Inkwizytor, okazało się że piraci nas zaatakowali.
                Ich próba jednakże skońćzyła się niepowodzeniem, zanim oddali jakikolwiek strzał,
                starszy-strzelec Wacław zestrzelił skurwieli jedną celną salwą z działa plazmowego!
                Miło, że chłopaki mogą chociaż poćwiczyć sobie cela, kontynuujemy podróż w spokoju.
        Dzień 15:
                Wkroczyliśmy przez podróż osnową na tereny zajmowane przez siły zdrajców i Xenos, 
                jesteśmy nieopodal celu, jednakże psionicy wyczuwają moce wroga działające na statek.
                Jeden z tech-kapłanów, mówił o jakimś szwankowaniu ducha maszyny w jednym z silników. 
                Jednakże jesteśmy silni. Imperator nas chroni! Nie zawiedziemy go! W imieniu ludzkości!
    =================================================================================================================================
        Orkowie- Opisanie rasy:
                      Orkowie, zwanie również kosmicznymi grzybami przez ludzkość znani są nam od zarania dziejów.
                Od zawsze te półgłowe stworzenia przeszkadzały nam w spokojnym życiu, nie mówiąc juz nic o innych rasach...
                Stworzone przez pradawnych, ich jedynym życiowym celem jest picie, jedzenie i walka (z naciskiem na to ostatnie).
                Są rasą tak zakorzenioną w wojnie, że pokój wydaje się dla nich niepojęty, ich hordy przemierzają naszą galaktykę.
                Prawda jest taka, że jeśli jakaś planeta zostanie przez nich najechana, to można uznać ją za straconą.
                Jest tak, ponieważ Orkowie mnożą się jak grzyby, z badań wynika że mają budowę podobną do zwierząt i fungus.
                Istoty te dzielą się na klany, które wśród siebie rywalizują, nie widać w nich znaczącej inteligencji.
                Faktem właściwie jest to, że inteligenję zastąpili instynktem przetrwania, brakuje im logicznego myślenia.
                Na szczęście nikomu nigdy nie udało się zdjednoczyć wszystkich Orkoidów, brakuje im brutalnego lidera.
                Cecha wartą zapamiętania jes to, że orkowie nie umieją strzelać, broń dystansową posiadają, jednakże
                służy ona zazwyczaj tylko jako ozdoba, są strasznie niecelni i strzelają z biodra na oślep.

             Orkowie posiadają swoją hierarchię uzależnioną od wielkości i siły osobnika:

                1. Gretchiny, zwane Goblinami... Orkowie w swym społeczeństwie używają ich raczej
                jako piłki do gry, bądź jako niewloników, gdyż mają nie całe poł metra, są bardzo słabi.
                Są oni najniżej w hierarchii, dla kogoś umiejętnego zupełnie nie szkodliwi.

                2. Boyz, to podstawowi wojownicy, Są opancerzeni dosyć ubogo, ich cechą jest liczebność.
                Do walki używają zaostrzonych kawałków metalu, dużych siekier, a także sporych "noży".
                Często dowodzi nimi Nob, większy i silniejszy ork, który przeżył więcej.

                3. 'Evy Boyz, Jest to rodzaj boyzów, którzy zadecydowali się, że warto zadbać o życie.
                Posiadają zatem dodatkowe płyty pancerza, jak i hełmy, jednak ogranicza to ich ruchy.
                Zamiast broni do walki wręcz używają stalowych tarcz balistycznych.

                4. Nobz, Silni, bardziej doświadczeni i więksi rozmiarem orkowie, lubią świecidełka.
                Często dowodzą oddziałami Boyzów, są przy tym brutalni, a strach karają  śmiercią.
                Bez odpowiedniej broni, starcie z Nobem często kończy się rozdarciem na strzępy.

                5. Warboss, Da WAAAAGH Lord! To oni dowodzą całym klanem, mówi się, że 
                istnieją orkowie powołani przez Gorka i Morka, mają oni za zadnie zjednoczyć orków, by
                wyruszyć na wielkie WAAAAAAAAGH, które oznacza po orkowemu wielką bitkę, podczas niej
                niszczone jest wszystko na drodze, galaktyka zalewa się zielonoskórymi.
""")
    inp=input()
    print(Fore.GREEN + "Na Imperatora! musiałem być nieprzytomny przez strasznie długi czas")
    obok_statku()
def obok_statku():
    print("Po prawej stronie widzisz gęsty las, drzewa w nim są iglaste, o barwie niebieskiej. Powiewa z tego miejsca tajemniczością.")
    print("Po lewej stronie zauważyłeś chatkę, która wygląda dosyć przyjaźnie." ,Fore.GREEN + "może będą tam jakieś zapasy...")

    if miasto_unlocked:
        print("gdzie idziesz? chatka/las/miasto")
        while True:
            inp=input().upper()
            if inp=="LAS":
                las()
                break
            elif inp=="CHATKA":
                chatka()
                break
            elif inp=="MIASTO":
                miasto()
                break
            else:
                print("nie ma takiej opcji")
    else:
        print("gdzie idziesz? chatka/las")
        while True:
            inp=input().upper()
            if inp=="LAS":
                las()
                break
            elif inp=="CHATKA":
                chatka()
                break
            else:
                print("nie ma takiej opcji")
def las():
    global ammo
    print("Powoli zmierzasz do lasu...")
    print("Po 5 minutach docierasz do pierwszego drzewa ")
    print("Znajdujesz fioltowe jabłko")
    print("Podnosisz je? T/N")
    while True:
        inp=input().upper()
        if inp=="T":
            if "jablko" in przedmioty:
                print("masz juz jablko")
            else:
                print("chowasz jabłko w plecaku")
                przedmioty.append("jablko")
            break
        elif inp=="N":
            print("przechodzisz dalej")
            break
        else:
            print("nie ma takiej opcji")

    print("Po chwili spotykasz Małpe")
    inp=input()
    print(Fore.RED + "Małpa: ugha guha buga")
    inp=input()
    print(Fore.GREEN +"Ty: O c**j mu chodzi?")
    inp=input()
    print("walczysz z nim?(tak/nie)")
    while True:
        inp=input().upper()
        if inp =="TAK" or inp=="T":
            print("------ROZPOCZYNASZ WALKE Z MAŁPĄ Z WĄSEM--------")
            malpa()
            walka()
            print("Patrzysz na małpę która zalewa się krwią z triumfem")
            break
        elif inp=="NIE" or inp=="N":
            print("Ucieczka nie udana, musisz walczyć!")
            malpa()
            walka()
            break
        else:
            print("nie ma takiej opcji")
    print("Małpa padła z rozwaloną głową")
    print("Dalej idziesz i nic sie nie dzieje")
    print("idziesz... idziesz ... idziesz ...")
    print("Widzisz jakąś złotą poświate za ostatnimi drzewami lasu")
    print("Podchodzisz w kierunku źródła tego światła")
    print("Otwórz/Zostaw")
    inp=input().upper()
    if inp =="OTWÓRZ":
        print(Fore.GREEN + 'A to ciekawe! Karabin, to chyba Scar. Widziałem tą broń w pradawnej grze "Fortnite"')
        if "scar" in guns:
            print("posiadasz już scara")
        else:
            guns.append("scar")
            print("bierzesz scara oraz 10 sztuk amunicji do plecaka")
            ammo+=10
    else:
        print("przechodzisz obok skrzynki")
        inp=input()
    print("Powoli kończy się las, a w oddali widzisz czubek wieży")
    print("Idziesz do wiezy, czy wracasz do statku Ide/Wracam")
    inp=input().upper()
    if inp =="IDE":
        print("Znajdujesz się przy wieży i czujesz zimne podmuchy powietrza")
        print("Czy dalej chcesz iść w tym kierunku? T/N?")
        inp=input().upper()
        if inp=="T":
            print("*Idziesz do wieży*")
            wieza()
        else:
            print("*Bezpiecznie wróciłeś pod statek*")
            obok_statku()
    elif inp=="WRACAM":
            print("*Bezpiecznie wracasz pod statek*")
            obok_statku()
    else:
        print("Nie mogąc się zdecydować, wróciłeś pod statek. W końcu tam bezpiecznie...")
        obok_statku()

def wieza():
    cum=False
    global straznik_wiezy,miasto_unlocked
    print("*Podbiega do ciebie strażnik wieży*")
    inp=input()
    print(Fore.RED + "GIŃ LUDZIAKU!!! WAAAAAGH")
    if straznik_wiezy:
        ork_nob()
        walka()
        straznik_wiezy=False
    print("*Przechodzisz przez drzwi wejsciowe wieży.*")
    print("Masz do wyboru trzy drogi: góra/dół lub powrót, którą wybierasz?")
    while True:
        inp=input().upper()
        if inp == "GÓRA":
            print("wchodzisz po schodach")
            inp=input()
            print(Fore.GREEN + "oooh! mało brakowało, prawie się poślizgnąłem!")
            inp=input()
            print("*rozglądasz się*")
            print("W oddali widzisz miasto ")
            miasto_unlocked=True
            print("*schodzisz z powrotem na dół*")
        elif inp == "DÓŁ":
            print("*schodzisz do podziemi po schodach*")
            inp=input()
            print("jesteś w lochach")
            if cum==False:
                print(Fore.GREEN + "Co to Kurwa jest?")
                print("*Patrzysz na obrzydliwego potwora składającego się z białej, śluzowatej i lepkiej cieczy*")
                inp=input()
                print(Fore.GREEN + "To monstrum strasznie się lepi! GRYZIE!!!")
                cummonster()
                walka()
                print("*znajdujesz skrzynke z cum pistolem*")
                cum=True
                if "cumpistol" in guns:
                    print("juz posiadasz ten rodzaj pistoletu")
                else:
                    guns.append("cumpistol")
            else:
                print("Nic tu więcej nie ma, oprócz białego kleistego śluzu")
        elif inp == "POWRÓT":
            las()
            break
        else:
            print("nie ma takiej opcji")
def miasto():
    print("Wchodzisz do miasta")
    print("Po obu stronach widzisz nieźle zachowane budynki, do którego idziesz?")
    inp=input()
    print("Po lewej stronie: <KARCZMA>")
    print("Po prawej stronie: <SKLEP> Z BRONIĄ")
    print("Przed tobą: <FORTECA>")
    inp=input().upper()
    if inp=="KARCZMA":
        karczma()
    elif inp =="SKLEP":
        sklep()
    elif inp =="FORTECA":
        forteca()
    else:
        print("Wiem, że nie jesteś kompasem, ale chyba pomyliłeś kierunki")
        miasto()
def karczma():
    global hp,maxhp,xp
    print(Fore.YELLOW + "SPRZEDAWCA: Witaj nieznajomy! Chcesz coś <kupić> czy pójśćć w <spanko> żeby zagoić rany? Możesz również <wyjść>")
    while True:
        inp=input().upper()
        if inp=="SPANKO":
            hp=maxhp
            print("*przespałeś się z orkiem(?)* Twoje hp wynosi teraz", maxhp)
            karczma()
            break
        elif inp=="KUPIĆ":
            print(Fore.YELLOW + "masz",przedmioty)
            if xp<0:
                print(Fore.YELLOW + "spadaj nie masz kasy")
                break

            else:
                print("masz",xp," xp, ale mozesz się lekko zadłużyć")
                a=input()
                print("-------------------cennik----------------------")
                print("==================jedzenie=====================")
                print("1.Fioletowe Jablko (hp)  - 5xp")
                print("2.Czarna Pomarańcza (aim)- 15xp")
                print("3.Żółw na tarczy (def)   - 30xp")
                print("4.Chipsy z orka (siła+10)- 30xp")
                print("===================PICIE=======================")
                print("5.Denaturat (siła+30) - 100xp")
                print("6.Łomża(maxhp)-30xp")
                print("7.WYJŚCIE")
                while xp>=0:
                    inp=str(input())
                    if inp=="1":
                        przedmioty.append("jablko")
                        print("pomyślnie zakupiłeś Fioletowe Jablko")
                        xp-=5
                    elif inp=="2":
                        przedmioty.append("czarna_pomarancza")
                        print("pomyślnie zakupiłeś Czarną Pomarańczę")
                        xp-=15
                    elif inp=="3":
                        przedmioty.append("zolw")
                        xp-=30
                        print("pomyślnie zakupiłeś Żółwia na tarczy")
                    elif inp=="4":
                        przedmioty.append("chipsy")
                        print("pomyślnie zakupiłeś Chipsy z orka")
                        xp-=30
                    elif inp=="5":
                        przedmioty.append("denaturat")
                        print("pomyślnie zakupiłeś Denaturat")
                        xp-=100
                    elif inp=="6":
                        przedmioty.append("lomza")
                        print("pomyślnie zakupiłeś Łomżę")
                        xp-=30
                    elif inp=="7":
                        print(Fore.GREEN + "Żegnaj")
                        print(Fore.YELLOW + "Do zobaczenia")
                        print(przedmioty)
                        break
                    else:
                        print(Fore.YELLOW + "nie ma takiego przedmiotu")
                else:
                    print("skończyły ci się pieniądze, wróciłeś do karczmy")
                    print(przedmioty)
                    karczma()
                    break

        elif inp=="WYJŚCIE" or "WYJŚĆ":
            miasto()
            break
        else:
            print("nie ma takiej opcji")

def chatka():
    print("Poszedłeś do zauważonej wcześniej chatki")
    print(".")
    print("Jesteś przed drzwiami chatki, 1.wchodzisz czy 2.rozglądasz się? Czy 3 Powrót pod statek")
    while True:
        inp=str(input())
        if inp == "1":
            print("Spotykasz znajomie wyglądającą postać o ciemnoskórej karnacji, oraz szczodrym zaroście")
            inp=input()
            print(Fore.YELLOW + "nieznajomy: الله عكبار الأم!")
            inp=input()
            print(Fore.GREEN + "yy.. Co?")
            inp=input()
            print(Fore.YELLOW + "Herbatki?")
            inp=str(input())
            if inp=="TAK":
                print("dobra herbatka leczy twoje wszystkie rany, oraz smutki i niepowodzenia w życiu")
                lomza()

            print("1.A tak w ogóle, to kim ty kurwa jesteś?")
            print("2.Umiesz po rozmawiać po terrańśku?")
            print("3.*skip*")
            inp=str(input())
            if inp == "1":
                print(Fore.GREEN + "A tak w ogóle, to kim ty kurwa jesteś?")
                inp=input()
                print(Fore.YELLOW + "Nieznajomy: Oh! A więc pochodzisz z najświętszej Terry!")
                inp=input()
                print(Fore.YELLOW + "Nieznajomy: Proszę mów mi Stasiek, nie wiesz jak dobrze ujrzeć drugiego człowieka")
                inp=input()
                print(Fore.GREEN + "A zatem opowiedz mi swoją historię, co tu robisz?")
                inp=input()
                print(Fore.YELLOW + "Stasiek: Sam nie wiem, tyle dni minęło... ")
                inp=input()
                print(Fore.YELLOW + "Stasiek: mówiąc w skrócie, byliśmy normalnymi mieszkańcami, dopóki jakiś wąsacz nie przybył i ni-")
                inp=input()
                print(Fore.GREEN + "chwila, chwila jaki wąsacz?")
                inp=input()
                print(Fore.YELLOW + "Stasiek: Przez orków zwany jest wielkim przywódcą, jak dla mnie to zwykły prostak")
                inp=input()
                print(Fore.YELLOW + "Stasiek: stylem przypomina Charliego Chaplina ze starożytnych okresów Terry")
                inp=input()
                print(Fore.YELLOW + "Stasiek: Przy okazji, zmienając temat.. znalazłem pistolet")
                inp=input()
                print(Fore.GREEN + "co? jaki pistolet?")
                inp=input()
                print(Fore.YELLOW + "Stasiek: W legendach mówiono, że jest to broń Bogów, zabije każdego bez wysiłku")
                inp=input()
                print(Fore.YELLOW + "Stasiek: Mółgbym ci go dać, jeśli odpowiesz mi na to pytanie: Podaj mi wzór na pole kwadratu (podpowiedź z potęgą)")
                inp=str(input()).upper
                if inp == "A^2":
                    print(Fore.YELLOW + "Stasiu: To by się zgadzało, oto twoja broń, używaj z rozwagą!")
                    print("otrzymujesz nową broń PODEJRZANY PISTOLET")
                    if "podejrzany_pistolet" in przedmioty:
                        print("juz posiadasz ten rodzaj pistoletu")
                    else:
                        przedmioty.append("podejrzany_pistolet")
                    print(Fore.YELLOW + "Stasiu: Podobno Hitler po II wojnie światowej użył go, aby zabić się użył tego pistoletu, ale słuch po jego ciele zaginął..")
                    print(Fore.YELLOW + "Stasiu: Nie chcę w to wierzyć, ale co jeśli Hitler żyje i to on przejął naszą planetę?")
                    print(Fore.YELLOW + "Stasiu: W końcu ta podróba Chaplina też mówi po szwabsku, na żołnierzy mówi blitzkriegorks..")
                    print(Fore.GREEN + "dzięki, bywaj")
                    print(Fore.YELLOW + "Stasiu: ja kurwa jestem, nie bywam")
                    print("Dowiadujesz się że tą planetą prawdopodobnie rządzi Hitler, powstała IV rzesza?")
            elif inp == "2":
                print(Fore.GREEN + "Umiesz po rozmawiać po terrańśku?")
                inp=input()
                print(Fore.YELLOW + "Nieznajomy: Na Imperatora, rodowity Terranin!")
                inp=input()
                print(Fore.YELLOW + "Nieznajomy: Pozwól, że się przedstawię, mam na imię Stasiek")
                inp=input()
                print(Fore.GREEN + "Nie czas na przyjemności, robiłem się jestem Inkwizytorem")
                inp=input()
                print(Fore.GREEN + "A zatem, Stachu co robisz na tym odludziu? Gdzie reszta mieszkańców?")
                inp=input()
                print(Fore.YELLOW + "Stasiek: Minęło kilka miesięcy od inwazji orków na nasze ziemie, mają nowego przywódcę...")
                inp=input()
                print(Fore.YELLOW + "Stasiek: mówiąc w skrócie, byliśmy normalnymi mieszkańcami, żyliśmy spokojnie... dopóki jakiś wąsaty kutas pojawił się z nikąd i ni-")
                inp=input()
                print(Fore.GREEN + "-gger Co? Wąsacz? Orkowie nie mają wąsów")
                inp=input()
                print(Fore.YELLOW + "Stasiek: Nie jest to ork, jest to człowiek, zwą go wielkim przywódcą...")
                print(Fore.YELLOW + "Stasiek: z wyglądu kogoś mi przypomina... Posiada charakterystyczny wąs")
                inp=input()
                print(Fore.GREEN + "Kogo ci przypomina? Cywilu")
                inp=input()
                print(Fore.YELLOW + "Stasiek: Hmm pomyślmy... Charliego Chaplina! Inkwizytorze, mam sprawę")
                inp=input()
                print(Fore.GREEN + "O co chodzi?")
                inp=input()
                print(Fore.YELLOW + "Stasiek: zmienając temat.. znalazłem pistolet... mógłby się Inkwizytorowi przydać")
                inp=input()
                print(Fore.GREEN + "cywilu, skąd macie pistolet?")
                inp=input()
                print(Fore.YELLOW + "Stasiek: Miasto zostało spustoszone, a ja znalazłem go w ruinach świątyni")
                print(Fore.YELLOW + "Stasiek: W legendach mówiono, że jest to broń Bogów, zabije każdego bez wysiłku")
                inp=input()
                print(Fore.YELLOW + "Stasiek: Mówią, że potrzeba wiedzy, by go skutecznie użyć")
                inp=input()
                print(Fore.YELLOW + "Stasiek: Mółgbym Panu go dać, jeśli odpowie mi Pan na to pytanie: Podaj mi wzór na pole kwadratu (podpowiedź z potęgą)")
                inp=str(input()).upper
                if inp == "A^2":
                    print(Fore.YELLOW + "Stasiu: Posiadasz wystarczającą wiedzę, by używać tego pistoletu!")
                    print(Fore.YELLOW + "Stasiu: To dla Ciebie Inkwizytorze!")
                    if "podejrzany_pistolet" in przedmioty:
                        print("juz posiadasz ten rodzaj pistoletu")
                    else:
                        przedmioty.append("podejrzany_pistolet")
                    print(Fore.YELLOW + "Stasiu: Podobno Hitler po II wojnie światowej aby zabić się użył tego pistoletu")
                    inp=input()
                    print(Fore.YELLOW + "Stasiu: Widocznie nie miał wiedzy, strzelił se w ten pusty łeb")
                    print(Fore.YELLOW + "Stasiu: Pózniej przejął naszą planetę i prowadzi brutalne rządy orkowie bez przerwy się biją,")
                    inp=input()
                    print(Fore.GREEN + "Uważaj na siebie, chwała Imperatorowi")
                    inp=input()
                    print(Fore.YELLOW + "Stasiu: Niech Imperator będzie z tobą Inkwizytorze")
                else:
                    print("niepoprawna odpowiedź")

            chatka()
            break
        elif inp == "2":
            print("*Rozglądasz się wokół spustoszonego świata...*")
            inp=input()
            print("Spoglądsz na chatkę, jednak po obejrzeniu jej z bliższego dystansu stwierdasz że prędzej możnaby ją nazwać meliną")
            print("*przebiega w tobie myśl: kurwa, jaki menel musi tam mieszkać, to jest po prostu jakaś tragedia!*")
            inp=input()
            print("Przypomina Ci się misja, ŚMIERĆ HERETYKOM!!!")
            inp=input()
            print("nagle dostrzegasz przez okno ciemnoskórego, brodatego humanoida")
            inp=input()
            print(Fore.GREEN + "czyli na tej planecie przebywają nie tylko nazistowskie grzyby...")
            chatka()
            break
        elif inp == "3":
            obok_statku()
        else:
            print("nie ma takiej opcji")
def sklep():
    global xp,ammo
    print(Fore.YELLOW + "SPRZEDAWCA: Dzień dobry co chciałbyś u nas kupić?")
    while xp>=0:
        print("masz dokładnie",xp,"xp")
        print("===================cennik=====================")
        print("1.RPG              - 150 xp      ")
        print("2.Snajperka        - 100 xp      ")
        print("3.Latające wąsy    - 200xp   ")
        print("4.rewolwer z oczami- 50xp ")
        print("5.amunicja x50     - 50xp ")
        print("6.wyjście")
        inp=str(input())
        if inp=="1":
            print("pomyślnie zakupiłeś RPG")
            guns.append("RPG")
            xp-=150
            print("zostało ci tyle",xp,"xp")
        elif inp=="2":
            print("pomyślno zakupiłeś Snajperkę")
            guns.append("Snajperka")
            xp-=150
            print("zostało ci tyle",xp,"xp")
        elif inp=="3":
            print("pomyślno zakupiłeś Latające wąsy")
            guns.append("Latajace Wasy")
            xp-=200
            print("zostało ci tyle",xp,"xp")
        elif inp=="4":
            print("pomyślno zakupiłeś rewolwer z oczami")
            guns.append("rewolwer")
            xp-=50
            print("zostało ci tyle",xp,"xp")
        elif inp=="5":
            print("pomyślno zakupiłeś amunicje x50")
            ammo=+50
            xp-=50
            print("zostało ci tyle",xp,"xp")
        elif inp=="6":
            print(Fore.YELLOW + "powodzenia !")
            print(Fore.GREEN + "Bywaj")
            miasto()
            break
        else:
            print(Fore.YELLOW + "nie mamy takiego produktu")

    else:
        print(Fore.YELLOW + "spadaj nie masz pieniedzy")
def forteca():
    print("*zbliżasz się do fortecy* Czujesz mrok i smród palonych ciał")
    if kanye:
        print("Widzisz z daleka pewną czarnoskórą osobę w masce")
    inp=input("Czy na pewno chcesz tam iść? <tak>/<nie>")
    while True:
        if inp=="tak":
            if kanye:
                print("gdy podchodzisz bliżej ta tajemnicza postac zdejmuje maske i mówi:")
                inp=input()
                print(Fore.RED + "Ja kocham wszystkich, mam dość segregacji, uważam że każdy człowiek ma w sobie coś wartościowego.")
                inp=input()
                print(Fore.RED + "PRZEDE WSZYSTKIM HITLER!!!!")
                inp=input()
                print("TO KANYE WEST")
                kanye_west()
                walka()
            else:
                print("*przechodzisz obok zwłok kanye westa i wchodzisz do fortecy*")
                print(Fore.GREEN + "ironia, chyba zabrakło mu oddechu")
            forteca_w_srodku()

        elif inp=="nie":
            miasto()
            break
        else:
            print("nie ma takiej opcji")

def sypialnia():
    global szafa,ammo
    szafa=True
    print("*wszedłeś do sypialni*")
    inp=input()
    print("widzisz szafe oraz łóżko")
    inp=input()
    print(Fore.RED + "WAAAAAGH, PORA LUDZIAKOFI ZROBIĆ BACH Z GUOWY")
    inp=input()
    print(Fore.GREEN + "CHOLERA! Mocno opancerzony ten ork..")
    ork_evyboy()
    walka()
    print(Fore.GREEN +"Gryzie glebę, ale było blisko. Teraz rozejrzę się po pokoju")
    print("najpierw patrzysz na <szafe>/<łóżko>")
    inp=input().upper()
    if inp=="SZAFE":
        print(Fore.GREEN + "Kto by się spodziewał, mundury ze swasstykami")
        inp=input()
        print(Fore.GREEN + "a co to?")
        inp=input()
        print(Fore.GREEN + "w lewym górnym rogu znalazła się amunicja ;D")
        if szafa:
            ammo+=100
            print("+100 amunicji. Twoja amunicja wynosi teraz",ammo)
            inp=input()
            print(Fore.GREEN + "Teraz musze zobaczyć co jest pod łóżkiem")
            inp=input()
            print("*spoglądasz pod łóżko i widzisz czyjąś ręke*")
            inp=input()
            print("BOO... pod łożkiem był upiór")
            duch()
            walka()
            print("Z jakże wielkim wysiłkiem pokonałeś upiora")
            print("Pod łózkiem znajodwała się skrzynia z amunicją")
            ammo+=10
            print("otrzymujesz 10 sztuk amunicj i masz",ammo)
            szafa=False
            forteca_w_srodku()
        else:
            print("nic tu juz nie ma")
            forteca_w_srodku()
    elif inp=="ŁÓŻKO":
        if szafa:
            print("*spoglądasz pod łóżko i widzisz czyjąś ręke*")
            inp=input()
            print("BOO... pod łożkiem był upiór")
            duch()
            walka()
            print("Pokonałeś upiora, cóż za wyzwanie")
            print("Pod łóżkiem znajdowała się skrzynia z amunicją")
            inp=input()
            print("otrzymujesz +100 sztuk amunicji")
            ammo+=100
            print(Fore.GREEN + "nie no, teraz muszę zobaczyć, co jest w szafie")
            inp=input()
            print(Fore.GREEN +  "wow jakie ładne ubrania")
            inp=input()
            print(Fore.GREEN  + "Same mundury *hatfu*")
            inp=input()
            print(Fore.GREEN + "a co to?")
            inp=input()
            print("*w lewym górnym rogu znalazła się amunicja*")
            ammo+=10
            print("+10 amunicji. Twoja amunicja wynosi teraz",ammo)
            szafa=False
            forteca_w_srodku()
        else:
            print("nic tu juz nie ma")
            forteca_w_srodku()
    else:
        print("Dopadł cię Orkowy ciężki zbrojny chłopak!")
        inp=input()
        print(Fore.RED + "WAAAAAAAA, ja być duży i zielony!")
        sypialnia()
def kuchnia():
    print("*Wchodzisz do kuchni*")
    print("Widzisz rozrzucone i pobite talerze na ziemii")
    inp=input()
    print(Fore.GREEN + "Oho, ktoś tu był...")
    inp=input()
    print("Twoim oczom ukazuje się kobieta!")
    inp=input()
    print(Fore.RED + "jestem królową tego miejsca!")
    kobieta()
    walka()
    print("*kobieta pada na ziemię*")
    print(Fore.GREEN + "ha, women, idealnie na swoim miejscu... czyli w kuchni")

    inp=input().upper()
    forteca_w_srodku()

##############################################################GRA WŁAŚCIWA####################################################################
intro_gry()
kreator_postaci()
statek()

#POPRAW CHATKĘ