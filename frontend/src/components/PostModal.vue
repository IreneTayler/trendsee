<template>
  <Teleport to="body">
    <Transition name="fade">
      <div v-if="visible" class="modal-overlay" @click.self="onClose">
        <Transition name="slide-up">
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
                  <button type="button" class="modal__more">Ещё ▾</button>
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
                  <div class="flex">
                    <img :src="music" alt="" class="size-[16px]"/>
                    <span class="color-[#343A40] text-xs pl-5">Tyga — Pop it off</span>
                  </div>
                  <div class="flex pl-20">
                    <span class="color-[#343A40] text-xs"> Язык:</span>                
                    <img :src="TrendSourceIcon" alt="" class="size-[16px] pl-5"/>
                    <span class="color-[#343A40] text-xs pl-5"> Английский</span>
                  </div>
                </div>
                <div class="modal__tags">
                  <span class="modal__tag modal__tag--blue">Туториал</span>
                  <span class="modal__tag modal__tag--green">Энергичное видео</span>
                  <span class="modal__tag modal__tag--orange">Изи монтаж</span>
                  <span class="modal__tag modal__tag--red">Трендовый звук</span>
                  <span class="modal__tag modal__tag--orange">Лид магнит</span>
                  <span class="modal__tag modal__tag--purple">Красота и здоровье</span>
                </div>
                <div class="modal__transcript">
                  <div class="modal__transcript-head">
                    <h3 class="modal__transcript-title">Транскрибация</h3>
                    <span class="modal__transcript-badge">Переведено</span>
                    <button type="button" class="modal__copy" aria-label="Копировать">⎘</button>
                  </div>
                  <p class="modal__transcript-text">{{ post.text }}</p>
                  <button type="button" class="modal__more">Ещё ▾</button>
                </div>
                <button type="button" class="modal__adapt">
                  <span>✨</span> Адаптировать
                </button>
                <div class="modal__essence">
                  <h3 class="modal__essence-title">Суть</h3>
                  <p class="modal__essence-text">
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
  align-items: center;
  justify-content: center;
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(8px);
  padding: 1.5rem;
  overflow-y: auto;
}

.modal {
  position: relative;
  width: 100%;
  max-width: 960px;
  max-height: calc(100vh - 3rem);
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
  grid-template-columns: minmax(0, 340px) 1fr;
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
  width: 216px;
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

.modal__more {
  margin-left: 0.25rem;
  padding: 0;
  border: none;
  background: none;
  color: #4338ca;
  font-size: 0.85rem;
  cursor: pointer;
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
  padding: 1.5rem 1.5rem 1.5rem 1.25rem;
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

.modal__tag {
  padding: 0.25rem 0.6rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 500;
}

.modal__tag--blue {
  background: #dbeafe;
  color: #1d4ed8;
}

.modal__tag--green {
  background: #dcfce7;
  color: #15803d;
}

.modal__tag--orange {
  background: #ffedd5;
  color: #c2410c;
}

.modal__tag--red {
  background: #ffe4e6;
  color: #be123c;
}

.modal__tag--purple {
  background: #f3e8ff;
  color: #6b21a8;
}

.modal__transcript {
  padding: 0.75rem 1rem;
  background: #f8fafc;
  border-radius: 0.75rem;
}

.modal__transcript-head {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.modal__transcript-title {
  margin: 0;
  font-size: 0.9rem;
  font-weight: 600;
  color: #0f172a;
}

.modal__transcript-badge {
  font-size: 0.7rem;
  padding: 0.15rem 0.5rem;
  border-radius: 999px;
  background: #dcfce7;
  color: #15803d;
}

.modal__copy {
  margin-left: auto;
  border: none;
  background: none;
  color: #64748b;
  cursor: pointer;
  font-size: 1rem;
}

.modal__transcript-text {
  margin: 0 0 0.5rem;
  font-size: 0.85rem;
  line-height: 1.6;
  color: #334155;
  white-space: pre-wrap;
}

.modal__adapt {
  width: 100%;
  padding: 0.75rem 1.25rem;
  border: none;
  border-radius: 0.75rem;
  background: #4338ca;
  color: #fff;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.modal__adapt:hover {
  background: #3730a3;
}

.modal__essence-title {
  margin: 0 0 0.5rem;
  font-size: 0.95rem;
  font-weight: 600;
  color: #0f172a;
}

.modal__essence-text {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.55;
  color: #475569;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-up-enter-active,
.slide-up-leave-active {
  transition: transform 0.25s ease, opacity 0.25s ease;
}

.slide-up-enter-from,
.slide-up-leave-to {
  transform: translateY(16px);
  opacity: 0;
}

.post-card__badges {
  position: absolute;
  display: flex;
  flex-direction: column;
  gap: 6px;
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
  top: 34px;
  left: 34px;
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
