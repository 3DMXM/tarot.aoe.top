import { defineConfig } from 'vitepress'
import { generateSidebar } from 'vitepress-sidebar';
// import vercel from 'vite-plugin-vercel';


// https://vitepress.dev/reference/site-config
export default defineConfig({
    title: "奥秘塔罗牌",
    description: "A VitePress Site",
    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        nav: [
            { text: '首页', link: '/' },
            { text: '大奥秘', link: '/MajorArcana' }
        ],

        sidebar: generateSidebar({
            useTitleFromFileHeading: true
        }),
        socialLinks: [
            { icon: 'github', link: 'https://github.com/3DMXM/tarot.aoe.top' }
        ]
    },
    sitemap: {
        hostname: 'https://tarot.aoe.top'
    },
})

