#!/usr/bin/env python3
"""
Generate all 20 country eSIM pages for esim.win
Run: python3 generate.py
"""

UTM = "?utm_medium=wpam_id_702"

COUNTRIES = {
    "japan": {
        "name": "Japan", "flag": "🇯🇵", "slug": "japan",
        "desc": "Buy prepaid Japan eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Japan from $4.50.",
        "subtitle": "Stay connected across Japan. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304270278","calls":False},
            {"label":"3 GB","days":"5 days","price":"$6.90","perday":"$1.38/day","id":"3342690230013","calls":False},
            {"label":"5 GB","days":"7 days","price":"$7.90","perday":"$1.13/day","id":"3342690230020","calls":False},
            {"label":"10 GB","days":"15 days","price":"$9.90","perday":"$0.66/day","id":"3342690230037","calls":False,"badge":"Popular"},
            {"label":"20 GB","days":"30 days","price":"$19.90","perday":"$0.66/day","id":"3342604210018","calls":False},
            {"label":"30 GB","days":"30 days","price":"$29.90","perday":"$1.00/day","id":"3342604210025","calls":False},
            {"label":"Unlimited","days":"20 days","price":"$39.90","perday":"$2.00/day","id":"3342509220013","calls":False},
            {"label":"50 GB","days":"30 days","price":"$44.90","perday":"$1.50/day","id":"3342604210032","calls":False},
        ]
    },
    "thailand": {
        "name": "Thailand", "flag": "🇹🇭", "slug": "thailand",
        "desc": "Buy prepaid Thailand eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Thailand from $3.90.",
        "subtitle": "Stay connected across Thailand. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$3.90","perday":"$0.56/day","id":"3352405311555","calls":False},
            {"label":"3 GB","days":"30 days","price":"$4.90","perday":"$0.16/day","id":"3352405313269","calls":False},
            {"label":"5 GB","days":"30 days","price":"$7.90","perday":"$0.26/day","id":"3352405314976","calls":False},
            {"label":"Unlimited","days":"10 days","price":"$9.90","perday":"$0.99/day","id":"8893010230015","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$14.90","perday":"$0.50/day","id":"3352405316680","calls":False},
            {"label":"Unlimited","days":"15 days","price":"$19.90","perday":"$1.33/day","id":"8893010230022","calls":True},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3352405318394","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3352406131558","calls":False},
            {"label":"Unlimited","days":"30 days","price":"$34.90","perday":"$1.16/day","id":"8893010230023","calls":True},
            {"label":"50 GB","days":"60 days","price":"$49.90","perday":"$0.83/day","id":"3352406133262","calls":False,"badge":"Best Value"},
        ]
    },
    "usa": {
        "name": "USA", "flag": "🇺🇸", "slug": "usa",
        "desc": "Buy prepaid USA eSIM data plans. 5G coverage, instant activation, no roaming fees. Best eSIM deals for the United States from $4.50.",
        "subtitle": "Stay connected across the United States with 5G coverage. Instant activation via QR code.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"30 days","price":"$4.50","perday":"$0.15/day","id":"7842774018355","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312404252556","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404252730","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253300","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404253829","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409186139","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409186146","calls":False,"badge":"Best Value"},
        ]
    },
    "united-kingdom": {
        "name": "United Kingdom", "flag": "🇬🇧", "slug": "united-kingdom",
        "desc": "Buy prepaid UK eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for the United Kingdom from $4.50.",
        "subtitle": "Stay connected across the UK. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312303310074","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312404252631","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312303310081","calls":False},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253621","calls":False},
            {"label":"15 GB","days":"15 days","price":"$15.90","perday":"$1.06/day","id":"3526356063671","calls":False,"badge":"Popular"},
            {"label":"20 GB","days":"30 days","price":"$19.90","perday":"$0.66/day","id":"5052503100041","calls":True},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254154","calls":False},
            {"label":"75 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"5052503100034","calls":True},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409186108","calls":False},
            {"label":"150 GB","days":"30 days","price":"$29.90","perday":"$1.00/day","id":"5052503100027","calls":True,"badge":"Best Value"},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409186115","calls":False},
            {"label":"Unlimited","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"5052503100010","calls":True},
        ]
    },
    "south-korea": {
        "name": "South Korea", "flag": "🇰🇷", "slug": "south-korea",
        "desc": "Buy prepaid South Korea eSIM data plans. 5G coverage, instant activation, no roaming fees. Best eSIM deals for Korea from $4.50.",
        "subtitle": "Stay connected across South Korea with 5G coverage. Instant activation via QR code.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312305240010","calls":False},
            {"label":"3 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312305240027","calls":False},
            {"label":"5 GB","days":"30 days","price":"$9.90","perday":"$0.33/day","id":"3312404252853","calls":False},
            {"label":"Unlimited","days":"3 days","price":"$14.90","perday":"$4.97/day","id":"3341110230015","calls":False},
            {"label":"10 GB","days":"30 days","price":"$18.90","perday":"$0.63/day","id":"3312305240034","calls":False,"badge":"Popular"},
            {"label":"Unlimited","days":"5 days","price":"$19.90","perday":"$3.98/day","id":"3341110230022","calls":False},
            {"label":"Unlimited","days":"10 days","price":"$29.90","perday":"$2.99/day","id":"3341110230039","calls":False},
            {"label":"20 GB","days":"30 days","price":"$33.90","perday":"$1.13/day","id":"3312305240041","calls":False},
            {"label":"Unlimited","days":"20 days","price":"$39.90","perday":"$2.00/day","id":"3341110230046","calls":False},
            {"label":"Unlimited","days":"30 days","price":"$44.90","perday":"$1.50/day","id":"3341110230053","calls":False},
            {"label":"30 GB","days":"30 days","price":"$47.90","perday":"$1.60/day","id":"3312409185415","calls":False},
            {"label":"50 GB","days":"30 days","price":"$75.90","perday":"$2.53/day","id":"3312409185422","calls":False},
        ]
    },
    "united-arab-emirates": {
        "name": "United Arab Emirates", "flag": "🇦🇪", "slug": "united-arab-emirates",
        "desc": "Buy prepaid UAE eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Dubai & UAE from $4.50.",
        "subtitle": "Stay connected across the UAE including Dubai & Abu Dhabi. Instant activation via QR code.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312404252365","calls":False},
            {"label":"3 GB","days":"30 days","price":"$11.90","perday":"$0.40/day","id":"3312404252372","calls":False},
            {"label":"5 GB","days":"30 days","price":"$17.90","perday":"$0.60/day","id":"3312404252389","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$32.90","perday":"$1.10/day","id":"3312404252396","calls":False},
            {"label":"20 GB","days":"30 days","price":"$59.90","perday":"$2.00/day","id":"3312404252402","calls":False},
            {"label":"30 GB","days":"30 days","price":"$84.90","perday":"$2.83/day","id":"3312409186085","calls":False},
        ]
    },
    "australia": {
        "name": "Australia", "flag": "🇦🇺", "slug": "australia",
        "desc": "Buy prepaid Australia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Australia from $4.50.",
        "subtitle": "Stay connected across Australia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312303310050","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312404252570","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404252754","calls":False},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253324","calls":False,"badge":"Popular"},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404253843","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409180267","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409180274","calls":False,"badge":"Best Value"},
        ]
    },
    "singapore": {
        "name": "Singapore", "flag": "🇸🇬", "slug": "singapore",
        "desc": "Buy prepaid Singapore eSIM data plans. 5G coverage, instant activation, no roaming fees. Best eSIM deals for Singapore from $4.50.",
        "subtitle": "Stay connected in Singapore with 5G coverage. Instant activation via QR code.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405311425","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3352405313139","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405314846","calls":False},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3352405316550","calls":False,"badge":"Popular"},
            {"label":"Unlimited","days":"7 days","price":"$14.90","perday":"$2.13/day","id":"3342404110013","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3352405318264","calls":False},
            {"label":"Unlimited","days":"15 days","price":"$29.90","perday":"$1.99/day","id":"3342404110020","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3352406131428","calls":False},
            {"label":"50 GB","days":"60 days","price":"$49.90","perday":"$0.83/day","id":"3352406133132","calls":False,"badge":"Best Value"},
            {"label":"Unlimited","days":"30 days","price":"$54.90","perday":"$1.83/day","id":"3342404110037","calls":False},
        ]
    },
    "vietnam": {
        "name": "Vietnam", "flag": "🇻🇳", "slug": "vietnam",
        "desc": "Buy prepaid Vietnam eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Vietnam from $4.50.",
        "subtitle": "Stay connected across Vietnam. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312305240423","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312404252624","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404252945","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312305240430","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312305240447","calls":False},
            {"label":"30 GB","days":"30 days","price":"$32.90","perday":"$1.10/day","id":"3312409186306","calls":False},
            {"label":"50 GB","days":"30 days","price":"$51.90","perday":"$1.73/day","id":"3312409186313","calls":False,"badge":"Best Value"},
        ]
    },
    "indonesia": {
        "name": "Indonesia", "flag": "🇮🇩", "slug": "indonesia",
        "desc": "Buy prepaid Indonesia eSIM data plans. 5G coverage, instant activation, no roaming fees. Best eSIM deals for Bali & Indonesia from $4.50.",
        "subtitle": "Stay connected across Indonesia including Bali. Instant activation via QR code.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312305240225","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312409182667","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312305240249","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312305240256","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312409182674","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409182681","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409182698","calls":False,"badge":"Best Value"},
        ]
    },
    "mexico": {
        "name": "Mexico", "flag": "🇲🇽", "slug": "mexico",
        "desc": "Buy prepaid Mexico eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Mexico from $4.50.",
        "subtitle": "Stay connected across Mexico. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312404251962","calls":False},
            {"label":"3 GB","days":"30 days","price":"$8.90","perday":"$0.30/day","id":"3312404251979","calls":False},
            {"label":"5 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404251986","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404251993","calls":False},
            {"label":"20 GB","days":"31 days","price":"$39.90","perday":"$1.29/day","id":"3561292400796","calls":True},
            {"label":"20 GB","days":"30 days","price":"$44.90","perday":"$1.50/day","id":"3312404252006","calls":False},
            {"label":"30 GB","days":"30 days","price":"$63.90","perday":"$2.13/day","id":"3312409183695","calls":False},
            {"label":"50 GB","days":"30 days","price":"$99.90","perday":"$3.33/day","id":"3312409183701","calls":False},
        ]
    },
    "canada": {
        "name": "Canada", "flag": "🇨🇦", "slug": "canada",
        "desc": "Buy prepaid Canada eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Canada from $4.50.",
        "subtitle": "Stay connected across Canada. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405310299","calls":False},
            {"label":"3 GB","days":"30 days","price":"$7.90","perday":"$0.26/day","id":"3352405312002","calls":False},
            {"label":"5 GB","days":"30 days","price":"$11.90","perday":"$0.40/day","id":"3352405313719","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$21.90","perday":"$0.73/day","id":"3352405315423","calls":False},
            {"label":"20 GB","days":"30 days","price":"$40.90","perday":"$1.36/day","id":"3352405317137","calls":False},
            {"label":"30 GB","days":"30 days","price":"$57.90","perday":"$1.93/day","id":"3352406130292","calls":False},
            {"label":"50 GB","days":"60 days","price":"$91.90","perday":"$1.53/day","id":"3352406132005","calls":False,"badge":"Best Value"},
        ]
    },
    "turkey": {
        "name": "Turkey", "flag": "🇹🇷", "slug": "turkey",
        "desc": "Buy prepaid Turkey eSIM data plans. 5G coverage, instant activation, no roaming fees. Best eSIM deals for Turkey from $4.50.",
        "subtitle": "Stay connected across Turkey with 5G coverage. Instant activation via QR code.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304040017","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312404252518","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312304040024","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312304040031","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312304040048","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409185965","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409185972","calls":False,"badge":"Best Value"},
            {"label":"100 GB","days":"30 days","price":"$64.90","perday":"$2.16/day","id":"3312501290017","calls":False},
        ]
    },
    "france": {
        "name": "France", "flag": "🇫🇷", "slug": "france",
        "desc": "Buy prepaid France eSIM data plans. 5G coverage, instant activation, no roaming fees. Best eSIM deals for France from $4.50.",
        "subtitle": "Stay connected across France with 5G coverage. Instant activation via QR code.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312303200030","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312303310029","calls":False},
            {"label":"Unlimited","days":"3 days","price":"$9.90","perday":"$3.30/day","id":"3352408060030","calls":False},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253232","calls":False},
            {"label":"Unlimited","days":"7 days","price":"$14.90","perday":"$2.13/day","id":"3352408060047","calls":False},
            {"label":"15 GB","days":"15 days","price":"$15.90","perday":"$1.06/day","id":"3526356063671","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$21.90","perday":"$0.73/day","id":"8595106658537","calls":True},
            {"label":"20 GB","days":"15 days","price":"$23.90","perday":"$1.59/day","id":"3526356063672","calls":True},
            {"label":"20 GB","days":"31 days","price":"$28.90","perday":"$0.93/day","id":"3561292347756","calls":True},
            {"label":"20 GB","days":"30 days","price":"$29.90","perday":"$1.00/day","id":"8595106658538","calls":True},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409181806","calls":False},
            {"label":"30 GB","days":"30 days","price":"$32.90","perday":"$1.10/day","id":"3526356063683","calls":True},
            {"label":"60 GB","days":"30 days","price":"$39.90","perday":"$1.33/day","id":"3522405130016","calls":True,"badge":"Best Value"},
            {"label":"50 GB","days":"31 days","price":"$49.90","perday":"$1.61/day","id":"3561292346865","calls":True},
            {"label":"100 GB","days":"31 days","price":"$55.90","perday":"$1.80/day","id":"3561292400826","calls":True},
            {"label":"120 GB","days":"30 days","price":"$55.90","perday":"$1.86/day","id":"3526350133054","calls":True},
        ]
    },
    "italy": {
        "name": "Italy", "flag": "🇮🇹", "slug": "italy",
        "desc": "Buy prepaid Italy eSIM data plans. 5G coverage, instant activation, no roaming fees. Best eSIM deals for Italy from $4.50.",
        "subtitle": "Stay connected across Italy with 5G coverage. Instant activation via QR code.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304100261","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304100278","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312305220012","calls":False},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253454","calls":False},
            {"label":"15 GB","days":"15 days","price":"$15.90","perday":"$1.06/day","id":"3526356063671","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$21.90","perday":"$0.73/day","id":"8595106658537","calls":True},
            {"label":"20 GB","days":"15 days","price":"$23.90","perday":"$1.59/day","id":"3526356063672","calls":True},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404253966","calls":False},
            {"label":"20 GB","days":"31 days","price":"$28.90","perday":"$0.93/day","id":"3561292347756","calls":True},
            {"label":"20 GB","days":"30 days","price":"$29.90","perday":"$1.00/day","id":"8595106658538","calls":True},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312304100285","calls":False},
            {"label":"30 GB","days":"30 days","price":"$32.90","perday":"$1.10/day","id":"3526356063683","calls":True},
            {"label":"60 GB","days":"30 days","price":"$39.90","perday":"$1.33/day","id":"3522405130016","calls":True,"badge":"Best Value"},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409182803","calls":False},
            {"label":"50 GB","days":"31 days","price":"$49.90","perday":"$1.61/day","id":"3561292346865","calls":True},
            {"label":"100 GB","days":"31 days","price":"$55.90","perday":"$1.80/day","id":"3561292400826","calls":True},
            {"label":"120 GB","days":"30 days","price":"$55.90","perday":"$1.86/day","id":"3526350133054","calls":True},
        ]
    },
    "spain": {
        "name": "Spain", "flag": "🇪🇸", "slug": "spain",
        "desc": "Buy prepaid Spain eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Spain from $4.50.",
        "subtitle": "Stay connected across Spain. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304110178","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304110185","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404253102","calls":False},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253614","calls":False},
            {"label":"15 GB","days":"15 days","price":"$15.90","perday":"$1.06/day","id":"3526356063671","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$21.90","perday":"$0.73/day","id":"8595106658537","calls":True},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254147","calls":False},
            {"label":"20 GB","days":"31 days","price":"$28.90","perday":"$0.93/day","id":"3561292347756","calls":True},
            {"label":"20 GB","days":"30 days","price":"$29.90","perday":"$1.00/day","id":"8595106658538","calls":True},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312304110192","calls":False},
            {"label":"30 GB","days":"30 days","price":"$32.90","perday":"$1.10/day","id":"3526356063683","calls":True},
            {"label":"60 GB","days":"30 days","price":"$39.90","perday":"$1.33/day","id":"3522405130016","calls":True,"badge":"Best Value"},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409185439","calls":False},
            {"label":"50 GB","days":"31 days","price":"$49.90","perday":"$1.61/day","id":"3561292346865","calls":True},
            {"label":"100 GB","days":"31 days","price":"$55.90","perday":"$1.80/day","id":"3561292400826","calls":True},
            {"label":"120 GB","days":"30 days","price":"$55.90","perday":"$1.86/day","id":"3526350133054","calls":True},
        ]
    },
    "germany": {
        "name": "Germany", "flag": "🇩🇪", "slug": "germany",
        "desc": "Buy prepaid Germany eSIM data plans. 5G coverage, instant activation, no roaming fees. Best eSIM deals for Germany from $4.50.",
        "subtitle": "Stay connected across Germany with 5G coverage. Instant activation via QR code.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304100124","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304100131","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404253003","calls":False},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253515","calls":False},
            {"label":"15 GB","days":"15 days","price":"$15.90","perday":"$1.06/day","id":"3526356063671","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$21.90","perday":"$0.73/day","id":"8595106658537","calls":True},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254048","calls":False},
            {"label":"20 GB","days":"31 days","price":"$28.90","perday":"$0.93/day","id":"3561292347756","calls":True},
            {"label":"20 GB","days":"30 days","price":"$29.90","perday":"$1.00/day","id":"8595106658538","calls":True},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312304100148","calls":False},
            {"label":"30 GB","days":"30 days","price":"$32.90","perday":"$1.10/day","id":"3526356063683","calls":True},
            {"label":"60 GB","days":"30 days","price":"$39.90","perday":"$1.33/day","id":"3522405130016","calls":True,"badge":"Best Value"},
            {"label":"50 GB","days":"60 days","price":"$49.90","perday":"$0.83/day","id":"3312306230027","calls":False},
            {"label":"50 GB","days":"31 days","price":"$49.90","perday":"$1.61/day","id":"3561292346865","calls":True},
            {"label":"100 GB","days":"31 days","price":"$55.90","perday":"$1.80/day","id":"3561292400826","calls":True},
            {"label":"120 GB","days":"30 days","price":"$55.90","perday":"$1.86/day","id":"3526350133054","calls":True},
        ]
    },
    "philippines": {
        "name": "Philippines", "flag": "🇵🇭", "slug": "philippines",
        "desc": "Buy prepaid Philippines eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for the Philippines from $4.50.",
        "subtitle": "Stay connected across the Philippines. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405311241","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3352405312958","calls":False},
            {"label":"5 GB","days":"30 days","price":"$7.90","perday":"$0.26/day","id":"3352405314662","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$14.90","perday":"$0.50/day","id":"3352405316376","calls":False},
            {"label":"20 GB","days":"30 days","price":"$26.90","perday":"$0.90/day","id":"3352405318080","calls":False},
            {"label":"30 GB","days":"30 days","price":"$38.90","perday":"$1.30/day","id":"3352406131244","calls":False},
            {"label":"50 GB","days":"60 days","price":"$60.90","perday":"$1.02/day","id":"3352406132951","calls":False,"badge":"Best Value"},
        ]
    },
    "india": {
        "name": "India", "flag": "🇮🇳", "slug": "india",
        "desc": "Buy prepaid India eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for India from $4.50.",
        "subtitle": "Stay connected across India. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312303310067","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312404252532","calls":False},
            {"label":"5 GB","days":"30 days","price":"$7.90","perday":"$0.26/day","id":"3312404252662","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$14.90","perday":"$0.50/day","id":"3312404253249","calls":False},
            {"label":"20 GB","days":"30 days","price":"$26.90","perday":"$0.90/day","id":"3312404253768","calls":False},
            {"label":"30 GB","days":"30 days","price":"$37.90","perday":"$1.26/day","id":"3312409182643","calls":False},
            {"label":"50 GB","days":"30 days","price":"$59.90","perday":"$2.00/day","id":"3312409182650","calls":False},
        ]
    },
    "brazil": {
        "name": "Brazil", "flag": "🇧🇷", "slug": "brazil",
        "desc": "Buy prepaid Brazil eSIM data plans. 5G coverage, instant activation, no roaming fees. Best eSIM deals for Brazil from $4.50.",
        "subtitle": "Stay connected across Brazil with 5G coverage. Instant activation via QR code.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405310237","calls":False},
            {"label":"3 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405311944","calls":False},
            {"label":"5 GB","days":"30 days","price":"$10.90","perday":"$0.36/day","id":"3352405313658","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$19.90","perday":"$0.66/day","id":"3352405315362","calls":False},
            {"label":"20 GB","days":"30 days","price":"$35.90","perday":"$1.20/day","id":"3352405317076","calls":False},
            {"label":"20 GB","days":"31 days","price":"$39.90","perday":"$1.29/day","id":"3561292400796","calls":True},
            {"label":"30 GB","days":"30 days","price":"$50.90","perday":"$1.70/day","id":"3352406130230","calls":False},
            {"label":"50 GB","days":"60 days","price":"$80.90","perday":"$1.35/day","id":"3352406131947","calls":False,"badge":"Best Value"},
        ]
    },
    # ── Asia ─────────────────────────────────────────────────────────────────
    "malaysia": {
        "name": "Malaysia", "flag": "🇲🇾", "slug": "malaysia",
        "desc": "Buy prepaid Malaysia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Malaysia from $4.50.",
        "subtitle": "Stay connected across Malaysia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312305240270","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312305240287","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404252877","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312305240294","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312305240300","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409183404","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409183411","calls":False,"badge":"Best Value"},
        ]
    },
    "taiwan": {
        "name": "Taiwan", "flag": "🇹🇼", "slug": "taiwan",
        "desc": "Buy prepaid Taiwan eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Taiwan from $4.50.",
        "subtitle": "Stay connected across Taiwan. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312305240188","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312305240195","calls":False},
            {"label":"5 GB","days":"30 days","price":"$7.90","perday":"$0.26/day","id":"3312404252822","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$14.90","perday":"$0.50/day","id":"3312305240201","calls":False},
            {"label":"20 GB","days":"30 days","price":"$26.90","perday":"$0.90/day","id":"3312305240218","calls":False},
            {"label":"30 GB","days":"30 days","price":"$37.90","perday":"$1.26/day","id":"3312409185651","calls":False},
            {"label":"50 GB","days":"30 days","price":"$59.90","perday":"$2.00/day","id":"3312409185668","calls":False,"badge":"Best Value"},
        ]
    },
    "hong-kong": {
        "name": "Hong Kong", "flag": "🇭🇰", "slug": "hong-kong",
        "desc": "Buy prepaid Hong Kong eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Hong Kong from $4.50.",
        "subtitle": "Stay connected across Hong Kong. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304270209","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304270216","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404253188","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253706","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254246","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409182582","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409182599","calls":False,"badge":"Best Value"},
        ]
    },
    "china": {
        "name": "China", "flag": "🇨🇳", "slug": "china",
        "desc": "Buy prepaid China eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for China from $4.50.",
        "subtitle": "Stay connected across China. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304270100","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3342604210056","calls":False},
            {"label":"5 GB","days":"30 days","price":"$7.90","perday":"$0.26/day","id":"3342604210063","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$11.90","perday":"$0.40/day","id":"3342604210070","calls":False},
            {"label":"20 GB","days":"30 days","price":"$21.90","perday":"$0.73/day","id":"3341810230063","calls":False},
            {"label":"30 GB","days":"30 days","price":"$29.90","perday":"$1.00/day","id":"3342604210087","calls":False},
            {"label":"50 GB","days":"30 days","price":"$44.90","perday":"$1.50/day","id":"3342604210049","calls":False,"badge":"Best Value"},
        ]
    },
    "new-zealand": {
        "name": "New Zealand", "flag": "🇳🇿", "slug": "new-zealand",
        "desc": "Buy prepaid New Zealand eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for New Zealand from $4.50.",
        "subtitle": "Stay connected across New Zealand. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405311128","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3352405312835","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405314549","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3352405316253","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3352405317960","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3352406131121","calls":False},
            {"label":"50 GB","days":"60 days","price":"$49.90","perday":"$0.83/day","id":"3352406132838","calls":False,"badge":"Best Value"},
        ]
    },
    "sri-lanka": {
        "name": "Sri Lanka", "flag": "🇱🇰", "slug": "sri-lanka",
        "desc": "Buy prepaid Sri Lanka eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Sri Lanka from $4.50.",
        "subtitle": "Stay connected across Sri Lanka. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405311487","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3352405313191","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405314907","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3352405316611","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3352405318325","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3352406131480","calls":False},
            {"label":"50 GB","days":"60 days","price":"$49.90","perday":"$0.83/day","id":"3352406133194","calls":False,"badge":"Best Value"},
        ]
    },
    "cambodia": {
        "name": "Cambodia", "flag": "🇰🇭", "slug": "cambodia",
        "desc": "Buy prepaid Cambodia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Cambodia from $4.50.",
        "subtitle": "Stay connected across Cambodia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405310275","calls":False},
            {"label":"3 GB","days":"30 days","price":"$7.90","perday":"$0.26/day","id":"3352405311982","calls":False},
            {"label":"5 GB","days":"30 days","price":"$11.90","perday":"$0.40/day","id":"3352405313696","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$21.90","perday":"$0.73/day","id":"3352405315409","calls":False},
            {"label":"20 GB","days":"30 days","price":"$39.90","perday":"$1.33/day","id":"3352405317113","calls":False},
            {"label":"30 GB","days":"30 days","price":"$56.90","perday":"$1.90/day","id":"3352406130278","calls":False},
            {"label":"50 GB","days":"60 days","price":"$89.90","perday":"$1.50/day","id":"3352406131985","calls":False,"badge":"Best Value"},
        ]
    },
    "bangladesh": {
        "name": "Bangladesh", "flag": "🇧🇩", "slug": "bangladesh",
        "desc": "Buy prepaid Bangladesh eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Bangladesh from $4.50.",
        "subtitle": "Stay connected across Bangladesh. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405310152","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3352405311869","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405313573","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3352405315287","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3352405316994","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3352406130155","calls":False},
            {"label":"50 GB","days":"60 days","price":"$49.90","perday":"$0.83/day","id":"3352406131862","calls":False,"badge":"Best Value"},
        ]
    },
    "nepal": {
        "name": "Nepal", "flag": "🇳🇵", "slug": "nepal",
        "desc": "Buy prepaid Nepal eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Nepal from $4.90.",
        "subtitle": "Stay connected across Nepal. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.90","perday":"$0.70/day","id":"3352405311098","calls":False},
            {"label":"3 GB","days":"30 days","price":"$14.90","perday":"$0.50/day","id":"3352405312804","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$22.90","perday":"$0.76/day","id":"3352405314518","calls":False},
            {"label":"10 GB","days":"30 days","price":"$42.90","perday":"$1.43/day","id":"3352405316222","calls":False},
            {"label":"20 GB","days":"30 days","price":"$78.90","perday":"$2.63/day","id":"3352405317939","calls":False,"badge":"Best Value"},
        ]
    },
    "maldives": {
        "name": "Maldives", "flag": "🇲🇻", "slug": "maldives",
        "desc": "Buy prepaid Maldives eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Maldives from $9.90.",
        "subtitle": "Stay connected across the Maldives. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$9.90","perday":"$1.41/day","id":"3312404255458","calls":False},
            {"label":"3 GB","days":"30 days","price":"$27.90","perday":"$0.93/day","id":"3312409183428","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$43.90","perday":"$1.46/day","id":"3312409183435","calls":False,"badge":"Best Value"},
        ]
    },
    "mongolia": {
        "name": "Mongolia", "flag": "🇲🇳", "slug": "mongolia",
        "desc": "Buy prepaid Mongolia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Mongolia from $5.90.",
        "subtitle": "Stay connected across Mongolia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3352405311036","calls":False},
            {"label":"3 GB","days":"30 days","price":"$16.90","perday":"$0.56/day","id":"3352405312743","calls":False},
            {"label":"5 GB","days":"30 days","price":"$25.90","perday":"$0.86/day","id":"3352405314457","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3352405316161","calls":False,"badge":"Best Value"},
            {"label":"20 GB","days":"30 days","price":"$91.90","perday":"$3.06/day","id":"3352405317878","calls":False},
        ]
    },
    # ── Middle East & Africa ──────────────────────────────────────────────────
    "saudi-arabia": {
        "name": "Saudi Arabia", "flag": "🇸🇦", "slug": "saudi-arabia",
        "desc": "Buy prepaid Saudi Arabia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Saudi Arabia from $4.50.",
        "subtitle": "Stay connected across Saudi Arabia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405311371","calls":False},
            {"label":"3 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405313085","calls":False},
            {"label":"5 GB","days":"30 days","price":"$10.90","perday":"$0.36/day","id":"3352405314792","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$19.90","perday":"$0.66/day","id":"3352405316505","calls":False},
            {"label":"20 GB","days":"30 days","price":"$36.90","perday":"$1.23/day","id":"3352405318219","calls":False},
            {"label":"30 GB","days":"30 days","price":"$52.90","perday":"$1.76/day","id":"3352406131374","calls":False},
            {"label":"50 GB","days":"60 days","price":"$83.90","perday":"$1.40/day","id":"3352406133088","calls":False,"badge":"Best Value"},
        ]
    },
    "israel": {
        "name": "Israel", "flag": "🇮🇱", "slug": "israel",
        "desc": "Buy prepaid Israel eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Israel from $4.50.",
        "subtitle": "Stay connected across Israel. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304270223","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304270230","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312304270247","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312304270254","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312304270261","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409182780","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409182797","calls":False,"badge":"Best Value"},
        ]
    },
    "jordan": {
        "name": "Jordan", "flag": "🇯🇴", "slug": "jordan",
        "desc": "Buy prepaid Jordan eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Jordan from $4.90.",
        "subtitle": "Stay connected across Jordan. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.90","perday":"$0.70/day","id":"3312404250514","calls":False},
            {"label":"3 GB","days":"30 days","price":"$13.90","perday":"$0.46/day","id":"3312404250521","calls":False},
            {"label":"5 GB","days":"30 days","price":"$20.90","perday":"$0.70/day","id":"3312404250538","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$38.90","perday":"$1.30/day","id":"3312404250545","calls":False},
            {"label":"20 GB","days":"30 days","price":"$71.90","perday":"$2.40/day","id":"3312404250552","calls":False},
            {"label":"30 GB","days":"30 days","price":"$101.90","perday":"$3.40/day","id":"3312409182957","calls":False,"badge":"Best Value"},
        ]
    },
    "egypt": {
        "name": "Egypt", "flag": "🇪🇬", "slug": "egypt",
        "desc": "Buy prepaid Egypt eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Egypt from $4.50.",
        "subtitle": "Stay connected across Egypt. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405310473","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3352405312187","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405313894","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3352405315607","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3352405317311","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3352406130476","calls":False},
            {"label":"50 GB","days":"60 days","price":"$49.90","perday":"$0.83/day","id":"3352406132180","calls":False,"badge":"Best Value"},
        ]
    },
    "morocco": {
        "name": "Morocco", "flag": "🇲🇦", "slug": "morocco",
        "desc": "Buy prepaid Morocco eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Morocco from $4.50.",
        "subtitle": "Stay connected across Morocco. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312404252013","calls":False},
            {"label":"3 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404252020","calls":False},
            {"label":"5 GB","days":"30 days","price":"$10.90","perday":"$0.36/day","id":"3312404252037","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$19.90","perday":"$0.66/day","id":"3312404252044","calls":False},
            {"label":"20 GB","days":"30 days","price":"$36.90","perday":"$1.23/day","id":"3312404252051","calls":False},
            {"label":"30 GB","days":"30 days","price":"$51.90","perday":"$1.73/day","id":"3312409183923","calls":False,"badge":"Best Value"},
        ]
    },
    "south-africa": {
        "name": "South Africa", "flag": "🇿🇦", "slug": "south-africa",
        "desc": "Buy prepaid South Africa eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for South Africa from $4.50.",
        "subtitle": "Stay connected across South Africa. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405311456","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3352405313160","calls":False},
            {"label":"5 GB","days":"30 days","price":"$9.90","perday":"$0.33/day","id":"3352405314877","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$17.90","perday":"$0.60/day","id":"3352405316581","calls":False},
            {"label":"20 GB","days":"30 days","price":"$32.90","perday":"$1.10/day","id":"3352405318295","calls":False},
            {"label":"30 GB","days":"30 days","price":"$46.90","perday":"$1.56/day","id":"3352406131459","calls":False},
            {"label":"50 GB","days":"60 days","price":"$73.90","perday":"$1.23/day","id":"3352406133163","calls":False,"badge":"Best Value"},
        ]
    },
    "kenya": {
        "name": "Kenya", "flag": "🇰🇪", "slug": "kenya",
        "desc": "Buy prepaid Kenya eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Kenya from $5.90.",
        "subtitle": "Stay connected across Kenya. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3312404251764","calls":False},
            {"label":"3 GB","days":"30 days","price":"$13.90","perday":"$0.46/day","id":"3312404251771","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$21.90","perday":"$0.73/day","id":"3312404251788","calls":False},
            {"label":"10 GB","days":"30 days","price":"$40.90","perday":"$1.36/day","id":"3312404251795","calls":False},
            {"label":"20 GB","days":"30 days","price":"$74.90","perday":"$2.50/day","id":"3312404251801","calls":False},
            {"label":"30 GB","days":"30 days","price":"$106.90","perday":"$3.56/day","id":"3312409182995","calls":False,"badge":"Best Value"},
        ]
    },
    "nigeria": {
        "name": "Nigeria", "flag": "🇳🇬", "slug": "nigeria",
        "desc": "Buy prepaid Nigeria eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Nigeria from $4.50.",
        "subtitle": "Stay connected across Nigeria. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405311159","calls":False},
            {"label":"3 GB","days":"30 days","price":"$11.90","perday":"$0.40/day","id":"3352405312866","calls":False},
            {"label":"5 GB","days":"30 days","price":"$17.90","perday":"$0.60/day","id":"3352405314570","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$34.90","perday":"$1.16/day","id":"3352405316284","calls":False},
            {"label":"20 GB","days":"30 days","price":"$63.90","perday":"$2.13/day","id":"3352405317991","calls":False},
            {"label":"30 GB","days":"30 days","price":"$90.90","perday":"$3.03/day","id":"3352406131152","calls":False,"badge":"Best Value"},
        ]
    },
    "qatar": {
        "name": "Qatar", "flag": "🇶🇦", "slug": "qatar",
        "desc": "Buy prepaid Qatar eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Qatar from $4.50.",
        "subtitle": "Stay connected across Qatar. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405311289","calls":False},
            {"label":"3 GB","days":"30 days","price":"$9.90","perday":"$0.33/day","id":"3352405312996","calls":False},
            {"label":"5 GB","days":"30 days","price":"$15.90","perday":"$0.53/day","id":"3352405314709","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$29.90","perday":"$1.00/day","id":"3352405316413","calls":False},
            {"label":"20 GB","days":"30 days","price":"$47.90","perday":"$1.60/day","id":"3352405318127","calls":False},
            {"label":"50 GB","days":"30 days","price":"$59.90","perday":"$2.00/day","id":"3312409184722","calls":False,"badge":"Best Value"},
        ]
    },
    "kuwait": {
        "name": "Kuwait", "flag": "🇰🇼", "slug": "kuwait",
        "desc": "Buy prepaid Kuwait eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Kuwait from $4.50.",
        "subtitle": "Stay connected across Kuwait. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312404250613","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312404250620","calls":False},
            {"label":"5 GB","days":"30 days","price":"$7.90","perday":"$0.26/day","id":"3312404250637","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$13.90","perday":"$0.46/day","id":"3312404250644","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404250651","calls":False},
            {"label":"30 GB","days":"30 days","price":"$34.90","perday":"$1.16/day","id":"3312409183138","calls":False},
            {"label":"50 GB","days":"30 days","price":"$54.90","perday":"$1.83/day","id":"3312409183145","calls":False,"badge":"Best Value"},
        ]
    },
    "bahrain": {
        "name": "Bahrain", "flag": "🇧🇭", "slug": "bahrain",
        "desc": "Buy prepaid Bahrain eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Bahrain from $4.50.",
        "subtitle": "Stay connected across Bahrain. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405310145","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3352405311852","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405313566","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3352405315270","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3352405316987","calls":False},
            {"label":"30 GB","days":"30 days","price":"$32.90","perday":"$1.10/day","id":"3352406130148","calls":False},
            {"label":"50 GB","days":"60 days","price":"$51.90","perday":"$0.87/day","id":"3352406131855","calls":False,"badge":"Best Value"},
        ]
    },
    "pakistan": {
        "name": "Pakistan", "flag": "🇵🇰", "slug": "pakistan",
        "desc": "Buy prepaid Pakistan eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Pakistan from $4.50.",
        "subtitle": "Stay connected across Pakistan. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405311180","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3352405312897","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405314600","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3352405316314","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3352405318028","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3352406131183","calls":False},
            {"label":"50 GB","days":"60 days","price":"$49.90","perday":"$0.83/day","id":"3352406132890","calls":False,"badge":"Best Value"},
        ]
    },
    # ── Americas ──────────────────────────────────────────────────────────────
    "argentina": {
        "name": "Argentina", "flag": "🇦🇷", "slug": "argentina",
        "desc": "Buy prepaid Argentina eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Argentina from $7.90.",
        "subtitle": "Stay connected across Argentina. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$7.90","perday":"$1.13/day","id":"3352405310084","calls":False},
            {"label":"3 GB","days":"30 days","price":"$15.90","perday":"$0.53/day","id":"3352405311791","calls":False},
            {"label":"5 GB","days":"30 days","price":"$25.90","perday":"$0.86/day","id":"3352405313504","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3352405315218","calls":False},
            {"label":"Unlimited","days":"7 days","price":"$54.90","perday":"$7.84/day","id":"3342404100014","calls":False,"badge":"Popular"},
            {"label":"50 GB","days":"30 days","price":"$86.90","perday":"$2.90/day","id":"3312409180182","calls":False,"badge":"Best Value"},
            {"label":"Unlimited","days":"15 days","price":"$79.90","perday":"$5.33/day","id":"3342404100021","calls":False},
            {"label":"Unlimited","days":"30 days","price":"$119.90","perday":"$4.00/day","id":"3342404100038","calls":False,"badge":"Best Value"},
        ]
    },
    "chile": {
        "name": "Chile", "flag": "🇨🇱", "slug": "chile",
        "desc": "Buy prepaid Chile eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Chile from $4.50.",
        "subtitle": "Stay connected across Chile. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405310336","calls":False},
            {"label":"3 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405312040","calls":False},
            {"label":"5 GB","days":"30 days","price":"$10.90","perday":"$0.36/day","id":"3352405313757","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$19.90","perday":"$0.66/day","id":"3352405315461","calls":False},
            {"label":"20 GB","days":"30 days","price":"$36.90","perday":"$1.23/day","id":"3352405317175","calls":False},
            {"label":"30 GB","days":"30 days","price":"$51.90","perday":"$1.73/day","id":"3352406130339","calls":False},
            {"label":"50 GB","days":"60 days","price":"$82.90","perday":"$1.38/day","id":"3352406132043","calls":False,"badge":"Best Value"},
        ]
    },
    "colombia": {
        "name": "Colombia", "flag": "🇨🇴", "slug": "colombia",
        "desc": "Buy prepaid Colombia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Colombia from $5.90.",
        "subtitle": "Stay connected across Colombia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3312404251566","calls":False},
            {"label":"3 GB","days":"30 days","price":"$15.90","perday":"$0.53/day","id":"3312404251573","calls":False},
            {"label":"5 GB","days":"30 days","price":"$23.90","perday":"$0.80/day","id":"3312404251580","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$45.90","perday":"$1.53/day","id":"3312404251597","calls":False},
            {"label":"20 GB","days":"30 days","price":"$82.90","perday":"$2.76/day","id":"3312404251603","calls":False},
            {"label":"30 GB","days":"30 days","price":"$118.90","perday":"$3.96/day","id":"3312409181240","calls":False,"badge":"Best Value"},
        ]
    },
    "peru": {
        "name": "Peru", "flag": "🇵🇪", "slug": "peru",
        "desc": "Buy prepaid Peru eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Peru from $4.50.",
        "subtitle": "Stay connected across Peru. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312404252167","calls":False},
            {"label":"3 GB","days":"30 days","price":"$8.90","perday":"$0.30/day","id":"3312404252174","calls":False},
            {"label":"5 GB","days":"30 days","price":"$13.90","perday":"$0.46/day","id":"3312404252181","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404252198","calls":False},
            {"label":"20 GB","days":"30 days","price":"$45.90","perday":"$1.53/day","id":"3312404252204","calls":False},
            {"label":"30 GB","days":"30 days","price":"$64.90","perday":"$2.16/day","id":"3312409184630","calls":False},
            {"label":"50 GB","days":"30 days","price":"$102.90","perday":"$3.43/day","id":"3312409184647","calls":False,"badge":"Best Value"},
        ]
    },
    "costa-rica": {
        "name": "Costa Rica", "flag": "🇨🇷", "slug": "costa-rica",
        "desc": "Buy prepaid Costa Rica eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Costa Rica from $4.50.",
        "subtitle": "Stay connected across Costa Rica. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405310381","calls":False},
            {"label":"3 GB","days":"30 days","price":"$7.90","perday":"$0.26/day","id":"3352405312095","calls":False},
            {"label":"5 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3352405313801","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$23.90","perday":"$0.80/day","id":"3352405315515","calls":False},
            {"label":"20 GB","days":"30 days","price":"$43.90","perday":"$1.46/day","id":"3352405317229","calls":False},
            {"label":"30 GB","days":"30 days","price":"$62.90","perday":"$2.10/day","id":"3352406130384","calls":False},
            {"label":"50 GB","days":"60 days","price":"$99.90","perday":"$1.67/day","id":"3352406132098","calls":False,"badge":"Best Value"},
        ]
    },
    "dominican-republic": {
        "name": "Dominican Republic", "flag": "🇩🇴", "slug": "dominican-republic",
        "desc": "Buy prepaid Dominican Republic eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $7.90.",
        "subtitle": "Stay connected across Dominican Republic. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$7.90","perday":"$1.13/day","id":"3312304050030","calls":False},
            {"label":"3 GB","days":"30 days","price":"$19.90","perday":"$0.66/day","id":"3312304050047","calls":False},
            {"label":"5 GB","days":"30 days","price":"$30.90","perday":"$1.03/day","id":"3312404252723","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$58.90","perday":"$1.96/day","id":"3312404253294","calls":False},
            {"label":"20 GB","days":"30 days","price":"$106.90","perday":"$3.56/day","id":"3312404253812","calls":False,"badge":"Best Value"},
        ]
    },
    "puerto-rico": {
        "name": "Puerto Rico", "flag": "🇵🇷", "slug": "puerto-rico",
        "desc": "Buy prepaid Puerto Rico eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Puerto Rico from $4.90.",
        "subtitle": "Stay connected across Puerto Rico. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.90","perday":"$0.70/day","id":"3312404250910","calls":False},
            {"label":"3 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404250927","calls":False},
            {"label":"5 GB","days":"30 days","price":"$19.90","perday":"$0.66/day","id":"3312404250934","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$36.90","perday":"$1.23/day","id":"3312404250941","calls":False},
            {"label":"20 GB","days":"30 days","price":"$66.90","perday":"$2.23/day","id":"3312404250958","calls":False},
            {"label":"30 GB","days":"30 days","price":"$95.90","perday":"$3.20/day","id":"3312409184692","calls":False,"badge":"Best Value"},
        ]
    },
    # ── Europe (individual) ───────────────────────────────────────────────────
    "poland": {
        "name": "Poland", "flag": "🇵🇱", "slug": "poland",
        "desc": "Buy prepaid Poland eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Poland from $4.50.",
        "subtitle": "Stay connected across Poland. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405311258","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3352405312965","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405314679","calls":False},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3352405316383","calls":False},
            {"label":"15 GB","days":"15 days","price":"$15.90","perday":"$1.06/day","id":"3526356063671","calls":False,"badge":"Popular"},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3352405318097","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3352406131251","calls":False},
            {"label":"60 GB","days":"30 days","price":"$39.90","perday":"$1.33/day","id":"3522405130016","calls":True,"badge":"Best Value"},
            {"label":"50 GB","days":"60 days","price":"$49.90","perday":"$0.83/day","id":"3352406132968","calls":False},
        ]
    },
    "netherlands": {
        "name": "Netherlands", "flag": "🇳🇱", "slug": "netherlands",
        "desc": "Buy prepaid Netherlands eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Netherlands from $4.50.",
        "subtitle": "Stay connected across the Netherlands. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304100384","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304100391","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404253065","calls":False},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253577","calls":False},
            {"label":"15 GB","days":"15 days","price":"$15.90","perday":"$1.06/day","id":"3526356063671","calls":False,"badge":"Popular"},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254109","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312304100407","calls":False},
            {"label":"60 GB","days":"30 days","price":"$39.90","perday":"$1.33/day","id":"3522405130016","calls":True,"badge":"Best Value"},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409184173","calls":False},
        ]
    },
    "switzerland": {
        "name": "Switzerland", "flag": "🇨🇭", "slug": "switzerland",
        "desc": "Buy prepaid Switzerland eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Switzerland from $4.50.",
        "subtitle": "Stay connected across Switzerland. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405311524","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3352405313238","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405314945","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3352405316659","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3352405318363","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3352406131527","calls":False},
            {"label":"50 GB","days":"60 days","price":"$49.90","perday":"$0.83/day","id":"3352406133231","calls":False,"badge":"Best Value"},
        ]
    },
    "greece": {
        "name": "Greece", "flag": "🇬🇷", "slug": "greece",
        "desc": "Buy prepaid Greece eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Greece from $4.50.",
        "subtitle": "Stay connected across Greece. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304100179","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304100186","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404253010","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253522","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254055","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409182056","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409182063","calls":False,"badge":"Best Value"},
        ]
    },
    "portugal": {
        "name": "Portugal", "flag": "🇵🇹", "slug": "portugal",
        "desc": "Buy prepaid Portugal eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Portugal from $4.50.",
        "subtitle": "Stay connected across Portugal. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304100681","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304100698","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404253072","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253584","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254116","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312304100704","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409184685","calls":False,"badge":"Best Value"},
        ]
    },
    "czech-republic": {
        "name": "Czech Republic", "flag": "🇨🇿", "slug": "czech-republic",
        "desc": "Buy prepaid Czech Republic eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Czech Republic from $4.50.",
        "subtitle": "Stay connected across Czech Republic. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304070120","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304070137","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404252990","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253508","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254031","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409181387","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409181394","calls":False,"badge":"Best Value"},
        ]
    },
    "sweden": {
        "name": "Sweden", "flag": "🇸🇪", "slug": "sweden",
        "desc": "Buy prepaid Sweden eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Sweden from $4.50.",
        "subtitle": "Stay connected across Sweden. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304110208","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304110215","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404252921","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253447","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404253959","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312304110222","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409185637","calls":False,"badge":"Best Value"},
        ]
    },
    "norway": {
        "name": "Norway", "flag": "🇳🇴", "slug": "norway",
        "desc": "Buy prepaid Norway eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Norway from $4.50.",
        "subtitle": "Stay connected across Norway. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405311166","calls":False},
            {"label":"3 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405312873","calls":False},
            {"label":"5 GB","days":"30 days","price":"$8.90","perday":"$0.30/day","id":"3352405314587","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$17.90","perday":"$0.60/day","id":"3352406140185","calls":False},
            {"label":"20 GB","days":"31 days","price":"$28.90","perday":"$0.93/day","id":"3561292347756","calls":True},
            {"label":"30 GB","days":"30 days","price":"$32.90","perday":"$1.10/day","id":"3526356063683","calls":True},
            {"label":"60 GB","days":"30 days","price":"$39.90","perday":"$1.33/day","id":"3522405130016","calls":True,"badge":"Best Value"},
        ]
    },
    "denmark": {
        "name": "Denmark", "flag": "🇩🇰", "slug": "denmark",
        "desc": "Buy prepaid Denmark eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Denmark from $4.50.",
        "subtitle": "Stay connected across Denmark. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304100018","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304100025","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404253119","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253638","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254161","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409181479","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409181486","calls":False,"badge":"Best Value"},
        ]
    },
    "finland": {
        "name": "Finland", "flag": "🇫🇮", "slug": "finland",
        "desc": "Buy prepaid Finland eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Finland from $4.50.",
        "subtitle": "Stay connected across Finland. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304100100","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304100117","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404253126","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253645","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254178","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409181783","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409181790","calls":False,"badge":"Best Value"},
        ]
    },
    "ireland": {
        "name": "Ireland", "flag": "🇮🇪", "slug": "ireland",
        "desc": "Buy prepaid Ireland eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Ireland from $4.50.",
        "subtitle": "Stay connected across Ireland. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304100247","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304100254","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404253034","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253546","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254079","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409182742","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409182759","calls":False,"badge":"Best Value"},
        ]
    },
    "austria": {
        "name": "Austria", "flag": "🇦🇹", "slug": "austria",
        "desc": "Buy prepaid Austria eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Austria from $4.50.",
        "subtitle": "Stay connected across Austria. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304070045","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304070052","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404252969","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253478","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254000","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409180281","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409180298","calls":False,"badge":"Best Value"},
        ]
    },
    "belgium": {
        "name": "Belgium", "flag": "🇧🇪", "slug": "belgium",
        "desc": "Buy prepaid Belgium eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Belgium from $4.50.",
        "subtitle": "Stay connected across Belgium. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304070069","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304070076","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404252976","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253485","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254017","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409180496","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409180502","calls":False,"badge":"Best Value"},
        ]
    },
    "romania": {
        "name": "Romania", "flag": "🇷🇴", "slug": "romania",
        "desc": "Buy prepaid Romania eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Romania from $4.50.",
        "subtitle": "Stay connected across Romania. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304100711","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304100728","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404253089","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253591","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254123","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312304100735","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409184821","calls":False,"badge":"Best Value"},
        ]
    },
    "hungary": {
        "name": "Hungary", "flag": "🇭🇺", "slug": "hungary",
        "desc": "Buy prepaid Hungary eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Hungary from $4.50.",
        "subtitle": "Stay connected across Hungary. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304100193","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304100209","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404253027","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253539","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404254062","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409182605","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409182612","calls":False,"badge":"Best Value"},
        ]
    },
    "croatia": {
        "name": "Croatia", "flag": "🇭🇷", "slug": "croatia",
        "desc": "Buy prepaid Croatia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Croatia from $4.50.",
        "subtitle": "Stay connected across Croatia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312304070106","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312304070113","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404252891","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404253416","calls":False},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404253928","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409181288","calls":False},
            {"label":"50 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409181295","calls":False,"badge":"Best Value"},
        ]
    },
    # ── Regional ──────────────────────────────────────────────────────────────
    "asia": {
        "name": "Asia", "flag": "🌏", "slug": "asia",
        "desc": "Buy prepaid Asia regional eSIM. Covers 26 Asian countries. Instant activation from $4.50.",
        "subtitle": "One eSIM for 26 Asian countries. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352406180082","calls":False},
            {"label":"3 GB","days":"30 days","price":"$10.90","perday":"$0.36/day","id":"3352406180099","calls":False},
            {"label":"5 GB","days":"30 days","price":"$17.90","perday":"$0.60/day","id":"3352406180105","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$29.90","perday":"$1.00/day","id":"3352406180112","calls":False},
            {"label":"20 GB","days":"30 days","price":"$54.90","perday":"$1.83/day","id":"3352406180129","calls":False},
            {"label":"30 GB","days":"30 days","price":"$79.90","perday":"$2.66/day","id":"3352406180136","calls":False,"badge":"Best Value"},
        ]
    },
    "middle-east": {
        "name": "Middle East", "flag": "🕌", "slug": "middle-east",
        "desc": "Buy prepaid Middle East regional eSIM. Covers 12 countries. Instant activation from $4.90.",
        "subtitle": "One eSIM for 12 Middle Eastern countries. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.90","perday":"$0.70/day","id":"3352406180150","calls":False},
            {"label":"3 GB","days":"30 days","price":"$13.40","perday":"$0.45/day","id":"3352406180167","calls":False},
            {"label":"5 GB","days":"30 days","price":"$17.90","perday":"$0.60/day","id":"3352406180174","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$34.90","perday":"$1.16/day","id":"3352406180181","calls":False},
            {"label":"20 GB","days":"30 days","price":"$59.90","perday":"$2.00/day","id":"3352406180198","calls":False,"badge":"Best Value"},
        ]
    },
    "africa": {
        "name": "Africa", "flag": "🌍", "slug": "africa",
        "desc": "Buy prepaid Africa regional eSIM. Covers 17 African countries. Instant activation from $7.40.",
        "subtitle": "One eSIM for 17 African countries. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$7.40","perday":"$1.06/day","id":"3352406180501","calls":False},
            {"label":"3 GB","days":"30 days","price":"$20.90","perday":"$0.70/day","id":"3352406180518","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$34.40","perday":"$1.15/day","id":"3352406180525","calls":False,"badge":"Best Value"},
        ]
    },
    "bermuda": {
        "name": "Bermuda", "flag": "🇧🇲", "slug": "bermuda",
        "desc": "Buy prepaid Bermuda eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Bermuda from $16.90.",
        "subtitle": "Stay connected across Bermuda. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$16.90","perday":"$2.41/day","id":"3312404254376","calls":False},
            {"label":"3 GB","days":"30 days","price":"$46.90","perday":"$1.56/day","id":"3312404254383","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$73.90","perday":"$2.46/day","id":"3312404254390","calls":False,"badge":"Best Value"},
        ]
    },
    "el-salvador": {
        "name": "El Salvador", "flag": "🇸🇻", "slug": "el-salvador",
        "desc": "Buy prepaid El Salvador eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $4.50.",
        "subtitle": "Stay connected across El Salvador. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405310480","calls":False},
            {"label":"3 GB","days":"30 days","price":"$8.90","perday":"$0.30/day","id":"3352405312194","calls":False},
            {"label":"5 GB","days":"30 days","price":"$13.90","perday":"$0.46/day","id":"3352405313900","calls":False,"badge":"Best Value"},
            {"label":"10 GB","days":"30 days","price":"$25.90","perday":"$0.86/day","id":"3352405315614","calls":False},
            {"label":"20 GB","days":"30 days","price":"$45.90","perday":"$1.53/day","id":"3352405317328","calls":False},
            {"label":"30 GB","days":"30 days","price":"$65.90","perday":"$2.20/day","id":"3352406130483","calls":False},
        ]
    },
    "guatemala": {
        "name": "Guatemala", "flag": "🇬🇹", "slug": "guatemala",
        "desc": "Buy prepaid Guatemala eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $7.90.",
        "subtitle": "Stay connected across Guatemala. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$7.90","perday":"$1.13/day","id":"3312409182278","calls":False},
            {"label":"3 GB","days":"30 days","price":"$19.90","perday":"$0.66/day","id":"3312304050085","calls":False},
            {"label":"5 GB","days":"30 days","price":"$30.90","perday":"$1.03/day","id":"3312404252693","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$58.90","perday":"$1.96/day","id":"3312404253263","calls":False},
            {"label":"20 GB","days":"30 days","price":"$106.90","perday":"$3.56/day","id":"3312404253782","calls":False,"badge":"Best Value"},
        ]
    },
    "honduras": {
        "name": "Honduras", "flag": "🇭🇳", "slug": "honduras",
        "desc": "Buy prepaid Honduras eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $6.90.",
        "subtitle": "Stay connected across Honduras. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$6.90","perday":"$0.99/day","id":"3312304050092","calls":False},
            {"label":"3 GB","days":"30 days","price":"$17.90","perday":"$0.60/day","id":"3312304050108","calls":False},
            {"label":"5 GB","days":"30 days","price":"$27.90","perday":"$0.93/day","id":"3312404252709","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$51.90","perday":"$1.73/day","id":"3312404253270","calls":False},
            {"label":"20 GB","days":"30 days","price":"$94.90","perday":"$3.16/day","id":"3312404253799","calls":False,"badge":"Best Value"},
        ]
    },
    "nicaragua": {
        "name": "Nicaragua", "flag": "🇳🇮", "slug": "nicaragua",
        "desc": "Buy prepaid Nicaragua eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $7.90.",
        "subtitle": "Stay connected across Nicaragua. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$7.90","perday":"$1.13/day","id":"3312304050115","calls":False},
            {"label":"3 GB","days":"30 days","price":"$20.90","perday":"$0.70/day","id":"3312404252549","calls":False},
            {"label":"5 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312404252716","calls":False,"badge":"Best Value"},
            {"label":"10 GB","days":"30 days","price":"$60.90","perday":"$2.03/day","id":"3312404253287","calls":False},
            {"label":"20 GB","days":"30 days","price":"$111.90","perday":"$3.73/day","id":"3312404253805","calls":False},
        ]
    },
    "panama": {
        "name": "Panama", "flag": "🇵🇦", "slug": "panama",
        "desc": "Buy prepaid Panama eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $6.90.",
        "subtitle": "Stay connected across Panama. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$6.90","perday":"$0.99/day","id":"3312304050122","calls":False},
            {"label":"3 GB","days":"30 days","price":"$16.90","perday":"$0.56/day","id":"3312304050139","calls":False},
            {"label":"5 GB","days":"30 days","price":"$25.90","perday":"$0.86/day","id":"3312404252785","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$48.90","perday":"$1.63/day","id":"3312404253355","calls":False},
            {"label":"20 GB","days":"30 days","price":"$88.90","perday":"$2.96/day","id":"3312404253874","calls":False,"badge":"Best Value"},
        ]
    },
    "greenland": {
        "name": "Greenland", "flag": "🇬🇱", "slug": "greenland",
        "desc": "Buy prepaid Greenland eSIM data plans. Instant activation, no roaming fees. Best eSIM deals for Greenland from $23.90.",
        "subtitle": "Stay connected across Greenland. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$23.90","perday":"$3.41/day","id":"3312404255076","calls":False},
            {"label":"3 GB","days":"30 days","price":"$66.90","perday":"$2.23/day","id":"3312404255083","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$107.90","perday":"$3.60/day","id":"3312409182070","calls":False,"badge":"Best Value"},
        ]
    },
    "bolivia": {
        "name": "Bolivia", "flag": "🇧🇴", "slug": "bolivia",
        "desc": "Buy prepaid Bolivia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $6.90.",
        "subtitle": "Stay connected across Bolivia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$6.90","perday":"$0.99/day","id":"3312304050016","calls":False},
            {"label":"3 GB","days":"30 days","price":"$17.90","perday":"$0.60/day","id":"3312304050023","calls":False},
            {"label":"5 GB","days":"30 days","price":"$27.90","perday":"$0.93/day","id":"3312404252808","calls":False,"badge":"Best Value"},
            {"label":"10 GB","days":"30 days","price":"$51.90","perday":"$1.73/day","id":"3312404253386","calls":False},
            {"label":"20 GB","days":"30 days","price":"$94.90","perday":"$3.16/day","id":"3312404253898","calls":False},
        ]
    },
    "ecuador": {
        "name": "Ecuador", "flag": "🇪🇨", "slug": "ecuador",
        "desc": "Buy prepaid Ecuador eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $4.50.",
        "subtitle": "Stay connected across Ecuador. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312404251665","calls":False},
            {"label":"3 GB","days":"30 days","price":"$8.90","perday":"$0.30/day","id":"3312404251672","calls":False},
            {"label":"5 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404251689","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$23.90","perday":"$0.80/day","id":"3312404251696","calls":False},
            {"label":"20 GB","days":"30 days","price":"$42.90","perday":"$1.43/day","id":"3312404251702","calls":False},
            {"label":"30 GB","days":"30 days","price":"$61.90","perday":"$2.06/day","id":"3312409181554","calls":False},
            {"label":"50 GB","days":"30 days","price":"$97.90","perday":"$3.26/day","id":"3312409181561","calls":False,"badge":"Best Value"},
        ]
    },
    "paraguay": {
        "name": "Paraguay", "flag": "🇵🇾", "slug": "paraguay",
        "desc": "Buy prepaid Paraguay eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $5.90.",
        "subtitle": "Stay connected across Paraguay. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3312404252112","calls":False},
            {"label":"3 GB","days":"30 days","price":"$14.90","perday":"$0.50/day","id":"3312404252129","calls":False},
            {"label":"5 GB","days":"30 days","price":"$22.90","perday":"$0.76/day","id":"3312404252136","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$42.90","perday":"$1.43/day","id":"3312404252143","calls":False},
            {"label":"20 GB","days":"30 days","price":"$78.90","perday":"$2.63/day","id":"3312404252150","calls":False},
            {"label":"30 GB","days":"30 days","price":"$112.90","perday":"$3.76/day","id":"3312409184616","calls":False,"badge":"Best Value"},
        ]
    },
    "palestine": {
        "name": "Palestine", "flag": "🇵🇸", "slug": "palestine",
        "desc": "Buy prepaid Palestine eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $11.90.",
        "subtitle": "Stay connected across Palestine. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$11.90","perday":"$1.70/day","id":"3312404254765","calls":False},
            {"label":"3 GB","days":"30 days","price":"$32.90","perday":"$1.10/day","id":"3312404254772","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$52.90","perday":"$1.76/day","id":"3312404254789","calls":False},
            {"label":"10 GB","days":"30 days","price":"$100.90","perday":"$3.36/day","id":"3312409184487","calls":False,"badge":"Best Value"},
        ]
    },
    "guadeloupe": {
        "name": "Guadeloupe", "flag": "🇬🇵", "slug": "guadeloupe",
        "desc": "Buy prepaid Guadeloupe eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $21.90.",
        "subtitle": "Stay connected across Guadeloupe. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"10 GB","days":"30 days","price":"$21.90","perday":"$0.73/day","id":"8595106658537","calls":True,"badge":"Popular"},
            {"label":"20 GB","days":"30 days","price":"$29.90","perday":"$1.00/day","id":"8595106658538","calls":True},
            {"label":"30 GB","days":"30 days","price":"$32.90","perday":"$1.10/day","id":"3526356063683","calls":True},
            {"label":"60 GB","days":"30 days","price":"$39.90","perday":"$1.33/day","id":"3522405130016","calls":True},
            {"label":"120 GB","days":"30 days","price":"$55.90","perday":"$1.86/day","id":"3526350133054","calls":True,"badge":"Best Value"},
        ]
    },
    "martinique": {
        "name": "Martinique", "flag": "🇲🇶", "slug": "martinique",
        "desc": "Buy prepaid Martinique eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $4.50.",
        "subtitle": "Stay connected across Martinique. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312404251917","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312404251924","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404251931","calls":False},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404251948","calls":False,"badge":"Popular"},
            {"label":"20 GB","days":"30 days","price":"$29.90","perday":"$1.00/day","id":"8595106658538","calls":True},
            {"label":"30 GB","days":"30 days","price":"$32.90","perday":"$1.10/day","id":"3526356063683","calls":True},
            {"label":"120 GB","days":"30 days","price":"$55.90","perday":"$1.86/day","id":"3526350133054","calls":True,"badge":"Best Value"},
        ]
    },
    "montserrat": {
        "name": "Montserrat", "flag": "🇲🇸", "slug": "montserrat",
        "desc": "Buy prepaid Montserrat eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $5.90.",
        "subtitle": "Stay connected across Montserrat. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3312404254673","calls":False},
            {"label":"3 GB","days":"30 days","price":"$15.90","perday":"$0.53/day","id":"3312404254680","calls":False},
            {"label":"5 GB","days":"30 days","price":"$23.90","perday":"$0.80/day","id":"3312404254697","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$45.90","perday":"$1.53/day","id":"3312409183886","calls":False},
            {"label":"20 GB","days":"30 days","price":"$82.90","perday":"$2.76/day","id":"3312409183893","calls":False},
            {"label":"30 GB","days":"30 days","price":"$118.90","perday":"$3.96/day","id":"3312409183909","calls":False,"badge":"Best Value"},
        ]
    },
    "saint-barthelemy": {
        "name": "Saint Barthélemy", "flag": "🇧🇱", "slug": "saint-barthelemy",
        "desc": "Buy prepaid Saint Barthélemy eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $4.50.",
        "subtitle": "Stay connected across Saint Barthélemy. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312409184876","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312409184883","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312409184890","calls":False},
            {"label":"6 GB","days":"30 days","price":"$19.90","perday":"$0.66/day","id":"5052503100041","calls":True,"badge":"Popular"},
            {"label":"12 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"5052503100034","calls":True},
            {"label":"18 GB","days":"30 days","price":"$29.90","perday":"$1.00/day","id":"5052503100027","calls":True},
            {"label":"30 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"5052503100010","calls":True,"badge":"Best Value"},
        ]
    },
    "saint-kitts-and-nevis": {
        "name": "Saint Kitts and Nevis", "flag": "🇰🇳", "slug": "saint-kitts-and-nevis",
        "desc": "Buy prepaid Saint Kitts and Nevis eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $6.90.",
        "subtitle": "Stay connected across Saint Kitts and Nevis. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$6.90","perday":"$0.99/day","id":"3312409184944","calls":False},
            {"label":"3 GB","days":"30 days","price":"$16.90","perday":"$0.56/day","id":"3312409184951","calls":False},
            {"label":"5 GB","days":"30 days","price":"$25.90","perday":"$0.86/day","id":"3312409184968","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409184975","calls":False},
            {"label":"20 GB","days":"30 days","price":"$90.90","perday":"$3.03/day","id":"3312409184982","calls":False,"badge":"Best Value"},
        ]
    },
    "saint-lucia": {
        "name": "Saint Lucia", "flag": "🇱🇨", "slug": "saint-lucia",
        "desc": "Buy prepaid Saint Lucia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $6.90.",
        "subtitle": "Stay connected across Saint Lucia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$6.90","perday":"$0.99/day","id":"3312404254611","calls":False},
            {"label":"3 GB","days":"30 days","price":"$16.90","perday":"$0.56/day","id":"3312404254628","calls":False},
            {"label":"5 GB","days":"30 days","price":"$25.90","perday":"$0.86/day","id":"3312404254635","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"3312409185019","calls":False},
            {"label":"20 GB","days":"30 days","price":"$90.90","perday":"$3.03/day","id":"3312409185026","calls":False,"badge":"Best Value"},
        ]
    },
    "saint-martin": {
        "name": "Saint Martin", "flag": "🇲🇫", "slug": "saint-martin",
        "desc": "Buy prepaid Saint Martin eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $4.50.",
        "subtitle": "Stay connected across Saint Martin. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312409185057","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312409185064","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312409185071","calls":False},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312409185088","calls":False,"badge":"Popular"},
            {"label":"18 GB","days":"30 days","price":"$29.90","perday":"$1.00/day","id":"5052503100027","calls":True},
            {"label":"30 GB","days":"30 days","price":"$49.90","perday":"$1.66/day","id":"5052503100010","calls":True,"badge":"Best Value"},
        ]
    },
    "turks-and-caicos-islands": {
        "name": "Turks and Caicos Islands", "flag": "🇹🇨", "slug": "turks-and-caicos-islands",
        "desc": "Buy prepaid Turks and Caicos Islands eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $6.90.",
        "subtitle": "Stay connected across the Turks and Caicos Islands. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$6.90","perday":"$0.99/day","id":"3312404254826","calls":False},
            {"label":"3 GB","days":"30 days","price":"$16.90","perday":"$0.56/day","id":"3312404254833","calls":False},
            {"label":"5 GB","days":"30 days","price":"$26.90","perday":"$0.90/day","id":"3312404254840","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$50.90","perday":"$1.70/day","id":"3312409185989","calls":False},
            {"label":"20 GB","days":"30 days","price":"$92.90","perday":"$3.10/day","id":"3312409185996","calls":False,"badge":"Best Value"},
        ]
    },
    "us-virgin-islands": {
        "name": "US Virgin Islands", "flag": "🇻🇮", "slug": "us-virgin-islands",
        "desc": "Buy prepaid US Virgin Islands eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $6.90.",
        "subtitle": "Stay connected across the US Virgin Islands. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$6.90","perday":"$0.99/day","id":"3312404252464","calls":False},
            {"label":"3 GB","days":"30 days","price":"$17.90","perday":"$0.60/day","id":"3312404252471","calls":False},
            {"label":"5 GB","days":"30 days","price":"$27.90","perday":"$0.93/day","id":"3312404252488","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$51.90","perday":"$1.73/day","id":"3312404252495","calls":False},
            {"label":"20 GB","days":"30 days","price":"$94.90","perday":"$3.16/day","id":"3312404252501","calls":False,"badge":"Best Value"},
        ]
    },
    "fiji": {
        "name": "Fiji", "flag": "🇫🇯", "slug": "fiji",
        "desc": "Buy prepaid Fiji eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $4.50.",
        "subtitle": "Stay connected across Fiji. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405310527","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3352405312231","calls":False},
            {"label":"5 GB","days":"30 days","price":"$8.90","perday":"$0.30/day","id":"3352405313948","calls":False},
            {"label":"10 GB","days":"30 days","price":"$17.90","perday":"$0.60/day","id":"3352405315652","calls":False,"badge":"Popular"},
            {"label":"20 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3352405317366","calls":False},
            {"label":"30 GB","days":"30 days","price":"$44.90","perday":"$1.50/day","id":"3352406130520","calls":False},
            {"label":"50 GB","days":"60 days","price":"$71.90","perday":"$1.20/day","id":"3352406132234","calls":False,"badge":"Best Value"},
        ]
    },
    "papua-new-guinea": {
        "name": "Papua New Guinea", "flag": "🇵🇬", "slug": "papua-new-guinea",
        "desc": "Buy prepaid Papua New Guinea eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $6.90.",
        "subtitle": "Stay connected across Papua New Guinea. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$6.90","perday":"$0.99/day","id":"3352405311210","calls":False},
            {"label":"3 GB","days":"30 days","price":"$19.90","perday":"$0.66/day","id":"3352405312927","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3352405314631","calls":False,"badge":"Best Value"},
        ]
    },
    "guam": {
        "name": "Guam", "flag": "🇬🇺", "slug": "guam",
        "desc": "Buy prepaid Guam eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $12.90.",
        "subtitle": "Stay connected across Guam. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$12.90","perday":"$1.84/day","id":"3312404254529","calls":False},
            {"label":"3 GB","days":"30 days","price":"$34.90","perday":"$1.16/day","id":"3312404254536","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$55.90","perday":"$1.86/day","id":"3312404254543","calls":False},
            {"label":"10 GB","days":"30 days","price":"$105.90","perday":"$3.53/day","id":"3312409182230","calls":False,"badge":"Best Value"},
        ]
    },
    "samoa": {
        "name": "Samoa", "flag": "🇼🇸", "slug": "samoa",
        "desc": "Buy prepaid Samoa eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $18.90.",
        "subtitle": "Stay connected across Samoa. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$18.90","perday":"$2.70/day","id":"3312404255311","calls":False},
            {"label":"3 GB","days":"30 days","price":"$52.90","perday":"$1.76/day","id":"3312404255328","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$83.90","perday":"$2.80/day","id":"3312409185163","calls":False,"badge":"Best Value"},
        ]
    },
    "vanuatu": {
        "name": "Vanuatu", "flag": "🇻🇺", "slug": "vanuatu",
        "desc": "Buy prepaid Vanuatu eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $60.90.",
        "subtitle": "Stay connected across Vanuatu. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$60.90","perday":"$8.70/day","id":"3312404255298","calls":False,"badge":"Best Value"},
        ]
    },
    "tonga": {
        "name": "Tonga", "flag": "🇹🇴", "slug": "tonga",
        "desc": "Buy prepaid Tonga eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $43.90.",
        "subtitle": "Stay connected across Tonga. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$43.90","perday":"$6.27/day","id":"3312404255274","calls":False,"badge":"Best Value"},
        ]
    },
    "nauru": {
        "name": "Nauru", "flag": "🇳🇷", "slug": "nauru",
        "desc": "Buy prepaid Nauru eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $48.90.",
        "subtitle": "Stay connected across Nauru. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$48.90","perday":"$6.99/day","id":"3312404255175","calls":False,"badge":"Best Value"},
        ]
    },
    "kiribati": {
        "name": "Kiribati", "flag": "🇰🇮", "slug": "kiribati",
        "desc": "Buy prepaid Kiribati eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $49.90.",
        "subtitle": "Stay connected across Kiribati. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$49.90","perday":"$7.13/day","id":"3312404255137","calls":False,"badge":"Best Value"},
        ]
    },
    "algeria": {
        "name": "Algeria", "flag": "🇩🇿", "slug": "algeria",
        "desc": "Buy prepaid Algeria eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $4.50.",
        "subtitle": "Stay connected across Algeria. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312404250064","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3312404250071","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404250088","calls":False},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404250095","calls":False,"badge":"Popular"},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3312404250101","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3312409180052","calls":False,"badge":"Best Value"},
        ]
    },
    "benin": {
        "name": "Benin", "flag": "🇧🇯", "slug": "benin",
        "desc": "Buy prepaid Benin eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $6.90.",
        "subtitle": "Stay connected across Benin. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$6.90","perday":"$0.99/day","id":"3312404255335","calls":False},
            {"label":"3 GB","days":"30 days","price":"$16.90","perday":"$0.56/day","id":"3312409180571","calls":False},
            {"label":"5 GB","days":"30 days","price":"$26.90","perday":"$0.90/day","id":"3312409180588","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$50.90","perday":"$1.70/day","id":"3312409180595","calls":False},
            {"label":"20 GB","days":"30 days","price":"$92.90","perday":"$3.10/day","id":"3312409180601","calls":False,"badge":"Best Value"},
        ]
    },
    "botswana": {
        "name": "Botswana", "flag": "🇧🇼", "slug": "botswana",
        "desc": "Buy prepaid Botswana eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $17.90.",
        "subtitle": "Stay connected across Botswana. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$17.90","perday":"$2.56/day","id":"3312404255014","calls":False},
            {"label":"3 GB","days":"30 days","price":"$50.90","perday":"$1.70/day","id":"3312404255021","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$80.90","perday":"$2.70/day","id":"3312409180762","calls":False,"badge":"Best Value"},
        ]
    },
    "burkina-faso": {
        "name": "Burkina Faso", "flag": "🇧🇫", "slug": "burkina-faso",
        "desc": "Buy prepaid Burkina Faso eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $29.90.",
        "subtitle": "Stay connected across Burkina Faso. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$29.90","perday":"$4.27/day","id":"3312409180915","calls":False},
            {"label":"3 GB","days":"30 days","price":"$83.90","perday":"$2.80/day","id":"3312409180922","calls":False,"badge":"Best Value"},
        ]
    },
    "cabo-verde": {
        "name": "Cabo Verde", "flag": "🇨🇻", "slug": "cabo-verde",
        "desc": "Buy prepaid Cabo Verde eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $39.90.",
        "subtitle": "Stay connected across Cabo Verde. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"20 GB","days":"31 days","price":"$39.90","perday":"$1.29/day","id":"3561292400796","calls":True,"badge":"Best Value"},
        ]
    },
    "cameroon": {
        "name": "Cameroon", "flag": "🇨🇲", "slug": "cameroon",
        "desc": "Buy prepaid Cameroon eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $20.90.",
        "subtitle": "Stay connected across Cameroon. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$20.90","perday":"$2.99/day","id":"3312404255038","calls":False},
            {"label":"3 GB","days":"30 days","price":"$58.90","perday":"$1.96/day","id":"3312404255045","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$93.90","perday":"$3.13/day","id":"3312409181004","calls":False,"badge":"Best Value"},
        ]
    },
    "central-african-republic": {
        "name": "Central African Republic", "flag": "🇨🇫", "slug": "central-african-republic",
        "desc": "Buy prepaid Central African Republic eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $39.90.",
        "subtitle": "Stay connected across the Central African Republic. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"20 GB","days":"31 days","price":"$39.90","perday":"$1.29/day","id":"3561292400796","calls":True,"badge":"Best Value"},
        ]
    },
    "chad": {
        "name": "Chad", "flag": "🇹🇩", "slug": "chad",
        "desc": "Buy prepaid Chad eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $5.90.",
        "subtitle": "Stay connected across Chad. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3312404251467","calls":False},
            {"label":"3 GB","days":"30 days","price":"$14.90","perday":"$0.50/day","id":"3312404251474","calls":False},
            {"label":"5 GB","days":"30 days","price":"$22.90","perday":"$0.76/day","id":"3312404251481","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$42.90","perday":"$1.43/day","id":"3312404251498","calls":False},
            {"label":"20 GB","days":"30 days","price":"$77.90","perday":"$2.60/day","id":"3312404251504","calls":False},
            {"label":"30 GB","days":"30 days","price":"$110.90","perday":"$3.70/day","id":"3312409181189","calls":False,"badge":"Best Value"},
        ]
    },
    "equatorial-guinea": {
        "name": "Equatorial Guinea", "flag": "🇬🇶", "slug": "equatorial-guinea",
        "desc": "Buy prepaid Equatorial Guinea eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $39.90.",
        "subtitle": "Stay connected across Equatorial Guinea. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"20 GB","days":"31 days","price":"$39.90","perday":"$1.29/day","id":"3561292400796","calls":True,"badge":"Best Value"},
        ]
    },
    "eswatini": {
        "name": "Eswatini", "flag": "🇸🇿", "slug": "eswatini",
        "desc": "Buy prepaid Eswatini eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $29.90.",
        "subtitle": "Stay connected across Eswatini. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$29.90","perday":"$4.27/day","id":"3312404255397","calls":False},
            {"label":"3 GB","days":"30 days","price":"$83.90","perday":"$2.80/day","id":"3312409185576","calls":False,"badge":"Best Value"},
        ]
    },
    "ethiopia": {
        "name": "Ethiopia", "flag": "🇪🇹", "slug": "ethiopia",
        "desc": "Buy prepaid Ethiopia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $39.90.",
        "subtitle": "Stay connected across Ethiopia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"10 GB","days":"31 days","price":"$39.90","perday":"$1.29/day","id":"3561292400796","calls":True,"badge":"Popular"},
            {"label":"1 GB","days":"7 days","price":"$59.90","perday":"$8.56/day","id":"3312404255489","calls":False,"badge":"Best Value"},
        ]
    },
    "gabon": {
        "name": "Gabon", "flag": "🇬🇦", "slug": "gabon",
        "desc": "Buy prepaid Gabon eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $5.90.",
        "subtitle": "Stay connected across Gabon. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3312404255052","calls":False},
            {"label":"3 GB","days":"30 days","price":"$14.90","perday":"$0.50/day","id":"3312404255069","calls":False},
            {"label":"5 GB","days":"30 days","price":"$22.90","perday":"$0.76/day","id":"3312409181899","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$42.90","perday":"$1.43/day","id":"3312409181905","calls":False},
            {"label":"20 GB","days":"30 days","price":"$77.90","perday":"$2.60/day","id":"3312409181912","calls":False},
            {"label":"30 GB","days":"30 days","price":"$110.90","perday":"$3.70/day","id":"3312409181929","calls":False,"badge":"Best Value"},
        ]
    },
    "gambia": {
        "name": "Gambia", "flag": "🇬🇲", "slug": "gambia",
        "desc": "Buy prepaid Gambia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $35.90.",
        "subtitle": "Stay connected across Gambia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$35.90","perday":"$5.13/day","id":"3312404255090","calls":False},
            {"label":"3 GB","days":"30 days","price":"$100.90","perday":"$3.36/day","id":"3312404255106","calls":False,"badge":"Best Value"},
        ]
    },
    "ghana": {
        "name": "Ghana", "flag": "🇬🇭", "slug": "ghana",
        "desc": "Buy prepaid Ghana eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $4.50.",
        "subtitle": "Stay connected across Ghana. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3312404250316","calls":False},
            {"label":"3 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3312404250323","calls":False},
            {"label":"5 GB","days":"30 days","price":"$9.90","perday":"$0.33/day","id":"3312404250330","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$18.90","perday":"$0.63/day","id":"3312404250347","calls":False},
            {"label":"20 GB","days":"30 days","price":"$33.90","perday":"$1.13/day","id":"3312404250354","calls":False},
            {"label":"30 GB","days":"30 days","price":"$47.90","perday":"$1.60/day","id":"3312409182025","calls":False},
            {"label":"50 GB","days":"30 days","price":"$75.90","perday":"$2.53/day","id":"3312409182025","calls":False,"badge":"Best Value"},
        ]
    },
    "guinea": {
        "name": "Guinea", "flag": "🇬🇳", "slug": "guinea",
        "desc": "Buy prepaid Guinea eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $29.90.",
        "subtitle": "Stay connected across Guinea. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$29.90","perday":"$4.27/day","id":"3312404255342","calls":False},
            {"label":"3 GB","days":"30 days","price":"$83.90","perday":"$2.80/day","id":"3312409182322","calls":False,"badge":"Best Value"},
        ]
    },
    "guinea-bissau": {
        "name": "Guinea-Bissau", "flag": "🇬🇼", "slug": "guinea-bissau",
        "desc": "Buy prepaid Guinea-Bissau eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $29.90.",
        "subtitle": "Stay connected across Guinea-Bissau. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$29.90","perday":"$4.27/day","id":"3312404255359","calls":False},
            {"label":"3 GB","days":"30 days","price":"$83.90","perday":"$2.80/day","id":"3312409182384","calls":False,"badge":"Best Value"},
        ]
    },
    "ivory-coast": {
        "name": "Ivory Coast", "flag": "🇨🇮", "slug": "ivory-coast",
        "desc": "Buy prepaid Ivory Coast eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $29.90.",
        "subtitle": "Stay connected across Ivory Coast. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$29.90","perday":"$4.27/day","id":"3312404255366","calls":False},
            {"label":"3 GB","days":"30 days","price":"$83.90","perday":"$2.80/day","id":"3312409182810","calls":False,"badge":"Best Value"},
        ]
    },
    "lesotho": {
        "name": "Lesotho", "flag": "🇱🇸", "slug": "lesotho",
        "desc": "Buy prepaid Lesotho eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $14.90.",
        "subtitle": "Stay connected across Lesotho. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$14.90","perday":"$2.13/day","id":"3312404255540","calls":False},
            {"label":"3 GB","days":"30 days","price":"$41.90","perday":"$1.40/day","id":"3312404255557","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$66.90","perday":"$2.23/day","id":"3312404255564","calls":False,"badge":"Best Value"},
        ]
    },
    "liberia": {
        "name": "Liberia", "flag": "🇱🇷", "slug": "liberia",
        "desc": "Buy prepaid Liberia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $29.90.",
        "subtitle": "Stay connected across Liberia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$29.90","perday":"$4.27/day","id":"3312404255373","calls":False},
            {"label":"3 GB","days":"30 days","price":"$83.90","perday":"$2.80/day","id":"3312409183220","calls":False,"badge":"Best Value"},
        ]
    },
    "madagascar": {
        "name": "Madagascar", "flag": "🇲🇬", "slug": "madagascar",
        "desc": "Buy prepaid Madagascar eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $4.90.",
        "subtitle": "Stay connected across Madagascar. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.90","perday":"$0.70/day","id":"3312404250712","calls":False},
            {"label":"3 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3312404250729","calls":False},
            {"label":"5 GB","days":"30 days","price":"$19.90","perday":"$0.66/day","id":"3312404250736","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$37.90","perday":"$1.26/day","id":"3312404250743","calls":False},
            {"label":"20 GB","days":"30 days","price":"$68.90","perday":"$2.30/day","id":"3312404250750","calls":False},
            {"label":"30 GB","days":"30 days","price":"$98.90","perday":"$3.30/day","id":"3312409183367","calls":False,"badge":"Best Value"},
        ]
    },
    "malawi": {
        "name": "Malawi", "flag": "🇲🇼", "slug": "malawi",
        "desc": "Buy prepaid Malawi eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $5.90.",
        "subtitle": "Stay connected across Malawi. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3312404251863","calls":False},
            {"label":"3 GB","days":"30 days","price":"$14.90","perday":"$0.50/day","id":"3312404251870","calls":False},
            {"label":"5 GB","days":"30 days","price":"$22.90","perday":"$0.76/day","id":"3312404251887","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$42.90","perday":"$1.43/day","id":"3312404251894","calls":False},
            {"label":"20 GB","days":"30 days","price":"$77.90","perday":"$2.60/day","id":"3312404251900","calls":False},
            {"label":"30 GB","days":"30 days","price":"$110.90","perday":"$3.70/day","id":"3312409183381","calls":False,"badge":"Best Value"},
        ]
    },
    "mali": {
        "name": "Mali", "flag": "🇲🇱", "slug": "mali",
        "desc": "Buy prepaid Mali eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $29.90.",
        "subtitle": "Stay connected across Mali. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$29.90","perday":"$4.27/day","id":"3312409183480","calls":False},
            {"label":"3 GB","days":"30 days","price":"$83.90","perday":"$2.80/day","id":"3312409183497","calls":False,"badge":"Best Value"},
        ]
    },
    "mauritania": {
        "name": "Mauritania", "flag": "🇲🇷", "slug": "mauritania",
        "desc": "Buy prepaid Mauritania eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $39.90.",
        "subtitle": "Stay connected across Mauritania. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"5 GB","days":"31 days","price":"$39.90","perday":"$1.29/day","id":"3561292400796","calls":True,"badge":"Best Value"},
        ]
    },
    "mauritius": {
        "name": "Mauritius", "flag": "🇲🇺", "slug": "mauritius",
        "desc": "Buy prepaid Mauritius eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $5.90.",
        "subtitle": "Stay connected across Mauritius. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3352405310992","calls":False},
            {"label":"3 GB","days":"30 days","price":"$14.90","perday":"$0.50/day","id":"3352405312705","calls":False},
            {"label":"5 GB","days":"30 days","price":"$22.90","perday":"$0.76/day","id":"3352405314419","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$43.90","perday":"$1.46/day","id":"3352405316123","calls":False},
            {"label":"20 GB","days":"30 days","price":"$79.90","perday":"$2.66/day","id":"3352405317830","calls":False,"badge":"Best Value"},
        ]
    },
    "mozambique": {
        "name": "Mozambique", "flag": "🇲🇿", "slug": "mozambique",
        "desc": "Buy prepaid Mozambique eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $11.90.",
        "subtitle": "Stay connected across Mozambique. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$11.90","perday":"$1.70/day","id":"3312404255595","calls":False},
            {"label":"3 GB","days":"30 days","price":"$32.90","perday":"$1.10/day","id":"3312404255601","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$51.90","perday":"$1.73/day","id":"3312404255618","calls":False},
            {"label":"10 GB","days":"30 days","price":"$99.90","perday":"$3.33/day","id":"3312404255625","calls":False,"badge":"Best Value"},
        ]
    },
    "namibia": {
        "name": "Namibia", "flag": "🇳🇦", "slug": "namibia",
        "desc": "Buy prepaid Namibia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $55.90.",
        "subtitle": "Stay connected across Namibia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$55.90","perday":"$7.99/day","id":"3312404255151","calls":False,"badge":"Best Value"},
        ]
    },
    "niger": {
        "name": "Niger", "flag": "🇳🇪", "slug": "niger",
        "desc": "Buy prepaid Niger eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $5.90.",
        "subtitle": "Stay connected across Niger. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3312404255465","calls":False},
            {"label":"3 GB","days":"30 days","price":"$15.90","perday":"$0.53/day","id":"3312409184296","calls":False},
            {"label":"5 GB","days":"30 days","price":"$23.90","perday":"$0.80/day","id":"3312409184302","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$45.90","perday":"$1.53/day","id":"3312409184319","calls":False},
            {"label":"20 GB","days":"30 days","price":"$82.90","perday":"$2.76/day","id":"3312409184326","calls":False},
            {"label":"30 GB","days":"30 days","price":"$118.90","perday":"$3.96/day","id":"3312409184333","calls":False,"badge":"Best Value"},
        ]
    },
    "rwanda": {
        "name": "Rwanda", "flag": "🇷🇼", "slug": "rwanda",
        "desc": "Buy prepaid Rwanda eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $5.90.",
        "subtitle": "Stay connected across Rwanda. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3352405311326","calls":False},
            {"label":"3 GB","days":"30 days","price":"$14.90","perday":"$0.50/day","id":"3352405313030","calls":False},
            {"label":"5 GB","days":"30 days","price":"$23.90","perday":"$0.80/day","id":"3352405314747","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$45.90","perday":"$1.53/day","id":"3352405316451","calls":False},
            {"label":"20 GB","days":"30 days","price":"$82.90","perday":"$2.76/day","id":"3352405318165","calls":False,"badge":"Best Value"},
        ]
    },
    "senegal": {
        "name": "Senegal", "flag": "🇸🇳", "slug": "senegal",
        "desc": "Buy prepaid Senegal eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $9.90.",
        "subtitle": "Stay connected across Senegal. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$9.90","perday":"$1.41/day","id":"3312404254796","calls":False},
            {"label":"3 GB","days":"30 days","price":"$27.90","perday":"$0.93/day","id":"3312404254802","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$43.90","perday":"$1.46/day","id":"3312404254819","calls":False},
            {"label":"10 GB","days":"30 days","price":"$83.90","perday":"$2.80/day","id":"3312409185248","calls":False,"badge":"Best Value"},
        ]
    },
    "seychelles": {
        "name": "Seychelles", "flag": "🇸🇨", "slug": "seychelles",
        "desc": "Buy prepaid Seychelles eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $33.90.",
        "subtitle": "Stay connected across Seychelles. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$33.90","perday":"$4.84/day","id":"3312404255212","calls":False},
            {"label":"3 GB","days":"30 days","price":"$95.90","perday":"$3.20/day","id":"3312404255229","calls":False,"badge":"Best Value"},
        ]
    },
    "sierra-leone": {
        "name": "Sierra Leone", "flag": "🇸🇱", "slug": "sierra-leone",
        "desc": "Buy prepaid Sierra Leone eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $39.90.",
        "subtitle": "Stay connected across Sierra Leone. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"20 GB","days":"31 days","price":"$39.90","perday":"$1.29/day","id":"3561292400796","calls":True,"badge":"Best Value"},
        ]
    },
    "sudan": {
        "name": "Sudan", "flag": "🇸🇩", "slug": "sudan",
        "desc": "Buy prepaid Sudan eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $12.90.",
        "subtitle": "Stay connected across Sudan. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$12.90","perday":"$1.84/day","id":"3312404255236","calls":False},
            {"label":"3 GB","days":"30 days","price":"$33.90","perday":"$1.13/day","id":"3312404255243","calls":False,"badge":"Popular"},
            {"label":"5 GB","days":"30 days","price":"$53.90","perday":"$1.80/day","id":"3312409185460","calls":False},
            {"label":"10 GB","days":"30 days","price":"$102.90","perday":"$3.43/day","id":"3312409185477","calls":False,"badge":"Best Value"},
        ]
    },
    "tanzania": {
        "name": "Tanzania", "flag": "🇹🇿", "slug": "tanzania",
        "desc": "Buy prepaid Tanzania eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $5.90.",
        "subtitle": "Stay connected across Tanzania. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3312404252266","calls":False},
            {"label":"3 GB","days":"30 days","price":"$13.90","perday":"$0.46/day","id":"3312404252273","calls":False},
            {"label":"5 GB","days":"30 days","price":"$21.90","perday":"$0.73/day","id":"3312404252280","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$41.90","perday":"$1.40/day","id":"3312404252297","calls":False},
            {"label":"20 GB","days":"30 days","price":"$75.90","perday":"$2.53/day","id":"3312404252303","calls":False,"badge":"Best Value"},
        ]
    },
    "tunisia": {
        "name": "Tunisia", "flag": "🇹🇳", "slug": "tunisia",
        "desc": "Buy prepaid Tunisia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $4.50.",
        "subtitle": "Stay connected across Tunisia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$4.50","perday":"$0.64/day","id":"3352405311586","calls":False},
            {"label":"3 GB","days":"30 days","price":"$5.90","perday":"$0.20/day","id":"3352405313290","calls":False},
            {"label":"5 GB","days":"30 days","price":"$6.90","perday":"$0.23/day","id":"3352405315003","calls":False},
            {"label":"10 GB","days":"30 days","price":"$12.90","perday":"$0.43/day","id":"3352405316710","calls":False,"badge":"Popular"},
            {"label":"20 GB","days":"30 days","price":"$24.90","perday":"$0.83/day","id":"3352405318424","calls":False},
            {"label":"30 GB","days":"30 days","price":"$31.90","perday":"$1.06/day","id":"3352406131589","calls":False},
            {"label":"50 GB","days":"60 days","price":"$49.90","perday":"$0.83/day","id":"3352406133293","calls":False,"badge":"Best Value"},
        ]
    },
    "uganda": {
        "name": "Uganda", "flag": "🇺🇬", "slug": "uganda",
        "desc": "Buy prepaid Uganda eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $5.90.",
        "subtitle": "Stay connected across Uganda. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3312404252310","calls":False},
            {"label":"3 GB","days":"30 days","price":"$13.90","perday":"$0.46/day","id":"3312404252327","calls":False},
            {"label":"5 GB","days":"30 days","price":"$21.90","perday":"$0.73/day","id":"3312404252334","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$40.90","perday":"$1.36/day","id":"3312404252341","calls":False},
            {"label":"20 GB","days":"30 days","price":"$74.90","perday":"$2.50/day","id":"3312404252358","calls":False},
            {"label":"30 GB","days":"30 days","price":"$106.90","perday":"$3.56/day","id":"3312409186047","calls":False,"badge":"Best Value"},
        ]
    },
    "zambia": {
        "name": "Zambia", "flag": "🇿🇲", "slug": "zambia",
        "desc": "Buy prepaid Zambia eSIM data plans. Instant activation, no roaming fees. Best eSIM deals from $5.90.",
        "subtitle": "Stay connected across Zambia. Instant activation via QR code — no physical SIM needed.",
        "compatible": "Works with iPhone XS+, Pixel 3+, Samsung S20+ and most modern phones.",
        "plans": [
            {"label":"1 GB","days":"7 days","price":"$5.90","perday":"$0.84/day","id":"3312404254949","calls":False},
            {"label":"3 GB","days":"30 days","price":"$14.90","perday":"$0.50/day","id":"3312404254956","calls":False},
            {"label":"5 GB","days":"30 days","price":"$23.90","perday":"$0.80/day","id":"3312404254963","calls":False,"badge":"Popular"},
            {"label":"10 GB","days":"30 days","price":"$44.90","perday":"$1.50/day","id":"3312409186399","calls":False},
            {"label":"20 GB","days":"30 days","price":"$80.90","perday":"$2.70/day","id":"3312409186405","calls":False,"badge":"Best Value"},
        ]
    },
}

GTM_SNIPPET = '''  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-FWN5WTYV2V"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-FWN5WTYV2V', {
      linker: {
        domains: ['esim.win', 'simoptions.com']
      }
    });
  </script>'''

NAV_LINKS = '''    <div class="hidden md:flex items-center gap-8">
          <a href="/" class="text-sm font-medium text-gray-500 hover:text-gray-900 transition-colors">Home</a>
          <a href="#plans" class="text-sm font-medium text-gray-500 hover:text-gray-900 transition-colors">Plans</a>
          <a href="#how-it-works" class="text-sm font-medium text-gray-500 hover:text-gray-900 transition-colors">How It Works</a>
          <a href="#faq" class="text-sm font-medium text-gray-500 hover:text-gray-900 transition-colors">FAQ</a>
        </div>'''

def is_unlimited(p):
    return p['label'].startswith('Unlimited')

def plan_row(p):
    url = f"https://www.simoptions.com/checkout/esim/{p['id']}/{UTM}"
    calls_attr = ' data-calls="1"' if p.get('calls') else ''
    ptype = 'unlimited' if is_unlimited(p) else 'data'
    badge = p.get('badge','')
    badge_html = ''
    if badge == 'Popular':
        badge_html = '<span class="shrink-0 text-[10px] font-bold text-brand-600 bg-orange-50 border border-orange-200 rounded-full px-2 py-0.5 leading-none">Popular</span>'
    elif badge == 'Best Value':
        badge_html = '<span class="shrink-0 text-[10px] font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 rounded-full px-2 py-0.5 leading-none">Best Value</span>'

    label_inner = f'<span class="text-[15px] font-bold text-gray-900">{p["label"]}</span>'
    label_div = f'<div class="flex-1 flex items-center gap-2 min-w-0">{label_inner}{(" " + badge_html) if badge_html else ""}</div>'

    return f'''        <div onclick="selectPlan(this)"
             data-url="{url}" data-ptype="{ptype}"
             data-label="{p["label"]}" data-days="{p["days"]}" data-price="{p["price"]}" data-perday="{p["perday"]}"{calls_attr}
             class="plan-row flex items-center gap-3.5 bg-white rounded-2xl px-4 py-3.5 cursor-pointer border-2 border-transparent shadow-plan">
          <div class="plan-check w-5 h-5 rounded-full border-2 border-gray-200 shrink-0 flex items-center justify-center">
            <svg class="plan-check-icon w-2.5 h-2.5 text-white hidden" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
          </div>
          {label_div}
          <div class="text-right shrink-0">
            <div class="text-[15px] font-bold text-gray-900">{p["price"]} <span class="text-xs font-medium text-gray-400">USD</span></div>
            <div class="text-[11px] text-gray-400 mt-0.5">{p["perday"]}</div>
          </div>
        </div>'''


def group_by_validity(plans):
    groups = {}
    for p in plans:
        d = p['days']
        if d not in groups:
            groups[d] = []
        groups[d].append(p)
    # Sort by numeric day count ascending (e.g. "3 days" → 3, "30 days" → 30)
    sorted_keys = sorted(groups.keys(), key=lambda d: int(d.split()[0]))
    return [(d, groups[d]) for d in sorted_keys]


def plans_html(plans):
    has_unlim = any(is_unlimited(p) for p in plans)
    has_data  = any(not is_unlimited(p) for p in plans)
    show_toggle = has_unlim and has_data

    toggle_html = ''
    if show_toggle:
        toggle_html = '''    <div class="flex gap-2 mb-6" id="plan-type-tabs">
      <button data-ptype="data" onclick="filterPlanType('data')"
        class="ptype-btn flex-1 py-2 text-sm font-bold rounded-xl border-2 border-brand-500 bg-brand-500 text-white transition-all">
        Data Plans
      </button>
      <button data-ptype="unlimited" onclick="filterPlanType('unlimited')"
        class="ptype-btn flex-1 py-2 text-sm font-bold rounded-xl border-2 border-gray-200 bg-white text-gray-500 transition-all">
        Unlimited
      </button>
    </div>'''

    groups = group_by_validity(plans)
    parts = [toggle_html] if toggle_html else []
    for i, (days, group) in enumerate(groups):
        mb = 'mb-7' if i < len(groups)-1 else ''
        parts.append(f'      <div class="validity-section {mb}">')
        parts.append(f'        <div class="validity-label"><span>{days}</span></div>')
        parts.append(f'        <div class="space-y-2">')
        for p in group:
            parts.append(plan_row(p))
        parts.append(f'        </div>')
        parts.append(f'      </div>')
    return '\n'.join(parts)


def generate(slug, c):
    name = c['name']
    flag = c['flag']
    plans = c['plans']
    from_price = plans[0]['price']
    p_html = plans_html(plans)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} eSIM Data Plans | From {from_price} | esim.win</title>
  <meta name="description" content="{c['desc']}">
  <link rel="canonical" href="https://esim.win/{slug}">
  <meta property="og:title" content="{name} eSIM | From {from_price} | esim.win">
  <meta property="og:description" content="{c['desc']}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://esim.win/{slug}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">

{GTM_SNIPPET}

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{ sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'] }},
          colors: {{
            brand: {{
              50:'#fff5eb',100:'#ffe9d0',200:'#ffd0a0',300:'#ffb06a',
              400:'#ff8c3a',500:'#ff6b1a',600:'#e85500',700:'#c44500',
              800:'#a03700',900:'#7c2b00'
            }}
          }},
          boxShadow: {{ 'plan':'0 1px 4px 0 rgba(0,0,0,.06)' }}
        }}
      }}
    }}
  </script>
  <style>
    html {{ scroll-behavior: smooth; }}
    body {{ background-color: #F7F6F3; }}
    details summary::-webkit-details-marker {{ display: none; }}
    details summary {{ list-style: none; }}
    .plan-row {{ transition: border-color .15s ease, box-shadow .15s ease, background-color .15s ease; }}
    .plan-row:hover {{ box-shadow: 0 4px 16px rgba(0,0,0,.09); }}
    .plan-row.selected {{ border-color: #ff6b1a !important; background-color: #fff9f5; }}
    .plan-check {{ transition: background-color .15s ease, border-color .15s ease; }}
    #sticky-bar {{ transition: transform .35s cubic-bezier(.16,1,.3,1); }}
    .validity-label {{ display:flex; align-items:center; gap:10px; margin-bottom:12px; }}
    .validity-label span {{ font-size:11px; font-weight:700; letter-spacing:.06em; text-transform:uppercase; color:#9CA3AF; white-space:nowrap; }}
    .validity-label::after {{ content:''; display:block; flex:1; height:1px; background:#E5E7EB; }}
  </style>
</head>
<body class="font-sans text-gray-900 antialiased">

  <!-- Nav -->
  <nav id="navbar" class="fixed top-0 left-0 right-0 z-50 bg-white/90 backdrop-blur-md transition-shadow duration-300">
    <div class="max-w-5xl mx-auto px-5 sm:px-8">
      <div class="flex items-center justify-between h-16">
        <a href="/" class="flex items-center gap-2 shrink-0">
          <span class="text-2xl leading-none">🌐</span>
          <span class="text-[17px] font-bold tracking-tight text-gray-900">esim<span class="text-brand-500">.win</span></span>
        </a>
{NAV_LINKS}
        <button id="menu-toggle" class="md:hidden p-2 -mr-1 rounded-xl hover:bg-gray-100" aria-label="Menu">
          <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
        </button>
      </div>
    </div>
    <div id="mobile-menu" class="hidden md:hidden border-t border-gray-100 bg-white/95">
      <div class="max-w-5xl mx-auto px-5 py-3 space-y-0.5">
        <a href="/"            class="block rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50">Home</a>
        <a href="#plans"       class="block rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50">Plans</a>
        <a href="#how-it-works" class="block rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50">How It Works</a>
        <a href="#faq"         class="block rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50">FAQ</a>
      </div>
    </div>
  </nav>

  <!-- Hero -->
  <section id="hero" class="relative pt-16">
    <div class="relative overflow-hidden" style="background:linear-gradient(135deg,#e85500 0%,#ff6b1a 40%,#ff9a00 100%)">
      <div class="absolute -top-20 -left-20 w-96 h-96 rounded-full" style="background:rgba(255,255,255,.18);filter:blur(60px)"></div>
      <div class="absolute -bottom-20 -right-20 w-80 h-80 rounded-full" style="background:rgba(255,255,255,.22);filter:blur(50px)"></div>
      <!-- Decorative geometric shapes (Airalo-style) -->
      <div class="pointer-events-none select-none absolute inset-0 overflow-hidden" aria-hidden="true">
        <!-- Right side shapes -->
        <div class="hidden sm:block absolute top-6 right-8 w-16 h-28 rounded-3xl rotate-[22deg]" style="background:rgba(255,255,255,.18)"></div>
        <div class="hidden sm:block absolute top-4 right-28 w-9 h-9 rotate-45 rounded-xl" style="background:rgba(255,255,255,.15)"></div>
        <div class="hidden md:block absolute top-16 right-48 w-6 h-6 rotate-45 rounded-md" style="background:rgba(255,255,255,.18)"></div>
        <div class="hidden sm:block absolute bottom-6 right-24 w-12 h-12 rounded-xl rotate-[12deg]" style="background:rgba(255,255,255,.14)"></div>
        <div class="hidden md:block absolute bottom-3 right-6 w-14 h-24 rounded-3xl -rotate-[18deg]" style="background:rgba(255,255,255,.14)"></div>
        <!-- Left side shapes -->
        <div class="hidden sm:block absolute top-8 left-8 w-10 h-10 rotate-45 rounded-xl" style="background:rgba(255,255,255,.15)"></div>
        <div class="hidden sm:block absolute bottom-8 left-12 w-20 h-20 rounded-full" style="background:rgba(255,255,255,.10)"></div>
        <div class="hidden md:block absolute top-1/2 left-6 w-7 h-7 rotate-[30deg] rounded-lg" style="background:rgba(255,255,255,.13)"></div>
        <!-- Floating dots -->
        <div class="hidden md:block absolute top-12 right-72 w-3 h-3 rounded-full" style="background:rgba(255,255,255,.35)"></div>
        <div class="hidden md:block absolute bottom-14 right-64 w-2 h-2 rounded-full" style="background:rgba(255,255,255,.40)"></div>
        <div class="hidden md:block absolute top-20 left-32 w-2.5 h-2.5 rounded-full" style="background:rgba(255,255,255,.30)"></div>
      </div>
      <div class="relative max-w-5xl mx-auto px-5 sm:px-8 pt-16 pb-20 sm:pt-20 sm:pb-24 text-center">
        <div class="inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm rounded-full px-4 py-1.5 mb-6">
          <span class="text-2xl leading-none">{flag}</span>
          <span class="text-xs font-bold text-white/90 tracking-wide uppercase">{name} eSIM</span>
        </div>
        <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white leading-[1.1] tracking-tight mb-5">
          {name} eSIM<br><span class="opacity-90">Data Plans</span>
        </h1>
        <p class="text-base sm:text-lg text-white/75 max-w-sm mx-auto mb-8 leading-relaxed">{c['subtitle']}</p>
        <a href="#plans" class="inline-flex items-center gap-2.5 bg-white text-gray-900 font-bold text-sm px-7 py-3.5 rounded-2xl hover:shadow-xl hover:-translate-y-0.5 transition-all duration-200">
          Get My eSIM
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"/></svg>
        </a>
        <div class="flex flex-wrap justify-center gap-4 mt-8">
          <div class="flex items-center gap-1.5 bg-white/20 backdrop-blur-sm rounded-full px-3.5 py-1.5"><svg class="w-3.5 h-3.5 text-white" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg><span class="text-xs font-semibold text-white">Instant Delivery</span></div>
          <div class="flex items-center gap-1.5 bg-white/20 backdrop-blur-sm rounded-full px-3.5 py-1.5"><svg class="w-3.5 h-3.5 text-white" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg><span class="text-xs font-semibold text-white">From {from_price}</span></div>
          <div class="flex items-center gap-1.5 bg-white/20 backdrop-blur-sm rounded-full px-3.5 py-1.5"><svg class="w-3.5 h-3.5 text-white" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg><span class="text-xs font-semibold text-white">No Contract</span></div>
        </div>
      </div>
    </div>
    <div class="bg-white border-b border-gray-100">
      <div class="max-w-5xl mx-auto px-5 sm:px-8 py-3.5 flex flex-wrap items-center justify-center gap-x-6 gap-y-2">
        <div class="flex items-center gap-2"><span style="color:#FBBF24;letter-spacing:-1px">★★★★★</span><span class="text-sm font-bold text-gray-900">4.9</span><span class="text-sm text-gray-400">· 10,000+ travelers</span></div>
        <span class="hidden sm:block text-gray-200 text-lg font-thin">|</span>
        <div class="flex items-center gap-4 text-sm text-gray-500">
          <span class="flex items-center gap-1.5"><svg class="w-3.5 h-3.5 text-green-500" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>Instant delivery</span>
          <span class="flex items-center gap-1.5"><svg class="w-3.5 h-3.5 text-green-500" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>No contract</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Plans -->
  <section id="plans" class="max-w-lg mx-auto px-4 sm:px-6 py-10 sm:py-14">
    <div class="mb-6">
      <h2 class="text-xl font-bold text-gray-900 mb-0.5">Choose your plan</h2>
      <p class="text-sm text-gray-500">{c['compatible']}</p>
    </div>
    <div class="space-y-0">
{p_html}
    </div>
  </section>

  <!-- How It Works -->
  <section id="how-it-works" class="bg-white border-t border-gray-100 py-14 sm:py-20">
    <div class="max-w-3xl mx-auto px-5 sm:px-8">
      <div class="text-center mb-12">
        <h2 class="text-2xl sm:text-3xl font-extrabold text-gray-900 tracking-tight">How it works</h2>
        <p class="text-sm text-gray-500 mt-2">Three steps. Less than two minutes.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-12">
        <div class="flex flex-col items-center text-center">
          <div class="w-11 h-11 rounded-full bg-orange-50 border-2 border-orange-100 flex items-center justify-center mb-4"><span class="text-base font-extrabold text-brand-500">1</span></div>
          <h3 class="text-base font-bold text-gray-900 mb-1.5">Pick a plan</h3>
          <p class="text-sm text-gray-500 leading-relaxed max-w-[180px]">Choose the data and validity that fits your trip.</p>
        </div>
        <div class="flex flex-col items-center text-center">
          <div class="w-11 h-11 rounded-full bg-orange-50 border-2 border-orange-100 flex items-center justify-center mb-4"><span class="text-base font-extrabold text-brand-500">2</span></div>
          <h3 class="text-base font-bold text-gray-900 mb-1.5">Scan the QR code</h3>
          <p class="text-sm text-gray-500 leading-relaxed max-w-[180px]">Your eSIM is delivered instantly to your inbox after purchase.</p>
        </div>
        <div class="flex flex-col items-center text-center">
          <div class="w-11 h-11 rounded-full bg-orange-50 border-2 border-orange-100 flex items-center justify-center mb-4"><span class="text-base font-extrabold text-brand-500">3</span></div>
          <h3 class="text-base font-bold text-gray-900 mb-1.5">Connect &amp; go</h3>
          <p class="text-sm text-gray-500 leading-relaxed max-w-[180px]">Activate on arrival. Full-speed data across {name}.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section id="faq" class="max-w-lg mx-auto px-4 sm:px-6 py-14 sm:py-20">
    <div class="text-center mb-10">
      <h2 class="text-2xl sm:text-3xl font-extrabold text-gray-900 tracking-tight">Frequently asked</h2>
    </div>
    <div class="space-y-2">
      <details class="bg-white rounded-2xl group"><summary class="flex items-center justify-between cursor-pointer px-5 py-4 text-sm font-semibold text-gray-900 select-none">What is an eSIM?<span class="ml-4 shrink-0 w-5 h-5 rounded-full bg-gray-100 flex items-center justify-center text-gray-500 group-open:bg-gray-200 transition-colors"><svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"/></svg></span></summary><div class="px-5 pb-4 text-sm text-gray-500 leading-relaxed">An eSIM is a digital SIM built into your phone. Scan a QR code to activate — no physical card, no local SIM shop needed.</div></details>
      <details class="bg-white rounded-2xl group"><summary class="flex items-center justify-between cursor-pointer px-5 py-4 text-sm font-semibold text-gray-900 select-none">Is my device compatible?<span class="ml-4 shrink-0 w-5 h-5 rounded-full bg-gray-100 flex items-center justify-center text-gray-500 group-open:bg-gray-200 transition-colors"><svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"/></svg></span></summary><div class="px-5 pb-4 text-sm text-gray-500 leading-relaxed">iPhone XS+, Pixel 3+, Samsung Galaxy S20+ and most modern phones support eSIM. Check Settings → Mobile Data → Add eSIM.</div></details>
      <details class="bg-white rounded-2xl group"><summary class="flex items-center justify-between cursor-pointer px-5 py-4 text-sm font-semibold text-gray-900 select-none">Can I keep my regular SIM?<span class="ml-4 shrink-0 w-5 h-5 rounded-full bg-gray-100 flex items-center justify-center text-gray-500 group-open:bg-gray-200 transition-colors"><svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"/></svg></span></summary><div class="px-5 pb-4 text-sm text-gray-500 leading-relaxed">Yes — dual SIM lets you keep your home number for calls while using the eSIM for data in {name}.</div></details>
      <details class="bg-white rounded-2xl group"><summary class="flex items-center justify-between cursor-pointer px-5 py-4 text-sm font-semibold text-gray-900 select-none">What if my data runs out?<span class="ml-4 shrink-0 w-5 h-5 rounded-full bg-gray-100 flex items-center justify-center text-gray-500 group-open:bg-gray-200 transition-colors"><svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"/></svg></span></summary><div class="px-5 pb-4 text-sm text-gray-500 leading-relaxed">Your connection pauses — no surprise charges. Buy a top-up or new plan anytime.</div></details>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-gray-950 text-gray-400 py-10 pb-32 sm:pb-10">
    <div class="max-w-lg mx-auto px-5 sm:px-8 text-center">
      <a href="/" class="inline-flex items-center gap-2 mb-4"><span class="text-xl">🌐</span><span class="text-base font-bold text-white">esim<span class="text-brand-400">.win</span></span></a>
      <p class="text-xs text-gray-500 leading-relaxed mb-6">Instant eSIM data plans for 200+ destinations.<br>No roaming. No contracts.</p>
      <div class="flex flex-wrap justify-center gap-5 text-xs mb-8">
        <a href="/"      class="hover:text-white transition-colors">Home</a>
        <a href="#plans" class="hover:text-white transition-colors">Plans</a>
        <a href="#faq"   class="hover:text-white transition-colors">FAQ</a>
        <a href="/europe"     class="hover:text-white transition-colors">Europe eSIM</a>
        <a href="/best-esim" class="hover:text-white transition-colors">Best eSIM</a>
      </div>
      <div class="border-t border-gray-800 pt-6 text-xs text-gray-500 space-y-1.5">
        <p class="font-semibold text-gray-400">Arty Digital Ltd</p>
        <p>9B Amtel Building, 148 Des Voeux Road, Central, Hong Kong</p>
        <div class="flex flex-wrap justify-center gap-4 pt-2 pb-1">
          <a href="/legal.html#privacy"   class="hover:text-white transition-colors">Privacy Policy</a>
          <a href="/legal.html#terms"     class="hover:text-white transition-colors">Terms of Service</a>
          <a href="/legal.html#affiliate" class="hover:text-white transition-colors">Affiliate Disclosure</a>
        </div>
        <p>&copy; 2026 esim.win &mdash; All rights reserved.</p>
        <p class="text-gray-600">We may earn a commission when you purchase through links on this site at no extra cost to you.</p>
      </div>
    </div>
  </footer>

  <!-- Sticky Buy Now Bar -->
  <div id="sticky-bar" class="fixed bottom-0 left-0 right-0 z-40 bg-white/95 backdrop-blur-md border-t border-gray-200/80 shadow-[0_-4px_24px_rgba(0,0,0,.10)] translate-y-full">
    <div class="max-w-lg mx-auto px-4 sm:px-6 py-3 flex items-center gap-4">
      <div class="flex-1 min-w-0">
        <p class="text-[11px] font-medium text-gray-400 uppercase tracking-wide truncate" id="bar-label">{plans[0]['label']} &middot; {plans[0]['days']}</p>
        <div class="flex items-baseline gap-2">
          <span class="text-lg font-extrabold text-gray-900 leading-tight" id="bar-price">{plans[0]['price']}</span>
          <span class="text-[11px] text-gray-400" id="bar-perday">{plans[0]['perday']}</span>
        </div>
      </div>
      <div class="hidden sm:flex flex-col items-end shrink-0">
        <div class="flex items-center gap-1 text-[11px] text-gray-400"><svg class="w-3 h-3 text-green-500 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd"/></svg>Secure checkout</div>
        <div class="text-[10px] text-gray-300 mt-0.5">Visa &middot; Mastercard &middot; Apple Pay</div>
      </div>
      <button id="buy-now-btn" class="shrink-0 inline-flex items-center gap-2 bg-brand-500 hover:bg-brand-600 active:scale-95 text-white font-bold text-sm px-6 py-3 rounded-xl transition-all duration-150 shadow-md shadow-orange-200">
        Buy Now
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
      </button>
    </div>
  </div>

  <script>
    var selectedUrl = '';

    function selectPlan(el) {{
      document.querySelectorAll('.plan-row').forEach(function(row) {{
        row.classList.remove('selected');
        row.querySelector('.plan-check').style.backgroundColor = '';
        row.querySelector('.plan-check').style.borderColor = '';
        row.querySelector('.plan-check-icon').classList.add('hidden');
      }});
      el.classList.add('selected');
      el.querySelector('.plan-check').style.backgroundColor = '#ff6b1a';
      el.querySelector('.plan-check').style.borderColor = '#ff6b1a';
      el.querySelector('.plan-check-icon').classList.remove('hidden');
      selectedUrl = el.dataset.url;
      document.getElementById('bar-label').textContent  = el.dataset.label + ' · ' + el.dataset.days;
      document.getElementById('bar-price').textContent  = el.dataset.price;
      document.getElementById('bar-perday').textContent = el.dataset.perday;
      document.getElementById('sticky-bar').classList.remove('translate-y-full');
      if (typeof gtag === 'function') {{
        gtag('event', 'select_item', {{
          item_list_name: '{name} eSIM Plans',
          items: [{{ item_id: el.dataset.url.split('/').filter(Boolean).pop(), item_name: el.dataset.label + ' · ' + el.dataset.days, price: parseFloat(el.dataset.price.replace('$','')), currency:'USD', quantity:1 }}]
        }});
      }}
    }}

    document.getElementById('buy-now-btn').addEventListener('click', function() {{
      if (!selectedUrl) return;
      if (typeof gtag === 'function') {{
        var price = parseFloat(document.getElementById('bar-price').textContent.replace('$',''));
        gtag('event','begin_checkout',{{ currency:'USD', value:price, items:[{{ item_id:selectedUrl.split('/').filter(Boolean).pop(), item_name:document.getElementById('bar-label').textContent, item_category:'{name} eSIM', price:price, currency:'USD', quantity:1 }}] }});
      }}
      // Cross-domain tracking: same-tab navigation so GA4 linker works and
      // popup blockers can't interfere. Manually append _ga (session continuity)
      // and gclid (Google Ads attribution) to the simoptions.com URL.
      var url = selectedUrl;
      var gclMatch = document.cookie.match(/_gcl_aw=GCL\.\d+\.([^;]+)/);
      var gclid = gclMatch ? gclMatch[1] : '';
      function goToCheckout(clientId) {{
        var params = [];
        if (clientId) params.push('_ga=' + encodeURIComponent('GA1.1.' + clientId));
        if (gclid)    params.push('gclid=' + encodeURIComponent(gclid));
        var sep = url.indexOf('?') !== -1 ? '&' : '?';
        window.location.href = params.length ? url + sep + params.join('&') : url;
      }}
      if (typeof gtag === 'function') {{
        gtag('get', 'G-FWN5WTYV2V', 'client_id', goToCheckout);
      }} else {{
        goToCheckout('');
      }}
    }});

    document.getElementById('menu-toggle').addEventListener('click',function(){{document.getElementById('mobile-menu').classList.toggle('hidden');}});
    document.querySelectorAll('#mobile-menu a').forEach(function(l){{l.addEventListener('click',function(){{document.getElementById('mobile-menu').classList.add('hidden');}});}});

    new IntersectionObserver(function(e){{document.getElementById('navbar').classList.toggle('shadow-sm',!e[0].isIntersecting);}},{{threshold:0}}).observe(document.getElementById('hero'));

    // Calls & SMS badges — DOM is ready (script is at bottom of body)
    document.querySelectorAll('.plan-row[data-calls="1"]').forEach(function(row) {{
      var wrap = row.querySelector('.flex-1');
      if (!wrap) return;
      var b = document.createElement('span');
      b.className = 'shrink-0 inline-flex items-center gap-1 text-[10px] font-bold text-sky-700 bg-sky-50 border border-sky-200 rounded-full px-2 py-0.5 leading-none whitespace-nowrap';
      b.innerHTML = '<svg class="w-2.5 h-2.5 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/></svg>Calls & SMS';
      wrap.appendChild(b);
    }});

    // Unlimited / Data toggle — defined globally so onclick attrs can call it immediately
    function filterPlanType(type) {{
      document.querySelectorAll('.ptype-btn').forEach(function(btn) {{
        var active = btn.dataset.ptype === type;
        btn.classList.toggle('bg-brand-500', active);
        btn.classList.toggle('text-white', active);
        btn.classList.toggle('border-brand-500', active);
        btn.classList.toggle('bg-white', !active);
        btn.classList.toggle('text-gray-500', !active);
        btn.classList.toggle('border-gray-200', !active);
      }});
      var firstVisible = null;
      document.querySelectorAll('.plan-row[data-ptype]').forEach(function(row) {{
        var show = row.dataset.ptype === type;
        row.style.display = show ? '' : 'none';
        if (show && !firstVisible) firstVisible = row;
      }});
      document.querySelectorAll('.validity-section').forEach(function(sec) {{
        var hasVisible = Array.from(sec.querySelectorAll('.plan-row[data-ptype]')).some(function(r){{return r.style.display !== 'none';}});
        sec.style.display = hasVisible ? '' : 'none';
      }});
      if (firstVisible) selectPlan(firstVisible);
    }}

    // Init: if toggle exists, default to Data Plans (hides unlimited rows immediately)
    (function() {{
      var tabs = document.getElementById('plan-type-tabs');
      if (tabs) {{
        filterPlanType('data');
      }} else {{
        var first = document.querySelector('.plan-row');
        if (first) selectPlan(first);
      }}
    }})();
  </script>
</body>
</html>'''
    return html


import os
out_dir = '/Users/jonathandion/esim.win'
for slug, c in COUNTRIES.items():
    html = generate(slug, c)
    path = os.path.join(out_dir, slug + '.html')
    with open(path, 'w') as f:
        f.write(html)
    print(f'  wrote {slug}.html ({len(c["plans"])} plans)')

print(f'\nDone — {len(COUNTRIES)} country pages generated.')
