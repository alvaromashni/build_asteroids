# Asteroids Game (Pygame)

Um jogo estilo clássico Asteroids, desenvolvido em Python utilizando a biblioteca Pygame.

Esse projeto foi construído como parte do curso da Boot.dev, com foco em praticar conceitos fundamentais de desenvolvimento de jogos e programação orientada a objetos.

---

## Sobre o jogo

Você controla uma nave no espaço e precisa destruir asteroides enquanto desvia deles.

Simples na ideia, mas quando a tela começa a encher, vira caos.

- Movimentação da nave
- Disparo de projéteis
- Asteroides com colisão
- Loop de jogo em tempo real
- Sistema de entidades baseado em classes

---

## O que eu pratiquei aqui

Esse projeto foi muito mais sobre fundamentos do que sobre “fazer um joguinho”.

- Game loop (render + update)
- Programação orientada a objetos (OOP)
- Separação de responsabilidades (arquivos por entidade)
- Detecção de colisão
- Controle de estado do jogo
- Estrutura modular em Python

Foi aquele tipo de projeto que parece simples, mas te obriga a pensar como um desenvolvedor de verdade.

---

## Estrutura do projeto

```
.
├── main.py
├── player.py
├── asteroid.py
├── asteroidfield.py
├── bullets.py
├── circleshape.py
├── constants.py
├── requirements.txt
```

---

## Tecnologias

- Python 3.x
- Pygame
- Programação Orientada a Objetos (OOP)

---

## Como rodar o projeto

1. Clone o repositório

git clone https://github.com/alvaromashni/build_asteroids.git  
cd build_asteroids

2. Crie um ambiente virtual (opcional)

python -m venv venv  
source venv/bin/activate  (Linux/Mac)  
venv\Scripts\activate     (Windows)

3. Instale as dependências

pip install -r requirements.txt

4. Execute o jogo

python main.py

---

## Controles

- W / ↑ → mover para frente
- A / ← → girar para esquerda
- D / → → girar para direita
- Espaço → atirar

---

## Melhorias futuras

- Sistema de pontuação
- Efeitos sonoros
- Partículas/explosões
- Menu inicial
- Sistema de vidas
- Dificuldade progressiva

---

## Considerações

Esse projeto foi uma ótima forma de transformar teoria em prática.

Construir algo interativo, mesmo simples, muda completamente a forma como você entende código.

---

## Licença

Esse projeto é apenas para fins educacionais.
