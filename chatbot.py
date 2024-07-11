import discord
from discord.ext import commands

# Substitua pelo novo token do seu bot
TOKEN = 'digite seu token aqui'

# Configurar intents para permitir acesso ao conteúdo da mensagem
intents = discord.Intents.default()
intents.message_content = True

# Criar uma instância do bot com os intents configurados
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado com {bot.user}')
    print('------')


# Comando de saudação
@bot.command(name='Oi')
async def Oi(ctx):
    await ctx.send('Olá, tudo bem? Seja bem vindo(a) à nossa uma loja virtual SuaLinda, eu sou sua atendente virtual BotLinda. Para ter acesso a informações de nossos produtos, digite "!ajuda". Como posso te ajudar hoje?')

# Comando para roupas
@bot.command(name='roupas')
async def roupas(ctx, categoria: str):
    if categoria.lower() == 'feminino':
        await ctx.send('Temos uma variedade de roupas femininas: Que tipo de roupa você está procurando? Escolha um !modelo: blusas, saias, vestidos, babydool, calças, peças intimas.')
    elif categoria.lower() == 'masculino':
        await ctx.send('Temos uma variedade de roupas masculinas! Que tipo de roupa você está procurando?  Escolha um !modelo: calças, shorts, camisas e cuecas.')
    elif categoria.lower() == 'infantil':
        await ctx.send('Temos uma variedade de roupas infantis. Você está procurando: Digite se é para !roupas para menina ou de menino.')
    elif categoria.lower() == 'menino':
        await ctx.send('Temos uma variedade de roupas para meninos! Que tipo de roupa você está procurando? Escolha um !modelo: calças, shorts, camisas e cuecas.')
    elif categoria.lower() == 'menina':
        await ctx.send('Temos uma variedade de roupas para meninas! Que tipo de roupa você está procurando?  Escolha um !modelo: blusas, saias, vestidos, babydool, calças, peças intimas.')
    else:
        await ctx.send('Por favor, escolha uma !categoria: feminino, masculino ou infantil.')

# Comando para modelos de roupas
@bot.command(name='modelo')
async def modelo(ctx, categoria: str):
    if categoria.lower() == 'blusas':
        await ctx.send('Temos uma variedade de modelos disponíveis! Qual !tamanho você está procurando: P, M, G ou GG.')
    elif categoria.lower() == 'saias':
        await ctx.send('Temos uma variedade de modelos disponíveis! Qual !tamanho você está procurando? Digite a opção: P, M, G ou GG.')
    elif categoria.lower() == 'vestidos':
        await ctx.send('Temos uma variedade de modelos disponíveis! Qual !tamanho você está procurando? Digite a opção: P, M, G ou GG.')
    elif categoria.lower() == 'babydool':
        await ctx.send('Temos uma variedade de modelos disponíveis! Qual !tamanho você está procurando? Digite a opção: P, M, G ou GG.')
    elif categoria.lower() == 'intimas':
        await ctx.send('Temos uma variedade de modelos disponíveis! Qual !tamanho você está procurando? Digite a opção: P, M, G, GG ou XG.')
    elif categoria.lower() == 'calças':
        await ctx.send('Temos uma variedade de modelos disponíveis! Qual !tamanho você está procurando? Digite a opção: P, M, G ou GG.')
    elif categoria.lower() == 'shorts':
        await ctx.send('Temos uma variedade de modelos disponíveis! Qual !tamanho você está procurando? Digite a opção: P, M, G ou GG.')
    elif categoria.lower() == 'camisas':
        await ctx.send('Temos uma variedade de modelos disponíveis! Qual !tamanho você está procurando? Digite a opção: P, M, G ou GG.')
    elif categoria.lower() == 'cuecas':
        await ctx.send('Temos uma variedade de modelos disponíveis! Qual !tamanho você está procurando? Digite a opção: P, M, G, GG ou XG.')
    else:
        await ctx.send('Não entendi, por favor, escolha um dos !modelos: blusas, saias, vestidos, babydool, intimas, calças, shorts, camisas ou cuecas.')

# Comando para os tamanhos
@bot.command(name='tamanho')
async def tamanho(ctx, tamanho: str):
    if tamanho.upper() in ['P', 'M', 'G', 'GG', 'XG']:
        await ctx.send('Muito obrigada por interagir comigo, agora aguarde um momento, que nossa atendente vai lhe repassar os modelos disponíveis!')
    else:
        await ctx.send('Não entendi, por favor, digite um dos !tamanhos: P, M, G, GG ou XG.')

#Comando para reclamações ou  sujestões
@bot.command(name='comentarios')
async def comentarios(ctx):
    await ctx.send('Deixe aqui seu comentário sobre nosso atendimento e produtos, gostaríamos de saber a satisfação de nossos clientes')

# Comando para obter ajuda
@bot.command(name='ajuda')
async def ajuda(ctx):
    help_text = (
        "Aqui estão os comandos que você pode usar:\n"
        "!Oi - Receba uma saudação do bot\n"
        "!roupas [categoria] - Pergunte sobre roupas (Digite: !roupas seguido de feminino, masculino, infantil, menino ou menina)\n"
        "!modelo [categoria] - Pergunte sobre modelos de roupas (Digite: !modelos seguido de, blusas, saias, vestidos, babydool, intimas, calças, shorts, camisas ou cuecas)\n"
        "!tamanho [categoria] - Pergunte sobre os tamanhos das roupas (Digite:  !tamanhos seguido de: P, M, G, GG e XG)\n"
        "!comentarios - Para fazer sujestões de atendimento ou reclamação \n"
    )
    await ctx.send(help_text)

# Comando padrão para qualquer outra mensagem
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith(bot.command_prefix):
        await bot.process_commands(message)
    else:
        await message.channel.send("Desculpe, não entendi o que você quis dizer. Digite !ajuda para ver a lista de comandos disponíveis.")

bot.run(TOKEN)

