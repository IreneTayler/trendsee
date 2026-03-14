<template>
  <Teleport to="body">
    <Transition name="fade">
      <div
        v-if="visible"
        class="modal-overlay"
        @click.self="onClose"
      >
        <Transition name="slide-up">
          <div class="modal" v-if="post">
            <button
              type="button"
              class="modal__close"
              aria-label="Закрыть"
              @click="onClose"
            >
              ✕
            </button>

            <div class="modal__grid">
              <!-- Left column: video + profile + metrics -->
              <div class="modal__left">
                <div class="modal__video-wrap">
                  <div class="modal__video-placeholder" />
                  <span class="modal__reels-badge">Reels 10</span>
                  <div class="modal__play-btn">▶</div>
                </div>
                <div class="modal__video-footer">
                  <span class="modal__date">{{ createdDate }}</span>
                  <button type="button" class="modal__share" aria-label="Поделиться">↗</button>
                </div>
                <div class="modal__profile">
                  <div class="modal__avatar">B</div>
                  <div class="modal__profile-text">
                    <p class="modal__username">@blogerich</p>
                    <p class="modal__followers">384.5K</p>
                  </div>
                  <div class="modal__profile-actions">
                    <span class="modal__profile-icon">+</span>
                    <span class="modal__profile-icon">👤</span>
                  </div>
                </div>
                <p class="modal__description">
                  {{ descriptionSnippet }}
                  <button type="button" class="modal__more">Ещё ▾</button>
                </p>
                <ul class="modal__metrics">
                  <li><span class="modal__metric-icon">👁</span> Просмотры <strong>1,2 млн</strong></li>
                  <li><span class="modal__metric-icon">♡</span> Лайки <strong>1,2 млн</strong></li>
                  <li><span class="modal__metric-icon">💬</span> Комментарии <strong>1,2 млн</strong></li>
                  <li><span class="modal__metric-icon">↗</span> Репосты <strong>1,2 млн</strong></li>
                  <li>ER <strong>1,2 млн</strong></li>
                </ul>
              </div>

              <!-- Right column: topic, tags, transcript, adapt, essence -->
              <div class="modal__right">
                <div class="modal__topic">
                  <p class="modal__topic-label">Тема видео</p>
                  <h2 class="modal__title">{{ post.title }}</h2>
                </div>
                <div class="modal__meta">
                  <span class="modal__music">♪ Tyga — Pop it off</span>
                  <span class="modal__lang">Язык: 🇬🇧 Английский</span>
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
                    Разбор состава/логики: он в человеческих словах переводит состав/механику («что реально делает Х»), называет 2-3 работающих активных компонента и 2-3 маркетинговых «пустых» обещания.
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

const props = defineProps<{ visible: boolean; post: Post | null }>();
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
}

@media (max-width: 768px) {
  .modal__grid {
    grid-template-columns: 1fr;
  }
}

.modal__left {
  padding: 1.25rem 1rem 1.5rem;
  border-right: 1px solid #e2e8f0;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.modal__video-wrap {
  position: relative;
  padding-top: 177%;
  background: linear-gradient(150deg, #f1f5f9, #e2e8f0);
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
  margin-right: 0.35rem;
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
  font-size: 0.75rem;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.modal__title {
  margin: 0 0 0.5rem;
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1.3;
  color: #0f172a;
}

.modal__meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem 1rem;
  font-size: 0.8rem;
  color: #64748b;
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

.modal__tag--blue { background: #dbeafe; color: #1d4ed8; }
.modal__tag--green { background: #dcfce7; color: #15803d; }
.modal__tag--orange { background: #ffedd5; color: #c2410c; }
.modal__tag--red { background: #ffe4e6; color: #be123c; }
.modal__tag--purple { background: #f3e8ff; color: #6b21a8; }

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
</style>
