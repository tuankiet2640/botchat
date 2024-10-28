# Build the application
FROM maven:3.8.5-openjdk-17 AS build

WORKDIR /app

COPY pom.xml .
RUN mvn dependency:go-offline

COPY src/ ./src
RUN mvn clean package -DskipTests

COPY ./botchat /app

# Run the application
FROM openjdk:17-jdk-slim

WORKDIR /app

COPY --from=build /app/target/config-server.jar config-server.jar

EXPOSE 8888

ENTRYPOINT ["java", "-jar", "config-server.jar"]
