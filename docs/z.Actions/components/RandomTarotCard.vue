<script lang='ts' setup>
import 'element-plus/dist/index.css'
import 'element-plus/theme-chalk/dark/css-vars.css'

import { ref } from 'vue'
import { ElButton, ElImage, ElSelect, ElOption, ElMessage } from 'element-plus'

type TTarot = {
    name: string
    image: string
    url: string
    upright?: "Reversed" | "Upright"  // 牌面正位或逆位
    open?: boolean // 是否翻开
    flipping?: boolean // 是否正在翻转中
}
type TSpread = {
    name: string
    nuber: number
    use: string
    describe: string
}

const yourTarot = ref<TTarot[]>([])
const yourSpread = ref<TSpread>({ name: '单张牌', nuber: 1, use: '简单问题', describe: '适合快速了解当前状况或简单问题' })

const tarots: TTarot[] = [
    { name: '愚者', image: '/tarot/images/yz.jpg', url: '/MajorArcana/0.TheFool.html' },
    { name: '魔术师', image: '/tarot/images/a1.webp', url: '/MajorArcana/1.TheMagician.html' },
    { name: '女祭司', image: '/tarot/images/a2.webp', url: '/MajorArcana/2.TheHighPriestess.html' },
    { name: '女皇', image: '/tarot/images/a3.webp', url: '/MajorArcana/3.TheEmpress.html' },
    { name: '皇帝', image: '/tarot/images/a4.webp', url: '/MajorArcana/4.TheEmperor.html' },
    { name: '教皇', image: '/tarot/images/a5.webp', url: '/MajorArcana/5.TheHierophant.html' },
    { name: '恋人', image: '/tarot/images/a6.webp', url: '/MajorArcana/6.TheLovers.html' },
    { name: '战车', image: '/tarot/images/a7.webp', url: '/MajorArcana/7.TheChariot.html' },
    { name: '力量', image: '/tarot/images/a8.webp', url: '/MajorArcana/8.Strength.html' },
    { name: '隐者', image: '/tarot/images/a9.webp', url: '/MajorArcana/9.TheHermit.html' },
    { name: '命运之轮', image: '/tarot/images/a10.webp', url: '/MajorArcana/10.WheelofFortune.html' },
    { name: '正义', image: '/tarot/images/a11.webp', url: '/MajorArcana/11.Justice.html' },
    { name: '吊人', image: '/tarot/images/a12.webp', url: '/MajorArcana/12.TheHangedMan.html' },
    { name: '死神', image: '/tarot/images/a13.webp', url: '/MajorArcana/13.Death.html' },
    { name: '节制', image: '/tarot/images/a14.webp', url: '/MajorArcana/14.Temperance.html' },
    { name: '恶魔', image: '/tarot/images/a15.webp', url: '/MajorArcana/15.TheDevil.html' },
    { name: '塔', image: '/tarot/images/a16.webp', url: '/MajorArcana/16.TheTower.html' },
    { name: '星星', image: '/tarot/images/a17.webp', url: '/MajorArcana/17.TheStar.html' },
    { name: '月亮', image: '/tarot/images/a18.webp', url: '/MajorArcana/18.TheMoon.html' },
    { name: '太阳', image: '/tarot/images/a19.webp', url: '/MajorArcana/19.TheSun.html' },
    { name: '审判', image: '/tarot/images/a20.webp', url: '/MajorArcana/20.Judgement.html' },
    { name: '世界', image: '/tarot/images/a21.webp', url: '/MajorArcana/21.TheWorld.html' },

    // 权杖组
    { name: '权杖 一', image: '/tarot/images/w1.webp', url: '/MinorArcana/1.wands/wands1.html' },
    { name: '权杖 二', image: '/tarot/images/w2.webp', url: '/MinorArcana/1.wands/wands2.html' },
    { name: '权杖 三', image: '/tarot/images/w3.webp', url: '/MinorArcana/1.wands/wands3.html' },
    { name: '权杖 四', image: '/tarot/images/w4.webp', url: '/MinorArcana/1.wands/wands4.html' },
    { name: '权杖 五', image: '/tarot/images/w5.webp', url: '/MinorArcana/1.wands/wands5.html' },
    { name: '权杖 六', image: '/tarot/images/w6.webp', url: '/MinorArcana/1.wands/wands6.html' },
    { name: '权杖 七', image: '/tarot/images/w7.webp', url: '/MinorArcana/1.wands/wands7.html' },
    { name: '权杖 八', image: '/tarot/images/w8.webp', url: '/MinorArcana/1.wands/wands8.html' },
    { name: '权杖 九', image: '/tarot/images/w9.webp', url: '/MinorArcana/1.wands/wands9.html' },
    { name: '权杖 十', image: '/tarot/images/w10.webp', url: '/MinorArcana/1.wands/wands10.html' },
    { name: '权杖 侍者', image: '/tarot/images/w11.webp', url: '/MinorArcana/1.wands/wands11.html' },
    { name: '权杖 骑士', image: '/tarot/images/w12.webp', url: '/MinorArcana/1.wands/wands12.html' },
    { name: '权杖 皇后', image: '/tarot/images/w13.webp', url: '/MinorArcana/1.wands/wands13.html' },
    { name: '权杖 国王', image: '/tarot/images/w14.webp', url: '/MinorArcana/1.wands/wands14.html' },

    // 圣杯组
    { name: '圣杯 一', image: '/tarot/images/c1.webp', url: '/MinorArcana/2.cups/cups1.html' },
    { name: '圣杯 二', image: '/tarot/images/c2.webp', url: '/MinorArcana/2.cups/cups2.html' },
    { name: '圣杯 三', image: '/tarot/images/c3.webp', url: '/MinorArcana/2.cups/cups3.html' },
    { name: '圣杯 四', image: '/tarot/images/c4.webp', url: '/MinorArcana/2.cups/cups4.html' },
    { name: '圣杯 五', image: '/tarot/images/c5.webp', url: '/MinorArcana/2.cups/cups5.html' },
    { name: '圣杯 六', image: '/tarot/images/c6.webp', url: '/MinorArcana/2.cups/cups6.html' },
    { name: '圣杯 七', image: '/tarot/images/c7.webp', url: '/MinorArcana/2.cups/cups7.html' },
    { name: '圣杯 八', image: '/tarot/images/c8.webp', url: '/MinorArcana/2.cups/cups8.html' },
    { name: '圣杯 九', image: '/tarot/images/c9.webp', url: '/MinorArcana/2.cups/cups9.html' },
    { name: '圣杯 十', image: '/tarot/images/c10.webp', url: '/MinorArcana/2.cups/cups10.html' },
    { name: '圣杯 侍者', image: '/tarot/images/c11.webp', url: '/MinorArcana/2.cups/cups11.html' },
    { name: '圣杯 骑士', image: '/tarot/images/c12.webp', url: '/MinorArcana/2.cups/cups12.html' },
    { name: '圣杯 皇后', image: '/tarot/images/c13.webp', url: '/MinorArcana/2.cups/cups13.html' },
    { name: '圣杯 国王', image: '/tarot/images/c14.webp', url: '/MinorArcana/2.cups/cups14.html' },

    // 宝剑组
    { name: '宝剑 一', image: '/tarot/images/s1.webp', url: '/MinorArcana/3.swords/swords1.html' },
    { name: '宝剑 二', image: '/tarot/images/s2.webp', url: '/MinorArcana/3.swords/swords2.html' },
    { name: '宝剑 三', image: '/tarot/images/s3.webp', url: '/MinorArcana/3.swords/swords3.html' },
    { name: '宝剑 四', image: '/tarot/images/s4.webp', url: '/MinorArcana/3.swords/swords4.html' },
    { name: '宝剑 五', image: '/tarot/images/s5.webp', url: '/MinorArcana/3.swords/swords5.html' },
    { name: '宝剑 六', image: '/tarot/images/s6.webp', url: '/MinorArcana/3.swords/swords6.html' },
    { name: '宝剑 七', image: '/tarot/images/s7.webp', url: '/MinorArcana/3.swords/swords7.html' },
    { name: '宝剑 八', image: '/tarot/images/s8.webp', url: '/MinorArcana/3.swords/swords8.html' },
    { name: '宝剑 九', image: '/tarot/images/s9.webp', url: '/MinorArcana/3.swords/swords9.html' },
    { name: '宝剑 十', image: '/tarot/images/s10.webp', url: '/MinorArcana/3.swords/swords10.html' },
    { name: '宝剑 侍者', image: '/tarot/images/s11.webp', url: '/MinorArcana/3.swords/swords11.html' },
    { name: '宝剑 骑士', image: '/tarot/images/s12.webp', url: '/MinorArcana/3.swords/swords12.html' },
    { name: '宝剑 皇后', image: '/tarot/images/s13.webp', url: '/MinorArcana/3.swords/swords13.html' },
    { name: '宝剑 国王', image: '/tarot/images/s14.webp', url: '/MinorArcana/3.swords/swords14.html' },

    // 星币组
    { name: '星币 一', image: '/tarot/images/p1.webp', url: '/MinorArcana/4.pentacles/pentacles1.html' },
    { name: '星币 二', image: '/tarot/images/p2.webp', url: '/MinorArcana/4.pentacles/pentacles2.html' },
    { name: '星币 三', image: '/tarot/images/p3.webp', url: '/MinorArcana/4.pentacles/pentacles3.html' },
    { name: '星币 四', image: '/tarot/images/p4.webp', url: '/MinorArcana/4.pentacles/pentacles4.html' },
    { name: '星币 五', image: '/tarot/images/p5.webp', url: '/MinorArcana/4.pentacles/pentacles5.html' },
    { name: '星币 六', image: '/tarot/images/p6.webp', url: '/MinorArcana/4.pentacles/pentacles6.html' },
    { name: '星币 七', image: '/tarot/images/p7.webp', url: '/MinorArcana/4.pentacles/pentacles7.html' },
    { name: '星币 八', image: '/tarot/images/p8.webp', url: '/MinorArcana/4.pentacles/pentacles8.html' },
    { name: '星币 九', image: '/tarot/images/p9.webp', url: '/MinorArcana/4.pentacles/pentacles9.html' },
    { name: '星币 十', image: '/tarot/images/p10.webp', url: '/MinorArcana/4.pentacles/pentacles10.html' },
    { name: '星币 侍者', image: '/tarot/images/p11.webp', url: '/MinorArcana/4.pentacles/pentacles11.html' },
    { name: '星币 骑士', image: '/tarot/images/p12.webp', url: '/MinorArcana/4.pentacles/pentacles12.html' },
    { name: '星币 皇后', image: '/tarot/images/p13.webp', url: '/MinorArcana/4.pentacles/pentacles13.html' },
    { name: '星币 国王', image: '/tarot/images/p14.webp', url: '/MinorArcana/4.pentacles/pentacles14.html' },
]

const tarotSpread: TSpread[] = [
    { name: '单张牌', nuber: 1, use: '简单问题', describe: '适合快速了解当前状况或简单问题' },
    { name: '三张牌', nuber: 3, use: '过去、现在、未来', describe: '适合了解过去、现在和未来的关系' },
    { name: '十字牌', nuber: 5, use: '复杂问题', describe: '适合深入分析复杂问题' },
    { name: '凯尔特十字', nuber: 10, use: '全面分析', describe: '适合全面分析问题的各个方面' },
    { name: '星形牌', nuber: 7, use: '多方面分析', describe: '适合多方面分析问题' },
    { name: '爱情牌', nuber: 2, use: '爱情问题', describe: '适合分析爱情关系' },
    { name: '事业牌', nuber: 3, use: '事业问题', describe: '适合分析事业发展' },
    { name: '财运牌', nuber: 4, use: '财运问题', describe: '适合分析财运状况' },
    { name: '健康牌', nuber: 5, use: '健康问题', describe: '适合分析健康状况' },
    { name: '人际关系牌', nuber: 6, use: '人际关系问题', describe: '适合分析人际关系' },
]

function getTarots() {
    if (yourSpread.value) {
        yourTarot.value = []
        console.log(yourSpread.value);

        // 创建已抽取牌的索引数组，用于去重
        const usedIndices: number[] = [];

        for (let i = 0; i < yourSpread.value.nuber; i++) {
            // 如果已经抽完所有牌，则退出循环
            if (usedIndices.length >= tarots.length) {
                ElMessage.warning('牌库中的牌已经抽完了！');
                break;
            }

            let randomIndex: number;
            // 确保不抽取重复的牌
            do {
                randomIndex = Math.floor(Math.random() * tarots.length);
            } while (usedIndices.includes(randomIndex));

            // 将已抽取的牌索引添加到数组中
            usedIndices.push(randomIndex);

            const selectedTarot = { ...tarots[randomIndex] }; // 创建对象副本，避免修改原数组中的对象

            selectedTarot.upright = Math.random() < 0.5 ? "Upright" : "Reversed"; // 随机决定正位或逆位
            selectedTarot.open = false; // 设置为未翻开状态
            selectedTarot.flipping = false; // 设置为未翻转状态

            console.log(`抽到的牌是：`, selectedTarot);
            yourTarot.value.push(selectedTarot);
        }
    } else {
        ElMessage.warning('请选择牌阵')
    }
}

// 添加翻牌动画函数
function flipCard(tarot: TTarot) {
    if (!tarot.flipping) {
        tarot.flipping = true;
        setTimeout(() => {
            tarot.open = true;
            setTimeout(() => {
                tarot.flipping = false;
            }, 300);
        }, 300);
    }
}

</script>
<template>
    <div class="wrap">
        <div class="actions">
            <el-select v-model="yourSpread" placeholder="请选择牌阵" style="width: 200px;" clearable value-key="name">
                <el-option v-for="(spread, index) in tarotSpread" :key="index" :label="spread.name" :value="spread">
                    {{ spread.name }} - {{ spread.nuber }}张 - {{ spread.use }} - {{ spread.describe }}
                </el-option>
            </el-select>
            <el-button @click="getTarots">抽取塔罗牌</el-button>
        </div>
        <div class="you-tarots">
            <div class="your-tarot" v-for="(tarot, index) in yourTarot" :key="index">
                <div class="card-container" :class="{ 'flipping': tarot.flipping }">
                    <div class="card" :class="{ 'flipped': tarot.open }">
                        <div v-if="!tarot.open" class="card-back" @click="flipCard(tarot)">
                            <el-image src="/tarot/un-open.jpg"></el-image>
                            <div>未翻开</div>
                        </div>
                        <div v-else class="card-front">
                            <el-image :class="tarot.upright" :src="tarot.image"></el-image>
                            <div>{{ tarot.name }}</div>
                            <div v-if="tarot.upright == 'Upright'">
                                <a :href="tarot.url" target="_blank">正位</a>
                            </div>
                            <div v-else>
                                <a :href="tarot.url" target="_blank">逆位</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang='ts'>

export default {
    name: 'RandomTarotCard',
}
</script>
<style lang='less' scoped>
.wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 200px;

    .actions {
        height: 70px;
        display: flex;
        justify-content: center;
        align-items: center;

        .button {
            padding: 6px;
            border-color: var(--vp-button-brand-border);
            color: var(--vp-button-brand-text);
            background-color: var(--vp-button-brand-bg);
            border-radius: 20px;
            padding: 0 20px;
            line-height: 38px;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.5s;

            &:hover {
                border-color: var(--vp-button-brand-active-border);
                color: var(--vp-button-brand-active-text);
                background-color: var(--vp-button-brand-active-bg);
            }
        }

    }


    .you-tarots {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;

        .your-tarot {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 5px;
            perspective: 1000px; // 添加3D视角

            .card-container {
                width: 200px;
                height: 364px;
                transition: transform 0.6s;

                &.flipping {
                    animation: cardShake 0.3s ease-in-out;
                }
            }

            .card {
                width: 100%;
                height: 100%;
                position: relative;
                transition: transform 0.6s;
                transform-style: preserve-3d;

                &.flipped {
                    transform: rotateY(180deg);
                }
            }

            .card-front,
            .card-back {
                width: 100%;
                height: 100%;
                backface-visibility: hidden;
                display: flex;
                flex-direction: column;
                align-items: center;
            }

            .card-back {
                cursor: pointer;
                z-index: 2;
                transform: rotateY(0deg);

                &:hover {
                    filter: brightness(1.1);
                }
            }

            .card-front {
                transform: rotateY(180deg);
            }

            .Reversed {
                transform: rotate(180deg);
            }
        }


    }
}

@keyframes cardShake {
    0% {
        transform: translateX(0) rotate(0);
    }

    25% {
        transform: translateX(-5px) rotate(-5deg);
    }

    50% {
        transform: translateX(5px) rotate(5deg);
    }

    75% {
        transform: translateX(-5px) rotate(-5deg);
    }

    100% {
        transform: translateX(0) rotate(0);
    }
}
</style>
