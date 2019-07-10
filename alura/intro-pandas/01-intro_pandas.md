# 02 - Instalação Anaconda

O primeiro passo para iniciarmos nosso curso de Pandas é configurar o ambiente. Conheceremos a distribuição do Python, Anaconda, própria para Data Science por conter todo o conjunto de ferramentas de que precisamos para resolver problemas.

O Anaconda ainda fornece uma IDE padrão denominada Spider, não usaremos este recurso no projeto, mas sim o Jupyter, uma ferramenta mais interativa. Faremos o download da distribuição Anaconda na versão 5.1, e usaremos a versão do Python 3.6. Baixado o recurso, teremos acesso à janela padrão de instalação, em que faremos as configurações básicas.

Na etapa "Advanced Options" assinalaremos apenas a opção "Registrer Anaconda as my default Python 3.6", para que posteriormente aprendermos como criar ambientes virtuais.

Janela de diálogo que exibe duas opções a serem assinaladas: "Add Anaconda to my Path environment variable" e "Registrer Anacoda as my default Python 3.6"

Concluída a instalação, abriremos o Anaconda Navigator. Na página principal da ferramenta, conseguiremos visualizar rapidamente alguns dos recursos principais, como o Jupyter que mencionamos.

Ao lado esquerdo da tela, haverá o menu de ferramentas em que temos, por exemplo, a opção "Enviromnments" que nos permite acessar todas as bibliotecas instaladas no ambiente padrão, como o próprio Pandas e Scikit-Learn.

 menu de ferramentas. Contém as opções "home", "Environments", "Projects(beta)", "Learning" e "Community"

Fecharemos o Anaconda, e trabalharemos na configuração das variáveis de ambiente. Iremos estabelecer dois caminhos em nosso path. Primeiro, coletaremos o endereço em que salvamos a ferramenta Anaconda, no caso C:\Users\Alura\Anaconda3.

Ainda no explorer, clicaremos sobre "Este Comptador" com o botão direito e selecionaremos a opção "Propriedades". Com a janela do sistema aberta, clicaremos em "Configurações Avançadas do Sistema"



Será aberta uma nova janela de "Propriedades do Sistema". Selecionaremos "Variáveis de Ambiente".



Na área "Variáveis de usuário para Alura" , selecionarems "Path" e clicaremos sobre a opção "Editar". Em seguida, inserimos o C:\Users\Anaconda3 caminho na área "Editar a variável de ambiente". Em seguida, clicaremos sobre o botão "Novo" e adicionaremos o caminho C:\Users\Alura\Anaconda3\Scripts.



Feito isso, clicaremos sobre o botão "Ok", fecharemos as janelas anteriores e concluímos a configuração. Agora no momento em que abrimos o prompt de comando e escreveremos python, a ferramenta será executada.

Acessaremos o ambiente de Anaconda Navigator e clicaremos sobre o ícone da ferramenta Jupyter.



Seremos direcionador para a pasta padrão do Jupyter, que inclusive contem a pasta "Anaconda3", que configuramos anteriormente. Nesta área poderemos criar um notebook, a ferramenta do Jupyter que utilizaremos para criar o projeto. Clicaremos sobre "New > Notebook: Python 3".

Teremos uma área de trabalho composta por células em que digitaremos os códigos. Se escrevermos uma operação matemática simples como 1 + 1 e pressionarmos "Shift + Enter", teremos a resposta já impressa na tela, isto é, uma saída (out). Ao escreveremos em uma célula:

```
for i in range(10):
    print(i)
```

teremos a saída:

```
1
2
3
4
5
6
7
8
9
```

O Jupyter possui diversos recursos que podemos utilizar ao longo do desenvolvimento do projeto, e ainda nos permite acessar o comando Shell, basta escrever !dir, e as informações contidas no diretório serão exibidas na saída.

Nas próximas aulas aprenderemos a criar ambientes virtuais para manter o sistema operando.

# 03 - Ambiente virtual
Nesta aula, criaremos ambientes virtuais, mas qual é a utilidade desses ambientes? Suponhamos que você tenha escrito um código há seis meses, e nesse processo, utilizou uma série de bibliotecas e pacotes, de forma que projeto final de base dados foi complexo e extenso.

O seu chefe decide atualizar essa base de dados, e de repente todo aquele código não é mais funcional. Isso ocorre porque as bibliotecas são atualizadas, e muitas funcionalidades se modificam ou deixam de existir.

Quando criamos um ambiente virtual, a manutenção de um código é mais simples: podemos inserir a versão da biblioteca que queremos utilizar, e assim o código será executado no ambiente da mesma maneira que antes da atualização.

No Anaconda Navigator, no menu principal, se clicarmos sobre "Environments" poderemos irar um novo ambiente virtual. Contudo, por essa via teremos um ambiente mais engessado, com menos recursos de gostaríamos. Desse modo, agora entenderemos a utilidade da configuração de variáveis que realizamos anteriormente.

Primeiramente, abriremos o prompt. No Python temos o gerenciador de pacotes padrãopip, o Anaconda possui um gerenciador próprio chamado conda, e ele que usaremos para criar o ambiente virtual.

Especificaremos a versão do Python utilizada, bem como a do Pandas, embora neste caso isso não seja necessário, pois essas são as versões instaladas na máquina. O comando que utilizaremos é este:

```
conda create --name alura_pandas python=3.6 pandas=0.22.0
```

Será exibido os pacotes a serem instalados, e caso utilizemos uma versão ultrapassada, atualizações serão realizadas. Pressionaremos a tecla "Y" para finalizarmos o processo.

Voltaremos Anaconda Navigator, na área "Enviroments". Verificaremos que alura_pandas já está disponível:

`ambientes "base(root)" e "alura_pandas" disponíveis`

Ao clicarmos sobre ele, poderemos conhecer todos os elementos instalados, inclusive o Pandas. Clicaremos em "Home" no menu principal, e de volta ao espaço principal do Anaconda Navigator, selecionaremos alura_pandas no boc "Applications on".


Precisamos instalar o Jupyter. Para isso, basta clicar sobre o botão "Install", logo abaixo do ícone da ferramenta, ainda na página home do Anaconda.



Quando a instalação for finalizada, clicaremos sobre o botão "Launch". Em seguida, clicaremos sobre "New > Pythons 2". Poderemos começar a construir nosso código com o channel Python 2. Antes, acessaremos o prompt e faremos algumas configurações adicionais e aprenderemos mais sobre conda e ambientes virtuais.

Para ativarmos um ambiente fora da via Anaconda, precisamos utilizar o comando activate e passar o nome do ambiente alura_pandas

```
activate alura_pandas
```

Assim feito, já teremos acessado alura_pandas, que aparecerá entre parênteses. Em seguida, escreveremos python para iniciá-lo.

```
(alura_pandas) C:Users\Alura>python
```

Teremos acesso a versão do Python utilizada. Em seguida, faremos a importação do Pandas:

```
import pandas
```

Para acessarmos a versão utilizada escreveremos o comando:

```
pandas.__version__
```

Para sairmos do ambiente virtual alura_pandas, utilizamos o comando:

```
deactivate
```

Dessa forma, retornamos para a versão base:

```
C:\Users\Alura>
```

Para visualizar os ambientes disponíveis escreveremos os comandos:

```
conda info -- envs
```

Atualmente, possuímos o ambiente alura_pandas e a versão base:

```
# conda environments:
#
base             * C:\Users\Alura\Anaconda3
alura_pandas       C:\Users\Alura\envs\alura_pandas
```

Para excluirmos os ambientes criados, utilizamos o comando remove --name, o nome do ambiente a ser deletado, por fim `--all`:

```
remove --name alura_pandas --all 
```

Dessa forma, o ambiente terá sido removido e não pode mais ser acessado via Anaconda.Temos todo o ferramental básico para iniciar o curso, agora podemos começar a codificar em Pandas.
