#### Fonction secondaire


def ispalindrome(s):
    s=s.lower()
    s=s.replace(" ","")

    remove = "!()-[]}{;:'\",<>./?@#$%^&*_~ "
    for p in s:
        for q in remove:
            if(q==p):
                s=s.replace(p,"")

    accents =['à','â','ä','á','ã','å','ç','é','è','ê','ë','í','ì','ï','î','ñ','ô','ö','ò','ó','õ','ù','û','ü','ú','ý','ÿ']
    for i in range(len(accents)):
        if i <= 5:
            s=s.replace(accents[i],'a')
        elif(i==6):
            s=s.replace(accents[i],'c')
        elif(i>6 and i<=10):
            s=s.replace(accents[i],'e')
        elif(i>10 and i<=14):
            s=s.replace(accents[i],'i')
        elif(i==15):
            s=s.replace(accents[i],'n')
        elif(i>15 and i<=20):
            s=s.replace(accents[i],'o')
        elif(i>20 and i<=24):
            s=s.replace(accents[i],'u')
        elif(i>24 and i<=26):
            s=s.replace(accents[i],'y')    

    n=len(s)
    k=n//2
    i=0
    pal=True
    while(i<k):
        if s[i]!=s[n-1-i]:
            pal=False
            break
        i+=1
    return pal

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()