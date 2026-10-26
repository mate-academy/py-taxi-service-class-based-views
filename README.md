<div align="center">

# 🚕 Taxi Service — Class-Based Views
### Listagens, detalhes e paginação com Django

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Study](https://img.shields.io/badge/Tipo-Projeto%20educacional-475569?style=for-the-badge)

</div>

## 🎯 Sobre o projeto

Etapa de prática de **class-based views** em Django para consultar carros, motoristas e fabricantes em interfaces HTML.

**Código relevante:** branch [`feature/class-based-views-taxi`](https://github.com/WalterMatheusgg/py-taxi-service-class-based-views/tree/feature/class-based-views-taxi). Desenvolvido como parte de exercícios práticos com Django; não representa um sistema comercial de transporte.

## ✨ Funcionalidades e estrutura

| Área | Recurso presente na implementação |
|:--|:--|
| **Listagem** | Views baseadas em classes para exibição das entidades. |
| **Detalhes** | Páginas específicas de carros e motoristas. |
| **Paginação** | Template compartilhado e navegação por páginas. |
| **Templates** | Telas separadas por entidade. |

## 🏗️ Arquitetura

```mermaid
flowchart LR
A["Navegador"] --> B["Django URLs + Views"]
B --> C["Models e regras"]
C --> D[("SQLite")]
B --> E["Templates HTML"]
```

Organização principal da aplicação:

```text
taxi/             # Models, views, admin e rotas
taxi_service/     # Configuração Django
templates/        # Páginas HTML (quando aplicável)
manage.py         # Comandos do Django
```

## 🚀 Executar localmente

Use um ambiente Python isolado, com versão compatível com as dependências do projeto.

```bash
git clone -b feature/class-based-views-taxi https://github.com/WalterMatheusgg/py-taxi-service-class-based-views.git
cd py-taxi-service-class-based-views
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py check
python manage.py runserver
```

Acesse **http://127.0.0.1:8000/**.

Para testar funcionalidades existentes:

```bash
python manage.py test
```

**Observação:** não executei o projeto ou a suíte nesta revisão. Em algumas etapas, os testes são fornecidos como parte do enunciado do curso e podem exigir configuração adicional.

## 🔒 Limites e cuidados

A branch secundária inclui views e templates adicionais que não aparecem integralmente na `master` atual.

Use somente dados de teste. Não reutilize senhas presentes em fixtures, mantenha `DEBUG` desabilitado em servidores públicos e revise dependências antes de qualquer implantação externa.

## 👨‍💻 Repositório

**Walter Matheus Soares da Silva** · [GitHub](https://github.com/WalterMatheusgg)

Outros projetos do portfólio: [NEXUS CRM](https://github.com/WalterMatheusgg/NEXUS) · [Biblioteca Digital](https://github.com/WalterMatheusgg/library-service/tree/develop)
