# 02 - Importando a base

Nas últimas aulas, instalamos o Anaconda, preparamos o ambiente de trabalho e conhecemos a ferramenta Jupyter. Está tudo pronto para de fato iniaciarmos o projeto.

Primeiramente, acessaremos a página oficial do Pandas. Clicaremos sobre a opção "Documentation", para consultamos sua documentação. Você encontrará informações úteis que inclusive podem ser baixadas em formato PDF. Mais adiante aprenderemos como acessar essa documentação via Jupyter.

De volta ao Anaconda Navigator, clicaremos no botão "Lauch" da ferramenta Jupyter e criaremos algumas pastas para nosso projeto. No ícone "New" selecionaremos a opção "Folder".

Na lista de documentos,terá sido criada uma pasta "Untitle Folder". Selecionaremos essa pasta e em seguida clicaremos sobre a opção "Rename" no topo da página

Renomearemos a pasta para "Projetos Python". Acessaremos a nova pasta criada, e dentro dela criaremos mais uma. Para isso seguiremos o mesmo percurso: "New > Folder" e o renomearemos para "Curso Pandas". Dentro dessa pasta criaremos mais uma, chamada "dados". Temos então a seguinte hierarquia de pastas: "Projetos Python > Curso Pandas > Dados".

Em "Dados" criaremos o primeiro notebook. Acionaremos "New > Python 3". Seremos direcionados para a área de codificação, e na parte superior da tela veremos o título do notebook como "Untitle", o alteraremos para "Base de Dados".

Fomos contratados por uma seguradora que nos forneceu uma base de dados para executarmos um trabalho de inteligência. A base contém milhares de imóveis disponíveis para locação no Rio de Janeiro. Precisamos realizar a importação dos dados para utilizá-los no Pandas. Para que você avance no curso, é necessário realizar o download do arquivo CSV disponibilizado.

Dentro da pasta "dados", clicaremos sobre a opção "Upload" e carregaremos o arquivo aluguel.csv. Assim feito, voltaremos para o notebook "Base de dados".

Para iniciar um projeto em Python, precisamos importar os pacotes a serem utilizados. Neste caso, importaremos o Pandas. Na primeira célula do notebook, bastaria escrever import pandas. Contudo, a comunidade de usuários usa um apelido mais sucinto: as pd. Todas as vezes que precisarmos evocar o Pandas usaremos essa terminologia.

import pandas as pd
Iremos refletir sobre como ler os dados do arquivo CSV no Pandas. Existe um método Pandas chamado read_csv(), e para este método passaremos o caminho do arquivo que gostaríamos de ler. No caso, será dados/aluguel.csv.

pd.read_csv('dados/aluguel.csv')
Ao pressionarmos "Shift + Enter", teremos como primeiros resultados:

Tipo;Bairro;Quartos;Vagas;Suítes;Area;Valor;Condominio;IPTU
0 Quitinete;Copacabada;1;0;0;40;1700;500;60
1 Casa;Jardim Botânico;2;0;1;100;7000;;
2 Conjunto Comercial/Sala;Barra da Tijuca;0;4;0...
3 Apartamento;Centro;1;0;0;15;800;390;20
Perceba que os separadores do arquivo não foram entendidos, logo, as informações na tabela aparecem aglutinadas em uma única coluna.

A ferramenta Jupyter possui um recurso muito útil: se posicionarmos o cursor dentro dos parênteses de uma função ou método e pressionarmos a tecla "Shift + Tab", será exibido todos os parâmetros necessários, e em alguns casos, exemplos de uso.

No caso de read_csv(), notaremos a necessidade do argumento sep com default ,. Nosso arquivo utiliza como separador o caractere;. Portanto faremos a seguinte adaptação no código:

``` 
pd.read_csv('dados/aluguel.csv', sep=';')
```

Teremos como saída o documento na formatação correta:

```
Tipo	Bairro	Quartos	Vagas	Suítes	Área	Valor	Condomínio	IPTU
0	Quitinete	Copacabana	1	0	0	40	1700.0	500.0	60.0
1	Casa	Jardim Botânico	2	0	1	100	7000.0	NaN	NaN
2	Conjunto Comercial/Sala	Barra da Tijuca	0	4	0	150	5200.0	4020.0	1111.0
3	Apartamento	Centro	1	0	0	48	800.0	390.0	20.0
```

Apesar de estar na formatação correta, trata-se apenas de uma visualização. Os conteúdos ainda não podem ser utilizados para o desenvolvimento do projeto. Precisamos incluir a visualização dos dados dentro de uma variável, que chamaremos de dados. Em seguida, evocaremos novamente o método read_csv() seguido do endereço do arquivo.

```
dados = pd.read_csv('dados/aluguel.csv', sep=';')
```

No Jupyter, basta escrever o nome da variável e pressionar "Shift + Enter" para acessar seu conteúdo. Agora, o conjunto de dados pode ser utilizado em outras células do notebook.

Verificaremos qual é o tipo(type) da variável dados.

```
type(dados)
```

Teremos como saída:

```
pandas.core.frame.DataFrame
```

Trata-se de um objeto do tipo DataFrame. Se utilizarmos um método de DataFrame chamado info(), poderemos adquirir ainda mais informações:

```
dados.info()
```

Como saída teremos:

```
<Class 'pandas.core.frame.DataFrame'> RangeIndex: 32960 entries, 0 to 32959 Data columns (total 9 columns): Tipo 32960 non-null object Bairro 32960 non-null object Quartos 32960 non-null int64 Vagas 32960 non-null int64 Suites 32960 non-null int64 Area 32960 non-null int64 Valor 32943 non-null float64 Condominio 28867 non-null float64 IPTU 22723 non-null float64 dtypes: float64(4), int64(4), object(2) memory usage: 2.3 +MB
```

Sabemos o número de colunas, os tipos de variável, a quantidade de registros que não são nulos e a memória usada.

O objeto DataFrame é semelhante estrutura do Pandas, que por sua vez nos lembra uma planilha do Excel: contém colunas, linhas e algumas funcionalidades. Essa será uma estrutura que utilizaremos durante todo o curso.

Neste projeto precisamos gerar relatórios, isto é, mostrar os dados para a empresa que nos contratou. Precisamos gerar uma visualização agradável para consulta e um pouco mais sucinta. Para tanto, usaremos o método head(), e serão exibidos apenas os cinco primeiros elementos da lista.

dados.head()
Tipo	Bairro	Quartos	Vagas	Suítes	Área	Valor	Condomínio	IPTU
0	Quitinete	Copacabana	1	0	0	40	1700.0	500.0	60.0
1	Casa	Jardim Botânico	2	0	1	100	7000.0	NaN	NaN
2	Conjunto Comercial/Sala	Barra da Tijuca	0	4	0	150	5200.0	4020.0	1111.0
3	Apartamento	Centro	1	0	0	15	800.0	390.0	20.0
4	Apartamento	Higienópolis	1	0	0	48	800.0	230.0	NaN
Podemos ampliar o valor de linhas exibidas especificando a quantidade do parâmetro do método, por exemplo head(10), e serão exibidas as 10 primeiras linhas da tabela.

Precisamos, ainda, documentar o relatório para evitar futuras confusões. Para criarmos uma célula logo acima da primeira gerada no projeto, acionamos o atalho "A". Para adicionar uma célula manualmente, basta acessar no menu de ferramentas as opções "Insert > Insert Cell Above".

Nesta nova célula escreveremos o título da seguinte maneira:

# Relatório de Análise I 
No menu de ferramentas podemos, inclusive mudar o tipo das células. As células que criamos até então são do tipo code. Mudaremos a célula de título para "Markdown".



Feita a alteração, pressionaremos a tecla "Alt + Shift",então teremos o efeito de uma <h1> no HTML.

Criaremos uma célula abaixo do título, para tanto acionaremos o atalho "Esc + B". Essa célula conterá um subtítulo, então escreveremos da seguinte maneira:

## Importando a Base de Dados
Podemos, ainda, inserir comentários nas células de código por meio do atalho "Ctrl + ;". Dessa forma podemos ir documentando nossos relatórios.


