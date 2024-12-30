# Nivers

Tem problema em dar/receber presentes? Convide todo mundo pra cá!

```mermaid
classDiagram

Amigo "1"--"*" SugestaoDePresente
Amigo "1"--"*" Amizade : remetente
Amigo "1"--"*" Amizade : destinatario


class Amigo {
    username
    bio
    data_de_nascimento
    foto
}

class Amizade {
    data
}

class SugestaoDePresente {
    nome
    link
    descricao
}
```