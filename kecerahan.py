import optparse, os, sys, time

if sys.platform in ['linux', 'linux2']:
    bred = '\033[1;31m'
    bgren = '\033[1;32m'
    white = '\033[0;37m'
else:
    bred = ''
    bgren = ''
    white = ''

def help():
    help = '''    \npython3'''+sys.argv[0]+''' [OPTIONS] <%brightnes>
  --light     > Gunakan untuk mencerahkan atau meredupkan komputer linux

[CONTOH/EXAMPLES]
  python3 ''' +sys.argv[0]+ ''' --light 50%
  Jika masih kebingungan coba cek di deskripsi script ini di github\n'''
    print(help);sys.exit()
    
menu = optparse.OptionParser('yang bener')
menu.add_option('--light', dest='light')
(options, args) = menu.parse_args()
light = options.light

if light:
    try:
        print('\n [~] Mengecek File /sys/class/backlight/intel_backlight/brightness....'); time.sleep(1)
        fs = open('/sys/class/backlight/intel_backlight/brightness')
        fs.read()
        print (bgren+' [✔️] File ditemukan')
        print(bgren+' [✔️] Cahaya berhasil di ubah\n'+white)
    except FileNotFoundError: print(bred+' [!] FIle tidak ditemukan. Tools ini tidak support dengan system anda'+white);sys.exit()
    except SyntaxError: pass

    if light.lower() == '1%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("20")
if light:
    if light.lower() == '2%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("40")
if light:
    if light.lower() == '3%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("60")
if light:
    if light.lower() == '4%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("80")
if light:
    if light.lower() == '5%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("100")
if light:
    if light.lower() == '6%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("120")
if light:
    if light.lower() == '7%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("130")
if light:
    if light.lower() == '7%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("130")
if light:
    if light.lower() == '8%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("140")
if light:
    if light.lower() == '9%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("150")
if light:
    if light.lower() == '10%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("160")
if light:
    if light.lower() == '10%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("170")
if light:
    if light.lower() == '11%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("175")
if light:
    if light.lower() == '12%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("180")
if light:
    if light.lower() == '13%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("190")
if light:
    if light.lower() == '14%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("195")
if light:
    if light.lower() == '15%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("200")
if light:
    if light.lower() == '16%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("210")
if light:
    if light.lower() == '17%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("220")
if light:
    if light.lower() == '18%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("225")
if light:
    if light.lower() == '19%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("230")
if light:
    if light.lower() == '20%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("240")
if light:
    if light.lower() == '21%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("250")
if light:
    if light.lower() == '22%':
        with open ('//sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("255")
if light:
    if light.lower() == '23%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("260")
if light:
    if light.lower() == '24%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("270")
if light:
    if light.lower() == '25%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("280")
if light:
    if light.lower() == '26%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("290")
if light:
    if light.lower() == '27%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("295")
if light:
    if light.lower() == '28%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("300")
if light:
    if light.lower() == '29%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("310")
if light:
    if light.lower() == '30%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("320")
if light:
    if light.lower() == '31%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("330")
if light:
    if light.lower() == '32%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("340")
if light:
    if light.lower() == '33%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("350")
if light:
    if light.lower() == '34%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("360")
if light:
    if light.lower() == '35%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("370")
if light:
    if light.lower() == '36%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("380")
if light:
    if light.lower() == '37%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("390")
if light:
    if light.lower() == '38%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("400")
if light:
    if light.lower() == '39%':
        with open ('/root/tai.txt', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("410")
if light:
    if light.lower() == '40%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("420")
if light:
    if light.lower() == '41%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("430")
if light:
    if light.lower() == '42%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("440")
if light:
    if light.lower() == '43%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("450")
if light:
    if light.lower() == '44%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("460")
if light:
    if light.lower() == '45%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("470")
if light:
    if light.lower() == '45%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("480")
if light:
    if light.lower() == '46%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("490")
if light:
    if light.lower() == '47%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("500")
if light:
    if light.lower() == '48%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("510")
if light:
    if light.lower() == '49%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("520")
if light:
    if light.lower() == '50%':
        with open ('//sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("530")
if light:
    if light.lower() == '51%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("540")
if light:
    if light.lower() == '52%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("550")
if light:
    if light.lower() == '53%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("560")
if light:
    if light.lower() == '54%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("570")
if light:
    if light.lower() == '55%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("580")
if light:
    if light.lower() == '56%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("590")
if light:
    if light.lower() == '57%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("600")
if light:
    if light.lower() == '58%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("610")
if light:
    if light.lower() == '59%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("620")
if light:
    if light.lower() == '60%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("630")
if light:
    if light.lower() == '61%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("640")
if light:
    if light.lower() == '62%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("650")
if light:
    if light.lower() == '63%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("660")
if light:
    if light.lower() == '64%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("670")
if light:
    if light.lower() == '65%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("680")
if light:
    if light.lower() == '66%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("690")
if light:
    if light.lower() == '67%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("700")
if light:
    if light.lower() == '68%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("710")
if light:
    if light.lower() == '69%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("720")
if light:
    if light.lower() == '70%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("730")
if light:
    if light.lower() == '71%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("740")
if light:
    if light.lower() == '72%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("750")
if light:
    if light.lower() == '73%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("760")
if light:
    if light.lower() == '74%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("770")
if light:
    if light.lower() == '75%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("780")
if light:
    if light.lower() == '76%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("790")
if light:
    if light.lower() == '77%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("800")
if light:
    if light.lower() == '78%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("810")
if light:
    if light.lower() == '79%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("820")
if light:
    if light.lower() == '80%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("830")
if light:
    if light.lower() == '81%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("840")
if light:
    if light.lower() == '82%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("850")
if light:
    if light.lower() == '83%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("860")
if light:
    if light.lower() == '84%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("870")
if light:
    if light.lower() == '85%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("880")
if light:
    if light.lower() == '86%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("890")
if light:
    if light.lower() == '87%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("900")
if light:
    if light.lower() == '88%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("910")
if light:
    if light.lower() == '89%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("920")
if light:
    if light.lower() == '90%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("930")
if light:
    if light.lower() == '91%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("940")
if light:
    if light.lower() == '92%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("950")
if light:
    if light.lower() == '93%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("960")
if light:
    if light.lower() == '94%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("970")
if light:
    if light.lower() == '95%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("980")
if light:
    if light.lower() == '96%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("990")
    if light.lower() == '97%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("1000")
    if light.lower() == '98%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("1500")
    if light.lower() == '99%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("2000")
    if light.lower() == '100%':
        with open ('/sys/class/backlight/intel_backlight/brightness', 'r+') as file:
            file.truncate(0)
            old = file.read()
            file.seek(0)
            file.write("2500")
else:
    print(menu.usage)