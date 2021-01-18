from PyInquirer import style_from_dict, Token, prompt, Separator

questions = [
    {
        'type': 'list',
        'message': 'Outil SSI_INSAT pour la cryptographie',
        'name': 'option',
        'choices': [
            Separator(' Options'),
            {

                'name': '1-Codage et Décodage d"un message'
            },
            {
                'name': '2-Hashage d"un message'
            },
            {
                'name': '3-Craquage d"un message hashé'
            },
            {
                'name': '4-Chiffrement et déchiffrement symétrique d"un message'
            },
            {
                'name': '5-Chiffrement et déchiffrement asymétrique d"un message'
            },
            {
                'name': '6-Quitter'
            }

        ],
        'validate': lambda answer: 'Vous devez choisir une option.'
        if len(answer) == 0 else True
    }
]

CodOrDec = [
    {
        'name': 'choice',
                'type': 'list',
                'message': 'Codage ou Décodage d"un message',
                'choices': [
                    {
                        'name': 'codage',
                        'value': 'codage'
                    },
                    {
                        'name': 'decodage',
                        'value': 'decodage'
                    }
                ]
    },
    {
        'name': 'str',
        'type': 'input',
        'message': 'entrer votre chaine de charactere',

    }
]


ChifOrDechif = [
    {
        'name': 'choice',
                'type': 'list',
                'message': 'Chiffrement ou Dechiffrement d"un message',
                'choices': [
                    {
                        'name': 'Chiffrement',
                        'value': 'chiffre'
                    },
                    {
                        'name': 'Dechiffrement',
                        'value': 'dechiffre'
                    }
                ]
    },
    {
        'name': 'str',
        'type': 'input',
        'message': 'entrer votre chaine de charactere',

    }
]

algorithmesCodage = [
    {
        'name': 'choice',
        'type': 'list',
                'message': 'choisir un algorithme',
                'choices': [
                    {
                        'name': 'Base64',
                        'value': 'BASE64'
                    },
                    {
                        'name': 'Ascci',
                        'value': 'ASCCI'
                    }
                ]
    }
]

algorithmesHashage = [
    {
        'name': 'choice',
        'type': 'list',
                'message': 'choisir un algorithme',
                'choices': [
                    {
                        'name': 'md5',
                        'value': 'md5'
                    },
                    {
                        'name': 'SHA-512',
                        'value': 'SHA-512'
                    }
                ]
    },
    {
        'name': 'str',
        'type': 'input',
        'message': 'entrer votre chaine de charactere',

    }
]
CrackAttack = [
    {
        'name': 'choice',
        'type': 'list',
                'message': 'choisir un algorithme',
                'choices': [
                    {
                        'name': 'brute force',
                        'value': 'BRUTE_FORCE'
                    },
                    {
                        'name': 'dictionary attack',
                        'value': 'DICTIONARY_ATTACK'
                    }
                ]
    },
    {
        'name': 'str',
        'type': 'input',
        'message': 'entrer votre Hash',

    }
]

algorithmesSymetrique = [
    {
        'name': 'choice',
        'type': 'list',
                'message': 'choisir un algorithme',
                'choices': [
                    {
                        'name': 'AES',
                        'value': 'AES'
                    }
                ]
    }
]

algorithmesAsymetrique = [
    {
        'name': 'choice',
        'type': 'list',
                'message': 'choisir un algorithme',
                'choices': [
                    {
                        'name': 'RSA',
                        'value': 'RSA'
                    }
                ]
    }
]
