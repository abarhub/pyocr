
import openai
 
openai.api_key = "coller ici votre clé"
 
lesmessages=[{"role": "user", "content": "On va jouer au jeu du plus petit ou plus grand. Je pense à un nombre entre 1 et 100.Tu dois deviner ce nombre. Propose un nombre et je te dirai si il est trop grand, trop petit ou si tu a gagne"}]
msg="perdu"
while msg != "gagne":
    reply = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=lesmessages,
                temperature = 0)
    
    print(reply['choices'][0]['message']['content'])
    lesmessages.append({"role": "assistant", "content":reply['choices'][0]['message']['content']})
    msg = input()
    lesmessages.append({"role": "user", "content": msg})
    
lesmessages = []   
msg = "On joue au jeu du plus petit ou plus grand! Maintenant tu choisis un nombre entre 1 et 100. Je vais essayer de le deviner. Je vais te faire des propositions. A chaque fois tu me répondras soit : 'trop grand' si ma proposition est trop grande, soit 'trop petit' si ma proposition est trop petite, ou 'gagné' si j'ai trouvé le nombre auquel tu pensais. Ma première proposition est"+ input("proposition?")
lesmessages.append({"role": "user", "content": msg})
 
while msg!="youpi":
    reply = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature = 0)
    
    print(reply['choices'][0]['message']['content'])
    messages.append({"role": "assistant", "content":reply['choices'][0]['message']['content']})
    msg = input("proposition?")
    messages.append({"role": "user", "content": msg}
