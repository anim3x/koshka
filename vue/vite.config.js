import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import tailwindcss from '@tailwindcss/vite';
import fs from 'fs';

export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(),
  ],
  
  server: {
    host: '0.0.0.0',
    port: 8080,
    allowedHosts: ['koshka.msk.ru'],
    https: {
      key: fs.readFileSync('../ssl/private.pem'),
      cert: fs.readFileSync('../ssl/koshka.pem'),
    },
  },
});
