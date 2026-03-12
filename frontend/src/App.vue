<template>
  <div class="shell">
    <aside class="sidebar">
      <div class="sidebar__brand">
        <span class="sidebar__logo-dot" />
        <span class="sidebar__logo-text">trendsee</span>
        <span class="sidebar__beta">Beta</span>
      </div>

      <nav class="sidebar__nav">
        <p class="sidebar__section-label">Поиск контента</p>
        <ul>
          <li class="sidebar__item sidebar__item--active">
            <span class="sidebar__item-dot" />
            <span>Главная</span>
          </li>
          <li class="sidebar__item">
            <span class="sidebar__item-dot" />
            <span>Видео</span>
          </li>
          <li class="sidebar__item">
            <span class="sidebar__item-dot" />
            <span>Шпионаж</span>
          </li>
          <li class="sidebar__item">
            <span class="sidebar__item-dot" />
            <span>Контент радар</span>
          </li>
        </ul>
      </nav>
    </aside>

    <main class="main">
      <header class="main__header">
        <div>
          <h1 class="main__title">Рассуждения на тему правильности и неправильности</h1>
          <p class="main__subtitle">
            Пример оформления карточки ролика: предпросмотр, метрики и расшифровка.
          </p>
        </div>
      </header>

      <section class="layout">
        <div class="layout__left">
          <div class="video-card">
            <div class="video-card__media">
              <div class="video-card__badge">x10</div>
              <button class="video-card__play" aria-label="Play video">
                ▶
              </button>
            </div>

            <div class="video-card__body">
              <div class="video-card__meta-row">
                <span class="video-card__date">12.12.2025</span>
                <span class="video-card__reels">Reels</span>
              </div>

              <div class="video-card__author">
                <div class="video-card__avatar">B</div>
                <div>
                  <p class="video-card__author-name">@blogerich</p>
                  <p class="video-card__author-followers">384.5K подписчиков</p>
                </div>
              </div>

              <p class="video-card__caption">
                Чтобы выиграть в этой игре, нужно быть настоящим психологом...
              </p>

              <div class="video-card__stats-grid">
                <div class="stat">
                  <p class="stat__label">Просмотры</p>
                  <p class="stat__value">1,2 млн</p>
                </div>
                <div class="stat">
                  <p class="stat__label">Лайки</p>
                  <p class="stat__value">1,2 млн</p>
                </div>
                <div class="stat">
                  <p class="stat__label">Комментарии</p>
                  <p class="stat__value">1,2 млн</p>
                </div>
                <div class="stat">
                  <p class="stat__label">Репосты</p>
                  <p class="stat__value">1,2 млн</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="layout__right">
          <section class="panel">
            <header class="panel__header">
              <div class="panel__tags">
                <span class="tag tag--outlined">Туториал</span>
                <span class="tag tag--outlined">Энергичное видео</span>
                <span class="tag tag--outlined">Лид магнит</span>
                <span class="tag tag--outlined tag--accent">Трендовый звук</span>
              </div>
            </header>

            <div class="panel__section">
              <div class="panel__section-header">
                <h2 class="panel__section-title">Транскрибация</h2>
                <span class="panel__badge">Переведено</span>
              </div>
              <p class="panel__text">
                SPF скатывается? Смотри — вот эти катушки. И нет, это не всегда "плохой SPF".
                Скатывается по трём причинам...
              </p>
            </div>

            <div class="panel__section panel__section--footer">
              <button class="primary-button">Адаптировать</button>
            </div>
          </section>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.shell {
  min-height: 100vh;
  display: grid;
  grid-template-columns: 260px minmax(0, 1fr);
  background: #020617;
  color: #e5e7eb;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.sidebar {
  border-right: 1px solid rgba(148, 163, 184, 0.35);
  padding: 1.25rem 1rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  background: radial-gradient(circle at top left, #1d283a 0, #020617 55%);
}

.sidebar__brand {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-weight: 600;
}

.sidebar__logo-dot {
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: linear-gradient(135deg, #38bdf8, #a855f7);
}

.sidebar__logo-text {
  letter-spacing: 0.04em;
}

.sidebar__beta {
  font-size: 0.7rem;
  padding: 0.1rem 0.4rem;
  border-radius: 999px;
  background: rgba(56, 189, 248, 0.12);
  color: #38bdf8;
}

.sidebar__section-label {
  margin: 0 0 0.4rem;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #6b7280;
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
  gap: 0.6rem;
  padding: 0.45rem 0.7rem;
  border-radius: 0.75rem;
  font-size: 0.9rem;
  color: #d1d5db;
  cursor: pointer;
  transition:
    background 0.14s ease,
    color 0.14s ease;
}

.sidebar__item--active {
  background: rgba(15, 23, 42, 0.95);
  color: #f9fafb;
}

.sidebar__item:hover {
  background: rgba(15, 23, 42, 0.8);
}

.sidebar__item-dot {
  width: 7px;
  height: 7px;
  border-radius: 999px;
  background: rgba(148, 163, 184, 0.7);
}

.main {
  padding: 1.5rem 2rem 2rem;
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
  color: #9ca3af;
}

.layout {
  display: grid;
  grid-template-columns: minmax(0, 340px) minmax(0, 1.6fr);
  gap: 1.5rem;
}

.layout__left,
.layout__right {
  min-width: 0;
}

.video-card {
  border-radius: 1.25rem;
  background: #020617;
  border: 1px solid rgba(148, 163, 184, 0.55);
  box-shadow:
    0 22px 60px rgba(15, 23, 42, 0.85),
    0 0 0 1px rgba(15, 23, 42, 0.95);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.video-card__media {
  position: relative;
  padding-top: 160%;
  background: linear-gradient(135deg, #f97316, #ec4899);
  display: flex;
  align-items: center;
  justify-content: center;
}

.video-card__badge {
  position: absolute;
  top: 0.75rem;
  left: 0.75rem;
  padding: 0.2rem 0.6rem;
  border-radius: 999px;
  font-size: 0.75rem;
  background: rgba(15, 23, 42, 0.7);
  color: #fbbf24;
}

.video-card__play {
  width: 52px;
  height: 52px;
  border-radius: 999px;
  border: none;
  background: rgba(15, 23, 42, 0.9);
  color: #f9fafb;
  font-size: 1.4rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 0 6px rgba(15, 23, 42, 0.35);
}

.video-card__body {
  padding: 1.1rem 1.2rem 1.2rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.video-card__meta-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  color: #9ca3af;
}

.video-card__reels {
  padding: 0.1rem 0.45rem;
  border-radius: 999px;
  background: rgba(56, 189, 248, 0.1);
  color: #38bdf8;
}

.video-card__author {
  display: flex;
  gap: 0.6rem;
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

.video-card__author-name {
  margin: 0;
  font-size: 0.9rem;
}

.video-card__author-followers {
  margin: 0;
  font-size: 0.75rem;
  color: #9ca3af;
}

.video-card__caption {
  margin: 0;
  font-size: 0.85rem;
  color: #d1d5db;
}

.video-card__stats-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.6rem;
  margin-top: 0.4rem;
}

.stat {
  border-radius: 0.9rem;
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.55);
  padding: 0.55rem 0.75rem;
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

