# Use Node 20
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY frontend/package*.json ./
RUN npm install

# Copy the rest of the frontend code
COPY frontend/ ./

# Expose Next.js dev port
EXPOSE 3000

# Start Next.js in dev mode
CMD ["npm", "run", "dev"]
