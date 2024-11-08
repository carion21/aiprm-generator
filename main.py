from datetime import datetime
from constants import INPUTS, LANGS, PROMPT_FILE_PATH

prompt = ""
try:
    with open(PROMPT_FILE_PATH, "r") as file:
        prompt = file.read()

    inputs: dict[str, str] = {}

    for key in INPUTS:
        print('=' * 50)

        if INPUTS[key]["values"]:
            print("Les valeurs possibles sont: ", INPUTS[key]["values"])

        inputs[key] = input(INPUTS[key]["label"] + " ")
        while INPUTS[key]["values"] and inputs[key].lower() not in INPUTS[key]["values"]:
            print('-' * 50)
            print(f"La valeur {inputs[key]} n'est pas valide.")
            inputs[key] = input(INPUTS[key]["label"] + " ")

    inputs['lang'] = LANGS[inputs['lang']]
    platform = "FACEBOOK + INSTAGRAM"
    prompt = prompt.format(
        inputs.get('lang').upper(),
        inputs.get('product').upper(),
        platform,
        inputs.get('product').upper(),
        platform.replace(" + ", " et "),
        platform.replace(" + ", " et "),
        platform.replace(" + ", " et "),
        inputs.get('product').upper(),
    )

    # save prompt to file with datetime
    print("Prompt en cours de génération...")
    fname = "prompt-{}.txt".format(
        datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    with open(f"./output/{fname}", "w") as file:
        file.write(prompt)
        print(f"Prompt généré avec succès dans le fichier {fname}")

    # prompt = prompt.format(**INPUTS)
except FileNotFoundError:
    print(f"Le fichier {PROMPT_FILE_PATH} n'existe pas.")
    exit(1)
