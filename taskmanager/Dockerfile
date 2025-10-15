# Build stage
FROM eclipse-temurin:17-jdk-focal AS builder

WORKDIR /app

# Copy Maven files
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .

# Download dependencies
RUN chmod +x mvnw
RUN ./mvnw dependency:go-offline -B

# Copy source code
COPY src src

# Build the application
RUN ./mvnw clean package -DskipTests

# Runtime stage
FROM eclipse-temurin:17-jre-focal

WORKDIR /app

# Copy the built jar from builder stage
COPY --from=builder /app/target/*.jar app.jar

# Expose port (Render will override with PORT env var)
EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-Dserver.port=${PORT:-8080}", "-jar", "app.jar"]
