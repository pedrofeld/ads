# Fundamentos da Programação Web – Resumo para Provas

---

## 📘 Aula 1 – HTML

### TEMA 1 – Conceitos Iniciais

#### História e definição
- **HTML**: linguagem de marcação usada para estruturar páginas web.
- Criado por **Tim Berners-Lee** em 1990.
- Baseado no SGML. Atual versão: **HTML5**.

#### Termos importantes
- **Front-end**: HTML, CSS, JS (interface).
- **Back-end**: banco de dados, lógica, servidor.
- **Full-stack**: ambos.
- **HTTP**: protocolo usado entre cliente e servidor.

---

### TEMA 2 – Ambiente de Desenvolvimento

#### Editores HTML
- **Notepad**, **Notepad++**, **Sublime Text**, **Visual Studio Code (VS Code)**

#### VS Code – Dicas
- `CTRL + SHIFT + P` → Paleta de comandos.
- Extensões úteis:
  - Live Server
  - vscode-icons
  - Material Icon Theme
  - Open in browser

---

### TEMA 3 – HTML Básico

#### Estrutura mínima
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Título</title>
</head>
<body>
  <!-- Conteúdo -->
</body>
</html>
```

#### Tags básicas
- `<h1>` a `<h6>` – títulos
- `<p>` – parágrafo
- `<br>` – quebra de linha
- `<hr>` – linha horizontal
- `<ul>`, `<ol>`, `<li>` – listas

---

### TEMA 4 – Links, Imagens e Tabelas

#### Links
```html
<a href="https://google.com" target="_blank">Google</a>
```

#### Imagens
```html
<img src="imagem.jpg" alt="descrição" width="200">
```

#### Tabelas
```html
<table border="1">
  <tr>
    <th>Nome</th><th>Id</th>
  </tr>
  <tr>
    <td>Maria</td><td>123</td>
  </tr>
</table>
```

---

### TEMA 5 – Formulários

#### Estrutura básica
```html
<form>
  <label for="nome">Nome:</label>
  <input type="text" id="nome" name="nome"><br>

  <label for="email">Email:</label>
  <input type="email" id="email" name="email"><br>

  <textarea name="msg">Digite sua mensagem</textarea><br>

  <button type="submit">Enviar</button>
</form>
```

---

## 🎨 Aula 2 – CSS

### TEMA 1 – Introdução ao CSS

#### Definição
- CSS define estilo/visual das páginas HTML.

#### Sintaxe
```css
h1 {
  color: blue;
  font-size: 12px;
}
```

#### Tipos de seletores
- ID: `#id`
- Classe: `.classe`
- Universal: `*`
- Agrupamento: `h1, h2, p { }`

#### Formas de aplicar CSS
1. CSS Externo: via `<link href="estilo.css">`
2. CSS Interno: dentro de `<style>` no `<head>`
3. CSS Inline: direto no elemento (`style="..."`)

#### Hierarquia
1. Inline
2. Interno/Externo
3. Estilo padrão do navegador

---

### TEMA 2 – Comentários, Cores, Fundo, Bordas, Margens e Padding

#### Comentários
```css
/* Comentário em CSS */
```

#### Cores
- Nome: `red`, `blue`
- RGB: `rgb(255, 0, 0)`
- HEX: `#ff0000`
- HSL: `hsl(0, 100%, 50%)`

#### Plano de fundo
```css
background-color: black;
background-image: url("fundo.jpg");
```

#### Bordas
```css
border: 2px solid red;
border-radius: 25px;
```

#### Margem
```css
margin: 25px 50px 75px 100px;
/* top, right, bottom, left */
```

#### Padding
```css
padding: 10px; /* Espaço interno */
```

---

### TEMA 3 – Width, Height, Texto, Fontes e Box Model

#### Tamanhos
```css
width: 300px;
height: 200px;
max-width: 100%;
```

#### Texto
```css
text-align: center;
text-decoration: underline;
text-decoration-style: dotted;
text-decoration-color: red;
```

#### Fontes
```css
font-family: Arial, Helvetica, sans-serif;
font-size: 16px;
```

#### Box Model
- Inclui: `content`, `padding`, `border`, `margin`

```css
div {
  width: 350px;
  padding: 10px;
  border: 5px dotted green;
  margin: 0;
}
```

---

### TEMA 4 – Float, Clear, Block e Inline

#### Float e Clear
```css
float: left | right;
clear: both;
```

#### Tipos de elementos
- **Block**: `<div>`, `<p>`, `<section>`
- **Inline**: `<span>`, `<a>`, `<strong>`

---

### TEMA 5 – Display, Position, Z-index e Overflow

#### Display
```css
display: block | inline | none;
```

#### Position
```css
position: static | relative | absolute | fixed;
```

#### Z-Index
```css
z-index: 1; /* controla a sobreposição */
```

#### Overflow
```css
overflow: visible | hidden | scroll | auto;
```

---

## ✅ Finalização

Com HTML e CSS, você pode criar páginas web estruturadas e estilizadas. Pratique os conceitos para reforçar seu aprendizado e desenvolver layouts cada vez mais completos.


---

## Aula 3 – CSS Avançado

## 📘 TEMA 1 – Árvore do Documento (DOM)

### Conceitos
- DOM é a estrutura hierárquica dos elementos HTML.
- CSS pode herdar propriedades (ex: `color`), outras não (ex: `width`).
- Relacionamentos: pai, filho, ancestral, descendente, irmãos.

### Seletores de relacionamento
| Seletor | Descrição |
|--------|-----------|
| `E F` | Seleciona `F` descendente de `E` |
| `E > F` | Seleciona `F` filho direto de `E` |
| `E + F` | Seleciona `F` imediatamente após `E` |
| `E ~ F` | Seleciona `F` irmão geral após `E` |
| `:first-child` / `:last-child` | Seleciona o primeiro/último filho |

---

## 🎯 TEMA 2 – Pseudoclasses e Pseudoelementos

### Pseudoclasses
- `:link` – link não visitado
- `:visited` – link visitado
- `:hover` – ao passar o mouse
- `:active` – ao clicar
- `:focus` – ao receber foco
- `:checked` – checkbox ou radio marcados
- `:enabled` / `:disabled` – campos habilitados/desabilitados

**Ordem correta**:
```css
a:link {}
a:visited {}
a:hover {}
a:active {}
```

### Pseudoelementos
- `::before` / `::after` – insere conteúdo antes ou depois
- `::first-letter` – estiliza a primeira letra
- `::first-line` – estiliza a primeira linha
- `::marker` – estiliza marcadores de lista
- `::selection` – estiliza texto selecionado

---

## 🧭 TEMA 3 – Menus e Botões

### Menu vertical (com `<ul>`)
```html
<ul>
  <li><a href="index.html">Home</a></li>
  <li><a href="noticias.html">Notícias</a></li>
  <li><a href="contato.html">Contato</a></li>
</ul>
```

**CSS**:
```css
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  width: 200px;
  background-color: #f1f1f1;
}
li a {
  display: block;
  color: #000;
  padding: 8px 16px;
  text-decoration: none;
}
li a:hover {
  background-color: #555;
  color: white;
}
```

### Menu horizontal
- Mudar `li { display: inline; }` ou `float: left;`

### Submenu (menu suspenso)
- Usa listas aninhadas (`<ul><li><ul>...</ul></li></ul>`)
- Exibir submenu com `li:hover ul { display: block; }`

### Botões CSS
```html
<button>Botão</button>
<a href="#" class="button">Link como botão</a>
<input type="button" class="button" value="Enviar">
```

```css
.button {
  background-color: gray;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
}
```

---

## 📦 TEMA 4 – Formatações Diversas

### Box model e `box-sizing`
- `box-sizing: border-box;` → inclui `padding` e `border` na `width`

### Variáveis CSS
```css
:root {
  --dourado: #DEB44B;
}
h2 {
  border-bottom: 2px solid var(--dourado);
}
```

### Imagens
```css
img {
  border-radius: 10px; /* arredondado */
  opacity: 0.5;
  display: block;
  margin: auto;
  max-width: 100%;
  height: auto;
}
```

---

## 🎞️ TEMA 5 – Transformações e Transições

### Transformações 2D
```css
transform: translateX(80px);
transform: translateY(100px);
transform: scaleX(1.5);
transform: scaleY(2);
transform: rotate(20deg);
transform: skewX(20deg);
transform: skewY(10deg);
transform: scale(1.5, 2);
transform: matrix(a, b, c, d, e, f);
```

### Transições CSS
```css
div {
  transition: width 2s, transform 2s;
}
div:hover {
  width: 300px;
  transform: rotate(360deg);
}
```

- `transition-delay`: atraso
- `transition-timing-function`: ease, linear, ease-in, etc.

---

## ✅ Finalização
Essa aula aprofundou o uso do CSS com:
- Relações no DOM
- Pseudoclasses e pseudoelementos
- Menus e botões
- Variáveis e imagens
- Transformações e transições

## 📘 Aula 4 – HTML5 Avançado e CSS Grid/Flexbox

### TEMA 1 – Elementos Semânticos (HTML5)
- `<header>`: Cabeçalho da seção ou página.
- `<section>`: Agrupamento temático de conteúdo.
- `<article>`: Conteúdo independente e reutilizável.
- `<nav>`: Navegação principal.
- `<aside>`: Conteúdo lateral ou relacionado.
- `<footer>`: Rodapé da seção/página.
- `<hgroup>`: Agrupa múltiplos títulos.
- `<div>`: Container genérico (semântico apenas se usado com `class`/`id`).

### TEMA 2 – CSS Grid
- `display: grid;`: transforma em grid container.
- `grid-template-columns` / `grid-template-rows`: define colunas e linhas.
- `gap`: espaçamento entre células (linhas/colunas).
- `grid-column` / `grid-row`: posicionamento por linha e coluna.
- `grid-area`: posicionamento por área.
- `repeat()`, `calc()`, `minmax()` e unidade `fr`: flexibilidade no layout.

### TEMA 3 – Flexbox
- `display: flex;`: organiza elementos em uma dimensão.
- Ideal para alinhamentos horizontais ou verticais simples.

---

## 💻 Aula 5 – JavaScript Introdução

### TEMA 1 – História e Ambiente
- Criado em 1995 por Brendan Eich (Netscape).
- ECMAScript é o nome oficial.
- Roda no navegador (lado do cliente).
- Editores recomendados: VS Code, CodePen, JSFiddle.

### TEMA 2 – Variáveis e Tipos de Dados
- `var`, `let`, `const`: formas de declarar variáveis.
- Tipos primitivos: `boolean`, `number`, `string`, `undefined`, `null`, `BigInt`.
- `typeof`: retorna o tipo da variável.
- Template string: `${variável}` com crase.
- Métodos comuns de string: `.length`, `.charAt()`, `.slice()`, `.split()`.

### TEMA 3 – Operadores
- Aritméticos: `+`, `-`, `*`, `/`, `%`, `**`
- Comparação: `==`, `===`, `!=`, `!==`, `<`, `>`, `<=`, `>=`
- Lógicos: `&&`, `||`, `!`

---

## 🧠 Aula 6 – JavaScript Avançado

### TEMA 1 – Objetos e Arrays
- Objetos: estrutura com propriedades (chave-valor).
- Arrays: lista indexada de valores.
- Métodos de array:
  - `.push()`, `.pop()`, `.shift()`, `.unshift()`
  - `.indexOf()`, `.reverse()`, `.slice()`, `.concat()`

### TEMA 2 – Funções
- Funções nomeadas e com parâmetros.
- `return`: retorna valores.
- Arrow function: `const soma = (a,b) => a + b;`
- Recursividade: função que chama a si mesma.
- `for...in`: itera sobre objetos.
- `for...of`: itera sobre arrays.

### TEMA 3 – Objeto `Date()`
- `new Date()`: cria data atual.
- Métodos úteis:
  - `.getDate()`, `.getDay()`, `.getFullYear()`
  - `.getMonth()`, `.getHours()`, `.getTime()`