import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path';
import { quasar } from '@quasar/vite-plugin'

// https://vitejs.dev/config/
export default defineConfig({
  resolve:{
    alias:{
      '@' : resolve(__dirname, './src')
    },
  },
  plugins: [
    vue(),
    quasar()
  ],
})
