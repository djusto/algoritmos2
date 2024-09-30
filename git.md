Para instalar, no Powershell, 
```
PS C:\users\dago> winget git.git

```

Para criar novo repositório:

* Abra o terminal de comando;
* Dentro da pasta do projeto, digite: `git init`  
* Para adicionar todos os arquivos alterados à fila de atualizações do repositório, execute o comando: `git add .`
* Antes de sincronizar as alterações, configure seu usuário do GitHub com os comandos:  
    `git config --global user.name "seu nome"`  
    `git config --global "email no GitHub"`
- Confirme as alterações com o comando: `git commit -m "mensagem"`  
    no qual “mensagem” geralmente é um resumo das alterações.
- Adicione o _remote_, ou seja, o link para o servidor do seu projeto no GitHub:  
    `git remote add origin usuário no GitHub>/<nome do repositório>.git`
- Por fim, envie as alterações com o comando:  
    `git push remote origin`
- Se tudo deu certo, será exibido uma mensagem confirmando o envio. Você também pode checar na página do repositório do projeto no GitHub.com


