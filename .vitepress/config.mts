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
            useTitleFromFileHeading: true,
            sortFolderTo: 'bottom',
            useFolderTitleFromIndexFile: true,
            includeFolderIndexFile: true,
            collapsed: true,
        }),
        socialLinks: [
            { icon: 'github', link: 'https://github.com/3DMXM/tarot.aoe.top' }
        ],
        search: {
            provider: 'local'
        },
        editLink: {
            text: "在GitHub上编辑此页面",
            pattern: 'https://github.com/3DMXM/tarot.aoe.top/edit/main/:path'
        },
        lastUpdated: {
            text: '最后更新于',
            formatOptions: {
                dateStyle: 'short',
                timeStyle: 'medium'
            }
        },
        docFooter: {
            prev: '上一页',
            next: '下一页'
        },
        outline: {
            label: '页面导航'
        },
    },
    head:[
        [
            'script',
            {
                async: "true",
                src: 'https://www.googletagmanager.com/gtag/js?id=G-L04H04RSS7',
            },
        ],
        [
            'script',
            {},
            "window.dataLayer = window.dataLayer || [];\nfunction gtag(){dataLayer.push(arguments);}\ngtag('js', new Date());\ngtag('config', 'G-L04H04RSS7');",
        ],
        [
            'script',
            {},
            `var _hmt = _hmt || [];
            (function() {
              var hm = document.createElement("script");
              hm.src = "https://hm.baidu.com/hm.js?0fba1f3013c5565107a4b39759647150";
              var s = document.getElementsByTagName("script")[0]; 
              s.parentNode.insertBefore(hm, s);
            })();`
        ],
        [
            'script',
            {
                "async": "true",
                'src': 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5978423097771370',
            }
        ],
        [
            'link',
            {
                "rel": "icon",
                "href": "https://mod.3dmgame.com/static/upload/mod/202307/MOD64a7767d0409f.png@webp",
            }
        ]
    ],
    sitemap: {
        hostname: 'https://tarot.aoe.top'
    },
    lastUpdated: true,
})

