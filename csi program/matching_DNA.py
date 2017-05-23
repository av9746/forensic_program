suspects = {
    "Eva": {
        "Gender": "Female",
        "Race": "White",
        "HairColor": "Blonde",
        "EyeColor": "Blue",
        "FaceShape": "Oval"
    },
    "Larisa": {
        "Gender": "Female",
        "Race": "White",
        "HairColor": "Brown",
        "EyeColor": "Brown",
        "FaceShape": "Oval"
    },
    "Matej": {
        "Gender": "Male",
        "Race": "White",
        "HairColor": "Black",
        "EyeColor": "Blue",
        "FaceShape": "Oval"
    },
    "Miha": {
        "Gender": "Male",
        "Race": "White",
        "HairColor": "Brown",
        "EyeColor": "Green",
        "FaceShape": "Square"
    }
}

characteristics = {
    "Gender": {
        "Female": "TGAAGGACCTTC",
        "Male": "TGCAGGAACTTC"
    },
    "Race": {
        "White": "AAAACCTCA",
        "Black": "CGACTACAG",
        "Asian": "CGCGGGCCG"
    },
    "HairColor": {
        "Black": "CCAGCAATCGC",
        "Brown": "GCCAGTGCCG",
        "Blonde": "TTAGCTATCGC"
    },
    "EyeColor": {
        "Blue": "TTGTGGTGGC",
        "Green": "GGGAGGTGGC",
        "Brown": "AAGTAGTGAC"
    },
    "FaceShape": {
        "Square": "GCCACGG",
        "Round": "ACCACAA",
        "Oval": "AGGCCTCA"
    }
}

class Thief:
    name = ""
    characteristics = {}

dna_file = open('dna.txt', 'r')
dna = dna_file.read()
dna_file.close()

for key, value in characteristics.items():
    for charateristic, letters in value.items():
        if letters in dna:
            Thief.characteristics[key] = charateristic

for suspect, characteristics in suspects.items():
    if characteristics == Thief.characteristics:
        Thief.name = suspect




print ("The bastard who ate the ice cream was %s 😤!!!!!!" % Thief.name)














