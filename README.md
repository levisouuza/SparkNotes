# Spark Notes

## Over View

* Framework para processamento de big data construído com foco em velocidade, facilidade de uso e análises sofisticadas. 
* Permite que aplicações em clusters Hadoop executem até 100x mais rápido em memória e até 10x mais rápido em disco.
* MapReduce é um ótima solução para cáculos em um único processamento, porém não muito eficiente para casos de uso que requerem cálculos e algoritmos com várias execuções. Isso por que cada etapa no fluxo de processamento tem apenas uma fase Map e uma Reduce, e desse modo é necessário converter qualquer caso de uso para o padrão MapReduce. 
* Os dados de saída do processamento de cada etapa devem ser armazenados no sistema de arquivo distribuído antes do passo seguinte começar. Assim, esta abordagem tende a ser lenta devido à replicação e armazenamento em disco. Além disso, as soluções Hadoop incluem tipicamente clusters que são difíceis de configurar e gerenciar.
* Caso seja necessário fazer algo complexo, seria preciso encadear uma série de jobs de MapReduce e executá-los em sequência. Cada um desses jobs terão alta latência e não poderá começar até que o anterior tenha terminado.
* O Spark permite que sejam desenvolvidos pipelines compostos por várias etapas complexas usando grafos direcionais acíclicos (DAG). Além disso, suporta o compartilhamento de dados da memória através desses grafos, de modo que os diferentes jobs possam trabalhar com os mesmos dados.

## CARACTERÍSTICAS DO SPARK

* O Spark funciona tanto na memória como em disco e, por isso, o Spark executa operações em disco quando os dados não cabem mais na memória. Assim, é possível usá-lo para o processamento de conjuntos de dados maiores que a memória agregada em um cluster. Ele armazenará a maior quantidade possível de dados na memória e, em seguida, irá persisti-los em disco.

## ECOSSISTEMA SPARK

- Spark Streaming
- Spark SQL
- Spark MLlib
- Spark GraphX

## ARQUITETURA SPARK

- Padrão Main/Worker

- O Main node possui driver program e, aqui, o Spark Context é utilizado como ponto de entrada na aplicação, ou seja, qualquer script Spark precisa possuir um Spark Context instanciado, similarmente como ocorre em conexões com banco de dados. Em tal aplicação, os processamentos serão enviados para o cluster Spark. 

- O cluster manager gerencia os jobs Spark submetidos via Spark Context e cada job enviado é quebrado em diferentes tasks. Essas task são distribuidas pelos workes node. 

- O worker node realiza o processamento das tasks enviadas pelo cluster e retorna o resultado para o Spark Context que submeteu o job. Com o recebimento de todas as soluções necessárias, é feito o agrupamento e agregação dos resultados, chegando ao produto final em questão. 

- Sendo assim, tem-se que o Apache Spark é baseado em duas principais abstrações: Resilient Distributed Dataset e Direct Acyclic Graph


### RDD - CONJUNTO DE DADOS RESILIENTES E DISTRIBUIDOS

- Resiliente, por ser tolerante a falhas e capaz de reconstruir os dados caso essas falhas acontençam;
- Distributed, pelo fato de estar dividida entre os diversos nós existentes no cluster;
- Dataset, por ser caracterizado como um conjunto de dados.

- Imagine o RDD como uma tabela de um banco de dados que pode guardar qualquer tipo de dado. O Spark armazena o RDD em diferentes partições, isso ajuda a reorganização computacional e a otimização no processamento dos dados.

- Os RDDs são imutáveis. Ainda que aparentemente seja possível modificar um RDD com uma transformação, na verdade o resultado é um novo RDD, sendo que o original permancece intocável. 

- O RDD suporta dois tipos de operações:
    * **TRANSFORMAÇÃO:** Não retornam um único valor, mas um novo RDD. Nada é avaliado quando a função de transformação é chamada, ela apenas recebe um RDD e retorna um novo RDD. 
    
    EX FUNÇÕES DE TRANSFORMAÇÃO: map, filter, flatMap, groupByKey, reduceByKey, aggregateByKey, pipe e coalesce. 

    * **ACAO:** Esta operação avalia e retorna um novo valor. Quando uma função de ação é chamado em um objeto RDD, todas as consultas de processamentos de dados são computadas e o valor é retornado. 
    
    EX FUNCOES DE ACAO: reduce, collect, count, firts, take, countByKey e foreach.

- Todas essas operações seguem a técnica de otimização lazy evaluation, significando que somente quando uma ação for submetida é que as transformações enviadas anteriormente são executadas.


### DAG - DIRECTED ACYCLIC GRAPH

- É uma transformação direta de dados, partindo do estado A para o estado B, dividida em diferentes estágios. Essas ações são realizadas de forma acíclica, impedindo que as transformações finalizadas retornem ao estágio anterior. Resultando em ganho de performance, a abstração de DAG's permite que o Spark utilize cada nó como uma partição de transformação de dados.


## CLUSTER MANAGEMENT 

- O gerenciamento do cluster de Spark é um serviço externo responsável por adquirir recursos presentes no cluster e alocar os jobs submetidos em cada um dos recursos. Esse gerenciamento pode ser:

    * **Standalone ->** O Spark gerencia seu próprio cluster, com cada aplicação sendo executada nos nós presentes. 

    * **Apache Mesos ->** Forma de gerenciamento externa com o cluster dedicado para gerenciamento de recurso que, de acordo com a necessidade, é capaz de aumentar e diminuir a quantidade de recursos providos para cada SparkContext.

    * **Hadoop Yarn ->** É permitido ao usuário alocar a quantidade de recursos que será necessária para a execução de seus jobs, além de possuir a funcionalidade de restrição de acesso ao cluster. 

- **Spark Application:** Consiste em um driver que compõem a Spark Session e o código do usuário, um conjunto de executores.

- **JVM:** Programa que gerencia a memória do sistema e prove um ambiente de execução portátil para aplicações baseadas em java.
    
    * **Definição Técnica ->** É uma especificação para um software que executa código e prover o ambiente de execução desse código. 

    * **Definição Diária ->** É como executamos um programa Java. Configuramos a JVM e automaticamente, começar a gerenciar os recursos do programa durante a execução.

    * Tem a função de permitir a execução de programas java em qualquer dispositivo/sistema operecional ("Escreva uma vez, rode em qualquer lugar") e gerenciar e otimizar a memória do programa. 


### DRIVER

- Orquestra e monitora a execução de uma aplicação Spark. Sempre existirá um driver para um Spark Application. Pode ser comparável a um envelope que encapsula a aplicação. 

- O driver roda a função main(), o coloca em um node no cluster e é responsável por:
    
    * Manter informação sobre a aplicação Spark
    * Responder ao programa do usuário
    * Requisitar memória ou recursos de CPU para os cluster managers.
    * Separar a lógica da aplicação em stages e tasks.
    * Enviar as tasks aos executores.
    * Coletar os resultados dos executores. 

* Driver = JVM que a aplicação Spark executa.


### EXECUTOR 

- Responsável por executar o trabalho que o driver envia para ele. 
    
    * Executa código dado pelo driver
    * Reporta o estado do processamento para o driver. 

### CORE | SLOTS | THREADS

- Core é a unidade de processamento separada capaz de lidar com tarefas independentes.

- Qtd de Cores = Qtd de Slots = Qtd de tarefas que o executor pode realizar naquele node (máquina) em paralelo.

- Ao criar Tasks, o driver tem que gerar unidades de trabalho para os slots de cada Executor para realizar o paralelismo. 

- O driver tem a responsabilidade de particionar o dado para o paralelismo. Essa ação, gera uma lógica que para cada tarefa criada seja atribuída uma partição do dado. 

## CONCEITOS ESSENCIAIS

- **NARROW TRANSFORMATION:** Transformações em que uma partição de um entrada pode ser processada e gerar dados em um partição de saída 
sem a necessidade de acessar e combinar dados de outras partições. Exemplo: Funções: filter() e contains().

- **SHUFFLE:** Mecanismo que redistribui os dados através de diferentes executores e até por máquinas. Acontece quando são chamadas operações como groupByKey(), reduceByKey().Join().Union(), groupBy, etc.

    É uma operação altamente onerora ao ambiente pois, sua escrita ocorre em disco, realiza serialização e desserilização de dados e alto tráfego de rede.

- **WIDE TRANSFORMATION:** Transformações que os dados de entrada da partição irão contribuir para a saída de outras partições. Normalmente você verá essa transformação sendo referenciada como shuffle. Operações como groupBy() e OrderBy() são transformações desse tipo, uma vez que as partições lidas, combinadas e escritas em disco. 

