# Build stage
FROM eclipse-temurin:17-jdk-focal AS builder

WORKDIR /app

# Copy taskmanager folder contents
COPY taskmanager/mvnw .
COPY taskmanager/.mvn .mvn
COPY taskmanager/pom.xml .
COPY taskmanager/src src

# Make mvnw executable and build
RUN chmod +x mvnw
RUN ./mvnw clean package -DskipTests

# Runtime stage
FROM eclipse-temurin:17-jre-focal

WORKDIR /app

# Copy the built jar from builder stage
COPY --from=builder /app/target/*.jar app.jar

# Expose port
EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-jar", "app.jar"]
