## Spark Install EC2

### Step by Step

1. sudo apt install -y default-jre

2. wget https://archive.apache.org/dist/spark/spark-3.0.0/spark-3.0.0-bin-hadoop2.7.tgz

3. sudo tar -zxvf spark-3.0.0-bin-hadoop2.7.tgz

4. /opt/spark-3.0.0-bin-hadoop2.7

5. vim /etc/profile

   export SPARK_HOME=/opt/spark-3.0.0-bin-hadoop2.7
   
   export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

**Para testar, executar:**

**Node master:** start-master.sh 

**Node Slave:** start-slave.sh host_spark_aplication 
