$SPARK_HOME/bin/spark-submit --master local[8]     --conf spark.rapids.sql.enabled=true     --conf spark.rapids.sql.concurrentGpuTasks=1     --conf spark.task.cpus=1     --conf spark.executor.resource.gpu.amount=1     --conf spark.sql.adaptive.enabled=false     --conf spark.rapids.memory.pinnedPool.size=2G     --conf spark.plugins=com.nvidia.spark.SQLPlugin     --conf spark.executor.resource.gpu.discoveryScript=/opt/sparkRapidsPlugin/getGpusResources.sh     --conf spark.sql.session.timeZone=UTC  --conf spark.rapids.sql.explain=ALL     --conf spark.sql.legacy.timeParserPolicy=LEGACY     --conf spark.rapids.sql.exec.CollectLimitExec=true     --files /opt/sparkRapidsPlugin/getGpusResources.sh     --jars /opt/sparkRapidsPlugin/rapids-4-spark_2.12-23.02.0.jar,/home/nikola/DiplomskiRad/haversineDistance/target/haversineDistance-24.04.0-SNAPSHOT.jar     --driver-java-options "-Duser.timezone=UTC"     --conf spark.executor.extraJavaOptions="-Duser.timezone=UTC"     haversine_distance_calc.py test_input.parquet output


