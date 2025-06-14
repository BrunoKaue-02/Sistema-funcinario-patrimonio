# Sistema Funcionário & Patrimônio

Este sistema foi desenvolvido como parte do trabalho final da disciplina de **Banco de Dados**. Ele permite o gerenciamento de funcionários e seus respectivos patrimônios de forma simples e eficiente.


## IMPORTANTE! Padrões de Commit
- adicionar feature -> ex: **feat:** adicionar uma funcionalidade no botão x
- corrigir um bug -> ex: **fix:** corrigindo o campo nome
- refatoração -> ex: **refactor:** refatorando o layout da página tal
- mexer no **README** -> ex: **docs:** intrução de como rodar o projeto
- mexer em funcionalidade que não afetam o código fonte -> ex: **chore:** modificando a depedência x
- mexer em CSS -> ex: **style:** adicionando espaçamento entre linhas


## Como baixar o projeto na sua máquina

Rode no seu terminal
```bash
git clone https://github.com/BrunoKaue-02/Sistema-funcinario-patrimonio.git
```

## Estrutura de pastas
Sistema-funcionario-patrimonio/ <br>
├── app/ <br>
│ ├── assets/ <br>
│ └── input.css <br>
| ├── controller/ <br>
| └── input.css <br>
| ├── database/ <br>
| ├── model/ <br>
| ├── routes/ <br>
│ │ └── home_routes.py <br>
│ │ ├── user_routes.py <br>
│ ├── templates/ <br>
│ │ └── index.html <br>
│ │ ├── home.html <br>
│ │ ├── sign_up.html <br>
│ ├── init.py <br>
│ ├── static/ <br>
│ │ ├── output.css <br>
│ │ └── icons/ <br>
│ │ ├── eye.svg <br>
│ │ └── eye_closed.svg <br>
├── app.py <br>
├── postcss.config.js <br>
├── README.md <br>
├── .gitignore <br>
└── tailwind.config.js <br>

##  Como iniciar o projeto

Siga os passos abaixo para rodar o projeto localmente:

### 1° Rodar o Tailwind CSS (modo watch)

Este comando irá compilar o CSS a partir do arquivo `input.css` e manter a escuta ativa para alterações:

```bash
npx tailwindcss -i ./app/assets/input.css -o ./app/static/output.css --watch
```
### 2° Iniciar a aplicação com Python
```bash
python app.py
```
> **Importante!** Certifique-se que todas depedências como flask e tailwindcss estão instaladas corretamente.
