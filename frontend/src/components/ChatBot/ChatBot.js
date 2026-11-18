import { computed, inject, nextTick, ref } from 'vue';
import { sendChatMessage } from '../../services/api';

export default {
  name: 'ChatBot',
  props: {
    recommendationContext: {
      type: Object,
      default: null
    }
  },
  setup(props) {
    const { t, locale } = inject('i18n');
    const isOpen = ref(false);
    const draft = ref('');
    const isSending = ref(false);
    const messages = ref([
      {
        role: 'assistant',
        text: 'Namaste! I can help you understand your crop, storage, mandi and profit recommendation.'
      }
    ]);
    const messagesContainer = ref(null);

    const title = computed(() => locale.value === 'hi'
      ? 'एग्रीट्रेड सहायक'
      : 'AgriTrade Assistant');

    function toggleChat() {
      isOpen.value = !isOpen.value;
      if (isOpen.value) {
        nextTick(() => {
          messagesContainer.value?.scrollTo({
            top: messagesContainer.value.scrollHeight,
            behavior: 'smooth'
          });
        });
      }
    }

    function closeChat() {
      isOpen.value = false;
    }

    async function sendMessage() {
      const message = draft.value.trim();
      if (!message || isSending.value) return;

      messages.value.push({ role: 'user', text: message });
      draft.value = '';
      isSending.value = true;

      await nextTick();
      messagesContainer.value?.scrollTo({
        top: messagesContainer.value.scrollHeight,
        behavior: 'smooth'
      });

      try {
        const response = await sendChatMessage({
          message,
          language: locale.value,
          context: props.recommendationContext
        });
        messages.value.push({
          role: 'assistant',
          text: response.reply || response.message || 'I could not generate a response.'
        });
      } catch (error) {
        messages.value.push({
          role: 'assistant',
          text: locale.value === 'hi'
            ? 'क्षमा करें, अभी सहायक उपलब्ध नहीं है। कृपया फिर प्रयास करें।'
            : 'Sorry, the assistant is unavailable right now. Please try again.'
        });
      } finally {
        isSending.value = false;
        await nextTick();
        messagesContainer.value?.scrollTo({
          top: messagesContainer.value.scrollHeight,
          behavior: 'smooth'
        });
      }
    }

    return {
      t,
      locale,
      title,
      isOpen,
      draft,
      messages,
      isSending,
      messagesContainer,
      toggleChat,
      closeChat,
      sendMessage
    };
  }
};
