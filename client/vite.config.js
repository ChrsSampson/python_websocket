import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [react()],
    mode: 'development',
    build: {
        outDir: path.resolve('../', 'static'),
        emptyOutDir: true,
        // remove this if this ever gets deployed
        watch: {},
    },
});
