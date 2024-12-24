# Stage 1: Build Frontend
FROM node:18-alpine AS frontend-build
WORKDIR /opt/app-root/src/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Build Backend
FROM node:18-alpine AS backend-build
WORKDIR /opt/app-root/src/backend
COPY backend/package*.json ./
RUN npm install
COPY backend/ ./
EXPOSE 5000
CMD ["npm", "start"]


# Stage 3: Serve Frontend with Nginx
FROM nginx:alpine
COPY --from=frontend-build /opt/app-root/src/frontend/dist /usr/share/nginx/html
RUN chmod -R 755 /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
