<template>
  <div class="shell">
    <aside class="sidebar">
      <div class="sidebar__brand">
        <img src="/src/imgs/Logo full.png" alt="Trendsee logo" class="sidebar__logo-image" />
      </div>

      <nav class="sidebar__nav">
        <section class="sidebar__group">
          <p class="sidebar__section-label">Поиск контента</p>
          <ul>
            <li
              class="sidebar__item"
              :class="{ 'sidebar__item--active': activePage === 'overview' }"
              @click="setPage('overview')"
            >
              <img src="/src/imgs/Vector.png" class="sidebar__item-icon" />
              <span>Главная</span>
            </li>
            <li class="sidebar__item">
              <img src="/src/imgs/Vector (1).png" class="sidebar__item-icon" />
              <span>Видео</span>
            </li>
            <li class="sidebar__item">
              <img src="/src/imgs/Vector (2).png" class="sidebar__item-icon" />
              <span>Шпионаж</span>
            </li>
            <li
              class="sidebar__item"
              :class="{ 'sidebar__item--active': activePage === 'feed' }"
              @click="setPage('feed')"
            >
              <img src="/src/imgs/Vector (3).png" class="sidebar__item-icon" />
              <span>Контент радар</span>
              <span class="sidebar__item-counter">712</span>
            </li>
          </ul>
        </section>

        <section class="sidebar__group">
             <p class="sidebar__section-label">Работа с соцсетями</p>
          <ul>
            <li class="sidebar__item">
              <img src="/src/imgs/Vector (4).png" class="sidebar__item-icon" />
              <span>Кросс-постинг</span>
            </li>
            <li class="sidebar__item">
              <img src="/src/imgs/Vector (5).png" class="sidebar__item-icon" />
              <span>Чат боты</span>
            </li>
          </ul>
        </section>

        <section class="sidebar__group">
          <p class="sidebar__section-label">Инструменты</p>
          <ul>
            <li class="sidebar__item">
              <img src="/src/imgs/Vector (6).png" class="sidebar__item-icon" />
              <span>ИИ-сценарий</span>
            </li>
            <li class="sidebar__item">
              <img src="/src/imgs/Vector (7).png" class="sidebar__item-icon" />
              <span>Карусели</span>
            </li>
            <li class="sidebar__item">
              <img src="/src/imgs/Vector (8).png" class="sidebar__item-icon" />
              <span>Анализ видео</span>
            </li>
            <li class="sidebar__item">
              <img src="/src/imgs/Vector (9).png" class="sidebar__item-icon" />
              <span>Анализ профиля</span>
            </li>
            <li class="sidebar__item sidebar__item--muted">
              <img src="/src/imgs/Vector (10).png" class="sidebar__item-icon" />
              <span>Черновики</span>
              <span class="sidebar__pill">Скоро</span>
            </li>
          </ul>
        </section>
      </nav>

      <div class="sidebar__bottom">
        <div class="sidebar__tokens">
          <div class="sidebar__tokens-header">
            <div class="sidebar__tokens-header">
              <img src="/src/imgs/Fire.png" class="sidebar__tokens-img"/>
              <span class="sidebar__tokens-title">Токены</span>
            </div>
            <div>
              <span class="sidebar__tokens-value">1 245 / 4 497</span>
            </div>
          </div>
          <div class="sidebar__tokens-bar">
            <span class="sidebar__tokens-bar-fill"></span>
          </div>
           <div class="sidebar__tokens-footer">
            <span class="sidebar__tokens-Creative">Creative +</span>
            <img src="/src/imgs/Icon Leading.png" class="sidebar__tokens-img"/>
          </div>
        </div>

        <div class="sidebar__profile">
          <div class="sidebar__profile-main">
            <img src="/src/imgs/image1.png" class="sidebar__avatar"/>
            <div class="sidebar__profile-text">
              <p class="sidebar__profile-name">Александра</p>
              <p class="sidebar__profile-phone">+7 (999) 999-99-99</p>
            </div>
          </div>
          <div class="sidebar__profile-footer">
            <img src="/src/imgs/RU.png" class="sidebar__profile-locale-img"/>
            <span class="sidebar__profile-locale">RU</span>
            <img src="/src/imgs/Icon Leading (1).png" class="sidebar__profile-img"/>
          </div>
        </div>
      </div>
    </aside>

    <main class="main">
      <section v-if="activePage === 'overview'" class="layout layout--cards">
        <div
          v-for="card in demoCards"
          :key="card.id"
          class="layout__card"
        >
          <div class="video-card">
            <div class="video-card-inner">
              <div class="video-card__media">
                <img :src="card.image" alt="card" class="card-image" />
                <div class="video-card_chip-list">

                  <div class="video-card__chip-row-left">
                    <div class="video-card__chip">
                      <img src="/src/imgs/Vector (14).png" alt="" class="video-card__chip-icon" />
                      <span class="video-card__chip-letter">Reels</span>
                    </div>

                    <div class="video-card__chip_down">
                      <img src="/src/imgs/Vector (12).png" alt="" class="video-card__chip-icon" />
                      <span class="video-card__chip-letter"> X 10</span>
                    </div>
                  </div>

                  <div class="video-card__chip-row-right">
                      <div class="video-card__chip">
                        <img src="/src/imgs/Vector (14).png" alt="" class="video-card__chip-icon" />
                        <span class="video-card__chip-letter">Reels</span>
                      </div>
                      <div class="video-card__chip_down">
                        <img src="/src/imgs/Vector (12).png" alt="" class="video-card__chip-icon" />
                        <span class="video-card__chip-letter"> X 10</span>
                    </div>

                  </div>
                </div>  

                <div class="video-card__metrics">
                  <div class="video-card__metric">
                    <span class="video-card__metric-icon">👁️</span>
                    <span class="video-card__metric-value">105k</span>
                  </div>
                  <div class="video-card__metric">
                    <span class="video-card__metric-icon">❤</span>
                    <span class="video-card__metric-value">85k</span>
                  </div>
                  <div class="video-card__metric">
                    <span class="video-card__metric-icon">💬</span>
                    <span class="video-card__metric-value">15k</span>
                  </div>
                  <div class="video-card__metric">
                    <span class="video-card__metric-icon">↻</span>
                    <span class="video-card__metric-value">485</span>
                  </div>
                </div>
              </div>

              <div class="video-card__body">
                <div class="video-card__author">
                  <div class="video-card__avatar">
                    <span>B</span>
                  </div>
                  <div class="video-card__author-text">
                    <p class="video-card__author-name">@blogerich</p>
                    <p class="video-card__author-followers">384.5K</p>
                  </div>
                </div>

                <p class="video-card__caption">
                  500 000 лайков на ютубе делаем , бля буду скидываю 😂😂
                </p>

                <p class="video-card__date">12.12.2025</p>

                <button class="video-card__cta" type="button">Анализ</button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section v-else class="feed-layout">
        <FeedView />
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import FeedView from "./views/FeedView.vue";

type Page = "overview" | "feed";

const activePage = ref<Page>("overview");

const demoCards = [
  { id: 1, image: "/src/imgs/image.png" },
  { id: 2, image: "/src/imgs/image.png" },
  { id: 3, image: "/src/imgs/image.png" },
  { id: 4, image: "/src/imgs/image.png" },
  { id: 5, image: "/src/imgs/image.png" },
  { id: 6, image: "/src/imgs/image.png" },
];

function setPage(page: Page) {
  activePage.value = page;
}
</script>

<style scoped>
.shell {
  min-height: 100vh;
  display: grid;
  grid-template-columns: 274px minmax(0, 1fr);
  background: #eaecf5;
  color: #111827;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.sidebar {
  display: flex;
  flex-direction: column;
  width: 274px;
  padding: 12px 12px 16px;
  background: #f4f5f6;
  border-radius: 16px;
}

.sidebar__brand {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 10px 10px;
  border-radius: 12px;
}

.sidebar__logo-dot {
  width: 30.18px;
  height: 22.65px;
  border-radius: 999px;
  background: #1b1a25;
}

.sidebar__logo-image {
  height: 28px;
  object-fit: contain;
}

.sidebar__nav {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 8px;
}

.sidebar__group {
  padding-inline: 8px;
}

.menu_header {
  width: 242px;
  height: 29px;
  padding-top: 4px;
  padding-right: 0px;
  padding-bottom: 4px;
  padding-left: 0px;
}

.sidebar__section-label {
  height: 21px;
  color: #83939c;
  font-weight: 600;
  font: font/family/heading;
  font-size: 15px;
  line-height:font/line-height/heading-6;
  letter-spacing: 0.1px;
}

.sidebar__nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.sidebar__item {
  display: flex;
  align-items: center;
  width: 242px;
  height: 40px;
  radius: 12px;
  padding: 8px;
  gap: 16px;
  border-bottom: 1px;
  color: #4e616b;
  cursor: pointer;
}

.sidebar__item-dot {
  width: 7px;
  height: 7px;
  border-radius: 999px;
  background: rgba(148, 163, 184, 0.7);
}

.sidebar__item-icon {
  width: 18px;
  height: 18.74840545654297px;
  angle: 0 deg;
  opacity: 1;
  top: 2.25px;
  left: 3px;
}

.sidebar__item-counter {
  margin-left: auto;
  font-size: 11px;
  padding: 0 6px;
  border-radius: 999px;
  background: #111827;
  color: #ffffff;
}

.sidebar__item--muted {
  opacity: 0.6;
}

.sidebar__pill {
  margin-left: auto;
  font-size: 10px;
  padding: 2px 8px;
  border-radius: 999px;
  background: #e5e7eb;
  color: #4b5563;
}

.sidebar__bottom {
  margin-top: 12px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.sidebar__tokens {
  padding: 10px 12px;
  border-radius: 12px;
  background: #ffffff;
  box-shadow: 0 0 0 1px rgba(15, 23, 42, 0.03);
}

.sidebar__tokens-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
  font-size: 11px;
  color: #374151;
}

.sidebar__tokens-img{
  width: 20px;
  height: 20px;
  angle: 0 deg;
  opacity: 1;

}
.sidebar__tokens-footer{
  width: 218px;
  height: 21px;
  display: flex;
  justify-content: space-between;
  angle: 0 deg;
  opacity: 1;
}
.sidebar__tokens-Creative{
  width: 72px;
  height: 21px;
  angle: 0 deg;
  opacity: 1;
  font-weight: 500;
  letter-spacing: 0.25px;
  color: #83939c;
  font-size: small;
  font-style: Medium;

}

.sidebar__tokens-title {
  font-weight: 700;
  font-style: Italic;
  font-size: small;
  leading-trim: NONE;
  line-height: small;
  letter-spacing: 0.25px;
  vertical-align: middle;
}

.sidebar__tokens-bar {
  position: relative;
  height: 6px;
  border-radius: 999px;
  background: #e5e7eb;
  overflow: hidden;
}

.sidebar__tokens-bar-fill {
  position: absolute;
  inset: 0;
  width: 60%;
  border-radius: inherit;
  background: linear-gradient(90deg, #6366f1, #22c55e);
}

.sidebar__profile {
  padding: 10px 12px;
  border-radius: 12px;
  background: #ffffff;
  display: flex;
  flex-direction: column;
  gap: 8px;
  box-shadow: 0 0 0 1px rgba(15, 23, 42, 0.03);
}

.sidebar__profile-main {
  display: flex;
  align-items: center;
  gap: 8px;
}

.sidebar__profile-locale-img{
  font-weight: 500;
  font-style: Medium;
  font-size: caption;
  letter-spacing: 0.4px;
  vertical-align: middle;
  width: 24px;
  height: 16px;
  angle: 0 deg;
  opacity: 1;
}

.sidebar__profile-img{
  width: 16px;
  height: 16px;
  angle: 0 deg;
  opacity: 1;

}

.sidebar__avatar {
  width: 32px;
  height: 32px;
  border-radius: 999px;
  background: linear-gradient(135deg, #6366f1, #22c55e);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  font-weight: 600;
  font-size: 14px;
}

.sidebar__profile-text {
  font-size: 11px;
  color: #374151;
}

.sidebar__profile-name {
  margin: 0;
  font-weight: 500;
}

.sidebar__profile-phone {
  margin: 0;
  color: #6b7280;
}

.sidebar__profile-footer {
  width: 97px;
  height: 32px;
  border-radius: radius-150;
  padding-top: space-100;
  padding-right: space-150;
  padding-bottom: space-100;
  padding-left: space-150;
  gap: 8px;
  angle: 0 deg;
  opacity: 1;
  display: flex;
  align-items: center;
  font-size: 11px;
  color: #83939c;
}

.sidebar__profile-label {
  padding: 2px 8px;
  border-radius: 999px;
  background: #f3e8ff;
}

.sidebar__profile-locale {
  padding: 2px 6px;
  border-radius: 999px;
  background: #f3f4f6;
}

.main {
  width: 974px;
  border-radius: radius-200;
  gap: space-0;
  angle: 0 deg;
  opacity: 1;
  padding: space-0;
  background: #ffffff;
}

.main__header {
  margin-bottom: 1.5rem;
}

.main__title {
  margin: 0 0 0.4rem;
  font-size: 1.4rem;
  font-weight: 600;
}

.main__subtitle {
  margin: 0;
  font-size: 0.9rem;
  color: #6b7280;
}

.layout {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
}

.layout--cards {
  padding-top: 8px;
  justify-content: center;
}

.layout__card {
  flex: 0 0 auto;
}

.card-image{
  width: 254px;
  height: 400px;
  border-radius: 16px;
  justify-content: space-between;
  angle: 0 deg;
  opacity: 1;
}

.feed-layout {
  background: #020617;
  border-radius: 1.25rem;
  border: 1px solid rgba(148, 163, 184, 0.55);
  padding: 1.5rem 1.75rem 1.75rem;
  box-shadow:
    0 22px 60px rgba(15, 23, 42, 0.85),
    0 0 0 1px rgba(15, 23, 42, 0.95);
}

.video-card {
  width: 262px;
  height: 576px;
  min-width: 220px;
  max-width: 262px;
  border-radius: 16px;
  padding-top: 4px;
  padding-right: 4px;
  padding-bottom: 8px;
  padding-left: 4px;
  gap: 4px;
  angle: 0 deg;
  opacity: 1;
}

.video-card > div,
.video-card__media,
.video-card__body {
  border-radius: 20px;
}

.video-card-inner {
  background: #ffffff;
  border-radius: 20px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.video-card__media {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.video-card__chip-row-left {
  position: absolute;
  top: 10px;
  left: 10px;
  gap: 6px;
}


.video-card__chip-row-right {
  position: absolute;
  top: 10px;
  right: 10px;
  gap: 6px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.video-card_chip-list{
  display: flex;
  justify-content: space-between;
}
.video-card__chip_down{  
  width: 57px;
  height: 28px;
  border-radius: 8px;
  gap: 4px;
  angle: 0 deg;
  opacity: 1;
  padding: 4px;
  background: var(--Black-40, #00000066);
  backdrop-filter: blur(16px);
  display: flex;  
  margin-top:3px
}
.video-card__chip {
  width: 67px;
  height: 28px;
  border-radius: 8px;
  gap: 4px;
  angle: 0 deg;
  opacity: 1;
  padding: 4px;
  background: var(--Black-40, #00000066);
  backdrop-filter: blur(16px);
  display: flex; 
}

.video-card__chip-icon{
  width: 20px;
  height: 20px;
  gap: 10px;
  angle: 0 deg;
  opacity: 1;
  padding: 2px;
}

.video-card__chip-letter{
  width: 35px;
  height: 15px;
  padding-right: 2px;
  gap: 10px;
  angle: 0 deg;
  opacity: 1;
  color: #ffffff;
  font-size: 13px;
}

.video-card__chip--light {
  background: rgba(0, 0, 0, 0.65);
  color: #ffffff;
}

.video-card__chip--dark {
  background: rgba(0, 0, 0, 0.85);
  color: #ffffff;
}

.video-card__metrics {
  position: absolute;
  left: 10px;
  right: 10px;
  bottom: 10px;
  padding: 6px 10px;
  border-radius: 999px;
  background: linear-gradient(90deg, rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.7));
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.video-card__metric {
  display: flex;
  align-items: center;
  gap: 4px;
}

.video-card__metric-icon {
  font-size: 12px;
  color: #f9fafb;
}

.video-card__metric-value {
  font-size: 11px;
  color: #f9fafb;
}

.video-card__body {
  padding: 10px 14px 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.video-card__author {
  display: flex;
  gap: 8px;
  align-items: center;
}

.video-card__avatar {
  width: 32px;
  height: 32px;
  border-radius: 999px;
  background: radial-gradient(circle at 30% 20%, #f97316, #ec4899 55%, #6366f1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  font-weight: 600;
}

.video-card__author-text {
  font-size: 11px;
}

.video-card__author-name {
  margin: 0;
  font-size: 12px;
  color: #2a3cff;
}

.video-card__author-followers {
  margin: 0;
  font-size: 11px;
  color: #6b7280;
}

.video-card__caption {
  margin: 0;
  font-size: 12px;
  line-height: 1.4;
  color: #111827;
}

.video-card__date {
  margin: 0;
  font-size: 11px;
  color: #9ca3af;
}

.video-card__cta {
  margin-top: 6px;
  width: 100%;
  border: none;
  border-radius: 999px;
  padding: 10px 0;
  background: #4338ca;
  color: #ffffff;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
}

.video-card__chip video-card__chip--light{
  width: 67px;
  height: 28px;
  border-radius: 8px;
  gap: 4px;
  angle: 0 deg;
  opacity: 1;
  padding: 4px;
}

.stat__label {
  margin: 0 0 0.1rem;
  font-size: 0.7rem;
  color: #9ca3af;
}

.stat__value {
  margin: 0;
  font-size: 0.9rem;
  font-weight: 600;
}

.panel {
  border-radius: 1.25rem;
  background: #020617;
  border: 1px solid rgba(148, 163, 184, 0.55);
  padding: 1.25rem 1.4rem 1.35rem;
  display: flex;
  flex-direction: column;
  gap: 1.1rem;
  box-shadow:
    0 22px 60px rgba(15, 23, 42, 0.75),
    0 0 0 1px rgba(15, 23, 42, 0.9);
}

.panel__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.tag {
  font-size: 0.75rem;
  padding: 0.25rem 0.6rem;
  border-radius: 999px;
  border: 1px solid rgba(148, 163, 184, 0.7);
  color: #e5e7eb;
  background: rgba(15, 23, 42, 0.9);
}

.tag--accent {
  border-color: #fb7185;
  color: #fecaca;
  background: rgba(127, 29, 29, 0.45);
}

.panel__section {
  border-radius: 0.9rem;
  background: rgba(15, 23, 42, 0.9);
  padding: 0.9rem 1rem;
}

.panel__section--footer {
  display: flex;
  justify-content: flex-start;
  background: transparent;
  padding: 0;
}

.panel__section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.panel__section-title {
  margin: 0;
  font-size: 0.95rem;
  font-weight: 600;
}

.panel__badge {
  font-size: 0.7rem;
  padding: 0.15rem 0.5rem;
  border-radius: 999px;
  background: rgba(34, 197, 94, 0.15);
  color: #4ade80;
}

.panel__text {
  margin: 0;
  font-size: 0.88rem;
  line-height: 1.6;
  color: #d1d5db;
}

.primary-button {
  padding: 0.65rem 1.4rem;
  border-radius: 999px;
  border: none;
  font-size: 0.9rem;
  font-weight: 600;
  background: linear-gradient(135deg, #6366f1, #22c55e);
  color: #f9fafb;
  cursor: pointer;
  box-shadow: 0 12px 30px rgba(22, 163, 74, 0.45);
  transition:
    transform 0.12s ease,
    box-shadow 0.12s ease,
    filter 0.12s ease;
}

.primary-button:hover {
  transform: translateY(-1px);
  filter: brightness(1.05);
  box-shadow: 0 18px 40px rgba(22, 163, 74, 0.55);
}

@media (max-width: 960px) {
  .shell {
    grid-template-columns: 1fr;
  }

  .sidebar {
    display: none;
  }

  .layout {
    grid-template-columns: minmax(0, 1fr);
  }
}

@media (max-width: 640px) {
  .main {
    padding-inline: 1rem;
  }

  .panel,
  .video-card {
    border-radius: 1rem;
  }
}
</style>

