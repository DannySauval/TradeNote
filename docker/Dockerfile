# Using 18 alpine because supports arm/v8 and arm/v8 needed for silicon chips
FROM node:18-alpine
RUN apk add --no-cache bash
RUN apk update && apk add python3
RUN apk add --no-cache build-base
WORKDIR /app
ADD ./ .
RUN npm install
RUN npm run build
CMD ["npm", "start"]