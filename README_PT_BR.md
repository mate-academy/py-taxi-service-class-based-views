# Taxi service class-based views

- Leia [o guia](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) antes de começar
- Use o seguinte comando para carregar os dados preparados da fixture para testar e depurar seu código:

```python manage.py loaddata taxi_service_db_data.json```

- Após carregar os dados da fixture, você pode usar o seguinte superusuário (ou criar outro por conta própria):
  - Login: `admin.user`
  - Senha: `1qazcde3`
- Certifique-se de alterar as configurações para os [arquivos html](https://github.com/mate-academy/py-task-guideline/blob/main/html_settings/README.MD).
Use 2 espaços de indentação nos arquivos `.html`.

Sinta-se à vontade para adicionar mais dados usando o painel de administração, se necessário.

Nesta tarefa, você deve implementar as views de lista e detalhe baseadas em classe.

1. Crie a view de lista `ManufacturerListView`.
    - Defina o model no qual a list view é baseada.
    - Defina o queryset, selecionando todos os fabricantes, que devem ser ordenados por nome por padrão.
    - Defina a paginação igual a 5. Isso indica quantas instâncias devem ser exibidas em uma única página.

2. Crie a view de lista `CarListView`.
    - Defina o model, paginação igual a 5, e o queryset.
    - **Observação**: o model Car possui uma chave estrangeira `manufacturer`, portanto não se esqueça de melhorar a performance da consulta _(problema N+1)_.

3. Crie a view de detalhe `CarDetailView`.
    - Defina apenas o model.
    
4. Crie a view de lista `DriverListView`.
    - Defina o model e a paginação igual a 5.

5. Crie a view de detalhe `DriverDetailView`.
    - Defina o model e o queryset.
    - Nesta view, você exibe informações sobre os carros do motorista.
      **Otimize a consulta**: não faça uma consulta ao fabricante para cada carro _(problema N+1)_.

6. Dentro de `taxi/urls.py`:
   - Crie os seguintes paths:
     - em `manufacturers/` você deve obter a view de lista de fabricantes;
     -  `cars/` - view de lista de carros;
     -  `cars/pk/` - view de detalhe de carro;
     -  `drivers/` - view de lista de motoristas;      
     -  `drivers/pk/` - view de detalhe de motorista.

7. Crie os templates para as views. 
   - Por padrão, as class-based views tentam encontrar um template baseado no nome do model e em um determinado sufixo: 
     1. Para list view - `_list`
     2. Para detail view - `_detail`
   - Crie templates para a lista de fabricantes, lista de carros e lista de motoristas. Nesses templates:
       - Crie uma tabela com as informações de cada instância.
         1. Na lista de carros, defina um link no campo id que leve à página de detalhe do carro.
         2. Na lista de motoristas, defina um link no campo username que leve à página de detalhe do motorista.
   - Crie o template de detalhe do motorista:
       - inclua informações sobre todos os carros do motorista.
   - Crie o template de detalhe do carro:
       - inclua informações sobre o fabricante do carro (nome, país);
       - inclua informações sobre todos os motoristas daquele carro.
   - Dentro de `templates/includes`:
       - crie o `pagination.html` para fins de paginação e inclua esse template dentro do `base.html`;
       - no `sidebar.html`, adicione links para a página inicial, página de lista de fabricantes, página de lista de carros e página de lista de motoristas.
   - Verifique se você colocou linhas vazias no final de cada arquivo html.
    
8. Rode o servidor, abra `http://127.0.0.1:8000/` e verifique se tudo está sendo exibido corretamente.
9. Verifique se você colocou linhas vazias no final de cada arquivo HTML.
10. Verifique o estilo do seu código com `flake8`.
11. Rode `python manage.py test` para verificar os resultados do seu código.

### Observação: Anexe capturas de tela de todas as páginas criadas ou modificadas ao pull request. 
seria melhor anexar as capturas de tela no comentário, e NÃO no commit. 
É importante **anexar as imagens**, não links para elas. Veja o exemplo:

![image](https://mate-academy-images.s3.eu-central-1.amazonaws.com/python_pr_with_images.png)
```