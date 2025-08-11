# Personal Portfolio - Django

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-v4.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

Um portfólio pessoal desenvolvido em Django para demonstrar habilidades técnicas e projetos desenvolvidos.

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Configuração](#configuração)
- [Como Executar](#como-executar)
- [Páginas e Rotas](#páginas-e-rotas)
- [Customização](#customização)
- [Deploy](#deploy)
- [Contribuição](#contribuição)
- [Licença](#licença)

## 🎯 Visão Geral

Este projeto é um portfólio pessoal desenvolvido com Django, criado para demonstrar competências em desenvolvimento web com Python. O site apresenta uma interface limpa e responsiva, showcaseando projetos, habilidades técnicas e informações profissionais.

### Objetivos do Projeto
- Demonstrar conhecimentos em Django framework
- Implementar sistema de templates e arquivos estáticos
- Criar uma aplicação web responsiva e profissional
- Praticar estruturação de projetos Django

## ✨ Funcionalidades

- **Página Inicial**: Apresentação pessoal com call-to-action
- **Sobre**: Informações profissionais, experiência e habilidades
- **Projetos**: Showcase de projetos desenvolvidos com detalhes técnicos
- **Contato**: Formulário de contato e informações para networking
- **Design Responsivo**: Interface adaptável para dispositivos móveis
- **Sistema de Navegação**: Menu intuitivo entre seções

## 🚀 Tecnologias Utilizadas

### Backend
- **Python 3.8+**
- **Django 4.0+**

### Frontend
- **HTML5**
- **CSS3** (Flexbox/Grid)
- **JavaScript** (vanilla)

### Ferramentas
- **Git** - Controle de versão
- **VS Code** - Editor de código
- **WhiteNoise** - Servir arquivos estáticos em produção

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git
- Virtualenv (recomendado)

```bash
python --version
pip --version
git --version
```

## ⚙️ Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/portfolio-django.git
cd portfolio-django
```

### 2. Crie um ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute as migrações
```bash
python manage.py migrate
```

### 5. Colete os arquivos estáticos (produção)
```bash
python manage.py collectstatic
```

## 📁 Estrutura do Projeto

```
portfolio_project/
│
├── portfolio_project/          # Configurações principais
│   ├── __init__.py
│   ├── settings.py            # Configurações do Django
│   ├── urls.py               # URLs principais
│   ├── wsgi.py
│   └── asgi.py
│
├── portfolio/                 # App principal
│   ├── migrations/
│   ├── static/               # Arquivos estáticos
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   │       ├── profile.jpg
│   │       └── projects/
│   ├── templates/            # Templates HTML
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── projects.html
│   │   └── contact.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── staticfiles/              # Arquivos estáticos coletados
├── media/                    # Arquivos de mídia (futuro)
├── .gitignore
├── requirements.txt
├── README.md
└── manage.py
```

## 🔧 Configuração

### Settings.py - Principais Configurações

```python
# Debug Mode (Development vs Production)
DEBUG = False  # Mude para True apenas em desenvolvimento local

# Hosts permitidos
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'seu-dominio.com']

# Arquivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'portfolio/static'),
]
```

### Requirements.txt
```txt
Django==4.2.0
whitenoise==6.0.0
```

## 🚀 Como Executar

### Desenvolvimento Local
```bash
# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Executar servidor de desenvolvimento
python manage.py runserver

# Acessar no navegador
http://127.0.0.1:8000/
```

### Produção
```bash
# Definir variáveis de ambiente
export DEBUG=False
export ALLOWED_HOSTS=seu-dominio.com

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Executar com servidor WSGI
python manage.py runserver
```

## 🌐 Páginas e Rotas

| Página | URL | Descrição |
|--------|-----|-----------|
| Home | `/` | Página inicial com apresentação |
| Sobre | `/sobre/` | Informações profissionais e habilidades |
| Projetos | `/projetos/` | Portfolio de projetos desenvolvidos |
| Contato | `/contato/` | Informações de contato e networking |

### URLs Configuration
```python
# portfolio/urls.py
urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.about, name='about'),
    path('projetos/', views.projects, name='projects'),
    path('contato/', views.contact, name='contact'),
]
```

## 🎨 Customização

### Modificar Informações Pessoais
1. Edite os dados nos views em `portfolio/views.py`
2. Atualize as imagens em `portfolio/static/images/`
3. Personalize o CSS em `portfolio/static/css/style.css`

### Adicionar Novos Projetos
```python
# Em views.py
def projects(request):
    projects_data = [
        {
            'title': 'Novo Projeto',
            'description': 'Descrição do projeto',
            'technologies': ['Python', 'Django'],
            'github_url': 'https://github.com/usuario/projeto',
            'demo_url': 'https://projeto-demo.com',
            'image': 'projects/projeto.jpg'
        },
        # ... outros projetos
    ]
    return render(request, 'projects.html', {'projects': projects_data})
```

## 🌍 Deploy

### Preparação para Deploy
1. Configure `DEBUG = False` em production
2. Defina `ALLOWED_HOSTS` adequadamente
3. Execute `python manage.py collectstatic`
4. Configure servidor web (Nginx/Apache)
5. Use WSGI server (Gunicorn/uWSGI)

### Variáveis de Ambiente Recomendadas
```bash
export SECRET_KEY='sua-secret-key-aqui'
export DEBUG=False
export ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

### Padrões de Código
- Siga PEP 8 para Python
- Use nomes descritivos para variáveis e funções
- Comente código complexo
- Escreva docstrings para funções importantes

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

**Seu Nome**

- LinkedIn: [mamadusama](https://linkedin.com/in/mamadusama)
- Email: mamadusama19@gmail.com
- GitHub: [@mamadusamadev](https://github.com/mamadusamadev)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!

## 📚 Próximos Passos

- [ ] Implementar sistema de administração Django
- [ ] Adicionar formulário de contato funcional
- [ ] Integrar com banco de dados para gerenciar projetos
- [ ] Implementar sistema de blog
- [ ] Adicionar testes automatizados
- [ ] Configurar CI/CD

---

*Desenvolvido com ❤️ usando Django*