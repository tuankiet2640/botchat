FROM eclipse-temurin:17-jre-alpine

COPY target/logging-service*.jar app.jar

ENTRYPOINT ["java", "-jar", "/app.jar"]