<template>
  <Teleport to="body">
    <!-- Overlay: simple fade in/out -->
    <Transition name="overlay-fade">
      <div v-if="visible" class="modal-overlay" @click.self="onClose">
        <!-- Panel: distinct slide-in-from-right animation -->
        <Transition name="panel-slide">
          <div class="modal" v-if="post">
            <button type="button" class="modal__close" aria-label="Закрыть" @click="onClose">
              ✕
            </button>

            <div class="modal__grid">
              <!-- Left column: video + profile + metrics -->
              <div class="modal__left">
                <div class="post-card__media">
                  <img v-if="imageSrc" :src="imageSrc" alt="" class="post-card__img" />
                  <div v-else class="post-card__media-placeholder" />
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
                <p class="modal__description">
                  {{ descriptionSnippet }}
                  <div class="flex justify-end">
                    <button type="button" class="flex items-center">
                      <img :src="IconleadingDown" alt="" class="size-[12px]"/>
                      <span class="text-[#171C1F] text-[12px] pl-1">Ещё</span> 
                    </button>
                  </div>
                </p>
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
                    <button type="button" class="bg-[#F4F5F6] pt-[4px] pb-[4px] pl-[12px] pr-[12px] rounded-full" aria-label="Копировать">
                      <img :src="ButtonSecondary" alt="" class="size-[12px]"/>
                    </button>
                  </div>
                </div>
                <div class="bg-[#F4F5F6] pt-[16px] pb-[8px] pr-[16px] pl-[18px] rounded-md">
                  <p class="text-[#4E616B]">{{ post.text }}</p>
                  <div class="flex justify-end pt-[12px]">
                    <button type="button" class="flex items-center">
                      <img :src="IconleadingDown" alt="" class="size-[12px]"/>
                      <span class="text-[#171C1F] text-[12px] pl-1">Ещё</span> 
                    </button>
                  </div>
                </div>
                <button type="button" class="flex justify-evenly items-center bg-[#2B31B3] w-[220px] h-[56px] rounded-xl p-[16px]">
                  <span>
                      <img :src="primary" alt="" class="size-[24px]"/>
                  </span> 
                  <span class="text-[#ffffff] text-[#18px]">Адаптировать</span>                   
                </button>
                <div class="modal__essence">
                  <h3 class="modal__essence-title">Суть</h3>
                  <p class="bg-[#F4F5F6] p-[16px] rounded-md text-[#4E616B]">
                    Разбор состава/логики: он в человеческих словах переводит состав/механику («что реально делает Х»),
                    называет 2-3 работающих активных компонента и 2-3 маркетинговых «пустых» обещания.
                  </p>
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
import { computed } from "vue";
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
}

.modal {
  position: relative;
  height: 100vh;
  width: min(960px, 100vw - 320px);
  overflow-y: auto;
  background: #fff;
  border-radius: 1.25rem;
  box-shadow: 0 24px 80px rgba(0, 0, 0, 0.2);
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

.modal__grid {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 0;
  min-height: 0;
  padding: 24px;
}

@media (max-width: 768px) {
  .modal__grid {
    grid-template-columns: 1fr;
  }
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

.modal__description {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.45;
  color: #334155;
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

/* Overlay fade animation */
.overlay-fade-enter-active,
.overlay-fade-leave-active {
  transition: opacity 0.25s ease-in-out;
}

.overlay-fade-enter-from,
.overlay-fade-leave-to {
  opacity: 0;
}

/* Panel slide from the right with slight scale */
.panel-slide-enter-active {
  transition: transform 0.3s cubic-bezier(0.22, 0.61, 0.36, 1), opacity 0.3s ease-out;
}

.panel-slide-leave-active {
  transition: transform 0.25s ease-in, opacity 0.25s ease-in;
}

.panel-slide-enter-from,
.panel-slide-leave-to {
  transform: translateX(24px);
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
  top: 30px;
  left: 30px;
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
