# Use node:18-alpine to support ARM/v8 (Apple Silicon)
FROM node:18-alpine

# Install necessary dependencies
RUN apk add --no-cache bash python3 build-base

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json for caching npm install
COPY package*.json ./

# Install dependencies (this step is cached unless package.json changes)
RUN npm install

# Copy the rest of the application code
COPY ./ .

# Build the application
RUN npm run build

# Start the application
CMD ["npm", "start"]
