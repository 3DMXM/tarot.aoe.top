<template>
    <div style="margin-top: 24px">
        <Giscus id="comments" repo="3DMXM/tarot.aoe.top" repoid="R_kgDOOPP23Q" category="General"
            categoryid="DIC_kwDOOPP23c4CpgaI" mapping="pathname" term="Welcome to giscus!" reactionsenabled="1"
            lang="zh-CN" emitmetadata="0" inputposition="top" loading="lazy" :theme="isDark ? 'dark' : 'light'"
            :key="route.path">
        </Giscus>
    </div>
</template>

<script setup>
import Giscus from '@giscus/vue';
import { useRoute, useData } from 'vitepress';


const route = useRoute();
const { isDark } = useData();
</script>