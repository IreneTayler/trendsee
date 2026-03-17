<template>
  <Teleport to="body">
    <!-- Overlay: simple fade in/out -->
    <Transition name="overlay-fade">
      <div v-if="visible" class="modal-overlay flex h-screen items-stretch justify-end" @click.self="onClose">
        <!-- Panel: distinct slide-in-from-right animation -->
        <Transition name="panel-slide">
          <div
            v-if="post"
            class="h-screen w-full max-w-[960px] flex flex-col overflow-hidden bg-white shadow-[0_24px_80px_rgba(0,0,0,0.2)] rounded-tl-2xl rounded-bl-2xl"
          >
            <button type="button" class="modal__close" aria-label="Закрыть" @click="onClose">
              ✕
            </button>

            <!-- Single scroll area: top card + protruding bottom panel -->
            <div class="flex-1 min-h-0 overflow-y-auto overflow-x-hidden">
              <!-- Top block: main card (video, tags, transcript, button) -->
              <div class="grid min-h-0 grid-cols-[340px,1fr] gap-0 px-10 pt-12 pb-0">
              <!-- Left column: video + profile + metrics -->
              <div class="modal__left">
                <div class="relative w-[216px] h-[340px]">
                  <img
                    v-if="imageSrc"
                    :src="imageSrc"
                    alt=""
                    class="absolute inset-0 h-full w-full rounded-xl object-cover"
                  />
                  <div
                    v-else
                    class="absolute inset-0 rounded-xl bg-slate-200"
                  />
                  <div class="post-card__badges post-card__badges--left">
                    <span class="post-card__badge">
                      <span><img :src="socialMediaLogos" alt="trendsee" class="size-[16px]" /> </span>
                      Reels
                    </span>
                    <span class="post-card__badge">
                      <span><img :src="whiteFire" alt="trendsee" class="h-[16px]" />
                      </span>
                      X10
                    </span>
                  </div>
                </div>
                <div class="modal__video-footer">
                  <span class="modal__date">{{ createdDate }}</span>
                  <button type="button" class="modal__share" aria-label="Поделиться">
                    <img :src="RightIcon" alt="trendsee" class="size-[24px]" />
                  </button>
                </div>
                <div class="post-card__profile">
                  <div class="">
                    <img :src="image1" alt="" class="size-[40px] post-card__avatar" />
                  </div>
                  <div class="post-card__profile-text">
                    <span class="post-card__username">@blogerich</span>
                    <span class="post-card__followers">384.5K</span>
                  </div>
                  <div class="size-[24px]">
                    <img :src="incognitoMode" alt="" />
                    <img :src="plus" alt="" />
                  </div>
                </div>
                <div
                  class="modal__expand"
                  :class="{ 'modal__expand--open': isDescriptionExpanded }"
                >
                  <div class="">
                    <div class="modal__description">
                      <p class="modal__description-text">{{ isDescriptionExpanded ? props.post?.text : descriptionSnippet }}</p>
                      <div class="flex justify-end">
                        <button type="button" class="flex items-center" @click="toggleDescription">
                          <img :src="IconleadingDown" alt="" class="size-[12px]"/>
                          <span class="text-[#171C1F] text-[12px] pl-1">
                            {{ isDescriptionExpanded ? "Скрыть" : "Ещё" }}
                          </span>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
                <ul class="modal__metrics">
                  <li
                    class="flex flex-wrap content-center justify-start items-center bg-[#f4f5f6] rounded-xl pt-[8px] pb-[8px] pl-[16px] pr-[16px]">
                    <img :src="blueEye" alt="" />
                    <span class="modal__metric-icon"> Просмотры </span>
                    <span class="modal__metric-label">1,2 млн</span>
                  </li>
                  <li
                    class="flex flex-wrap content-center justify-start items-center bg-[#f4f5f6] rounded-xl pt-[8px] pb-[8px] pl-[16px] pr-[16px]">
                    <img :src="pinkHeart" alt="" />
                    <span class="modal__metric-icon"></span> Лайки
                    <span class="modal__metric-label">1,2 млн</span>
                  </li>
                  <li
                    class="flex flex-wrap content-center justify-start items-center bg-[#f4f5f6] rounded-xl pt-[8px] pb-[8px] pl-[16px] pr-[16px]">
                    <img :src="greenComments" alt="" />
                    <span class="modal__metric-icon"></span> Комментарии
                    <span class="modal__metric-label">1,2 млн</span>
                  </li>
                  <li
                    class="flex flex-wrap content-center justify-start items-center bg-[#f4f5f6] rounded-xl pt-[8px] pb-[8px] pl-[16px] pr-[16px]">
                    <img :src="orangeShares" alt="" />
                    <span class="modal__metric-icon"></span> Репосты
                    <span class="modal__metric-label">1,2 млн</span>
                  </li>
                  <li
                    class="flex flex-wrap content-center justify-start items-center bg-[#f4f5f6] rounded-xl pt-[8px] pb-[8px] pl-[16px] pr-[16px]">
                    <img :src="er_label" alt="" />
                    <span class="modal__metric-icon"></span> Репосты
                    <span class="modal__metric-label">1,2 млн</span>
                  </li>
                </ul>
              </div>

              <!-- Right column: topic, tags, transcript, adapt, essence -->
              <div class="modal__right">
                <div class="modal__topic">
                  <p class="modal__topic-label">Тема видео</p>
                  <h2 class="modal__title">{{ post.title }}</h2>
                </div>
                <div class="flex">
                  <div class="flex bg-[#F1F3F5] rounded-3xl pt-[6px] pb-[6px] pl-[12px] pr-[12px]">
                    <img :src="music" alt="" class="size-[16px]"/>
                    <span class="color-[#343A40] text-xs pl-3">Tyga — Pop it off</span>
                  </div>
                  <div class="flex pl-20">
                    <span class="color-[#343A40] text-xs"> Язык:</span>                
                    <img :src="TrendSourceIcon" alt="" class="size-[16px] ml-2"/>
                    <span class="color-[#343A40] text-xs pl-2"> Английский</span>
                  </div>
                </div>
                <div class="modal__tags">
                  <span class="bg-[#D5D6F8] text-[#333CD3] text-[14px] pt-[4px] pb-[4px] pl-[12px] pr-[12px] rounded-full">Туториал</span>
                  <span class="bg-[#E1F7D8] text-[#1E6D00] text-[14px] pt-[4px] pb-[4px] pl-[12px] pr-[12px] rounded-full">Энергичное видео</span>
                  <span class="bg-[#FFF0CB] text-[#9E3F00] text-[14px] pt-[4px] pb-[4px] pl-[12px] pr-[12px] rounded-full">Изи монтаж</span>
                  <span class="bg-[#FFECF1] text-[#BF0031] text-[14px] pt-[4px] pb-[4px] pl-[12px] pr-[12px] rounded-full">Трендовый звук</span>
                  <span class="bg-[#FFF0CB] text-[#9E3F00] text-[14px] pt-[4px] pb-[4px] pl-[12px] pr-[12px] rounded-full">Лид магнит</span>
                  <span class="bg-[#D5D6F8] text-[#2B31B3] text-[14px] pt-[4px] pb-[4px] pl-[12px] pr-[12px] rounded-full">Красота и здоровье</span>
                </div>
                <div class="h-[32px] flex justify-between">
                  <div>
                    <h3 class="color-black font-semibold p-[8px] text-[16px]">Транскрибация</h3>
                  </div>
                  <div class="flex">
                    <div  class="bg-[#F4F5F6] text-[#2B31B3] text-[14px] pt-[4px] pb-[4px] pl-[12px] pr-[12px] rounded-full flex items-center">
                      <img :src="IconLeading" alt="" class="size-[16px]"/>
                      <span> Переведено</span>
                    </div>
                    <button
                      type="button"
                      class="bg-[#F4F5F6] pt-[4px] pb-[4px] pl-[12px] pr-[12px] rounded-full"
                      aria-label="Копировать"
                      @click="copyTranscript"
                    >
                      <img :src="ButtonSecondary" alt="" class="size-[12px]"/>
                    </button>
                  </div>
                </div>
                <div
                  class="modal__expand modal__expand--transcript"
                  :class="{ 'modal__expand--open': isTranscriptExpanded }"
                >
                  <div class="modal__expand-inner bg-[#F4F5F6] rounded-md">
                    <div class="pt-[16px] pb-[16px] pr-[16px] pl-[18px] ">
                      <p class="text-[#4E616B]">
                        {{ isTranscriptExpanded ? post.text : transcriptSnippet }}
                      </p>
                      <div class="flex justify-end">
                        <button type="button" class="flex items-center" @click="toggleTranscript">
                          <img :src="IconleadingDown" alt="" class="size-[12px]"/>
                          <span class="text-[#171C1F] text-[12px] pl-1">
                            {{ isTranscriptExpanded ? "Скрыть" : "Ещё" }}
                          </span>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
                <button type="button" class="flex justify-evenly items-center bg-[#2B31B3] w-[220px] h-[56px] rounded-xl p-[16px]">
                  <span>
                    <img :src="primary" alt="" class="size-[24px]"/>
                  </span>
                  <span class="text-[#ffffff] text-[18px]">Адаптировать</span>
                </button>

                 <!-- Protruding panel (right column only), scrolls with content above -->
                <div class="gap-0 border-t border-slate-200 bg-white pt-4 pb-8">
                  <div class="min-w-0 space-y-8">
                    <!-- Суть -->
                    <section>
                      <div class="flex items-center gap-2 mb-2">
                        <h3 class="text-slate-900 font-bold text-lg">Суть</h3>
                      </div>
                      <div class="bg-[#F4F5F6] p-4 rounded-xl text-[#4E616B] text-sm leading-relaxed">
                        Разбор состава/логики: он в человеческих словах переводит состав/механику («что реально делает Х»),
                        называет 2-3 работающих активных компонента и 2-3 маркетинговых «пустых» обещания.
                      </div>
                    </section>

                    <!-- Структура -->
                    <section>
                      <h3 class="text-slate-900 font-bold text-lg mb-4">Структура</h3>
                      <div class="bg-[#F4F5F6] rounded-xl p-4 space-y-0">
                        <div class="flex gap-4">
                          <div class="flex flex-col items-center">
                            <div class="flex items-start gap-2">
                              <span class="text-slate-400 text-xs mt-0.5">
                                <img :src="iconTime" alt="" class="size-[16px]"/>
                              </span>
                              <span class="text-slate-400 text-xs whitespace-nowrap">0-3 сек</span>
                            </div>
                          </div>
                          <div>
                            <img :src="Ellipse1" alt="" class="size-[16px]"/>
                            <img :src="StepTimeIcon" class="ml-[7px]" alt="" />
                          </div>                         
                          <div class="flex-1 pb-4">
                            <p class="font-semibold text-slate-900 text-sm">Шок-сравнение</p>
                            <p class="text-[#4E616B] text-sm mt-1">Визуальный (Девушка с предметом) + Текст на экране: «Это спасет вашу зиму»</p>
                          </div>
                        </div>

                        <div class="flex gap-4">
                          <div class="flex flex-col items-center">
                            <div class="flex items-start gap-2">
                              <span class="text-slate-400 text-xs mt-0.5">
                                <img :src="iconTime" alt="" class="size-[16px]"/>
                              </span>
                              <span class="text-slate-400 text-xs whitespace-nowrap">0-3 сек</span>
                            </div>
                          </div>
                          <div>
                            <img :src="Ellipse2" alt="" class="size-[16px]"/>
                            <img :src="StepTimeIcon" class="ml-[7px]" alt="" />
                          </div>                         
                          <div class="flex-1 pb-4">
                            <p class="font-semibold text-slate-900 text-sm">Сюжет</p>
                            <p class="text-[#4E616B] text-sm mt-1">[Герой] показывает проблему -> Резкар смена кадра -> Решение</p>
                          </div>
                        </div>

                        <div class="flex gap-4">
                          <div class="flex flex-col items-center">
                            <div class="flex items-start gap-2">
                              <span class="text-slate-400 text-xs mt-0.5">
                                <img :src="iconTime" alt="" class="size-[16px]"/>
                              </span>
                              <span class="text-slate-400 text-xs whitespace-nowrap">0-3 сек</span>
                            </div>
                          </div>
                          <div>
                            <img :src="Ellipse3" alt="" class="size-[16px]"/>
                            <img :src="StepTimeIcon" class="ml-[7px]" alt="" />
                          </div>                         
                          <div class="flex-1 pb-4">
                            <p class="font-semibold text-slate-900 text-sm">Финал / CTA</p>
                            <p class="text-[#4E616B] text-sm mt-1">Призыв: "Пиши слово "ССЫЛКА" в комменты"</p>
                          </div>
                        </div>

                      </div>
                    </section>

                    <!-- Хук фраза, Визуальный хук, Текстовый хук -->
                    <section class="bg-[#F4F5F6] rounded-xl p-4 space-y-4">
                      <div class="flex items-start justify-between gap-3">
                        <div>
                          <p class="font-bold text-slate-900 text-sm">Хук фраза</p>
                          <p class="text-[#4E616B] text-sm mt-1">Одна из них — пустышка. Угадаешь какая?</p>
                        </div>
                        <button type="button" class="flex-shrink-0 p-1.5 rounded hover:bg-white/60 text-slate-500" aria-label="Копировать">⎘</button>
                      </div>
                      <div class="border-t border-slate-200 pt-4 flex items-start justify-between gap-3">
                        <div>
                          <p class="font-bold text-slate-900 text-sm">Визуальный хук</p>
                          <p class="text-[#4E616B] text-sm mt-1">Одна из них — пустышка. Угадаешь какая?</p>
                        </div>
                        <button type="button" class="flex-shrink-0 p-1.5 rounded hover:bg-white/60 text-slate-500" aria-label="Копировать">⎘</button>
                      </div>
                      <div class="border-t border-slate-200 pt-4 flex items-start justify-between gap-3">
                        <div class="flex items-center gap-2">
                          <span class="text-slate-500" aria-hidden="true">👆</span>
                          <div>
                            <p class="font-bold text-slate-900 text-sm">Текстовый хук</p>
                            <p class="text-[#4E616B] text-sm mt-1">Одна из них — пустышка. Угадаешь какая?</p>
                          </div>
                        </div>
                        <button type="button" class="flex-shrink-0 p-1.5 rounded hover:bg-white/60 text-slate-500" aria-label="Копировать">⎘</button>
                      </div>
                    </section>

                    <!-- Рабочие приемы -->
                    <section>
                      <div class="flex items-center justify-between gap-3 mb-3">
                        <h3 class="text-slate-900 font-bold text-lg">Рабочие приемы</h3>
                        <button type="button" class="p-1.5 rounded hover:bg-slate-100 text-slate-500" aria-label="Копировать">⎘</button>
                      </div>
                      <div class="space-y-6 text-sm">
                        <div>
                          <p class="font-semibold text-slate-900">2. Суть видео</p>
                          <p class="text-[#4E616B] mt-1">Приём: «кому подходит / кому нет» двумя блоками.</p>
                          <p class="text-[#4E616B] mt-2">Почему сработало: это формат «диагноз → лечение → решение». Люди сохраняют не эмоции, а инструкцию. И это «обзор», а не философия.</p>
                        </div>
                        <div>
                          <p class="font-semibold text-slate-900">3. Монтаж</p>
                          <p class="text-[#4E616B] mt-1">Приём: смена планов каждые 1-2 секунды: лицо → продукт крупно → рука (демо) → снова лицо.</p>
                          <p class="text-[#4E616B] mt-2">Почему сработало: вертикалки смотрят на автопилоте. Частая смена планов держит внимание даже без звука.</p>
                          <p class="text-[#4E616B] mt-2">Приём: все доказательства — через B-roll вставки на 0.3-0.8 сек (катышки, блеск, этикетка, нанесение).</p>
                          <p class="text-[#4E616B] mt-2">Почему сработало: речь в кадре быстро утомляет. B-roll делает ощущение «я реально тестировал».</p>
                        </div>
                      </div>
                    </section>
                  </div>
                </div>
              </div>
            </div>

           
            </div>
          </div>
        </Transition>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import type { Post } from "../api";
import socialMediaLogos from "../imgs/Social media Logos.png";
import whiteFire from "../imgs/white_fire.png";
import RightIcon from "../imgs/Right Icon.png";
import image1 from "../imgs/image1.png";
import incognitoMode from "../imgs/Incognito_mode.png";
import blueEye from "../imgs/blue_eye.png";
import pinkHeart from "../imgs/pink_heart.png";
import greenComments from "../imgs/green_comments.png";
import orangeShares from "../imgs/orange_shares.png";
import er_label from "../imgs/er_label.png";
import music from "../imgs/music.png";
import TrendSourceIcon from "../imgs/Trend Source Icon.png";
import IconLeading from "../imgs/Icon Leading (1).png";
import ButtonSecondary from "../imgs/Button Secondary.png";
import IconleadingDown from "../imgs/Icon_leading_down.png";
import primary from "../imgs/primary.png";
import iconTime from "../imgs/Icon_time.png";
import Ellipse1 from "../imgs/Ellipse 1.png";
import Ellipse2 from "../imgs/Ellipse 1 (1).png";
import Ellipse3 from "../imgs/Ellipse 1 (2).png";
import StepTimeIcon from "../imgs/Step Time Icon.png";


const props = defineProps<{ visible: boolean; imageSrc?: string; post: Post | null }>();
const emit = defineEmits<{ (e: "close"): void }>();

const onClose = () => emit("close");

const createdDate = computed(() =>
  props.post
    ? new Date(props.post.created_at).toLocaleDateString("ru-RU", {
      day: "2-digit",
      month: "2-digit",
      year: "numeric"
    })
    : ""
);

const descriptionSnippet = computed(() => {
  if (!props.post?.text) return "";
  return props.post.text.length > 80 ? props.post.text.slice(0, 80) + "..." : props.post.text;
});

const transcriptSnippet = computed(() => {
  if (!props.post?.text) return "";
  return props.post.text.length > 200 ? props.post.text.slice(0, 200) + "..." : props.post.text;
});

const isDescriptionExpanded = ref(false);
const isTranscriptExpanded = ref(false);

const toggleDescription = () => {
  isDescriptionExpanded.value = !isDescriptionExpanded.value;
};

const toggleTranscript = () => {
  isTranscriptExpanded.value = !isTranscriptExpanded.value;
};

const copyTranscript = async () => {
  const text = props.post?.text ?? "";
  if (!text) return;
  try {
    await navigator.clipboard.writeText(text);
  } catch {
    // Fallback: hidden textarea
    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.style.position = "fixed";
    textarea.style.opacity = "0";
    document.body.appendChild(textarea);
    textarea.select();
    try {
      document.execCommand("copy");
    } finally {
      document.body.removeChild(textarea);
    }
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 50;
  display: flex;
  align-items: stretch;
  justify-content: flex-end;
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(8px);
  overflow: hidden;
}

.modal__close {
  position: absolute;
  top: 1rem;
  right: 1rem;
  z-index: 2;
  width: 2rem;
  height: 2rem;
  border: none;
  background: transparent;
  color: #64748b;
  font-size: 1.25rem;
  cursor: pointer;
  border-radius: 999px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal__close:hover {
  background: #f1f5f9;
  color: #0f172a;
}

.modal__left {
  background-color: #ffffff;
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 100%;
  max-width: 220px;
}

.modal__video-wrap {
  width: 216px;
  height: 340px;
  position: relative;
  background-size: contain;
  border-radius: 0.75rem;
  overflow: hidden;
}

.modal__video-placeholder {
  position: absolute;
  inset: 0;
}

.modal__reels-badge {
  position: absolute;
  top: 0.5rem;
  left: 0.5rem;
  padding: 0.25rem 0.5rem;
  border-radius: 0.5rem;
  background: rgba(15, 23, 42, 0.75);
  color: #fff;
  font-size: 0.7rem;
  font-weight: 600;
}

.modal__play-btn {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 3rem;
  text-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
}

.modal__video-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.8rem;
  color: #64748b;
}

.modal__share {
  border: none;
  background: none;
  cursor: pointer;
  color: #64748b;
  font-size: 1rem;
}

.modal__profile {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.modal__avatar {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 999px;
  background: linear-gradient(135deg, #f97316, #ec4899 50%, #6366f1);
  color: #fff;
  font-size: 0.9rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.modal__profile-text {
  flex: 1;
  min-width: 0;
}

.modal__username {
  margin: 0;
  font-size: 0.9rem;
  font-weight: 600;
  color: #4338ca;
}

.modal__followers {
  margin: 0;
  font-size: 0.75rem;
  color: #64748b;
}

.modal__profile-actions {
  display: flex;
  gap: 0.25rem;
  font-size: 0.8rem;
  color: #64748b;
}

.modal__expand {
  overflow: hidden;
  transition: max-height 0.35s ease-out;
}
.modal__expand:not(.modal__expand--open) {
  max-height: 100px;
}
.modal__expand.modal__expand--open {
  max-height: 2000px;
}
.modal__expand--transcript:not(.modal__expand--open) {
  max-height: 217px;
}

.modal__description {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.45;
  color: #334155;
}
.modal__description-text {
  margin: 0 0 0.5rem;
}


.modal__metrics {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  font-size: 0.8rem;
  color: #475569;
}

.modal__metrics strong {
  color: #0f172a;
  margin-left: 0.25rem;
}

.modal__metric-icon {
  padding-left: 10px;
  color: #343A40;
  font-weight: 500;
  font-style: Medium;
  font-size: 12px;
  letter-spacing: 0.4px;
}

.modal__metric-label {
  padding-left: 10px;
  color: #393C4C;
  font-weight: 500;
  font-style: Medium;
  font-size: 14px;
  line-height: 21px;
  letter-spacing: 0.25px;
  vertical-align: middle;

}

/* Right column */
.modal__right {
  padding: 1.25rem 1.5rem 1.25rem 0.75rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.modal__topic-label {
  margin: 0 0 0.25rem;
  font-size: 14px;
  color: #4E616B;
  letter-spacing: 0.05em;
}

.modal__title {
  font-weight: 600;
  font-style: Semi Bold;
  font-size: 24px;
  line-height: font/line-height/heading-3;
  letter-spacing: 0px;
  color: #000000;
}

.modal__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
}

.modal__transcript {
  padding: 0.75rem 1rem;
  background: #f8fafc;
  border-radius: 0.75rem;
}

.modal__transcript-title {
  margin: 0;
  font-size: 0.9rem;
  font-weight: 600;
  color: #0f172a;
}

.modal__essence-title {
  margin: 0 0 0.5rem;
  font-size: 0.95rem;
  font-weight: 600;
  color: #0f172a;
}

/* Overlay fade animation - radial spotlight */
.overlay-fade-enter-active,
.overlay-fade-leave-active {
  transition: opacity 0.35s ease-in-out;
}

.overlay-fade-enter-from,
.overlay-fade-leave-to {
  opacity: 0;
}

/* Panel animation - slide, skew and slight 3D rotate from the right */
.panel-slide-enter-active {
  transition:
    transform 0.4s cubic-bezier(0.19, 1, 0.22, 1),
    opacity 0.35s ease-out,
    box-shadow 0.4s ease-out;
}

.panel-slide-leave-active {
  transition:
    transform 0.3s cubic-bezier(0.55, 0.06, 0.68, 0.19),
    opacity 0.25s ease-in;
}

.panel-slide-enter-from {
  transform: translateX(40px) translateZ(0) skewX(-3deg) rotateY(-6deg);
  opacity: 0;
  box-shadow: 0 0 0 rgba(0, 0, 0, 0);
}

.panel-slide-leave-to {
  transform: translateX(24px) translateZ(0) skewX(-2deg) rotateY(-4deg);
  opacity: 0;
}

.post-card__badges {
  position: absolute;
  display: flex;
  flex-direction: column;
  gap: 6px;
  height: 28px;
}

.post-card__badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  border-radius: 8px;
  background: var(--Black-40, #00000066);
  backdrop-filter: blur(16px);
  color: #fff;
  font-size: 12px;
}

.post-card__badges--left {
  top: 10px;
  left: 10px;
}

.post-card__img {
  width: 216;
  height: 340.157470703125;
  border-radius: 16px;
  gap: 4px;
  angle: 0 deg;
  opacity: 1;
}

.post-card__profile {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
}

.post-card__profile-text {
  display: flex;
  flex-direction: column;
  flex: 1;
  min-width: 0;
}

.post-card__username {
  font-size: 14px;
  font-weight: 600;
  color: #2b31b3;
}

.post-card__followers {
  font-size: 12px;
  color: #4e616b;
}

.post-card__avatar {
  width: 36px;
  height: 36px;
  border-radius: 999px;
  background: linear-gradient(135deg, #f97316, #ec4899 50%, #6366f1);
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
</style>
