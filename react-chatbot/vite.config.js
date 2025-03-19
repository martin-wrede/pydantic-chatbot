// filepath: c:\Users\marti\OneDrive\Documents\CODING\pydantic-ai-tutorial-rabbitmetrics\react-chatbot\vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: '/pydantic-chatbot/', // This should match your GitHub repository name
});