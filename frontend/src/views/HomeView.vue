<template>
  <div class="min-h-screen bg-[radial-gradient(ellipse_at_top,rgba(16,185,129,0.25),transparent_55%),linear-gradient(to_bottom,#052e16,#022c22_60%,#020617)] flex items-center justify-center p-4 font-sans">
    <div class="w-full max-w-2xl bg-white/5 backdrop-blur-2xl border border-white/10 rounded-[2rem] shadow-[0_25px_80px_-15px_rgba(0,0,0,0.8)] overflow-hidden">
      <header class="relative px-6 pt-6 pb-5">
        <div class="absolute inset-x-0 top-0 h-24 bg-gradient-to-r from-emerald-500/20 to-green-500/20 -z-0"></div>
        <div class="relative flex items-center gap-4">
          <div class="relative">
            <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-emerald-400 to-green-600 flex items-center justify-center text-3xl shadow-lg shadow-emerald-500/30 rotate-6">
              <img src="@/assets/logos/logo_foot_ai.png" alt="FootAI Logo" class="rounded-2xl object-cover" />
            </div>
            <span class="absolute -bottom-1 -right-1 w-4 h-4 rounded-full bg-green-400 border-2 border-slate-900"></span>
          </div>
          <div class="flex-1">
            <h1 class="text-white text-2xl font-extrabold tracking-tight">Foot<span class="text-emerald-400">AI</span></h1>
            <p class="text-emerald-200/80 text-sm flex items-center gap-1.5">
              <span class="inline-block w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
              Online football assistant
            </p>
          </div>
          <div class="text-3xl opacity-30 hidden sm:block">🏆</div>
        </div>
      </header>

      <main class="h-96 overflow-y-auto px-5 py-6 space-y-5 bg-black/20" ref="messagesRef">
        <div
          v-for="(message, index) in messages"
          :key="index"
          :class="message.role === 'user' ? 'flex justify-end' : 'flex justify-start items-end gap-2.5'"
        >
          <div
            v-if="message.role === 'bot'"
            class="w-8 h-8 rounded-full bg-gradient-to-br from-emerald-400 to-green-600 flex items-center justify-center text-sm shadow-md shadow-emerald-500/20 flex-shrink-0"
          >
            <img src="@/assets/logos/logo_foot_ai.png" alt="FootAI Logo" class="rounded-2xl w-10 h-10 object-cover" />
          </div>
          <div
            :class="message.role === 'user'
              ? 'bg-gradient-to-br from-emerald-500 to-green-600 text-white rounded-3xl rounded-br-md shadow-lg shadow-emerald-600/25'
              : 'bg-slate-800/90 text-slate-100 border border-white/10 rounded-3xl rounded-bl-md'"
            class="max-w-[75%] px-4 py-3 text-[15px] leading-relaxed"
          >
            {{ message.text }}
          </div>
        </div>

        <div v-if="loading" class="flex justify-start items-end gap-2.5">
          <div class="w-8 h-8 rounded-full bg-gradient-to-br from-emerald-400 to-green-600 flex items-center justify-center text-sm flex-shrink-0">
            ⚽
          </div>
          <div class="bg-slate-800/90 border border-white/10 rounded-3xl rounded-bl-md px-4 py-3 flex gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-bounce"></span>
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-bounce" style="animation-delay: 150ms"></span>
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-bounce" style="animation-delay: 300ms"></span>
          </div>
        </div>
      </main>

      <div class="px-5 pt-3 flex flex-wrap gap-2">
        <button
          v-for="suggestion in suggestions"
          :key="suggestion"
          @click="input = suggestion"
          class="px-3 py-1.5 text-xs font-medium rounded-full bg-white/5 border border-white/10 text-emerald-100/80 hover:bg-emerald-500/20 hover:border-emerald-400/40 transition"
        >
          {{ suggestion }}
        </button>
      </div>

      <footer class="p-5 flex gap-3">
        <input
          v-model="input"
          @keyup.enter="sendMessage"
          type="text"
          placeholder="Posez votre question sur le football..."
          class="flex-1 px-5 py-3.5 rounded-2xl bg-white/10 border border-white/10 text-white placeholder:text-slate-400 focus:outline-none focus:border-emerald-400/60 focus:ring-2 focus:ring-emerald-500/20 transition"
        >
        <button
          @click="sendMessage"
          :disabled="loading || !input.trim()"
          class="px-5 py-3.5 rounded-2xl bg-gradient-to-br from-emerald-400 to-green-600 text-white font-bold shadow-lg shadow-emerald-600/30 hover:brightness-110 active:scale-95 disabled:opacity-40 disabled:pointer-events-none transition"
          title="Envoyer"
        >
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 2L11 13" />
            <path d="M22 2l-7 20-4-9-9-4 20-7z" />
          </svg>
        </button>
      </footer>
    </div>
  </div>
</template>

<script lang="ts">
import api from '../service/api'

interface Message {
  role: 'user' | 'bot'
  text: string
}

export default {
  data() {
    return {
      input: '',
      loading: false,
      suggestions: [
        'Qui a gagné la dernière Coupe du Monde ?',
        'Qui est le meilleur buteur de l\'histoire ?',
        'Quelle équipe a remporté la Ligue des Champions 2024 ?'
      ],
      messages: [
        { role: 'bot', text: 'Bonjour ! Je suis FootAI ⚽ Posez-moi vos questions sur le football.' }
      ] as Message[]
    }
  },
  methods: {
    async sendMessage() {
      const text = this.input.trim()
      if (!text || this.loading) return

      this.messages.push({ role: 'user', text })
      this.input = ''
      this.loading = true

      try {
        const { data } = await api.post('/chat', { message: text })
        this.messages.push({ role: 'bot', text: data.message })
      } catch {
        this.messages.push({ role: 'bot', text: 'Erreur : impossible de joindre le backend.' })
      } finally {
        this.loading = false
        this.scrollToBottom()
      }
    },
    scrollToBottom() {
      const el = this.$refs.messagesRef as HTMLElement
      if (el) el.scrollTop = el.scrollHeight
    }
  }
}
</script>
