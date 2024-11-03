FROM eclipse-temurin:17-jre-alpine
VOLUME /tmp
# Install curl for healthcheck
RUN apk add --no-cache curl
COPY target/config-server*.jar app.jar
EXPOSE 8888
ENTRYPOINT ["java", "-jar", "/app.jar"]
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:8888/actuator/health || exit 1